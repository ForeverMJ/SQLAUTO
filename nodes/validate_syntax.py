# SQL 语法校验节点
import sqlparse

def validate_sql(state):
    sql = state["sql"]
    try:
        sqlparse.parse(sql)
        return state
    except Exception as e:
        return {"error": f"语法错误: {str(e)}"}