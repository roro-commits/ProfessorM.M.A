import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const list = [
  {message:'List1',
   id : 0},
   {message:'List1',
   id : 1},
   {message:'List1',
   id : 2},
   {message:'List1',
   id : 3},
]

ReactDOM.render(

    <App list = {list} />,

  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
