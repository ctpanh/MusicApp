'use client'
import React, { useState, useRef } from 'react';
import { FaPlay, FaPause, FaVolumeUp, FaVolumeDown } from 'react-icons/fa';

interface AudioPlayerProps {
  audioSource: string;
}

const AudioPlayer: React.FC<AudioPlayerProps> = ({ audioSource }) => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [volume, setVolume] = useState(0.5);

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

  const volumeChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newVolume = parseFloat(e.target.value);
    setVolume(newVolume);
    if (audioRef.current) {
      audioRef.current.volume = newVolume;
    }
  };

  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-md text-white">
      <audio ref={audioRef} src={audioSource} />

      <div className="flex items-center justify-center">
        <button
          className="text-3xl mr-4 focus:outline-none"
          onClick={playPauseHandler}
        >
          {isPlaying ? <FaPause /> : <FaPlay />}
        </button>

        <input
          type="range"
          min={0}
          max={1}
          step={0.01}
          value={volume}
          onChange={volumeChangeHandler}
          className="mr-4"
        />

        <FaVolumeDown className="mr-2" />
        <FaVolumeUp />
      </div>
    </div>
  );
};

export default AudioPlayer;
