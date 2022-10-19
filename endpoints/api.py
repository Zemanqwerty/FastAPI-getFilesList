from fastapi import APIRouter
from config import DIR
from service import api_service


router = APIRouter()


@router.get('/meta')
async def get_files():
    filse_data = await api_service.get_files_data()

    return {'data': filse_data}
