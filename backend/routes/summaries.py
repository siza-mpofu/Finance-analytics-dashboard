from flask import Blueprint, request, jsonify
from db_instance import db
from models.transaction import Transaction
from models.category import Category
from sqlalchemy import func, extract, case, text

summaries_bp = Blueprint('summaries', __name__)


@summaries_bp.route('/monthly-summary', methods=['GET'])
def get_monthly_summary():
    months = request.args.get('months', 6, type=int)

    # Build the month expression
    month_expr = func.date_format(Transaction.date, '%Y-%m')

    # Use raw SQL for date_sub with interval
    date_filter = text(
        f"transactions.date >= DATE_SUB(CURDATE(), INTERVAL {months} MONTH)"
    )

    results = db.session.query(
        month_expr.label('month'),
        func.sum(
            case(
                (Transaction.type == 'income', Transaction.amount),
                else_=0
            )
        ).label('income'),
        func.sum(
            case(
                (Transaction.type == 'expense', Transaction.amount),
                else_=0
            )
        ).label('expenses')
    ).filter(
        date_filter
    ).group_by(
        month_expr
    ).order_by(
        month_expr.asc()
    ).all()

    return jsonify([{
        'month': r.month,
        'income': float(r.income or 0),
        'expenses': float(r.expenses or 0),
        'savings': float(r.income or 0) - float(r.expenses or 0)
    } for r in results])


@summaries_bp.route('/category-summary', methods=['GET'])
def get_category_summary():
    month = request.args.get('month')

    if not month:
        query = db.session.query(
            Category.name.label('category'),
            func.sum(Transaction.amount).label('total')
        ).join(
            Transaction, Transaction.category_id == Category.id
        ).filter(
            Transaction.type == 'expense',
            extract('month', Transaction.date) == extract('month', func.current_date()),
            extract('year', Transaction.date) == extract('year', func.current_date())
        ).group_by(
            Category.id, Category.name
        ).order_by(
            func.sum(Transaction.amount).desc()
        ).all()
    else:
        try:
            year, month_num = map(int, month.split('-'))
            query = db.session.query(
                Category.name.label('category'),
                func.sum(Transaction.amount).label('total')
            ).join(
                Transaction, Transaction.category_id == Category.id
            ).filter(
                Transaction.type == 'expense',
                extract('month', Transaction.date) == month_num,
                extract('year', Transaction.date) == year
            ).group_by(
                Category.id, Category.name
            ).order_by(
                func.sum(Transaction.amount).desc()
            ).all()
        except ValueError:
            return jsonify({'error': 'Invalid month format. Use YYYY-MM'}), 400

    return jsonify([{
        'category': r.category,
        'total': float(r.total or 0)
    } for r in query])