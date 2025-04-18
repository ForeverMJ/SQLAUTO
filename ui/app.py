import streamlit as st
import sys
import os
import subprocess

# 親ディレクトリをPythonパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from agent_graph import graph

st.set_page_config(page_title="SQL 测试 Agent", layout="centered")

st.title("🧪 SQL 自动化测试 Agent")

# Hugging Faceトークン入力
st.markdown("**请输入你的 Hugging Face Token**")
hf_token = st.text_input("🔐 Hugging Face Token", type="password")

st.markdown("---")

sql_code = st.text_area("请输入你的 SQL 查询：", height=200)

if st.button("运行测试"):
    if not sql_code.strip():
        st.warning("请输入 SQL 查询语句。")
    elif not hf_token.strip():
        st.warning("请输入 Hugging Face Token。")
    else:
        with st.spinner("正在处理，请稍候..."):
            try:
                # Hugging Faceトークンを環境変数に設定
                os.environ["HUGGING_FACE_HUB_TOKEN"] = hf_token
                
                # 別のプロセスでテストを実行
                result = graph.invoke({
                    "input_sql": sql_code
                })
                
                st.success("测试完成！")
                st.markdown("### 🧾 测试结果")
                st.code(result["summary"], language="text")
            except Exception as e:
                st.error(f"执行时出错: {str(e)}")
                st.error("詳細なエラー情報:")
                st.exception(e)