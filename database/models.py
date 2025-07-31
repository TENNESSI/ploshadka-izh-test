from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Связь многие-ко-многим: Мастер ↔ Услуги
master_service = Table(
    "master_service",
    Base.metadata,
    Column("master_id", Integer, ForeignKey("masters.id")),
    Column("service_id", Integer, ForeignKey("services.id")),
)

class Master(Base):
    __tablename__ = "masters"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    services = relationship("Service", secondary=master_service, back_populates="masters")

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer)
    masters = relationship("Master", secondary=master_service, back_populates="services")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)
    master_id = Column(Integer, ForeignKey("masters.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    date = Column(String(10))  # Формат: 'YYYY-MM-DD'
    time = Column(String(5))   # Формат: 'HH:MM'