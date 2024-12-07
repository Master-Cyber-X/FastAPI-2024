from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



import sqlite3

con = sqlite3.connect('Data\\data.db', check_same_thread=False)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Staffs (id INT,username TEXT,branch TEXT,salary TEXT)')

class Add_User(BaseModel):
    id:int
    username:str
    brachs:str
    salary:str

list_users = [
    Add_User(id=120021,username='سامي مغير',brachs='الرياض', salary='2500'),
    Add_User(id=990021,username='سامي الفقية',brachs='جدة', salary='3500'),
    Add_User(id=990021,username='سامي شيبان',brachs='الدمام', salary='5200'),
    Add_User(id=139121,username='احمد مطر',brachs='الدمام', salary='6500')
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_method=["*"],
    allow_header=["*"]
)
@app.get('/list_users/')
async def get_user():
    try:
        data = cur.execute('SELECT * FROM Staffs').fetchall()
        print(data)
        return data
    except sqlite3.Error as e:
        print(e)

@app.post("/list_users/")
async def add_user(New_user:Add_User):
    try:
        cur.execute(f'INSERT INTO Staffs VALUES("{New_user.id}","{New_user.username}")')
        con.commit()
        return New_user
    except sqlite3.Error as msg:
        print(msg)

@app.put('/list_users/{user_id  }')
async def update(id:int,user:Add_User):
    try:
        cur.execute(f'UPDATE Staffs SET user="Alu" WHERE id = "{id}"')
        con.commit()
    except sqlite3.Error as msg:
        print(msg)



@app.delete('/list_users/{user_id  }')
async def update(id:int,user:Add_User):
    try:
        print(id)
        cur.execute(f'DELETE FROM Staffs WHERE id = "{id}"')
        con.commit()
    except sqlite3.Error as msg:
        print(msg)