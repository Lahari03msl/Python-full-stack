import React,{useState} from "react";

function ClickButton(){
    const [message , setMess] = useState("")
    function handleClick(){
        setMess("I love you");
    }
    return(
        <div>
            <button onClick={handleClick}>Click me!</button>
            <p>{message}</p>
        </div>
    )
}

export default ClickButton;