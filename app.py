from tensorflow.keras import models
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import numpy as np
import os

def canny(filename):
    
    #保存したモデルの読み込み
    model = model_from_json(open('./fish_predict3.json').read())
    #保存した重みの読み込み
    model.load_weights('./fish_predict3.hdf5')
    categories = ["カサゴ","クロダイ","マダイ","マアジ","スズキ","メジナ","カワハギ","シロギス","ギンガメアジ","ムラソイ","ホシササノハベラ","シロメバル","キュウセン","マハゼ","イシダイ","アイゴ","クサフグ","ヒラメ","キチヌ","アカハタ","アイナメ","オハグロベラ","オヤビッチャ","オキフエダイ"]

    #画像を読み込む
    img_path = os.path.abspath(os.path.dirname(__file__)) + '/target/' + filename

    img = image.load_img(img_path,target_size=(150, 150, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    #予測
    features = model.predict(x)

    #予測結果によって処理を分ける
    for i in range(0,24):
      if features[0,i] == 1:
          print(features[0,i])
          return categories[i]