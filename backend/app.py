from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

# Environment variables
DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'changeme')
DB_NAME = os.getenv('DB_NAME', 'appdb')


@app.get('/api/health')
def health():
    """Health check endpoint."""
    return jsonify(status='ok')


@app.get('/api')
def index():
    """Simple greeting from MySQL."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from MySQL via Flask!'")
        row = cur.fetchone()
        return jsonify(message=row[0])
    except mysql.connector.Error as e:
        return jsonify(error=str(e)), 500
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


@app.get('/api/time')
def get_time():
    """Fetch current MySQL server time."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW()")
        row = cur.fetchone()
        server_time = str(row[0]) if row else None
        return jsonify(server_time=server_time)
    except mysql.connector.Error as e:
        return jsonify(error=str(e)), 500
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
