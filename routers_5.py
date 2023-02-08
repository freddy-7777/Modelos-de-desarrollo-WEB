#En vez de Importar el framework fastapi, importamos APIRouter a nuestro entorno de trabajo
from fastapi import APIRouter

#En vez de crear fastApi creo APIRouter
router= APIRouter()

#***Instancia productos
@router.get("/products/")
async def products():
    return ["Producto1","Producto2","Producto3","Producto4","Producto5"]    