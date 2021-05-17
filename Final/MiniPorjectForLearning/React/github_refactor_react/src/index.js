import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import PropTypes from 'prop-types'
import Time from './time'

const FileList = ({files}) => (
  <table className="file-list ">
  <tbody>
    {files.map( 
      
        file =>
        <FileListItem key={file.id} file = {file} />
    )}
  </tbody>
  </table>
);

FileList.propTypes = {
  files: PropTypes.array
};

const FileListItem = ( { file }) =>(

  <tr className="file-list-item">
    {getFilename(file)}
    <CommitMessage commit={file.latestCommit} />
    <td className="age">
      <Time time ={file.upload_at}/>
    </td>
  </tr>
);

const CommitMessage =  ({ commit }) => (
  <td className="commit-message">
    {commit.message}
  </td>
);

CommitMessage.propTypes = {
  commit: PropTypes.object.isRequired
};

FileListItem.propTypes = {
  files: PropTypes.array
};


function FileIcon({ file }) {
  let icon =' fa-file-text-o';
  if (file.type === 'folder')
  {
    icon = 'fa-folder';
  }

  return (
    <td className="file-icon">
      <i className={`fa ${icon}`}></i>
    </td>
  );
}

FileIcon.propTypes ={
  file: PropTypes.object.isRequired
};



function getFilename (file)
{

  return[
    <FileIcon file= {file} key ={0}/>,
    <td className="file-name" key ={1}>{file.name}</td>
  ];



}

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
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:3, 
    name: 'app.py',
    type: 'file',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:4, 
    name: 'app.css',
    type: 'file',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
  {
    id:5, 
    name: 'README',
    type: 'file',
    updated_at: "2016-07-11 21:24:00",
    latestCommit: {
      message: 'Initial commit'
    }
  },
]




ReactDOM.render(

  <FileList files = {testFiles} />,
  
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
