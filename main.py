from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional
import uuid

app = FastAPI(title="Collify Mock API", version="1.0.0")
security = HTTPBearer()

# -----------------------------------------------------------------------
# Generato automaticamente da export_products_for_mock.py
# Database: prodotti esportati da Odoo
# Data generazione: 2026-05-11 20:57:11 UTC
# Totale prodotti: 191
# -----------------------------------------------------------------------

VALID_USERS = {
    "admin": "admin123",
    "acquashop": "acquashop123",
}

MOCK_TRANSACTIONS = [
    # ACQUA PURA 2ltx6 | ref: PF877 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 1,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 1, "idTransaction": 1, "idProduct": 299, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE 2 LT | ref: BORB. BLU 100 CLD | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 2,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 2, "idTransaction": 2, "idProduct": 300, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE LT 2x6 | ref: C620 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 3,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 3, "idTransaction": 3, "idProduct": 301, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE BLU 1x150 | ref: BLU.150 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 4,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 4, "idTransaction": 4, "idProduct": 302, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE RED 1x150 | ref: RED.150 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 5,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 5, "idTransaction": 5, "idProduct": 303, "quantity": 1, "price": 1.00},
        ]
    },
    # COCA COLA 0.9ltx6 | ref: 01379 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 6,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 6, "idTransaction": 6, "idProduct": 304, "quantity": 1, "price": 1.00},
        ]
    },
    # DOLCE GUSTO RED X90 | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 7,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 7, "idTransaction": 7, "idProduct": 305, "quantity": 1, "price": 1.00},
        ]
    },
    # DON CARLO RED 1x100 | ref: DONCARLO.RED.100 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 8,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 8, "idTransaction": 8, "idProduct": 306, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA 1,5 LT | ref: BORB. BLU 150 CLD | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 9,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 9, "idTransaction": 9, "idProduct": 307, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA LT 1,5X6 | ref: IT06080 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 10,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 10, "idTransaction": 10, "idProduct": 308, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5L | ref: BORB. RED 100 CLD | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 11,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 11, "idTransaction": 11, "idProduct": 309, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5Lx6 | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 12,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 12, "idTransaction": 12, "idProduct": 310, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI 2 LT | ref: BORB. RED 150 CLD | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 13,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 13, "idTransaction": 13, "idProduct": 311, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI LT 2X6 | ref: 10029 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 14,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 14, "idTransaction": 14, "idProduct": 312, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE | ref: DOLCE GUSTO RED | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 15,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 15, "idTransaction": 15, "idProduct": 313, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE 2lt x 6 | ref: 14743 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 16,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 16, "idTransaction": 16, "idProduct": 314, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE 1,5 | ref: DON CARLO RED | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 17,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 17, "idTransaction": 17, "idProduct": 315, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE LT 1,5X6 | ref: 2095 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 18,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 18, "idTransaction": 18, "idProduct": 316, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 19,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 19, "idTransaction": 19, "idProduct": 317, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA LT 2 X 6 | ref: 4903314 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 20,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 20, "idTransaction": 20, "idProduct": 318, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 1 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 21,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 21, "idTransaction": 21, "idProduct": 319, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 22,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 22, "idTransaction": 22, "idProduct": 320, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZ. 1L | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 23,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 23, "idTransaction": 23, "idProduct": 321, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZZANTE LT 1X6 | ref: C211 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 24,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 24, "idTransaction": 24, "idProduct": 322, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 1X6 | ref: C212 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 25,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 25, "idTransaction": 25, "idProduct": 323, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 2 X 6 | ref: C220 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 26,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 26, "idTransaction": 26, "idProduct": 324, "quantity": 1, "price": 1.00},
        ]
    },
    # NESPRESSO RED1x100 | ref: RESPRESSO.RED.100 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 27,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 27, "idTransaction": 27, "idProduct": 325, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 28,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 28, "idTransaction": 28, "idProduct": 326, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT x6 | ref: 28.0023 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 29,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 29, "idTransaction": 29, "idProduct": 327, "quantity": 1, "price": 1.00},
        ]
    },
    # PURA 2LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 30,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 30, "idTransaction": 30, "idProduct": 328, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 31,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 31, "idTransaction": 31, "idProduct": 329, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE LT 2X6 | ref: 28.0022 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 32,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 32, "idTransaction": 32, "idProduct": 330, "quantity": 1, "price": 1.00},
        ]
    },
    # RESPRESSO RED 100 | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 33,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 33, "idTransaction": 33, "idProduct": 331, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA 1,5 | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 34,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 34, "idTransaction": 34, "idProduct": 332, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA LT 1,5X6 | ref: 10015 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 35,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 35, "idTransaction": 35, "idProduct": 333, "quantity": 1, "price": 1.00},
        ]
    },
    # S.ANNA  2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 36,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 36, "idTransaction": 36, "idProduct": 334, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 37,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 37, "idTransaction": 37, "idProduct": 335, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA lt 2 x6 | ref: SABLT2 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 38,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 38, "idTransaction": 38, "idProduct": 336, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENDETTO 0,50 FRIZZ | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 39,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 39, "idTransaction": 39, "idProduct": 337, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 0,50 NAT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 40,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 40, "idTransaction": 40, "idProduct": 338, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 1,5 LT FRIZ | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 41,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 41, "idTransaction": 41, "idProduct": 339, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 42,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 42, "idTransaction": 42, "idProduct": 340, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 0,5X12 | ref: 1556.12 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 43,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 43, "idTransaction": 43, "idProduct": 341, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 1,5X6 | ref: 10211 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 44,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 44, "idTransaction": 44, "idProduct": 342, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO LT 2x6 | ref: 10213 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 45,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 45, "idTransaction": 45, "idProduct": 343, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO NAT. LT 0,5X12 | ref: 1555.12 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 46,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 46, "idTransaction": 46, "idProduct": 344, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO 1,5L | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 47,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 47, "idTransaction": 47, "idProduct": 345, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO LT 1,5X6 | ref: 12500114 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 48,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 48, "idTransaction": 48, "idProduct": 346, "quantity": 1, "price": 1.00},
        ]
    },
    # SANT'ANNA LT 2 X 6 | ref: 00020 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 49,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 49, "idTransaction": 49, "idProduct": 347, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 50,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 50, "idTransaction": 50, "idProduct": 348, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA LT 2x6 | ref: 8018800202748 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 51,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 51, "idTransaction": 51, "idProduct": 349, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 52,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 52, "idTransaction": 52, "idProduct": 350, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT x6 | ref: 10014 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 53,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 53, "idTransaction": 53, "idProduct": 351, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT | ref:  | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 54,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 54, "idTransaction": 54, "idProduct": 352, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT x6 | ref: 10210 - 4905012 | company: AcquaShop Petrosino srl (Gaia)
    {
        "id": 55,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 55, "idTransaction": 55, "idProduct": 353, "quantity": 1, "price": 1.00},
        ]
    },
    # ACQUA PURA 2ltx6 | ref: PF877 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 56,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 56, "idTransaction": 56, "idProduct": 409, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE 2 LT | ref: BORB. BLU 100 CLD | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 57,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 57, "idTransaction": 57, "idProduct": 410, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE LT 2x6 | ref: C620 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 58,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 58, "idTransaction": 58, "idProduct": 411, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE BLU 1x150 | ref: BLU.150 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 59,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 59, "idTransaction": 59, "idProduct": 412, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE RED 1x150 | ref: RED.150 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 60,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 60, "idTransaction": 60, "idProduct": 413, "quantity": 1, "price": 1.00},
        ]
    },
    # COCA COLA 0.9ltx6 | ref: 01379 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 61,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 61, "idTransaction": 61, "idProduct": 414, "quantity": 1, "price": 1.00},
        ]
    },
    # DOLCE GUSTO RED X90 | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 62,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 62, "idTransaction": 62, "idProduct": 415, "quantity": 1, "price": 1.00},
        ]
    },
    # DON CARLO RED 1x100 | ref: DONCARLO.RED.100 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 63,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 63, "idTransaction": 63, "idProduct": 416, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA 1,5 LT | ref: BORB. BLU 150 CLD | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 64,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 64, "idTransaction": 64, "idProduct": 417, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA LT 1,5X6 | ref: IT06080 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 65,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 65, "idTransaction": 65, "idProduct": 418, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5L | ref: BORB. RED 100 CLD | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 66,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 66, "idTransaction": 66, "idProduct": 419, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5Lx6 | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 67,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 67, "idTransaction": 67, "idProduct": 420, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI 2 LT | ref: BORB. RED 150 CLD | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 68,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 68, "idTransaction": 68, "idProduct": 421, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI LT 2X6 | ref: 10029 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 69,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 69, "idTransaction": 69, "idProduct": 422, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE | ref: DOLCE GUSTO RED | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 70,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 70, "idTransaction": 70, "idProduct": 423, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE 2lt x 6 | ref: 14743 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 71,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 71, "idTransaction": 71, "idProduct": 424, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE 1,5 | ref: DON CARLO RED | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 72,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 72, "idTransaction": 72, "idProduct": 425, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE LT 1,5X6 | ref: 2095 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 73,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 73, "idTransaction": 73, "idProduct": 426, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 74,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 74, "idTransaction": 74, "idProduct": 427, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA LT 2 X 6 | ref: 4903314 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 75,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 75, "idTransaction": 75, "idProduct": 428, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 1 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 76,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 76, "idTransaction": 76, "idProduct": 429, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 77,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 77, "idTransaction": 77, "idProduct": 430, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZ. 1L | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 78,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 78, "idTransaction": 78, "idProduct": 431, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZZANTE LT 1X6 | ref: C211 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 79,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 79, "idTransaction": 79, "idProduct": 432, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 1X6 | ref: C212 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 80,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 80, "idTransaction": 80, "idProduct": 433, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 2 X 6 | ref: C220 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 81,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 81, "idTransaction": 81, "idProduct": 434, "quantity": 1, "price": 1.00},
        ]
    },
    # NESPRESSO RED1x100 | ref: RESPRESSO.RED.100 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 82,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 82, "idTransaction": 82, "idProduct": 435, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 83,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 83, "idTransaction": 83, "idProduct": 436, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT x6 | ref: 28.0023 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 84,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 84, "idTransaction": 84, "idProduct": 437, "quantity": 1, "price": 1.00},
        ]
    },
    # PURA 2LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 85,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 85, "idTransaction": 85, "idProduct": 438, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 86,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 86, "idTransaction": 86, "idProduct": 439, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE LT 2X6 | ref: 28.0022 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 87,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 87, "idTransaction": 87, "idProduct": 440, "quantity": 1, "price": 1.00},
        ]
    },
    # RESPRESSO RED 100 | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 88,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 88, "idTransaction": 88, "idProduct": 441, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA 1,5 | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 89,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 89, "idTransaction": 89, "idProduct": 442, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA LT 1,5X6 | ref: 10015 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 90,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 90, "idTransaction": 90, "idProduct": 443, "quantity": 1, "price": 1.00},
        ]
    },
    # S.ANNA  2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 91,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 91, "idTransaction": 91, "idProduct": 444, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 92,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 92, "idTransaction": 92, "idProduct": 445, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA lt 2 x6 | ref: SABLT2 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 93,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 93, "idTransaction": 93, "idProduct": 446, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENDETTO 0,50 FRIZZ | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 94,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 94, "idTransaction": 94, "idProduct": 447, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 0,50 NAT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 95,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 95, "idTransaction": 95, "idProduct": 448, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 1,5 LT FRIZ | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 96,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 96, "idTransaction": 96, "idProduct": 449, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 97,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 97, "idTransaction": 97, "idProduct": 450, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 0,5X12 | ref: 1556.12 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 98,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 98, "idTransaction": 98, "idProduct": 451, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 1,5X6 | ref: 10211 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 99,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 99, "idTransaction": 99, "idProduct": 452, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO LT 2x6 | ref: 10213 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 100,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 100, "idTransaction": 100, "idProduct": 453, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO NAT. LT 0,5X12 | ref: 1555.12 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 101,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 101, "idTransaction": 101, "idProduct": 454, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO 1,5L | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 102,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 102, "idTransaction": 102, "idProduct": 455, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO LT 1,5X6 | ref: 12500114 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 103,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 103, "idTransaction": 103, "idProduct": 456, "quantity": 1, "price": 1.00},
        ]
    },
    # SANT'ANNA LT 2 X 6 | ref: 00020 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 104,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 104, "idTransaction": 104, "idProduct": 457, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 105,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 105, "idTransaction": 105, "idProduct": 458, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA LT 2x6 | ref: 8018800202748 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 106,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 106, "idTransaction": 106, "idProduct": 459, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 107,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 107, "idTransaction": 107, "idProduct": 460, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT x6 | ref: 10014 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 108,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 108, "idTransaction": 108, "idProduct": 461, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT | ref:  | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 109,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 109, "idTransaction": 109, "idProduct": 462, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT x6 | ref: 10210 - 4905012 | company: AcquaShop Trapani srl (Gaia)
    {
        "id": 110,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 110, "idTransaction": 110, "idProduct": 463, "quantity": 1, "price": 1.00},
        ]
    },
    # Sant'Anna - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 111,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 111, "idTransaction": 111, "idProduct": 218, "quantity": 1, "price": 1.00},
        ]
    },
    # Norda - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 112,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 112, "idTransaction": 112, "idProduct": 219, "quantity": 1, "price": 1.00},
        ]
    },
    # Lieve - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 113,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 113, "idTransaction": 113, "idProduct": 220, "quantity": 1, "price": 1.00},
        ]
    },
    # San Bernardo - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 114,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 114, "idTransaction": 114, "idProduct": 221, "quantity": 1, "price": 1.00},
        ]
    },
    # Lete - Lete Ferrarelle | ref:  | company: Acquashop Pesaro srl
    {
        "id": 115,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 115, "idTransaction": 115, "idProduct": 222, "quantity": 1, "price": 1.00},
        ]
    },
    # Sant' Anna - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 116,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 116, "idTransaction": 116, "idProduct": 223, "quantity": 1, "price": 1.00},
        ]
    },
    # San Bernardo - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 117,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 117, "idTransaction": 117, "idProduct": 224, "quantity": 1, "price": 1.00},
        ]
    },
    # Eva - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 118,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 118, "idTransaction": 118, "idProduct": 225, "quantity": 1, "price": 1.00},
        ]
    },
    # Monviso - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 119,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 119, "idTransaction": 119, "idProduct": 226, "quantity": 1, "price": 1.00},
        ]
    },
    # S.Benedetto - Frizzante 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 120,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 120, "idTransaction": 120, "idProduct": 227, "quantity": 1, "price": 1.00},
        ]
    },
    # Monviso - Frizzante 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 121,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 121, "idTransaction": 121, "idProduct": 228, "quantity": 1, "price": 1.00},
        ]
    },
    # Lieve - Frizzante 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 122,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 122, "idTransaction": 122, "idProduct": 229, "quantity": 1, "price": 1.00},
        ]
    },
    # S.benedet 0,5frizz12bottiglie - Frizzante 0,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 123,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 123, "idTransaction": 123, "idProduct": 230, "quantity": 1, "price": 1.00},
        ]
    },
    # Levissima  - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 124,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 124, "idTransaction": 124, "idProduct": 231, "quantity": 1, "price": 1.00},
        ]
    },
    # Ferrarelle - Lete Ferrarelle | ref:  | company: Acquashop Pesaro srl
    {
        "id": 125,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 125, "idTransaction": 125, "idProduct": 232, "quantity": 1, "price": 1.00},
        ]
    },
    # Mia 6x1,5Lt - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 126,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 126, "idTransaction": 126, "idProduct": 233, "quantity": 1, "price": 1.00},
        ]
    },
    # San Benedetto 2lt - Naturale 2 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 127,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 127, "idTransaction": 127, "idProduct": 234, "quantity": 1, "price": 1.00},
        ]
    },
    # Valmora lt 1,5 - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 128,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 128, "idTransaction": 128, "idProduct": 235, "quantity": 1, "price": 1.00},
        ]
    },
    # San Benedetto 05x12 Nat - Naturale 0,5 Litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 129,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 129, "idTransaction": 129, "idProduct": 236, "quantity": 1, "price": 1.00},
        ]
    },
    # Coca Cola 0.33 Vetro - Coca Cola &  The | ref:  | company: Acquashop Pesaro srl
    {
        "id": 130,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 130, "idTransaction": 130, "idProduct": 237, "quantity": 1, "price": 1.00},
        ]
    },
    # Eva 1 litro - Naturale 1 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 131,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 131, "idTransaction": 131, "idProduct": 238, "quantity": 1, "price": 1.00},
        ]
    },
    # The  Pesca 6 x 1,5 - Coca Cola &  The | ref:  | company: Acquashop Pesaro srl
    {
        "id": 132,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 132, "idTransaction": 132, "idProduct": 239, "quantity": 1, "price": 1.00},
        ]
    },
    # The Limone 1,5 x 6 - Coca Cola &  The | ref:  | company: Acquashop Pesaro srl
    {
        "id": 133,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 133, "idTransaction": 133, "idProduct": 240, "quantity": 1, "price": 1.00},
        ]
    },
    # Levissima 1,5 - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 134,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 134, "idTransaction": 134, "idProduct": 241, "quantity": 1, "price": 1.00},
        ]
    },
    # S.Bernardo nat 8 bott - Naturale 0,5 Litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 135,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 135, "idTransaction": 135, "idProduct": 242, "quantity": 1, "price": 1.00},
        ]
    },
    # S.Benedet1,5 nat - Naturale 1,5 litri | ref:  | company: Acquashop Pesaro srl
    {
        "id": 136,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 136, "idTransaction": 136, "idProduct": 243, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE LT 2x6 | ref: C620 | company: Gaia Srl
    {
        "id": 137,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 137, "idTransaction": 137, "idProduct": 111, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA LT 1,5X6 | ref: IT06080 | company: Gaia Srl
    {
        "id": 138,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 138, "idTransaction": 138, "idProduct": 112, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5Lx6 | ref:  | company: Gaia Srl
    {
        "id": 139,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 139, "idTransaction": 139, "idProduct": 113, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI LT 2X6 | ref: 10029 | company: Gaia Srl
    {
        "id": 140,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 140, "idTransaction": 140, "idProduct": 114, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE 2lt x 6 | ref: 14743 | company: Gaia Srl
    {
        "id": 141,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 141, "idTransaction": 141, "idProduct": 115, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE LT 1,5X6 | ref: 2095 | company: Gaia Srl
    {
        "id": 142,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 142, "idTransaction": 142, "idProduct": 116, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA LT 2 X 6 | ref: 4903314 | company: Gaia Srl
    {
        "id": 143,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 143, "idTransaction": 143, "idProduct": 117, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 1X6 | ref: C212 | company: Gaia Srl
    {
        "id": 144,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 144, "idTransaction": 144, "idProduct": 118, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA LT 2 X 6 | ref: C220 | company: Gaia Srl
    {
        "id": 145,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 145, "idTransaction": 145, "idProduct": 119, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZZANTE LT 1X6 | ref: C211 | company: Gaia Srl
    {
        "id": 146,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 146, "idTransaction": 146, "idProduct": 120, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT x6 | ref: 28.0023 | company: Gaia Srl
    {
        "id": 147,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 147, "idTransaction": 147, "idProduct": 121, "quantity": 1, "price": 1.00},
        ]
    },
    # ACQUA PURA 2ltx6 | ref: PF877 | company: Gaia Srl
    {
        "id": 148,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 148, "idTransaction": 148, "idProduct": 122, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE LT 2X6 | ref: 28.0022 | company: Gaia Srl
    {
        "id": 149,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 149, "idTransaction": 149, "idProduct": 123, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA LT 1,5X6 | ref: 10015 | company: Gaia Srl
    {
        "id": 150,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 150, "idTransaction": 150, "idProduct": 124, "quantity": 1, "price": 1.00},
        ]
    },
    # SANT'ANNA LT 2 X 6 | ref: 00020 | company: Gaia Srl
    {
        "id": 151,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 151, "idTransaction": 151, "idProduct": 125, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA lt 2 x6 | ref: SABLT2 | company: Gaia Srl
    {
        "id": 152,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 152, "idTransaction": 152, "idProduct": 126, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 0,5X12 | ref: 1556.12 | company: Gaia Srl
    {
        "id": 153,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 153, "idTransaction": 153, "idProduct": 127, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO NAT. LT 0,5X12 | ref: 1555.12 | company: Gaia Srl
    {
        "id": 154,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 154, "idTransaction": 154, "idProduct": 128, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO FRIZZANTE LT 1,5X6 | ref: 10211 | company: Gaia Srl
    {
        "id": 155,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 155, "idTransaction": 155, "idProduct": 129, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO LT 2x6 | ref: 10213 | company: Gaia Srl
    {
        "id": 156,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 156, "idTransaction": 156, "idProduct": 130, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO LT 1,5X6 | ref: 12500114 | company: Gaia Srl
    {
        "id": 157,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 157, "idTransaction": 157, "idProduct": 131, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA LT 2x6 | ref: 8018800202748 | company: Gaia Srl
    {
        "id": 158,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 158, "idTransaction": 158, "idProduct": 132, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT x6 | ref: 10014 | company: Gaia Srl
    {
        "id": 159,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 159, "idTransaction": 159, "idProduct": 133, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT x6 | ref: 10210 - 4905012 | company: Gaia Srl
    {
        "id": 160,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 160, "idTransaction": 160, "idProduct": 134, "quantity": 1, "price": 1.00},
        ]
    },
    # COCA COLA 0.9ltx6 | ref: 01379 | company: Gaia Srl
    {
        "id": 161,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 161, "idTransaction": 161, "idProduct": 135, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE BLU 1x150 | ref: BLU.150 | company: Gaia Srl
    {
        "id": 162,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 162, "idTransaction": 162, "idProduct": 136, "quantity": 1, "price": 1.00},
        ]
    },
    # CIALDA BORBONE RED 1x150 | ref: RED.150 | company: Gaia Srl
    {
        "id": 163,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 163, "idTransaction": 163, "idProduct": 137, "quantity": 1, "price": 1.00},
        ]
    },
    # DOLCE GUSTO RED X90 | ref:  | company: Gaia Srl
    {
        "id": 164,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 164, "idTransaction": 164, "idProduct": 138, "quantity": 1, "price": 1.00},
        ]
    },
    # DON CARLO RED 1x100 | ref: DONCARLO.RED.100 | company: Gaia Srl
    {
        "id": 165,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 165, "idTransaction": 165, "idProduct": 139, "quantity": 1, "price": 1.00},
        ]
    },
    # NESPRESSO RED1x100 | ref: RESPRESSO.RED.100 | company: Gaia Srl
    {
        "id": 166,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 166, "idTransaction": 166, "idProduct": 140, "quantity": 1, "price": 1.00},
        ]
    },
    # CAVAGRANDE 2 LT | ref: BORB. BLU 100 CLD | company: Gaia Srl
    {
        "id": 167,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 167, "idTransaction": 167, "idProduct": 141, "quantity": 1, "price": 1.00},
        ]
    },
    # EVA 1,5 LT | ref: BORB. BLU 150 CLD | company: Gaia Srl
    {
        "id": 168,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 168, "idTransaction": 168, "idProduct": 142, "quantity": 1, "price": 1.00},
        ]
    },
    # FERRARELLE 1,5L | ref: BORB. RED 100 CLD | company: Gaia Srl
    {
        "id": 169,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 169, "idTransaction": 169, "idProduct": 143, "quantity": 1, "price": 1.00},
        ]
    },
    # GERACI 2 LT | ref: BORB. RED 150 CLD | company: Gaia Srl
    {
        "id": 170,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 170, "idTransaction": 170, "idProduct": 144, "quantity": 1, "price": 1.00},
        ]
    },
    # LA FONTE | ref: DOLCE GUSTO RED | company: Gaia Srl
    {
        "id": 171,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 171, "idTransaction": 171, "idProduct": 145, "quantity": 1, "price": 1.00},
        ]
    },
    # LETE 1,5 | ref: DON CARLO RED | company: Gaia Srl
    {
        "id": 172,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 172, "idTransaction": 172, "idProduct": 146, "quantity": 1, "price": 1.00},
        ]
    },
    # LEVISSIMA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 173,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 173, "idTransaction": 173, "idProduct": 147, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 1 LT | ref:  | company: Gaia Srl
    {
        "id": 174,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 174, "idTransaction": 174, "idProduct": 148, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 175,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 175, "idTransaction": 175, "idProduct": 149, "quantity": 1, "price": 1.00},
        ]
    },
    # MANGIATORELLA FRIZ. 1L | ref:  | company: Gaia Srl
    {
        "id": 176,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 176, "idTransaction": 176, "idProduct": 150, "quantity": 1, "price": 1.00},
        ]
    },
    # NORDA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 177,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 177, "idTransaction": 177, "idProduct": 151, "quantity": 1, "price": 1.00},
        ]
    },
    # PURA 2LT | ref:  | company: Gaia Srl
    {
        "id": 178,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 178, "idTransaction": 178, "idProduct": 152, "quantity": 1, "price": 1.00},
        ]
    },
    # REALE 2 LT | ref:  | company: Gaia Srl
    {
        "id": 179,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 179, "idTransaction": 179, "idProduct": 153, "quantity": 1, "price": 1.00},
        ]
    },
    # RESPRESSO RED 100 | ref:  | company: Gaia Srl
    {
        "id": 180,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 180, "idTransaction": 180, "idProduct": 154, "quantity": 1, "price": 1.00},
        ]
    },
    # ROCCHETTA 1,5 | ref:  | company: Gaia Srl
    {
        "id": 181,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 181, "idTransaction": 181, "idProduct": 155, "quantity": 1, "price": 1.00},
        ]
    },
    # S.ANNA  2 LT | ref:  | company: Gaia Srl
    {
        "id": 182,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 182, "idTransaction": 182, "idProduct": 156, "quantity": 1, "price": 1.00},
        ]
    },
    # SABRINELLA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 183,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 183, "idTransaction": 183, "idProduct": 157, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENDETTO 0,50 FRIZZ | ref:  | company: Gaia Srl
    {
        "id": 184,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 184, "idTransaction": 184, "idProduct": 158, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 0,50 NAT | ref:  | company: Gaia Srl
    {
        "id": 185,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 185, "idTransaction": 185, "idProduct": 159, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 1,5 LT FRIZ | ref:  | company: Gaia Srl
    {
        "id": 186,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 186, "idTransaction": 186, "idProduct": 160, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BENEDETTO 2 LT | ref:  | company: Gaia Srl
    {
        "id": 187,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 187, "idTransaction": 187, "idProduct": 161, "quantity": 1, "price": 1.00},
        ]
    },
    # SAN BERNARDO 1,5L | ref:  | company: Gaia Srl
    {
        "id": 188,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 188, "idTransaction": 188, "idProduct": 162, "quantity": 1, "price": 1.00},
        ]
    },
    # SERRICELLA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 189,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 189, "idTransaction": 189, "idProduct": 163, "quantity": 1, "price": 1.00},
        ]
    },
    # ULIVETO 1,5 LT | ref:  | company: Gaia Srl
    {
        "id": 190,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 190, "idTransaction": 190, "idProduct": 164, "quantity": 1, "price": 1.00},
        ]
    },
    # VERA 2 LT | ref:  | company: Gaia Srl
    {
        "id": 191,
        "idUser": 1,
        "data": (datetime.utcnow() - timedelta(hours=1)).isoformat(),
        "costo": 1.00,
        "metodoPagamento": "CASH",
        "soldiInseriti": 1.00,
        "resto": 0.00,
        "products": [
            {"id": 191, "idTransaction": 191, "idProduct": 165, "quantity": 1, "price": 1.00},
        ]
    },
]

ACTIVE_TOKENS: dict = {}


class JwtRequest(BaseModel):
    username: str
    password: str


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token not in ACTIVE_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return ACTIVE_TOKENS[token]


def parse_date(date_str: str) -> datetime:
    for fmt in ('%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise HTTPException(status_code=400, detail=f"Formato data non valido: {date_str}")


@app.get("/", tags=["health"])
def health_check():
    return {
        "status": "ok",
        "service": "Collify Mock API",
        "products_loaded": 191,
        "time": datetime.utcnow().isoformat()
    }


@app.post("/api/authenticate", tags=["jwt-authentication-controller"])
def authenticate(body: JwtRequest):
    expected = VALID_USERS.get(body.username)
    if not expected or expected != body.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = str(uuid.uuid4())
    ACTIVE_TOKENS[token] = {"username": body.username, "id": 1}
    return {
        "accessToken": token,
        "user": {"id": 1, "username": body.username, "role": "ADMIN", "enabled": True}
    }


@app.get("/api/history/transactions", tags=["history-controller"])
def get_transactions(
    startDate: str = Query(...),
    endDate: str = Query(...),
    page: int = Query(0),
    pageSize: int = Query(50),
    user=Depends(verify_token)
):
    start = parse_date(startDate)
    end = parse_date(endDate)
    filtered = [t for t in MOCK_TRANSACTIONS
                if start <= datetime.fromisoformat(t["data"]) <= end]
    total = len(filtered)
    paginated = filtered[page * pageSize:(page + 1) * pageSize]
    return {"content": paginated, "totalElements": total, "page": page, "pageSize": pageSize}


@app.get("/api/history/product", tags=["history-controller"])
def get_product_history(
    productId: int = Query(...),
    startDate: str = Query(...),
    endDate: str = Query(...),
    page: int = Query(0),
    pageSize: int = Query(50),
    user=Depends(verify_token)
):
    start = parse_date(startDate)
    end = parse_date(endDate)
    results = []
    for t in MOCK_TRANSACTIONS:
        if not (start <= datetime.fromisoformat(t["data"]) <= end):
            continue
        for p in t.get("products", []):
            if p["idProduct"] == productId:
                results.append({
                    "idProduct": p["idProduct"],
                    "quantity": p["quantity"],
                    "price": p["price"],
                    "idTransaction": p["idTransaction"],
                    "transactionDate": t["data"],
                })
    paginated = results[page * pageSize:(page + 1) * pageSize]
    return {"content": paginated, "totalElements": len(results), "page": page, "pageSize": pageSize}


@app.get("/api/refreshToken", tags=["jwt-authentication-controller"])
def refresh_token(user=Depends(verify_token)):
    new_token = str(uuid.uuid4())
    ACTIVE_TOKENS[new_token] = user
    return {"accessToken": new_token, "user": user}
