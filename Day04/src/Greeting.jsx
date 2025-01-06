import React from "react";

function Greeting(props) {
  const currentHour = new Date().getHours()
  let greetMessage;
  if (currentHour <12){
    greetMessage = "Good Morning";
  }
  else if(currentHour<18){
    greetMessage = "Good Afternoon";
  }
  else{
    greetMessage = "Good Evening";
  }
  return (
      <div> 
        <p>{greetMessage} i am {props.name} </p>
      </div>
  )
}

export default Greeting;
