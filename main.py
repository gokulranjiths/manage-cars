from fastapi import FastAPI, Query, Path, HTTPException, status, Body
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from database import cars
app= FastAPI(
    title="Car Management",
    version= "1.0",
    description="""An application built with FastAPI python to maintain information about cars""")

class Car(BaseModel):
    make: str
    model: str
    year: int = Field(...,ge= 1970, le= 2022)
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]

class UpdateCar(BaseModel):
    id: int = Field(..., ge=0, lt=100)
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(ge= 1970, le= 2022)
    price: Optional[float]
    engine: Optional[str]
    autonomous: Optional[bool]
    sold: Optional[List[str]]


@app.get("/")
def root():
    return {"Welcome to":"FastAPI First API"}


@app.get("/cars", response_model=List[Dict[str,Car]])
def get_cars(number: Optional[int] = Query(10)):
    response=[]
    for id, car_details in list(cars.items())[:int(number)]:
        to_add={}
        to_add[id]=car_details
        response.append(to_add)
    return response

@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int =Path(..., ge=0, lt=100)):
    car = cars.get(id)
    if car:
        return car
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find car details for given ID")

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars:List[Car]):
    if len(body_cars)<1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No cars to add")
    min_id = len(cars.values())+1
    for car in body_cars:
        cars[min_id]=car
        min_id +=1

@app.delete("/cars/{id}", status_code=status.HTTP_200_OK)
def delete_cars(id: int =Path(..., ge=0, lt=100)):
    car=cars.get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No car with this id")
    del cars[id]

@app.put("/cars", status_code=status.HTTP_200_OK)
def update_cars(body_cars: UpdateCar =Body(...)):
    car_id=body_cars.id
    car=cars.get(car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "No Car with this id")
    body_cars=body_cars.dict(exclude_unset=True)
    print(body_cars)
    car=dict(car)
    for key in body_cars:
        car[key]=body_cars[key]
    cars[car_id]=car


