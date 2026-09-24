from fastapi import FastAPI
from sqlite3 import *
app = FastAPI()

@app.get("/")

def accueil():
	return {"message":"API Growatt"}

@app.get("/aide")
def aide():
	return {"Hello"}
	
@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
