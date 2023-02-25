import uuid

import yaml
from fastapi.requests import Request
from fastapi.routing import APIRouter


from fastapi import status, HTTPException

import logging

logger = logging.getLogger()
router = APIRouter(
    prefix="/api/yaml",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_yaml(request: Request):
    logger.info(f"creating YAML")
    yaml_uuid = str(uuid.uuid4())
    raw_body = await request.body()
    try:
        loaded_yaml = yaml.load(raw_body, Loader=yaml.Loader)
        with open(f"yaml_db/{yaml_uuid}.yaml", "w") as f:
            yaml.dump(loaded_yaml, f, sort_keys=False, default_flow_style=False)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    return {"detail": "success", "yaml_doc_id": yaml_uuid}


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
