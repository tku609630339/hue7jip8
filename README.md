# 匯入到臺灣言語資料庫
[![Build Status](https://travis-ci.org/sih4sing5hong5/hue7jip8.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/hue7jip8)

會當參考服務的[文件](https://github.com/sih4sing5hong5/tai5-uan5_gian5-gi2_hok8-bu7/wiki/%E5%BF%AB%E9%80%9F%E8%AA%AA%E6%98%8E#%E8%A8%93%E7%B7%B4%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90%E6%A8%A1%E5%9E%8B)

## 族語
```
python manage.py 族語辭典0下載 --下載幾筆 10 # 匯入10筆就好，試驗用
python manage.py 族語辭典0下載 # 完整匯入。較慢，愛五六工
python manage.py 族語辭典1轉檔
python manage.py 族語辭典2匯入
python manage.py 訓練HTS Pangcah 語者
```

## 閩南語
```
bash 下載臺語教典音檔-dropbox.sh # 20160926掠的版本
bash 下載臺語教典音檔-官網沓沓掠.sh # 較慢，愛一工
bash 臺語教典轉wav格式.sh
python manage.py 匯入教典音檔 --匯入幾筆 100 # 匯入100筆就好，試驗用
python manage.py 匯入教典音檔 # 完整匯入
python manage.py 訓練HTS 臺語 王秀容
```
