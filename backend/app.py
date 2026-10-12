from flask import Flask
from flask_cors import CORS
from config import Config
from db_instance import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize db with app
    db.init_app(app)
    CORS(app)

    # Import and register routes
    from routes.transactions import transactions_bp
    from routes.summaries import summaries_bp
    from routes.trends import trends_bp

    app.register_blueprint(transactions_bp, url_prefix='/api')
    app.register_blueprint(summaries_bp, url_prefix='/api')
    app.register_blueprint(trends_bp, url_prefix='/api')

    return app

# ⬇️ Re-export models so seed_data.py can import them
from models.category import Category
from models.transaction import Transaction

__all__ = ['create_app', 'db', 'Category', 'Transaction']

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)