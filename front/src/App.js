
import './App.css';
import AudioPlayer from './components/AudioPlayer';
import FileUpload from './components/Upload';
import React, { useState } from 'react'; 


function App() {
  const [translatedAudioBase64, setTranslatedAudioBase64] = useState(null);

  const handleAudioUploaded = (audioBase64) => {
    setTranslatedAudioBase64(audioBase64);
  };

  return (
    <div className="App">
      <FileUpload onAudioUploaded={handleAudioUploaded} />
      <AudioPlayer audioBase64={translatedAudioBase64} />
    </div>
  );
}


export default App;
