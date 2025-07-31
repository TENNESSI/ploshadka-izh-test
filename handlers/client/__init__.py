from aiogram import Router
from .start import router as start_router
# from .booking import router as booking_router

router = Router()
router.include_router(start_router)
# router.include_router(booking_router)

__all__ = ['router']