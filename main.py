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
	tout = cur.execute("SELECT * FROM unite")
	f = {}
	for i in tout:
		f[i[0]] = i[1]
	return f
	
@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
