import platform
from fastapi import APIRouter, Request
import os
from config import DIR


async def get_files_data():
    files_list = os.listdir(DIR)
    all_files = []

    for file in files_list:

        if platform.system() == 'Windows':
            created_at = os.path.getctime(f'{DIR}/{file}')
        else:
            stat = os.stat(f'{DIR}/{file}')
            try:
                created_at = stat.st_birthtime
            except AttributeError:
                created_at = stat.st_mtime

        file_data = {
            'name': file,
            'type': 'file' if os.path.splitext(file)[1] != '' else 'folder',
            'time': created_at
        }
        
        all_files.append(file_data)

    return all_files