# 运行测试用例
from utils.db import get_connection

def run_generated_tests(state):
    conn = get_connection()
    cursor = conn.cursor()
    passed, failed = 0, 0
    errors = []

    for test_sql in state["tests"]:
        try:
            cursor.execute(test_sql)
            passed += 1
        except Exception as e:
            failed += 1
            errors.append(f"SQL: {test_sql}\n错误: {str(e)}")

    state.update({
        "passed": passed,
        "failed": failed,
        "errors": errors
    })
    return state