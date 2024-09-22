
const startButton = document.getElementById('main-button');
let status = "Passive";
startButton.addEventListener('click', () => {
  if (status == "Passive"){
    status = "Active";
    startButton.textContent = 'Stop Recording';
    startButton.className = 'btn btn-danger';
    startVideo();
  }
  else{
    status = "Passive";
    startButton.textContent = 'Start Recording';
    startButton.className = 'btn btn-primary';
  }
});

function startVideo() {
  video.addEventListener('play', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const displaySize = { width: video.videoWidth, height: video.videoHeight };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
      const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions());
      const resizedDetections = faceapi.resizeResults(detections, displaySize);
      const context = canvas.getContext('2d');

      context.clearRect(0, 0, canvas.width, canvas.height);
      context.setTransform(-1, 0, 0, 1, canvas.width, 0);  // Mirroring canvas horizontally
      faceapi.draw.drawDetections(canvas, resizedDetections);

      // Check if two or more faces are detected
      if (resizedDetections.length > 1) {
        console.log('Multiple faces detected');
      } else {
        console.log('There is only one face');
      }
    }, 100);
  });
}