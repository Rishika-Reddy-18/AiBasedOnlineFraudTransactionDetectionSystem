from utils.database import get_connection

def get_user_stats():

    conn = get_connection()
    cursor = conn.cursor()

    # USERS
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # TRANSACTIONS
    cursor.execute("SELECT COUNT(*) FROM transactions")
    total_transactions = cursor.fetchone()[0]

    # FRAUD COUNT
    cursor.execute("""
        SELECT COUNT(*) FROM transactions
        WHERE prediction = 'FRAUD DETECTED'
    """)
    fraud_count = cursor.fetchone()[0]

    # SAFE COUNT
    cursor.execute("""
        SELECT COUNT(*) FROM transactions
        WHERE prediction = 'SAFE TRANSACTION'
    """)
    safe_count = cursor.fetchone()[0]

    conn.close()

    return {
        "total_users": total_users,
        "total_transactions": total_transactions,
        "fraud_count": fraud_count,
        "safe_count": safe_count
    }