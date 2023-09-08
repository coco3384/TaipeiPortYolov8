#### detect.py

* detect 裡的 main(model, img) 做港區岸邊設施的物件偵測，輸出為REUSLT CLASS.
* 在偵測的時候會壓縮圖片來提高偵測效果，因此偵測的結果圖是壓縮後(640 x 640)的。所以我想說我用資料格式存結果，資料格式的boxes裡的座標是原圖尺寸的結果，可能比較方便平台的展圖（？）

##### main( **model path** , **img path** )

##### class RESULT的attribute有以下：

* boxes: numpy array, 偵測到的bounding box的xyxy座標（左上、右下）
* cls: numpy array, 偵測到的bounding box的類別
* conf: numpy array, 偵測到的bounding box的信心值
* img: numpy array, 偵測的結果圖

##### class RESULT的function有以下：

* \__len__(): 回傳總共偵測到幾個物件
* \__getitme__(idx): 回傳偵測到的第idx物件，以dict的方式回傳
* show(): cv2.imshow偵測結果圖(壓縮過的)

> Result[0]: 第一個偵測到的物件，以dict的方式回傳

____

##### detect.py直接執行範例，資料夾的結構如下，範例照著這個路徑讀一張照片與模型跑偵測。

* yolov8
  * Model:
    * best.pt
  * 0504
    * 103FTASK
      * MAX_0435.JPG
