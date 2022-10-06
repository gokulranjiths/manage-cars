# Manage-cars
An application built with _FastAPI python_ to maintain information about cars. 

## ToDo
- Database connectivity: For now just the dictionary in `database.py` file is used to store the details
- UI application
- Logging

## Available Operations
- View list of available car information
- Add car information 
- Delete exisiting car information


## To run the application
- Install ```pipenv``` using ```pip install pipenv```
- Clone the repository
- Move to the project folder and activate pipenv shell using ```pipenv shell``` 
- Install all the dependencies ```pipenv install```
- Run the application with the help of _uvicorn_ using command ```uvicorn main:app```
- The swagger UI will be available in `http://127.0.0.1:8000/docs`
