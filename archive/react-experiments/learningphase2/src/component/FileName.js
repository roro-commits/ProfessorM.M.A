import React from 'react'
import FileIcon from './FileIcon'




function getFilename (file)
{

  return[
    <FileIcon file= {file} key ={0}/>,
    <span className="file-name" key ={1}>{file.name}</span>
  ];



}

export default getFilename;