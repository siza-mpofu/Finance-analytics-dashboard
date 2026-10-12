from flask import Blueprint, request, jsonify
from db_instance import db
from models.transaction import Transaction
from sqlalchemy import func, text

trends_bp = Blueprint('trends', __name__)


@trends_bp.route('/trends', methods=['GET'])
def get_trends():
    period = request.args.get('period', 30, type=int)
    type_filter = request.args.get('type', 'expense')

    # Build the date expression
    date_expr = func.date_format(Transaction.date, '%Y-%m-%d')

    # Use raw SQL for date_sub with interval
    date_filter = text(
        f"transactions.date >= DATE_SUB(CURDATE(), INTERVAL {period} DAY)"
    )

    results = db.session.query(
        date_expr.label('date'),
        func.sum(Transaction.amount).label('total')
    ).filter(
        Transaction.type == type_filter,
        date_filter
    ).group_by(
        date_expr
    ).order_by(
        date_expr.asc()
    ).all()

    return jsonify([{
        'date': r.date,
        'total': float(r.total or 0),
        'type': type_filter
    } for r in results])