import React, { Component } from 'react';
import api from '../services/api';
import languages from '../data/linguagens.json'; // Importe o arquivo de idiomas

class FileUpload extends Component {
  constructor() {
    super();
    this.state = {
      selectedFile: null,
      selectedLanguage: 'en', // Defina a linguagem padrão ou uma opção pré-selecionada
    };
  }

  handleFileChange = (e) => {
    const file = e.target.files[0];
    this.setState({
      selectedFile: file,
    });
  };

  handleLanguageChange = (e) => {
    const selectedLanguage = e.target.value;
    this.setState({
      selectedLanguage,
    });
  }

  fileToBytes = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = (event) => {
        const arrayBuffer = event.target.result;
        const byteArray = new Uint8Array(arrayBuffer);
        resolve(byteArray);
      };

      reader.onerror = (error) => {
        reject(error);
      };

      reader.readAsArrayBuffer(file);
    });
  };

  handleUpload = async () => {
    const { selectedFile, selectedLanguage } = this.state;
  
    if (selectedFile) {
      try {
        const bytes = await this.fileToBytes(selectedFile);
  
        const formData = new FormData();
        formData.append('audio', new Blob([new Uint8Array(bytes)], { type: 'application/octet-stream' }));
  
        const headers = {
          'Content-Type': 'multipart/form-data',
          'Linguagem': selectedLanguage, // Adicione a linguagem como um cabeçalho personalizado
        };
  
        try {
          const response = await api.post('/audio/upload', formData, {
            headers: headers,
            responseType: 'arraybuffer',
          });
  
          if (response.status === 200) {
            console.log('Resposta do servidor:', response.data);
            console.log(response.data);
            const audioData = response.data;

            // Criando um elemento de áudio
            const audio = new Audio();
            audio.src = URL.createObjectURL(new Blob([audioData], { type: 'audio/mpeg' }));
      
            // Reproduzindo o áudio
            audio.play();
          } else {
            console.error('Erro ao fazer upload:', response.status, response.statusText);
            if (response.data && response.data.message) {
              console.error('Detalhes do erro:', response.data.message);
            }
          }
        } catch (error) {
          console.error('Erro ao fazer upload:', error);
        }
      } catch (error) {
        console.error('Erro ao converter o arquivo:', error);
      }
    }
  };

  isUploadEnabled() {
    const { selectedFile, selectedLanguage } = this.state;
    return selectedFile !== null && selectedLanguage !== '';
  }

  render() {
    const { selectedLanguage } = this.state;

    return (
      <div>
        <section>
          <h1>Tradução de Áudio</h1>
          <p>Este serviço permite enviar um arquivo de áudio para que seja feita a tradução em uma linguagem desejada.</p>
        </section>

        <section>
          <h3>Selecione o idioma de destino:</h3>
          <select id="language" onChange={this.handleLanguageChange} value={selectedLanguage}>
            {Object.keys(languages).map((code) => (
              <option key={code} value={code}>
                {languages[code]}
              </option>
            ))}
          </select>
        </section>

        <section>
        <input type="file" onChange={this.handleFileChange} accept="audio/mpeg, audio/wav" />
        <button onClick={this.handleUpload} disabled={!this.isUploadEnabled()}>
            Enviar
          </button>
        </section>
      </div>
    );
  }
}

export default FileUpload;
