# Stock Market API 

An API built with **FastAPI** that allows the user to get real time data from Yahoo Finance. With its functions, you can delete companies, add them, and watch the entire dictionary or just one.

## Instalation

Check out the requirements in requirements.txt and install all the libraries to execute the progeam by:

```bash
pip install -r requirements.txt
```

## Structure

* app: Aplication code.
    * repositories
        * YahooFinance.py: Code with the yfinance API that gets the data from the Companies in real time.
    * main.py: main program file.
    * schemas.py: database.

## Database 

The data base `companies` 

| Column      | Data Type   | Description                               |
| ----------- | ----------- | ----------------------------------------- |
| ticker      | TEXT        | The tocker of the stock                   |
| name        | TEXT        | Name of the company                       |
| price       | float       | Price of the stock                        |
| market cap  | TEXT        | Market Capitalization of the company      |
| volume      | INTEGER     | image path                                |
| sector      | TEXT        | Sector of the company                     |



## Usage

* Execute API:

```bash
uvicorn app.main:app --reload
```

Enter on the URL in the Terminal
To Log on Swagger UI add /docs after the link 


* Endpoints:

In SwaggerUI:

```/ (GET)```: Root message to check if the API is running.

```/companies (GET)```: Gets a list of all companies with their market data.

```/companies/{company_id} (GET)```: Gets a specific company by its ID.

```/companies (POST)```: Adds a new company using its ticker symbol.

TO CREATE A COMPANY, "ticker"= "string", CHANGE THE TEXT string to the ticker of certain company example: "AAPL", "PM", "NU"
```/companies/{company_id} (PUT)```: Modifies an existing company.

```/companies/{company_id} (DELETE)```: Deletes a company by its ID.

To stop the API server, kill the terminal process (Ctrl+C).

