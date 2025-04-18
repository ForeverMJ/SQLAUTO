# 汇总测试结果
def summarize(state):
    summary = f"✅ 测试通过：{state['passed']} 条\n❌ 失败：{state['failed']} 条\n"
    if state['errors']:
        summary += "\n详细错误信息：\n" + "\n".join(state['errors'])
    return {"summary": summary}