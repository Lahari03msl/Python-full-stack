// src/WelcomeMessage.jsx
import React, { useState } from 'react';
import PartyVoteCounter from './Counter'
import Greeting from './Greeting';
import InputName from './InputName.jsx';

function WelcomeMessage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);  // State for login status

  // Toggle login status
  function toggleLogin() {
    setIsLoggedIn(!isLoggedIn);
  }

  // Conditional rendering using 'if' statement
  if (isLoggedIn) {
    return (
      <div>
        <h1>Welcome back, User!</h1>

        <Greeting name="lahari"/>
        <PartyVoteCounter/>
        <button onClick={toggleLogin}>Log out</button>

      </div>
    );
  } else {
    return (
      <div>
        <h1>Please log in to continue</h1>
        <InputName />
        
        <button onClick={toggleLogin}>Log in</button>
      </div>
    );
  }
}

export default WelcomeMessage;