import sqlite3
import os

DB_PATH = "users.db"

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

def init_db():
    """Initialize the schema for the authentication database."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            plain_password TEXT NOT NULL,
            national_id TEXT NOT NULL,
            address TEXT NOT NULL,
            monthly_income TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'staff',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

    # Migrate existing DBs that don't have the 'role' column yet
    try:
        c.execute("ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'staff'")
        conn.commit()
    except sqlite3.OperationalError:
        pass  # Column already exists

    conn.close()


def init_admin():
    """Seed the default admin account if no admin exists. Also calls init_db."""
    from src.security import hash_password
    init_db()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE role = 'admin' LIMIT 1")
    if c.fetchone() is None:
        admin_pass = "admin123"
        hashed = hash_password(admin_pass)
        try:
            c.execute(
                '''INSERT INTO users
                   (full_name, phone_number, email, username, password_hash,
                    plain_password, national_id, address, monthly_income, role)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                ("Administrator", "+998000000000", "admin@bank.uz",
                 "admin", hashed, admin_pass,
                 "ADMIN-000", "Bank HQ", "0", "admin")
            )
            conn.commit()
        except sqlite3.IntegrityError:
            pass  # admin username already exists; ensure role is set
    conn.close()


def add_user(username, password_hash, plain_password, full_name, phone_number,
             email, national_id, address, monthly_income, role="staff"):
    """Insert a new user into the database."""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute(
            '''INSERT INTO users
               (full_name, phone_number, email, username, password_hash,
                plain_password, national_id, address, monthly_income, role)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (full_name, phone_number, email, username, password_hash,
             plain_password, national_id, address, monthly_income, role)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False


def get_user(username):
    """Retrieve a full user row by username."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    row = c.fetchone()
    conn.close()
    return row  # sqlite3.Row or None


def get_user_hash(username):
    """Retrieve the password hash for a user (kept for backward compatibility)."""
    row = get_user(username)
    if row:
        return row['password_hash']
    return None


def get_all_staff():
    """Return all bank staff accounts (role='staff')."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        '''SELECT id, full_name, username, email, phone_number, created_at
           FROM users WHERE role = 'staff' ORDER BY created_at DESC'''
    )
    rows = c.fetchall()
    conn.close()
    return rows


def delete_user(username):
    """Delete a user by username. Returns True on success."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username = ? AND role != ?', (username, 'admin'))
    affected = c.rowcount
    conn.commit()
    conn.close()
    return affected > 0


def update_password(username, new_hash, new_plain):
    """Update the password for an existing user. Returns True on success."""
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        'UPDATE users SET password_hash = ?, plain_password = ? WHERE username = ?',
        (new_hash, new_plain, username)
    )
    affected = c.rowcount
    conn.commit()
    conn.close()
    return affected > 0
