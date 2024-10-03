from fastapi import APIRouter, Path
from typing import Annotated

router = APIRouter(prefix="/items")

@router.get("/")
def list_items():
    return {
        "item1",
        "item2",
        "item3",
    }


@router.get("/{item_id}")
def list_items(item_id: Annotated[int, Path(..., ge=1)]):
    return {
        "message": "success",
        "item": item_id,
    }


@router.get("/latest/")
def get_latest_item():
    return{
        "item": "latest",
    }


