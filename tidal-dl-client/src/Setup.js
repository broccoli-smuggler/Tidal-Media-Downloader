import React from 'react';
import { Button } from '@material-ui/core'
import App from './App';
import './App.css';
import './Setup.css'
import fetch from "node-fetch";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function Setup() {
  let is_logged_in = "login";

  async function loginRequest() {
    let res = await fetch('http://localhost:5000/login', { method: 'POST', body: "login;poo;poos" })
    let text = await res.text();
    console.log(text);
    if (text === "ack") {
      is_logged_in = "poo"
    }
  }

  return (
    <Router>
      <div className="App">
         <Switch>
           <Route path="/login">
             <li>
               <Link to="/app">Main downloader</Link>
             </li>
           </Route>
           <Route path="/app">
             <App />
           </Route>
         </Switch>
      </div>
      <div className="Setup-body">
        <Button onClick={loginRequest} color="primary">
          {is_logged_in}
        </Button>
      </div>
    </Router>
  )
}

export default Setup