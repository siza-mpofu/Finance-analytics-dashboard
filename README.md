# Finance Analytics Dashboard

## Project Overview

The Finance Analytics Dashboard is a full-stack web application designed to help users explore financial transactions and understand their financial activity through interactive tables and visual analytics.

The dashboard uses a frontend interface, a Flask REST API, and a MySQL relational database to retrieve, process, and display financial data dynamically.

## Main Features

- Interactive transaction table using DataTables.js
- Search, filtering, sorting, and pagination
- Expense breakdown by category
- Monthly income versus expenses
- Spending trend analysis
- Interactive charts using Chart.js
- RESTful API for communication between the frontend and backend
- Dynamic SQL-based financial summaries
- Validation to ensure transaction types match their categories
- Responsive interface using Bootstrap 5

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- DataTables.js
- Chart.js

### Backend
- Python 3
- Flask
- RESTful APIs

### Database
- MySQL
- SQL aggregation using `SUM()`, `CASE`, `GROUP BY`, and `JOIN`

### Development Tools
- Git
- GitHub
- Postman

## Dashboard Views

### Transactions View

The Transactions view displays financial transactions in an interactive DataTable. Users can search, filter, sort, and navigate through transaction records using server-side pagination.

### Analytics View

The Analytics view presents financial insights using interactive charts, including:

- Expenses by category
- Monthly income versus expenses
- Spending trends over time

## API

The backend provides RESTful API endpoints for retrieving transaction and analytical data.

Example:

`GET /api/transactions?page=1&limit=25&sort=date&order=desc`

Additional endpoints provide category summaries, monthly summaries, and spending trends.

## Database Structure

The database uses two core tables:

- `categories`
- `transactions`

Each transaction is linked to a category using `category_id`. The application includes a validation endpoint that checks whether existing transactions have the same type as their associated categories and reports any mismatches.


## Installation and Setup

### 1. Prerequisites

Before running the application, ensure the following are installed:

- Python 3
- MySQL Server
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/siza-mpofu/Finance-analytics-dashboard.git
cd Finance-analytics-dashboard
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Database

- Create the MySQL database using `backend/db/schema.sql`.
- Copy `backend/.env.example` to `backend/.env`.
- Update the values in `backend/.env` with your own MySQL credentials. Set `DB_NAME` to `finance_dashboard` unless you intentionally use a different database.
- Keep `backend/.env` private and never commit it to GitHub.
- Ensure the database name matches the configuration.

Do not commit your `.env` file or database passwords to GitHub.

### 6. Populate the Database with Sample Data

After creating the database and configuring `backend/.env`, run the sample data script from the project root:

```bash
python backend/seed_data.py
```

This script creates sample income and expense categories and transactions.

**Warning:** Running this script deletes existing transactions and categories before inserting the sample data. Use it only when you intend to reset the database with sample data.


### 7. Start the Backend

From the project root, run:

```bash
cd backend
python app.py
```

The Flask API should be available at:

`http://127.0.0.1:5000`


### 8. Open the Frontend

Open `frontend/index.html` in a browser to access the transactions view. Open `frontend/analytics.html` to access the analytics view.

The frontend requires the Flask backend and MySQL database to be running.



## Project Status

This project is being developed in phases:

1. Conceptual Design
2. Development
3. Finalization

## Project Documentation

The project documentation is organized according to the three development phases:

- [Conception Phase](docs/conception/)
- [Development Phase](docs/development/)
- [Finalization Phase](docs/finalization/)

## Author

Sizalokuhle Mpofu
