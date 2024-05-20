from fastapi import FastAPI  # noqa: INP001
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root() -> JSONResponse:
    """テスト.

    Returns
    -------
        JSONResponse: メッセージ

    """
    return JSONResponse(content={"message": "hello world"})
