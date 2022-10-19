from fastapi import FastAPI
import uvicorn
from endpoints import api

app = FastAPI(title='FastAPI homework')
app.include_router(api.router, prefix='/api')


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)