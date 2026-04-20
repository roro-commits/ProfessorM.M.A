import React from 'react'
import PropTypes from 'prop-types'




function FileIcon({ file }) {
    let icon ='fa fa-file-text-o';
    if (file.type === 'folder')
    {
      icon = 'fa fa-folder';
    }
    if (file.type === 'python')
    {
        icon = 'fa fa-file';
    }
  
    return (
      <span className="file-icon">
        <i className={`${icon}`}></i>
      </span>
    );
  }
  
  FileIcon.propTypes ={
    file: PropTypes.object.isRequired
  };

export default FileIcon;