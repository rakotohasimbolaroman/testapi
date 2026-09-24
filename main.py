from fastapi import FastAPI
import sqlite3
app = FastAPI()

@app.get("/")

def accueil():
	return {"message":"API Growatt"}

@app.get("/aide")
def aide():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	return {cur}
	
@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
