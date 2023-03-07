#Código de autenticación segura

#Instalamos libreria de criptografía para encriptar token
# pip install "python-jose[cryptography]"

#Instalamos libreria que contiene el algoritmo de encriptación
# pip install "passlib[bcrypt]"

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI, Depends, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#Importamos librería jwt
from jose import jwt, JWTError
#Importamos libreria passlib (algoritmo de encriptación)
from passlib.context import CryptContext
#Importamos libreria de fechas para la expiración del token
from datetime import datetime, timedelta

#Creamos un objeto o instancia a partir de la clase FastAPI
app= FastAPI()

#Autenticación por contraseña para eso:
#Creamos un endpoint llamado "login"
oauth2=OAuth2PasswordBearer(tokenUrl="login")

#Creamos contexto de encriptación para eso importamos libreria passlib y elegimos algoritmo de incriptación "bcrypt"
#Utilizamos bcrypt generator para encriptar nuestras contraseñas
crypt= CryptContext(schemes="bcrypt")

# generamos la contraseña encriptada para guardarla en base de datos
#https://bcrypt-generator.com/4

class User(BaseModel):
    username:str
    full_name: str
    email:str
    disabled:bool

#Definimos la clase para el usuario de base de datos 
class UserDB(User):
    password:str
    
#Creo una base de datos no relacional de usuarios 
users_db ={
     "Freddy":{
         "username":"Freddy",
         "full_name": "Freddy García",
         "email": "alfredo.garcias@alumno.buap.mx",
         "disabled": False,
         "password": "$2a$12$Px4/G9Onxs4m6QxjAwsbtOmqf4BFxkLUvn3F5PFPbWmhWLYEyGObG"#"1234"
    },
    "Eliana":{
         "username":"Eliana",
         "full_name": "Eliana Gonzalez",
         "email": "eliana.gonzalez@alumno.buap.mx",
         "disabled": True,
         "password": "$2a$12$hjZJlYEXiyMGyH237boqJerUaIiScb81hgh480cJIfUtlxFSuLa.6"#"5678"
    }
}