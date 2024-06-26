# 開発開始
```python
pip install fastapi
pip install "uvicorn[standard]"
```

## firebase
```python
pip install --upgrade firebase-admin
```

# 実行
```python
python -m uvicorn main:app --reload
```

# 変更を共有(github)
まずは git の [install](https://prog-8.com/docs/git-env-win) をする
コードの変更を保存すること！
```bash
git add .
git commit -m "何を変更したかを書く"
git push
```

# 変更を取得
```bash
git pull
```
# 開発開始
```python
pip install fastapi
pip install "uvicorn[standard]"
```

## firebase
```python
pip install --upgrade firebase-admin
```

# 実行
```python
python -m uvicorn main:app --reload
```

# 変更を共有
コードの変更を保存すること！
```bash
git add .
git commit -m "何を変更したかを書く"
git push
```

# 変更を取得
```bash
git pull
```

# Firebase にデータを保存する
[公式ドキュメンㇳ](https://firebase.google.com/docs/firestore/manage-data/add-data?hl=ja&authuser=0)を参照
```python
data = {"name": "Los Angeles", "state": "CA", "country": "USA"}
# Add a new doc in collection 'cities' with ID 'LA'
db.collection("cities").document("LA").set(data)
```
↑　のサンプルコードの data を 受け取ったデータにする。

```db.collection("Parking").document(deviceId).set(data)```

のようにする。