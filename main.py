from fastapi import FastAPI
import sqlite3
app = FastAPI()

@app.get("/")
def accueil():
	return {"message":"Bienvenue Chez Growatt Madagascar"}

@app.get("/allunite")
def getallunite():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	tout = cur.execute("SELECT * FROM unite")
	f = {}
	for i in tout:
		f[i[0]] = i[1]
	return f

@app.get("/alltype")
def getalltype():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	tout = cur.execute("SELECT * FROM type")
	f = {}
	for i in tout:
		f[i[0]] = i[1]
	con.close()
	return f

@app.get("/prodprtype")
def getprodbytype(type):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	e = cur.execute(f"SELECT * FROM produits where id_type='{type}'").fetchall()
	f = {}
	nb = 0
	for i in e:
		f[nb] = i[1]
		nb += 1
	return f

@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
