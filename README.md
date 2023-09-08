#### detect.py

> detect 裡的 main(model, img) 做港區岸邊設施的物件偵測，輸出為REUSLT CLASS.
>
> main(**model path**, **img path**)

> class RESULT:
>
> ​	boxes:	numpy array, 偵測到的bounding box的xyxy座標（左上、右下）
> ​	cls:		  numpy array, 偵測到的bounding box的類別
> ​	conf:       numpy array, 偵測到的bounding box的信心值
>
> Result[0]: 第一個偵測到的物件、以此類推

____

##### detect.py直接執行範例，資料夾的結構如下，範例照著這個路徑讀一張照片與模型跑偵測。

* yolov8
  * Model:
    * best.pt
  * 0504
    * 103FTASK
      * MAX_0435.JPG