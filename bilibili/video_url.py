from dataclasses import dataclass


@dataclass
class VideoUrl:
    """Video urls for different quality"""

    _1080P: str | None = None
    _720P: str | None = None
    _480P: str | None = None
    _360P: str | None = None
