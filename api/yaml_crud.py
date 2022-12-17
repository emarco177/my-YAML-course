from fastapi.requests import Request
from fastapi.routing import APIRouter


from fastapi import status

import logging

logger = logging.getLogger()
router = APIRouter(
    prefix="/api/yaml",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_yaml(request: Request):
    logger.info(f"creating YAML")
    return {"detail": "Hello World"}


@router.get("/{yaml_doc_id}")
def read_yaml(yaml_doc_id: str):
    return {"detail": "Hello World"}


@router.put("/{yaml_doc_id}")
async def update_yaml(yaml_doc_id: str, request: Request):
    return {"detail": "Hello World"}


@router.delete("/{yaml_doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_yaml(yaml_doc_id: str):
    return {"detail": "Hello World"}


@router.get("/")
def read_yaml_list():
    return {"detail": "Hello World"}
