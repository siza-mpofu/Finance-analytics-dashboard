from flask import Blueprint, request, jsonify
from db_instance import db
from models.transaction import Transaction
from models.category import Category

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    # Get query parameters
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 25, type=int)
    sort = request.args.get('sort', 'date')
    order = request.args.get('order', 'desc')
    category = request.args.get('category')
    type_filter = request.args.get('type')
    search = request.args.get('search')

    # Build query
    query = Transaction.query

    # Apply filters
    if category:
        query = query.join(Transaction.category).filter(Category.name == category)

    if type_filter:
        query = query.filter(Transaction.type == type_filter)

    if search:
        query = query.filter(Transaction.description.ilike(f'%{search}%'))

    # Apply sorting
    if sort == 'date':
        order_column = Transaction.date
    elif sort == 'amount':
        order_column = Transaction.amount
    elif sort == 'category':
        order_column = Category.name
        query = query.join(Transaction.category)
    else:
        order_column = Transaction.id

    if order == 'desc':
        query = query.order_by(order_column.desc())
    else:
        query = query.order_by(order_column.asc())

    # Paginate
    paginated = query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        'data': [t.to_dict() for t in paginated.items],
        'pagination': {
            'page': page,
            'limit': limit,
            'total': paginated.total,
            'pages': paginated.pages
        }
    })


@transactions_bp.route('/transactions/validate', methods=['GET'])
def validate_transactions():
    """Check whether transaction types match their category types."""
    mismatches = []

    transactions = Transaction.query.join(
        Transaction.category
    ).all()

    for transaction in transactions:
        if transaction.type != transaction.category.type:
            mismatches.append({
                'transaction_id': transaction.id,
                'transaction_type': transaction.type,
                'category': transaction.category.name,
                'category_type': transaction.category.type
            })

    return jsonify({
        'valid': len(mismatches) == 0,
        'checked': len(transactions),
        'mismatches': mismatches
    })



@transactions_bp.route('/transactions/<int:tx_id>', methods=['GET'])
def get_transaction(tx_id):
    transaction = Transaction.query.get_or_404(tx_id)
    return jsonify(transaction.to_dict())
