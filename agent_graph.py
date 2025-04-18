from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional

from nodes.input_node import handle_input
from nodes.validate_syntax import validate_sql
from nodes.generate_tests import generate_test_cases
from nodes.run_tests import run_generated_tests
from nodes.summarize import summarize

# 状態の型定義
class State(TypedDict):
    input_sql: str
    sql: Optional[str]
    tests: Optional[List[str]]
    results: Optional[List[dict]]
    summary: Optional[str]
    error: Optional[str]

# LangGraph 状态图定义
workflow = StateGraph(State)

workflow.add_node("input_node", handle_input)
workflow.add_node("validate_syntax", validate_sql)
workflow.add_node("generate_tests", generate_test_cases)
workflow.add_node("run_tests", run_generated_tests)
workflow.add_node("summarize_result", summarize)

workflow.set_entry_point("input_node")
workflow.add_edge("input_node", "validate_syntax")
workflow.add_edge("validate_syntax", "generate_tests")
workflow.add_edge("generate_tests", "run_tests")
workflow.add_edge("run_tests", "summarize_result")
workflow.add_edge("summarize_result", END)

graph = workflow.compile()