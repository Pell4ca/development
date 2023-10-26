import cv2

def main():

    # 変数の定義
    input_path = "SAMPLE/monkey.png"

    # 画像の読み込み
    image = cv2.imread(input_path)

    # 画像が読み込めなかった場合の例外処理
    if image is None:
        print('Failed to load image')
        return

    # 画像の表示
    cv2.imshow("sample", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()