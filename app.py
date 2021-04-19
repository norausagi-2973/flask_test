import cv2
import os

def canny(filename):

    arr = {}
    TARGET_FILE = filename
    IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'
    print(IMG_DIR)
    IMG_SIZE = (200, 200)

    target_img_path = os.path.abspath(os.path.dirname(__file__)) + '/target/' + filename
    target_img = cv2.imread(target_img_path, cv2.IMREAD_GRAYSCALE)
    target_img = cv2.resize(target_img, IMG_SIZE)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    # detector = cv2.ORB_create()
    detector = cv2.AKAZE_create()
    (target_kp, target_des) = detector.detectAndCompute(target_img, None)

    print('TARGET_FILE: %s' % (TARGET_FILE))

    files = os.listdir(IMG_DIR)
    for file in files:
        if file == '.DS_Store' or file == TARGET_FILE:
            continue

        comparing_img_path = IMG_DIR + file
        try:
            comparing_img = cv2.imread(comparing_img_path, cv2.IMREAD_GRAYSCALE)
            comparing_img = cv2.resize(comparing_img, IMG_SIZE)
            (comparing_kp, comparing_des) = detector.detectAndCompute(comparing_img, None)
            matches = bf.match(target_des, comparing_des)
            dist = [m.distance for m in matches]
            ret = sum(dist) / len(dist)
        except cv2.error:
            ret = 100000
            
        arr[file] = ret
        print(file, ret)
        
    arr_sorted = sorted(arr.items(), key=lambda x:x[1])
    kore = next(iter(arr_sorted))[0]
    if kore == "01.jpg":
      return "これはメカバーンのSです！"
    elif kore == "02.jpg":
      return "これはメカバーンのAです！"
    elif kore == "03.jpg":
      return "これはメカバーンのBです！"
    elif kore == "04.jpg":
      return "これはメカバーンのCです！"
    elif kore == "05.jpg":
      return "これはメカバーンのDです！"
    elif kore == "06.jpg":
      return "これはヘルクラウダーのSです！"
    elif kore == "07.jpg":
      return "これはヘルクラウダーのAです！"
    elif kore == "08.jpg":
      return "これはヘルクラウダーのBです！"
    elif kore == "09.jpg":
      return "これはヘルクラウダーのCです！"
    elif kore == "10.jpg":
      return "これはヘルクラウダーのDです！"