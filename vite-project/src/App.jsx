import { useContext, useEffect, useState } from 'react'
import './App.css';
import 'papercss/dist/paper.min.css'
import sample from "./sample.json"
import tags from "./tags.json"

import { io } from "socket.io-client";

const socket = io('http://localhost:5000');


function App() {
  const [text, setText] = useState("");
  const [data, setData] = useState([]);

  useEffect(() => {
    socket.on("message", str => setData(JSON.parse(str)))
  })



  const onText = () => {
    console.log("hello world")
    socket.emit('message', text);
  }

  return (
   <main>

     <section id="left-side">
      <div className="form-group">
        <div className="textInput">
          <label htmlFor="text-input" className="text-input-lbl">Your text</label>
        </div>
        <textarea id="text-input" cols={64} rows={12} onChange={e=> setText(e.target.value)} placeholder="Input your text here"></textarea>
      </div>

      <button onClick={onText}>click me !</button>
    </section>
    <div id="result" className='paper border-3'>
     {data.map((w, i) => <span key={'key_' + i} style={{color: tags[w.type] ?? "#ffffff"}}>{w.word}{' '}</span>)}
    </div>
   </main>
  )
}

export default App
