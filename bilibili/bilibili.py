import requests

import re
import json

from .video_url import VideoUrl


class Bilibili:
    """Get a video's all information"""

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

    def __init__(self, bv: str, page: int = 1, cookie: str = "") -> None:
        self.bv = bv
        self.page = page
        self.cookie = cookie

        self.url = f"https://www.bilibili.com/video/{self.bv}/?p={self.page}&vd_source=d661678d00d6e5eb6e143488415a5d0a"
        self.headers = {
            "Cookie": self.cookie,
            "User-Agent": self.user_agent,
            "Referer": self.url,
        }

        """Load all information"""
        raw_html = self.__get_raw_html()

        # extract information from raw html
        playinfo = self.__extract_playinfo(raw_html)
        initial_state = self.__extract_initial_state(raw_html)

        # extract information from initial_state
        self.up = self.__extract_up(initial_state)
        self.title = self.__extract_title(initial_state)
        self.pubdate = self.__extract_pubdate(initial_state)

        # extract information from playinfo
        self.video_urls: VideoUrl = self.__extract_video_urls(playinfo)
        self.audio_url = self.__extract_audio_url(playinfo)

    def __get_raw_html(self) -> str:
        with requests.get(self.url, headers=self.headers) as response:
            if response.status_code == 200:
                return response.text
            else:
                print(response.status_code)
                print(response.text)
                raise Exception("Error when getting raw html")

    def __extract_playinfo(self, raw_html: str) -> dict:
        match = re.search(r"<script>window.__playinfo__=(.*?)</script>", raw_html)
        if match:
            playinfo_str = match.group(1)
            return json.loads(playinfo_str)
        raise Exception("Can't find playinfo in html")

    def __extract_initial_state(self, raw_html: str) -> dict:
        match = re.search(
            r"<script>window.__INITIAL_STATE__=(.*?);\(function\(\)", raw_html
        )
        if match:
            initial_state = match.group(1)
            return json.loads(initial_state)
        raise Exception("Can't find initial_state in html")

    def __extract_up(self, initial_state: dict) -> str:
        return initial_state["videoData"]["owner"]["name"]

    def __extract_title(self, initial_state: dict) -> str:
        return initial_state["videoData"]["title"]

    def __extract_pubdate(self, initial_state: dict) -> int:
        return initial_state["videoData"]["pubdate"]

    def __extract_video_urls(self, playinfo: dict) -> VideoUrl:
        video_url = VideoUrl()
        for obj in playinfo["data"]["dash"]["video"]:
            match obj["id"]:
                case 80:
                    video_url._1080P = obj["baseUrl"]
                case 64:
                    video_url._720P = obj["baseUrl"]
                case 32:
                    video_url._480P = obj["baseUrl"]
                case 16:
                    video_url._360P = obj["baseUrl"]
        return video_url

    def __extract_audio_url(self, playinfo: dict) -> str:
        return playinfo["data"]["dash"]["audio"][0]["baseUrl"]
