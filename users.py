#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn users:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000


#creamos la función asincrona con formato JSON
@app.get("/usersjson")
async def usersjson():
    return [{"Name":"Alfredo", "LastName":"Garcia", "Age":"30"},
            {"Name":"Juan", "LastName":"Perez", "Age":"45"},
            {"Name":"María", "LastName":"López", "Age":"22"}]
    
    # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/users
    
##################################Clase 4############################################
#Para no ingresar registro por registro, trabajaremos con orientación a objetos

#Definimos nuestra entidad: user

class User(BaseModel):
    id:int
    Name: str
    LastName:str
    Age:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=1,Name="Alfredo", LastName="Garcia", Age="30"),
             User(id=2,Name="Juan", LastName="Perez", Age="45"),
             User(id=3,Name="María", LastName="Lopez", Age="22")]

@app.get("/usersclass")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/
 
 
 #################################FILTERS###########################################
####Obtengo filtro por Path
#Path para datos fijos. Datos en específico. cantidad limitada
@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1

#####################################################################
####Obtengo filtro por query
#El typado es muy importante para devolver los valores del filter
#Query para datos variables. Paginación de 10 en 10 consultas
@app.get("/userquery/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/userquery/?id=1
     #Ejemplo de busqueda por dos parámetros:
     #http://127.0.0.1:8000/userquery/?id=1&Name=Alfredo