from functions import frame_extract, decode_frame, remove
from threading import Thread


class Decode(Thread):
    file_name = "enc-video.mov"  # Video to be decoded
    caesarn = 5

    frame_extract(str(file_name))
    decoded_text = decode_frame("temp", caesarn)
    remove("temp")
    print("Decoded...")
    print('Decoded Text: ', decoded_text)


de = Decode()
de.start()
