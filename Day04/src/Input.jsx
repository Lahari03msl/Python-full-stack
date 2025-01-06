import React, { useState } from "react";

function InputName({ onNameSubmit }) {
  const [name, setName] = useState("");

  function handleInput(event) {
    setName(event.target.value);
  }

  function handleSubmit() {
    onNameSubmit(name); // Pass the name to the parent component
  }

  return (
    <div>
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={handleInput}
      />
      <button onClick={handleSubmit}>Submit Name</button>
    </div>
  );
}

export default InputName;
