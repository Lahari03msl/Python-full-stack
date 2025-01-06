import React,{useState} from "react";
function InputName(){
    const [name,setName]=useState("");
    function handleInput(event){
        setName(event.target.value)
    }

    return(
        <div>
            <input type="text" placeholder="Enter your name" onChange={handleInput}/>
            <p>hello..! {name}</p>
        </div>
    )
}
export default InputName;
