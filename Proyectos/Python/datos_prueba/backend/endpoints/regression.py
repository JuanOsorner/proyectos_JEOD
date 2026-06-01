from fastapi import APIRouter

from services.bitcoin_service import BitcoinService
from domain.regresion_lineal import RegresionLineal

router = APIRouter()


@router.get("/regression/bitcoin")
def bitcoin_regression():

    data = BitcoinService.get_bitcoin_prices()

    result = RegresionLineal.fit(
        data["x"],
        data["y"]
    )

    return {
        "data_points": result["samples"],
        "intercept": result["intercept"],
        "slope": result["slope"]
    }