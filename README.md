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

Each transaction is linked to a category using `category_id`. Transaction and category types are validated to prevent income transactions from being assigned to expense categories and vice versa.

## Project Status

This project is being developed in phases:

1. Conceptual Design
2. Development
3. Finalization

## Author

Sizalokuhle Mpofu
