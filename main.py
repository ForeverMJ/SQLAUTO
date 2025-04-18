# 入口文件，运行 Agent
from agent_graph import graph

if __name__ == "__main__":
    input_sql = open("test_sql.sql", "r").read()
    result = graph.invoke({"input_sql": input_sql})
    print(result["summary"])