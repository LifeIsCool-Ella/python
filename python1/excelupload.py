from flask import Flask, request, redirect, url_for, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# SQLite 데이터베이스 연결
DATABASE_URI = 'sqlite:///uploaded_data.db'
engine = create_engine(DATABASE_URI)

# 데이터베이스 테이블 생성
def create_table():
    with engine.connect() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            col1 TEXT,
            col2 TEXT,
            col3 TEXT
        )
        """)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # 엑셀 파일 읽기
        df = pd.read_excel(file)

        # 데이터베이스에 저장
        df.to_sql('data', con=engine, if_exists='append', index=False)

        return 'File uploaded and data saved to database successfully!'

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
