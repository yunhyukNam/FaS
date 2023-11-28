from PIL import Image
import numpy as np
import os

def extract_filename(image_path):
    filename = os.path.basename(image_path)
    return filename

def encode_message(image_path, message):
    img = Image.open(image_path)
    
    pixels = np.array(img)

    message_bytes = message.encode('utf-8')

    # 데이터 길이를 배열에 추가
    data_length = len(message_bytes)
    if (data_length < 0 or data_length > 16777215):
        print("Data must be between 0 and 16777215")
        exit(1)
    
    length_bytes = data_length.to_bytes(4, byteorder='big')
    data_with_length = bytearray(length_bytes) + message_bytes

    pixel_index = 0
    for i in range(len(data_with_length)):
        byte = data_with_length[i]
        for j in range(8):
            pixels.flat[pixel_index] &= 0b11111110  # 마지막 비트를 0으로 설정
            pixels.flat[pixel_index] |= (byte & 1)  # 마지막 비트에 메시지 비트 삽입
            byte >>= 1
            pixel_index += 1

    encoded_image = Image.fromarray(pixels)

    encoded_image.save("encoded_image.jpg")

def decode_message(image_path):
    img = Image.open(image_path)
    
    pixels = np.array(img)

    data_length = 0
    for i in range(4):
        data_length |= pixels.flat[i] & 0b1
        if i < 3:
            data_length <<= 8

    decoded_message = bytearray()
    pixel_index = 32
    for i in range(data_length):
        byte = 0
        for j in range(8):
            byte |= (pixels.flat[pixel_index] & 0b1) << j
            pixel_index += 1
        decoded_message.append(byte)

    decoded_message_str = decoded_message.decode()
    print("Decoded Message:", decoded_message_str)

#--------------------------------------------------------------------

message = input("Encoding data input : ")
image_path = "C:/Users/Doubl/OneDrive - KookminUNIV/그림/Cat03.jpg"
image_name = extract_filename(image_path)

encode_message(image_path, message)
decode_message("encoded_image.jpg")