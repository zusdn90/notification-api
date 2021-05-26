from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()


@router.get("/")
async def index(
    session: Session = Depends(db.session),
):
    """
    :param session:
    :return:
    """
    user = Users(status="active", name="HelloWorld")
    session.add(user)
    session.commit()

    Users().create(session, auto_commit=True, name="홍현우")
    current_time = datetime.utcnow()
    return Response(
        f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})"
    )
