from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"], 
)
class Product(BaseModel):
    id: str
    name: str
    image: str
    saleprice: str
    discount: str

# conn = mysql.connector.connect(
#     host='db',
#     user='root',
#     password='psw123',
#     database='dienmaycholon')
# cursor = conn.cursor()

def connect_to_db():
    db_config = { 
        'host': 'ooo_mysql_container',
        'port': '3306',
        'user': 'root',
        'password': 'psw123',
        'database': 'dienmaycholon'
    }
    return mysql.connector.connect(**db_config)


@app.post("/insert_data")
async def insert_data(product: Product):
    try:
        connection = connect_to_db()
        cursor = connection.cursor
        sql = ("INSERT INTO Product (id, name, image, saleprice, discount) VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(sql, (product.id, product.name, product.image, product.saleprice, product.discount))

        connection.commit()
        
        return {"message": "Data inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_data")
async def get_all_data():
    try:
        connection = connect_to_db()
        cursor = connection.cursor
        cursor.execute('SELECT * FROM Product')

        data = cursor.fetchall()

        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search/")
async def search(search_input: str):
    try:
        connection = connect_to_db()
        cursor = connection.cursor
        sql = "SELECT * FROM Product WHERE name LIKE %s"
        cursor.execute(sql, ("%" + search_input + "%",))

        data = cursor.fetchall()

        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))