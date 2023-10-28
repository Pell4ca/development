# import cv2

# image_path = 'img/MPAN.png'

# # 画像を読み込む
# image = cv2.imread(image_path)

# # BGR形式からRGB形式に変換
# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # SIFTアルゴリズムを作成
# sift = cv2.SIFT_create()

# # 画像から特徴点を抽出
# keypoints, descriptors = sift.detectAndCompute(rgb_image, None)

# # 特徴点を元の画像に描画
# img_with_keypoints = cv2.drawKeypoints(rgb_image, keypoints, outImage=None)

# # 画像を表示
# cv2.imshow("output", img_with_keypoints)
# cv2.waitKey(0)
# cv2.destroyAllWindows()