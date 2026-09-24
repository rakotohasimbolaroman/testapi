from fastapi import FastAPI
app = FastAPI()

@app.get("/")

def accueil():
	return {"message":"API Growatt"}

@app.post("/devis")
def creer_devis(client,num):
	return{
		"success":True,
		"Client": client,
		"num": num
	}
