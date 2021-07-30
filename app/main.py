from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_client, close_db
from api.api_router import form_router
app = FastAPI()
app.add_event_handler("startup", get_db_client)
app.add_event_handler("shutdown", close_db)
#app.add_middleware(SessionMiddleware, secret_key="!secret")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)