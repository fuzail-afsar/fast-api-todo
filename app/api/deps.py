from fastapi import Query, Depends
from typing import Annotated


def pagination(offset: int = 0, limit: int = Query(default=100, le=100)):
    return {"offset": offset, "limit": limit}


Pagination = Annotated[dict, Depends(pagination)]
