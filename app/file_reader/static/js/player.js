function playAudio(id) {
    document.getElementById("audio-" + id).play();
}

function pauseAudio(id) {
    document.getElementById("audio-" + id).pause();
}

function stopAudio(id) {
    let audio = document.getElementById("audio-" + id);
    audio.pause();
    audio.currentTime = 0;
}

function restartAudio(id) {
    let audio = document.getElementById("audio-" + id);
    audio.currentTime = 0;
    audio.play();
}

