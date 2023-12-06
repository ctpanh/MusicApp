const { ZingMp3 } = require("zingmp3-api-full");

ZingMp3.getNewReleaseChart().then((data) => {
  // Send the data to your FastAPI backend
  console.log('Data to be sent:', data.data.items);

  fetch('http://127.0.0.1:8000/save-data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(result => {
    console.log('Data saved successfully:', result);
  })
  .catch(error => {
    console.error('Error saving data:', error);
  });
});
