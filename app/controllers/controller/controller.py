from fastapi import APIRouter, HTTPException,Cookie, Depends,Header,File, Body,Query
from starlette.responses import JSONResponse
from core.factories import settings
from app.controllers.controller.schemas import TestErrorSchema, TestSchema

router = APIRouter()


@router.get("/",tags=["Test"],
    response_description="test",
    description="test",
    include_in_schema=settings.INCLUDE_SCHEMA,
    response_model=TestSchema, 
    responses={
        404: {"model": TestErrorSchema}
    }
)
async def test_test(test: dict=Body(None,example={"test": "mytest" })) -> JSONResponse:
    if test:
        return JSONResponse({"result" : test.get("test")})

    return JSONResponse({"result" : True})



@router.get("/test",tags=["Test"],
    response_description="test",
    description="test",
    include_in_schema=settings.INCLUDE_SCHEMA,
    response_model=TestSchema, 
    responses={
        404: {"model": TestErrorSchema}
    }
)
async  def test_2(test: str= Query(None, alias="token", title="token", description="Send token in the query"))-> JSONResponse:

    return JSONResponse({"result" : True})

