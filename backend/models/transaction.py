from db_instance import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    type = db.Column(db.Enum('income', 'expense'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.relationship('Category', backref='transactions', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description,
            'category': self.category.name if self.category else None,
            'category_id': self.category_id,
            'amount': float(self.amount),
            'type': self.type
        }