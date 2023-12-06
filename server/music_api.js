const { ZingMp3 } = require("zingmp3-api-full");

ZingMp3.getNewReleaseChart().then(async (data) => {
  // Send the data to your FastAPI backend
  const song_album = await Promise.all(
    data.data.items.map(async (song) => {
      const { encodeId, album } = song;
      let detailedSong;  // Declare the detailedSong variable
      let detailedAlbum;
      let info;
      let res_songInfo;
      let res_albumInfo;
      try {
        // Fetch only the necessary information from ZingMp3.getSong        
        detailedSong = await ZingMp3.getSong(encodeId);
        songInfo = await ZingMp3.getInfoSong(encodeId);
        detailedAlbum = await ZingMp3.getDetailPlaylist(album.encodeId)
        // genre = await ZingMp3
        

        // song
        const title = song.title
        const artist = song.artistsNames
        const audio_file_path = detailedSong.data['128']
        const image_file_path = song.thumbnailM
        const release_date = new Date(song.releaseDate * 1000)
        const views = songInfo.data.listen

        // album
        const album_title = detailedAlbum.data.title
        const album_release_date = detailedAlbum.data.releaseDate
        const album_artist = detailedAlbum.data.artistsNames
        const album_genre = detailedAlbum.data.genres.map(item => item.name);
        const album_img_path = detailedAlbum.data.thumbnail


        res_songInfo = {title, artist, audio_file_path, image_file_path, release_date, views}
        res_albumInfo = {album_title, album_release_date, album_artist, album_genre, album_img_path}
      } catch (error) {
        console.error('Error fetching detailed song:', error);
      }
      return {"song": res_songInfo, "album": res_albumInfo}
    })
  );
  const filteredData = song_album.filter(entry => entry.song !== undefined && entry.album !== undefined);
  console.log(filteredData)
  // Send the detailedSongs data to the FastAPI backend
  fetch('http://127.0.0.1:8000/save-data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(filteredData), // Send the detailedSongs array as JSON in the request body
    
  })
  .then(result => {
    console.log('Data saved successfully:', result);
  })
  .catch(error => {
    console.error('Error saving data:', error);
  });
});



