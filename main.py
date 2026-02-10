from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def show():
    return {"message":"project deployed sucessfully"}
