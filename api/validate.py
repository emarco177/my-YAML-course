from typing import Dict
from fastapi.applications import Request
from fastapi.routing import APIRouter

import logging

logger = logging.getLogger()


router = APIRouter(
    prefix="/api/validate",
)


@router.post("/")
async def validate(request: Request) -> Dict[str, str]:
    logger.info(f"Validating Yaml from user")
    return {"detail": "Hello World"}
