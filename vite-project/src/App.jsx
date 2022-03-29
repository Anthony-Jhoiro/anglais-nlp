import { useContext, useEffect, useState } from 'react'
import './App.css';

import { io } from "socket.io-client";

const socket = io('http://localhost:5000');


function App() {
  const [text, setText] = useState("");

  useEffect(() => {
    socket.on("mess", console.log)
  })



  const onText = () => {
    console.log("hello world")
    socket.emit('message', text);
  }

  return (
   <main>
    <textarea name="toto" id="" cols="30" rows="10" className='text-area' value={text} onChange={v => setText(v.target.value)}>

    </textarea>

    <button onClick={onText}>click me !</button>
   </main>
  )
}

export default App
