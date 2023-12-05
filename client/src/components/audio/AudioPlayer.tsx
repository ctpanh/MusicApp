"use client";
import { useSongStore } from "@/stores/songStore";
import React, { useState, useRef, useEffect, use } from "react";
import { FaPlay, FaPause, FaVolumeUp, FaVolumeDown } from "react-icons/fa";
import {
  IoShuffleOutline,
  IoPlayCircleOutline,
  IoRepeat,
  IoPauseCircleOutline,
} from "react-icons/io5";
import { MdSkipPrevious, MdSkipNext } from "react-icons/md";

import Image from "next/image";

interface AudioPlayerProps {
  audioSource: string;
}

const AudioPlayer: React.FC<AudioPlayerProps> = ({ audioSource }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const {
    song,
    songID,
    isPlaying,
    volume,
    songTime,
    setSong,
    setIsPlaying,
    setVolume,
    setSongTime,
  } = useSongStore();
  const playPauseHandler = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const volumeChangeHandler = (newVolume: number) => {
    if (newVolume >= 0 && newVolume <= 1) {
      setVolume(newVolume);
      if (audioRef.current) {
        audioRef.current.volume = newVolume;
      }
    }
  };
  const handleSongTimeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newSongTime = parseFloat(e.target.value);
    setSongTime(newSongTime);
    if (audioRef.current) {
      audioRef.current.currentTime = newSongTime;
    }
  };
  const formatTime = (seconds: number): string => {
    if (seconds === 0 || Number.isNaN(seconds)) {
      return "00:00";
    }
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    const formattedMinutes = String(minutes).padStart(2, "0");
    const formattedSeconds = String(remainingSeconds).padStart(2, "0");
    return `${formattedMinutes}:${formattedSeconds}`;
  };
  useEffect(() => {
    const updateSongTime = () => {
      if (audioRef.current) {
        setSongTime(audioRef.current.currentTime);
      }
    };

    if (audioRef.current) {
      audioRef.current.addEventListener("timeupdate", updateSongTime);
    }

    return () => {
      if (audioRef.current) {
        audioRef.current.removeEventListener("timeupdate", updateSongTime);
      }
    };
  }, []);

  useEffect(() => {
    const newSong = {
      id: 1,
      album_id: 1,
      playlist_id: 1,
      title: "String",
      artist: "string",
      audio_file_path:
        "https://vnso-zn-23-tf-a320-zmp3.zmdcdn.me/a5e0debc57e4d8a6fd251b8835df717a?authen=exp=1701971212~acl=/a5e0debc57e4d8a6fd251b8835df717a/*~hmac=353a1aff8eb71658a72f7463d78cbae5",
      image_file_path: "/next.svg",
      release_date: "2023/11/2",
      views: 0,
    };
    setSong(newSong);
  }, []);
  return (
    <div className="h-full flex justify-between border rounded-white shadow-md text-white">
      <div
        className="flex items-center p-2 gap-5 max-w-3xl rounded focus:bg-[#393243] hover:bg-[#393243] cursor-default"
        style={{ position: "relative" }}
      >
        <div className="w-[60px] h-[60px] flex items-center">
          {song && (
            <Image
              src={song.image_file_path}
              width={60}
              height={60}
              alt="Image"
            />
          )}
        </div>
        <div className="text-xs tracking-tight text-white">
          <div className="font-bold">{song?.title}</div>
          <div className="font-light opacity-50">{song?.artist}</div>
        </div>
      </div>

      <div className="flex flex-col justify-center gap">
        <audio ref={audioRef} src={song?.audio_file_path} />
        <div className="flex justify-center items-center gap-4">
          <IoShuffleOutline className="w-8 h-8" />
          <MdSkipPrevious className="w-8 h-8" />
          <button onClick={playPauseHandler}>
            {isPlaying ? (
              <IoPauseCircleOutline className="w-12 h-12" />
            ) : (
              <IoPlayCircleOutline className="w-12 h-12" />
            )}
          </button>
          <MdSkipNext className="w-8 h-8" />
          <IoRepeat className="w-8 h-8" />
        </div>
        <div className="flex items-center justify-center gap-2">
          <span>{formatTime(songTime)}</span>
          <input
            type="range"
            min={0}
            max={audioRef.current ? audioRef.current.duration : 0}
            step={1}
            value={songTime}
            onChange={handleSongTimeChange}
            className="w-[300px]"
          />
          <span>
            {formatTime(audioRef.current ? audioRef.current.duration : 0)}
          </span>
        </div>
      </div>
      <div className="flex items-center gap-2 p-2">
        <FaVolumeDown
          className="cursor-pointer"
          onClick={() => volumeChangeHandler(volume - 0.1)}
        />
        <input
          type="range"
          min={0}
          max={1}
          step={0.01}
          value={volume}
          onChange={(event) =>
            volumeChangeHandler(parseFloat(event.target.value))
          }
        />
        <FaVolumeUp
          className="cursor-pointer"
          onClick={() => volumeChangeHandler(volume + 0.1)}
        />
      </div>
    </div>
  );
};

export default AudioPlayer;
