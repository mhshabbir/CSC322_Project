
import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import badWords from 'bad-words'


const ChatBox = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const filter = new badWords();
  const handleFormSubmit = (e) => {

    e.preventDefault();
    const filteredMessage = filter.clean(inputValue);
    

    setMessages([
      ...messages,
      { user: "me", message: filteredMessage },
      { user: "bot", message: `You said: ${filteredMessage}` }
    ]);
    setInputValue("");
  };

  return (
    <div className="chat-box">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.user}`}>
            {message.message}
          </div>
        ))}
      </div>
      <form onSubmit={handleFormSubmit}>
        <TextField
          type="text"
          placeholder="Type your message here"
          value={inputValue}
          onChange={handleInputChange}
        />

        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatBox;
