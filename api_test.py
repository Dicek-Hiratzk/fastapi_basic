import requests
import json
from datetime import datetime

def main():
    url = "http://localhost:8000/contacts"
    # JSON変換できるようにISO形式に変換 
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "山田さん",
        "email": "test1@test.com",
        "url": "https://example.com",
        "gender": 2,
        "message": "メッセージです",
        "is_enabled": True,
        "created_at": current_datetime
    }
    # json.dumpsでjson型に変換(辞書型のままでは送信できない)
    res = requests.post(url, json.dumps(body))
    print(res.json())

# コマンドを実行したときにだけ動かす
if __name__ == "__main__":
    main()