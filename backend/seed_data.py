"""
Seed data script for Finance Analytics Dashboard.
Populates the database with sample categories and transactions.
"""

import random
from datetime import datetime, timedelta
from app import create_app, db, Category, Transaction

def seed_database():
    app = create_app()
    with app.app_context():
        print("🌱 Starting database seeding...")

        # Clear existing data
        print("🗑️  Clearing existing data...")
        Transaction.query.delete()
        Category.query.delete()
        db.session.commit()

        # ===== CREATE CATEGORIES =====
        print("📁 Creating categories...")
        categories_data = [
            {'name': 'Salary', 'type': 'income'},
            {'name': 'Freelance', 'type': 'income'},
            {'name': 'Investment', 'type': 'income'},
            {'name': 'Bonus', 'type': 'income'},
            {'name': 'Food', 'type': 'expense'},
            {'name': 'Transport', 'type': 'expense'},
            {'name': 'Entertainment', 'type': 'expense'},
            {'name': 'Rent', 'type': 'expense'},
            {'name': 'Utilities', 'type': 'expense'},
            {'name': 'Shopping', 'type': 'expense'},
            {'name': 'Healthcare', 'type': 'expense'},
            {'name': 'Education', 'type': 'expense'},
        ]

        category_objects = []
        for cat_data in categories_data:
            cat = Category(name=cat_data['name'], type=cat_data['type'])
            db.session.add(cat)
            category_objects.append(cat)
        db.session.commit()
        print(f"   ✅ Created {len(category_objects)} categories")

        income_categories = [c for c in category_objects if c.type == 'income']
        expense_categories = [c for c in category_objects if c.type == 'expense']

        # ===== CREATE TRANSACTIONS =====
        print("💰 Creating transactions...")
        transactions = []
        today = datetime.now().date()

        income_descriptions = [
            'Monthly salary payment', 'Freelance project payment',
            'Dividend payout', 'Performance bonus', 'Client consulting fee',
        ]

        expense_descriptions = {
            'Food': ['Grocery shopping', 'Restaurant dinner', 'Coffee shop', 'Lunch at cafe', 'Takeaway'],
            'Transport': ['Fuel refill', 'Bus ticket', 'Taxi ride', 'Uber trip', 'Car maintenance'],
            'Entertainment': ['Movie tickets', 'Netflix subscription', 'Spotify premium', 'Concert tickets', 'Gaming'],
            'Rent': ['Monthly rent', 'Property maintenance'],
            'Utilities': ['Electricity bill', 'Water bill', 'Internet subscription', 'Phone bill'],
            'Shopping': ['Clothing purchase', 'Electronics', 'Home decor', 'Shoes', 'Accessories'],
            'Healthcare': ['Doctor visit', 'Pharmacy', 'Health insurance', 'Dental checkup'],
            'Education': ['Online course', 'Books', 'Workshop fee', 'Certification exam'],
        }

        # Income transactions (1-2 per month)
        for month_offset in range(6):
            base_date = today - timedelta(days=30 * month_offset)
            for _ in range(random.randint(1, 2)):
                category = random.choice(income_categories)
                amount = round(random.uniform(1500, 5000), 2)
                day = random.randint(1, 28)
                date = base_date.replace(day=day)
                transactions.append({
                    'date': date,
                    'description': random.choice(income_descriptions),
                    'category_id': category.id,
                    'amount': amount,
                    'type': 'income'
                })

        # Expense transactions (5-10 per month)
        for month_offset in range(6):
            base_date = today - timedelta(days=30 * month_offset)
            for _ in range(random.randint(5, 10)):
                category = random.choice(expense_categories)
                if category.name == 'Rent':
                    amount = round(random.uniform(800, 1200), 2)
                elif category.name == 'Utilities':
                    amount = round(random.uniform(50, 200), 2)
                elif category.name == 'Food':
                    amount = round(random.uniform(20, 150), 2)
                else:
                    amount = round(random.uniform(10, 300), 2)
                day = random.randint(1, 28)
                date = base_date.replace(day=day)
                transactions.append({
                    'date': date,
                    'description': random.choice(expense_descriptions[category.name]),
                    'category_id': category.id,
                    'amount': amount,
                    'type': 'expense'
                })

        # Insert all transactions
        for tx_data in transactions:
            tx = Transaction(
                date=tx_data['date'],
                description=tx_data['description'],
                category_id=tx_data['category_id'],
                amount=tx_data['amount'],
                type=tx_data['type']
            )
            db.session.add(tx)

        db.session.commit()
        print(f"   ✅ Created {len(transactions)} transactions")

        # ===== SUMMARY =====
        total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')

        print("\n" + "="*50)
        print("🎉 DATABASE SEEDING COMPLETE!")
        print("="*50)
        print(f"📁 Categories:        {len(categories_data)}")
        print(f"💰 Transactions:      {len(transactions)}")
        print(f"📈 Total Income:      ${total_income:,.2f}")
        print(f"📉 Total Expenses:    ${total_expenses:,.2f}")
        print(f"💵 Net Savings:       ${total_income - total_expenses:,.2f}")
        print("="*50)


if __name__ == '__main__':
    seed_database()