from fastapi import FastAPI
from sqlite3 import *
app = FastAPI()

@app.get("/")

def accueil():
	return {"message":"API Growatt"}

@app.get("/aide")
def aide():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	f = []
	e = cur.execute("SELECT * FROM Unite")
	for i in e:
		f.append(i[0])
	return {f}
	
@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
