import React from 'react';
import App from './App';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function Setup() {



  return (
    <Router>
      <div>
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
    </Router>
  );
}

export default Setup