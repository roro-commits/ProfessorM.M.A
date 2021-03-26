import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import FileList from './component/List'



const testFiles = [
 
  {
    id : 1,
    name: 'src',
    type: 'folder',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:2, 
    name: 'testing',
    type: 'folder',
    updated_at: "2016-07-11 20:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id : 3,
    name: 'Artifacts',
    type: 'folder',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:4, 
    name: 'WebAPP',
    type: 'folder',
    updated_at: "2016-07-11 20:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:5, 
    name: 'app.py',
    type: 'python',
    updated_at: "2020-07-11 19:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:6, 
    name: 'app.css',
    type: 'file',
    updated_at: "2021-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    },
  },
  {
    id:7, 
    name: 'README',
    type: 'file',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  
]


const report = {
  id: 0,
  user_name:'roro-commits',
  latestCommit:'@commit-prop',
  check:'fail',
  ids:'i3h5usia0',
  commits:'130',
  updated_at: "2016-07-11 21:24:00",
};


ReactDOM.render(
  <FileList  files = {testFiles} report = {report} />,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
