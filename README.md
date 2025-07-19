## 📝 靜脈特徵增強演算法

使用 Python 實現參考文獻的靜脈特徵增強演算法。

### 🔗 參考文獻
- IEEE TRANSACTIONS ON INDUSTRIAL INFORMATICS: [Recognizing Palm Vein in Smartphones Using RGB Images](https://ieeexplore.ieee.org/document/9648012)

### 📁 壓所檔內容
- `vein_enhance.py` - 主程式
- `requirements.txt` - Python3.9.2 用到的函式庫及其版本

## 📊 測試結果

| 輸入影像 | 靜脈增強結果 |
|-------------|-----------------|
| ![Input](image/input.png) | ![Enhanced](image/enhanced.png) |

## 🚀 如何使用
請輸入以下指令建置 Python3.9.2 環境用到的函式庫及其版本:
```
pip install -r .\requirements.txt
```
請將 `vein_enhance.py` 中的變數 `image_path` 替換為您想測試的靜脈影像，並輸入以下指令執行程式:
```
python .\vein_enhance.py 
```
