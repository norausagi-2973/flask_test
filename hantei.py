from keras import models
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np

#保存したモデルの読み込み
model = model_from_json(open('/content/drive/MyDrive/fish_predict.json').read())
#保存した重みの読み込み
model.load_weights('/content/drive/MyDrive/fish_predict.hdf5')

categories = ["カサゴ","クロダイ","マダイ","マアジ","スズキ","メジナ","カワハギ","シロギス","ギンガメアジ","ムラソイ","ホシササノハベラ","シロメバル","キュウセン","マハゼ","イシダイ","アイゴ","クサフグ","ヒラメ","キチヌ","アカハタ","アイナメ","オハグロベラ","オヤビッチャ","オキフエダイ"]

#画像を読み込む
img_path = "/content/drive/MyDrive/kusafugu.jpeg"

img = image.load_img(img_path,target_size=(150, 150, 3))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

#予測
features = model.predict(x)

#予測結果によって処理を分ける
for i in range(0,24):
  # print(features[0,i])
  if features[0,i] == 1:
      print(categories[i])