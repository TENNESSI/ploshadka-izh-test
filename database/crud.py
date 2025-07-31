from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Master, Service, Booking
from .database import get_db

# Функция для получения сессии БД
def get_session():
    return next(get_db())

def get_masters(db: Session):
    """Получить всех активных мастеров"""
    return db.query(Master).all()

def add_master(db: Session, name: str):
    """Добавить нового мастера"""
    master = Master(name=name)
    db.add(master)
    db.commit()
    db.refresh(master)
    return master

def get_services_by_master(db: Session, master_id: int):
    """Получить услуги конкретного мастера"""
    stmt = select(Service).join(Master.services).where(Master.id == master_id)
    return db.execute(stmt).scalars().all()

def create_booking(db: Session, client_id: int, master_id: int, service_id: int, date: str, time: str):
    """Создать новую запись"""
    booking = Booking(
        client_id=client_id,
        master_id=master_id,
        service_id=service_id,
        date=date,
        time=time
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking