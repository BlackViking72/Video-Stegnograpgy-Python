from ffmpy import FFmpeg
from functions import frame_extract, encode_frame, remove
from threading import Thread

class Encode(Thread):
    def run(self):
        file_name = "video.mp4"  # Source video file to encode
        caesarn = 5
        path_to_ffmpeg = "./ffmpeg"  # Location of ffmpeg package if windows (path to ffmpeg.exe) if linux install ffmpeg package

        frame_extract(str(file_name))

        ff = FFmpeg(
            executable=path_to_ffmpeg,
            global_options=("-y", "-v error"),
            inputs={str(file_name): None},
            outputs={"temp/audio.mp3": ["-q:a", "0", "-map", "a"]}
        )
        ff.run()

        encode_frame("temp", "Hello This is sample text", caesarn)

        fff = FFmpeg(
            executable=path_to_ffmpeg,
            global_options=("-y", "-v error"),
            inputs={"temp/%d.png": None},
            outputs={"temp/video.mov": ["-vcodec", "png"]}
        )
        fff.run()

        ffff = FFmpeg(
            executable=path_to_ffmpeg,
            global_options=("-y", "-v error"),
            inputs={"temp/video.mov": None,
                    "temp/audio.mp3": None},
            outputs={"enc-video.mov": ["-codec", "copy"]}
        )
        ffff.run()

        remove("temp")
        print('Video encoded')


en = Encode()

en.start()
en.join()