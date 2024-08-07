from database.database_connection import db_session, init_db
from cronjob import init_cron
from flask import Flask
from external_requests.get_user_data import get_daily_user_data
from config import DB_NAME

app = Flask(__name__)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h1>'


@app.route('/users')
def get_users_data():
    get_daily_user_data()
    return '<h1>getting data</h1>'

if __name__ == "__main__":
    init_db()
    init_cron()
    app.run(debug=True, host='0.0.0.0')