
from fastapi import FastAPI, HTTPException
from app.database import get_connection

app = FastAPI(title="E-Commerce Backend")

@app.get("/")
def home():
    return {"message": "E-Commerce Backend is running"}

@app.get("/api/health")
def health():
    return {"status": "healthy"}

@app.get("/api/products")
def get_products():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, name, price, description FROM products"
        )

        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )