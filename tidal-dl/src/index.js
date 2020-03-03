import React from 'react';
import ReactDOM from 'react-dom';
import {getCookie} from './Cookie'
import Setup from "./Setup";
import './index.css';
import * as serviceWorker from './serviceWorker';
import {
  Redirect,
  BrowserRouter,
  Switch,
  Route
} from "react-router-dom";
import App from "./App";

ReactDOM.render(
  <BrowserRouter>
    <Redirect from='/' to={(getCookie('p') === null) ? '/login' : '/app'}/>
    <Switch>
      <Route path='/login' component={Setup}/>
      <Route path='/app' component={App}/>
    </Switch>
  </BrowserRouter>,
  document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
