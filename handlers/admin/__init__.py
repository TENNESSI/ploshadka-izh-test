from aiogram import Router
from .masters import router as masters_router

router = Router()
router.include_router(masters_router)

__all__ = ['router']