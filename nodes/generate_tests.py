# 基于 SQL 自动生成测试用例
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import traceback

# グローバル変数としてモデルとトークナイザーを保持
_model = None
_tokenizer = None

def load_model():
    global _model, _tokenizer
    try:
        if _model is None or _tokenizer is None:
            print("モデルを読み込んでいます...")
            model_name = "deepseek-ai/deepseek-coder-1.3b-base"
            
            # トークンの確認
            if "HUGGING_FACE_HUB_TOKEN" not in os.environ:
                raise ValueError("Hugging Faceトークンが設定されていません")
            
            _tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                token=os.environ["HUGGING_FACE_HUB_TOKEN"]
            )
            _model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map="auto",
                trust_remote_code=True,
                token=os.environ["HUGGING_FACE_HUB_TOKEN"]
            )
            print("モデルの読み込みが完了しました")
    except Exception as e:
        print(f"モデルの読み込み中にエラーが発生しました: {str(e)}")
        print(traceback.format_exc())
        raise

def generate_test_cases(state):
    try:
        sql = state["sql"]
        
        # モデルの読み込み（初回のみ）
        load_model()
        
        prompt = f"""
你是一个 SQL 测试专家，请为以下查询生成5个不同场景的 SQL 测试用例（可以是 insert/select/update/delete）：
{sql}
每个测试用例请以一行 SQL 语句输出。
"""
        
        print("テストケースを生成中...")
        # モデルで生成
        inputs = _tokenizer(prompt, return_tensors="pt").to(_model.device)
        outputs = _model.generate(
            **inputs,
            max_length=500,
            temperature=0.7,
            do_sample=True,
            top_p=0.95,
            repetition_penalty=1.1
        )
        result = _tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("テストケースの生成が完了しました")
        
        # 結果の処理
        test_cases = [line for line in result.strip().split("\n") if line]
        state["tests"] = test_cases
        return state
    except Exception as e:
        print(f"テストケース生成中にエラーが発生しました: {str(e)}")
        print(traceback.format_exc())
        state["error"] = f"テストケース生成エラー: {str(e)}"
        return state