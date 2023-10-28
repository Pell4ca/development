import cv2
import os

folder_path = 'Melon_bread_pic'

image_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.png', '.jpeg'))]

#フォルダ内の画像を読み込む
images = []
sift = cv2.SIFT_create()
for image_path in image_files:
    image = cv2.imread(image_path)
    if image is not None:
        images.append(image)
    else:
        print(f"Failed to load image: {image_path}")

# SIFT特徴点の検出と描画
keypoints_list = []
for idx, image in enumerate(images):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    keypoints, descriptors = sift.detectAndCompute(gray_image, None)
    keypoints_list.append(keypoints)
    img_with_keypoints = cv2.drawKeypoints(gray_image, keypoints, outImage=None)
    cv2.imshow(f"Image {idx+1} with Keypoints", img_with_keypoints)

#画像の表示
cv2.waitKey(0)
cv2.destroyAllWindows()
