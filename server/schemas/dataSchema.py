# from typing import List, Dict

# from pydantic import BaseModel

# class ItemModel(BaseModel):
#     encodeId: str
#     title: str
#     alias: str
#     isOffical: bool
#     artistsNames: str
#     # Add other fields as needed

# class DetailedSongModel(BaseModel):
#     encodeId: str
#     title: str
#     alias: str
#     isOffical: bool
#     username: str
#     artistsNames: str
#     artists: List[ArtistModel]
#     isWorldWide: bool
#     previewInfo: PreviewInfoModel
#     thumbnailM: str
#     link: str
#     thumbnail: str
#     duration: int
#     zingChoice: bool
#     isPrivate: bool
#     preRelease: bool
#     releaseDate: int
#     genreIds: List[str]
#     album: AlbumModel
#     distributor: str
#     indicators: List[Dict]
#     isIndie: bool
#     streamingStatus: int
#     allowAudioAds: bool
#     hasLyric: bool
#     rakingStatus: int
#     releasedAt: int

# class ZingMp3DataModel(BaseModel):
#     err: int
#     msg: str
#     data: DetailedSongModel
#     timestamp: int
