from fastapi import FastAPI
from models.databaseconnection import engine, Base
from routes import user_routes, product_routes, order_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)