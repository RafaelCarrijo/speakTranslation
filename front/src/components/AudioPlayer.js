import React from 'react';

const AudioPlayer = ({ audioResponse }) => {
  if (audioResponse) {
    const decodedData = atob(audioResponse);
    const audioUrl = `data:audio/mpeg;base64,${decodedData}`;

    return (
      <div>
        <audio controls>
          <source src={audioUrl} type="audio/mpeg" />
          Seu navegador não suporta a reprodução de áudio.
        </audio>
      </div>
    );
  } else {
    return null;
  }
};

export default AudioPlayer;
