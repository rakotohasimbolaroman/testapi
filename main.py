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

@app.post("/gendevis")
def generer():
	from docx import Document
	doc = Document()
	doc.add_paragraph("hello")
	doc.save("devis.docx")

@app.get("/tousproduits")
def gettousprod():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	tout = cur.execute("SELECT * FROM produits")
	compt = 1
	f = {}
	e = {}
	info = {}
	for i in tout:
		e["nom"] = i[1]
		
		info["marque"] = i[3]
		info["type"] = i[4]
		info["prix"] = i[5]
		info["taille"] = i[6]
		info["sary"] = None
		info["sys"] = i[7]
		f[i[1]] = {"unite" : i[2], "marque": i[3], "type":i[4],"prix":i[5],"taille":i[6],"sary":None,"sys":i[7]}

	con.close()
	return f

@app.put("/setprice")
def changepr():
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	tout = cur.execute('UPDATE produits SET prix_unitaire = "20000" WHERE n_produit = "GPEO-6KL1" ')
	con.commit()
