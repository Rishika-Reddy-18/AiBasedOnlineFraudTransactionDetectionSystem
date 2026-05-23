from utils.database import get_connection


# =========================
# REGISTER USER
# =========================
def register_user(username, email, password, role="user"):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # 🔍 check username exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return "USERNAME_EXISTS"

        # 🔍 check email exists
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return "EMAIL_EXISTS"

        # ✅ insert only if both are unique
        cursor.execute("""
            INSERT INTO users (username, email, password, role)
            VALUES (?, ?, ?, ?)
        """, (username, email, password, role))

        conn.commit()
        return "SUCCESS"

    except Exception as e:
        conn.rollback()
        print(e)
        return "ERROR"

    finally:
        cursor.close()
        conn.close()

# =========================
# VALIDATE USER (LOGIN FIX)
# =========================
def validate_user(username_or_email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE (username = ? OR email = ?) AND password = ?
    """, (username_or_email, username_or_email, password))

    user = cursor.fetchone()

    conn.close()
    return user

# =========================
# OPTIONAL: GET ALL USERS (ADMIN)
# =========================
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()