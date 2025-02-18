from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact]) # 一覧表示
async def get_contact_all():
    dummy_date = datetime.now()
    return [contact_schema.Contact(
        id=1, 
        name="山田", 
        email="test@test.com", 
        url="http://test.com", 
        gender=1, message="テスト", 
        is_enabled=False, 
        created_at=dummy_date
    )]

@router.post("/contacts") # 保存
async def create_contact():
    pass

@router.get("/contacts/{id}") # 詳細表示
async def get_contact():
    pass

@router.put("/contacts/{id}") # 更新
async def update_contact():
    pass

@router.delete("/contacts/{id}") # 削除
async def delete_contact():
    pass
