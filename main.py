from bilibili import Bilibili
import utils


def download_a_video_and_a_audio():
    bv = "BV1Tw411F7A3"
    bilibili = Bilibili(bv, page=1, cookie="")
    video_url = str(bilibili.video_urls._360P)
    audio_url = bilibili.audio_url

    utils.download(
        url=video_url, filename=f"{bilibili.title}.mp4", headers=bilibili.headers
    )
    utils.download(
        url=audio_url, filename=f"{bilibili.title}.mp3", headers=bilibili.headers
    )


def main():
    download_a_video_and_a_audio()


if __name__ == "__main__":
    main()
