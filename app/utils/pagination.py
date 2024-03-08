from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession


async def paginate(
    session: AsyncSession,
    query,
    page: int = 1,
    per_page: int = 10,
):
    """
    Paginate a SQLModel query.
    :param session: The SQLAlchemy session instance.
    :param query: The SQLModel query to paginate.
    :param page: The page number to retrieve.
    :param per_page: The number of items per page.
    :return: Tuple containing the paginated data and pagination information.
    """
    total_items = await session.execute(select(func.count()).select_from(query))
    count = total_items.scalar()

    if count == 0:
        return [], {"total_pages": 0, "current_page": 0, "next_page": None}

    total_pages = (count - 1) // per_page + 1

    if page > total_pages:
        raise HTTPException(status_code=404, detail="Page not found")

    offset = (page - 1) * per_page
    items = await session.scalars(query.offset(offset).limit(per_page))
    result = items.all()

    next_page = page + 1 if page < total_pages else None

    pagination = {
        "total_pages": total_pages,
        "current_page": page,
        "next_page": next_page,
    }

    return result, pagination
