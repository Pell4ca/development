import cv2

def main():

    # 変数の定義
    input_path = './SAMPLE/monkey.png'

    # 画像の読み込み
    image = cv2.imread(input_path)

    # 画像が読み込めなかった場合の例外処理
    if image is None:
        print(f'Failed to load image from {input_path}')
        return

    # 画像情報の表示
    print(f'data:\n{image}')
    print(f'type: {type(image)}')
    print(f'dtype: {image.dtype}')
    print(f'size: {image.size}')
    print(f'shape: {image.shape}')

if __name__ == '__main__':
    main()