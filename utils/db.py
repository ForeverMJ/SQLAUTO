import sqlite3

def get_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    # 初始化一个简单的测试表（你可以根据实际场景修改）
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    conn.commit()
    return conn