"use client";
import { IconHeart, IconPlay1, TrashIcon } from "@/assets/icons";
import { SongChart } from "@/services/chart/chartHelpers";
import { Song } from "@/services/discovery/discoveryHelpers";
import {
  deleteFavoriteSongs,
  getFavoriteSongs,
  setFavoriteSongs,
  setRecentlyHeardSongs,
  updateSongView,
} from "@/services/library/libraryApi";
import { useSongStore } from "@/stores/songStore";
import { useUserStore } from "@/stores/userStore";
import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<number | null>(null);
  const [songs, setSongs] = useState<SongChart[]>([]);
  const { userID } = useUserStore();
  const { setSong } = useSongStore();

  const getSongs = async () => {
    if (userID) {
      const res = await getFavoriteSongs(userID!);
      setSongs(res.data);
    }
  };
  const handlePlaySong = async (song: Song) => {
    const currentDate = new Date();
    const formattedDate = currentDate.toISOString();
    if (userID) {
      await setRecentlyHeardSongs({
        play_date: formattedDate,
        user_id: userID,
        song_id: song.id,
      });
    } else {
      await updateSongView(song.id);
    }
    setSong(song);
  };
  const handleDeleteFavoriteSong = async (songId: number) => {
    if (userID) await deleteFavoriteSongs(userID, songId);
  };
  useEffect(() => {
    getSongs();
  }, []);
  return (
    <div className="w-full h-[calc(100%_-_84px)] overflow-auto p-10">
      <div className="w-full flex items-center gap-3 mb-8 capitalize text-4xl text-white font-bold">
        Bài hát yêu thích
      </div>
      {songs.length ? (
        songs.map((item, index) => (
          <button
            key={index}
            onMouseEnter={() => setHoveredButton(item.id)}
            onMouseLeave={() => setHoveredButton(null)}
            className="w-full flex items-center text-left p-2.5 text-xs font-light gap-4 text-white rounded focus:bg-[#393243] hover:bg-[#393243] "
          >
            <div className="flex items-center gap-10 w-1/2 mr-2.5">
              <div
                className="flex items-center gap-5 max-w-3xlcursor-default"
                style={{ position: "relative" }}
              >
                <Image
                  src={item.image_file_path}
                  width={60}
                  height={60}
                  alt="Image"
                  className={`rounded-lg w-[60px] h-[60px] ${
                    hoveredButton === item.id && "opacity-50"
                  }`}
                />
                <div className="text-xs tracking-tight text-white">
                  <div className="font-bold">{item.title}</div>
                  <div className="font-light opacity-50">{item.artist}</div>
                </div>
                {hoveredButton === item.id && (
                  <div
                    className="absolute px-4 text-white cursor-pointer"
                    onClick={() => handlePlaySong(item)}
                  >
                    <IconPlay1 />
                  </div>
                )}
              </div>
            </div>
            <div className={`w-1/2 opacity-50`}>{item.albums_title}</div>
            <div
              className="flex gap-5 justify-end items-center mr-0 opacity-50"
              style={{ position: "relative" }}
            >
              {hoveredButton === item.id && (
                <div
                  className="px-12 absolute cursor-pointer"
                  onClick={() => handleDeleteFavoriteSong(item.id)}
                >
                  <TrashIcon />
                </div>
              )}
            </div>
          </button>
        ))
      ) : (
        <div className="flex flex-col items-center justify-center gap-4 p-4 text-neutral-400 text-xl">
          <Image
            src={
              "https://zmp3-static.zmdcdn.me/skins/zmp3-v6.1/images/icons/empty-fav-song-dark.png"
            }
            alt="empty-fav-song"
            width={200}
            height={200}
          />
          Chưa có bài hát nào tại đây!
          <Link
            href={"/"}
            className="bg-[#9b4de0] text-white rounded-3xl py-2 px-4"
          >
            Khám phá ngay
          </Link>
        </div>
      )}
    </div>
  );
}
