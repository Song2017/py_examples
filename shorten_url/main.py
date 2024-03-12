from flask import Flask, request, redirect
import sqlite3
import string
import random

app = Flask(__name__)

# 创建数据库并初始化表
conn = sqlite3.connect('short_links.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_url TEXT NOT NULL,
        short_path TEXT NOT NULL
    )
''')
conn.commit()


# 生成短链接路径
def generate_short_path():
    characters = string.ascii_letters + string.digits
    short_path = ''.join(random.choice(characters) for _ in range(6))  # 生成6位短链接
    return short_path


# 根据短链接查找原始链接
def get_original_url(short_path):
    cursor.execute('SELECT original_url FROM urls WHERE short_path = ?', (short_path,))
    result = cursor.fetchone()
    return result[0] if result else None


# 创建短链接
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_path = generate_short_path()
    cursor.execute('INSERT INTO urls (original_url, short_path) VALUES (?, ?)', (original_url, short_path))
    conn.commit()
    return short_path


# 重定向至原始链接
@app.route('/<short_path>')
def redirect_to_original(short_path):
    original_url = "https://www.baidu.com"  # get_original_url(short_path)
    if original_url:
        return redirect(original_url)
    return "Short URL not found", 404


if __name__ == '__main__':
    app.run(debug=True)
