import tkinter as tk
from tkinter import messagebox
import os

def save_api_key():
    api_key = api_key_entry.get()
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        messagebox.showinfo("成功", "APIキーが保存されました")
        root.destroy()
    else:
        messagebox.showerror("エラー", "APIキーを入力してください")

root = tk.Tk()
root.title("OpenAI APIキー設定")
root.geometry("400x150")

# APIキー入力フィールド
api_key_label = tk.Label(root, text="OpenAI APIキーを入力してください:")
api_key_label.pack(pady=10)

api_key_entry = tk.Entry(root, width=40, show="*")
api_key_entry.pack(pady=10)

# 保存ボタン
save_button = tk.Button(root, text="保存", command=save_api_key)
save_button.pack(pady=10)

root.mainloop() 