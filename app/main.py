
from fastapi import FastAPI, HTTPException
from app.schemas import Company
from app.repositories.YahooFinance import get_data

app = FastAPI(title="Stock Market API")

# Inicializamos la base de datos con GGAL, YPF y PAM
companies = [
    {"name": "Grupo Financiero Galicia", "ticker": "GGAL", "price": 0, "market_cap": 0, "sector": "", "volume": 0},
    {"name": "YPF S.A.", "ticker": "YPF", "price": 0, "market_cap": 0, "sector": "", "volume": 0},
    {"name": "Pampa Energía", "ticker": "PAM", "price": 0, "market_cap": 0, "sector": "", "volume": 0},
]

def update_company_data(company):
    stock_data = get_data(company["ticker"])
    if stock_data:
        company.update(stock_data)  # Solo actualiza si hay datos nuevos
    return company

@app.get("/")
def root():
    return {"message": "Stock Market API is running!"}

@app.get("/companies")
def get_companies():
    return {"companies": [update_company_data(company) for company in companies]}  # Retorna JSON estructurado

@app.get("/companies/{company_id}")
def get_company(company_id: int):
    if company_id < 0 or company_id >= len(companies):
        raise HTTPException(status_code=404, detail="Company not found")
    return update_company_data(companies[company_id])

@app.post("/companies")
def create_company(company: Company):
    for existing in companies:
        if existing["ticker"] == company.ticker:
            raise HTTPException(status_code=400, detail="Company already exists")

    
    stock_data = get_data(company.ticker)
    if not stock_data:
        raise HTTPException(status_code=400, detail="Invalid ticker or data not available")

    companies.append(stock_data)  # Guardar empresa con los datos obtenidos
    return {"message": "Company added", "company": stock_data}

@app.put("/companies/{company_id}")
def update_company(company_id: int, company: Company):
    if company_id < 0 or company_id >= len(companies):
        raise HTTPException(status_code=404, detail="Company not found")
    companies[company_id] = company.model_dump()
    return companies[company_id]

@app.delete("/companies/{company_id}")
def delete_company(company_id: int):
    if company_id < 0 or company_id >= len(companies):
        raise HTTPException(status_code=404, detail="Company not found")
    companies.pop(company_id)
    return {"message": "Company deleted"}
