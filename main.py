from fastapi import FastAPI
import uvicorn
from items_views import router as items_router


app = FastAPI()
app.include_router(items_router, tags=["Items"])

@app.get("/")
def hello():
    return {"message": "success"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

