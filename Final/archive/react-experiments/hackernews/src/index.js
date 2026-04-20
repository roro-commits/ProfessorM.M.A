import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const threads = [
  {
  id:0,
  thread_name : 'Categories of Nets ',
  web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
  stats: {
    point:'130',
    time: '6 hours ago',
    hide: 'hide',
    comments: '19'
  },
},

{
  id:1,
  thread_name : 'Tracking down a segfault that suddenly started happening',
  web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
  stats: {
    point:'10',
    time: '1 hours ago',
    hide: 'hide',
    comments: '19'
  },
},

  {
    id:2,
    thread_name : 'Show HN: 100 LOC Ruby forward proxy using only standard libraries',
    web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
    stats: {
      point:'50',
      time: '2 hours ago',
      hide: 'hide',
      comments: '19'
    },

  },
  {
    id:3,
    thread_name : 'Three reasons fungi are not plants',
    web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
    stats: {
      point:'50',
      time: '2 hours ago',
      hide: 'hide',
      comments: '19'
    },
  },
  {
    id:4,
    thread_name : 'Tech Companies Are Profiling Us from Before Birth',
    web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
    stats: {
      point:'50',
      time: '2 hours ago',
      hide: 'hide',
      comments: '19'
    },
  },
    {
    id:5,
    thread_name : 'GPT-Neo – Building a GPT-3-sized model, open source and free ',
    web: 'https://news.ycombinator.com/from?site=johncarlosbaez.wordpress.com',
    stats: {
      point:'50',
      time: '2 hours ago',
      hide: 'hide',
      comments: '19'
    },

  }
];

ReactDOM.render(
  <React.StrictMode>
    <App  threads = {threads}/>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
