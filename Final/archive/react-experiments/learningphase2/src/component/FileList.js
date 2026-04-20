import React from 'react'
import PropTypes from 'prop-types'
import getFilename from './FileName'
import CommitMessage from './CommitMessage'
import Time from './time'






const FileListItem = ( { file }) =>(
  
  <tr className="file-list-item">
    <td>
      {getFilename(file)}
    </td>
    <td>
     <CommitMessage commit={file.latestCommit} />
    </td>
    <td className="age">
      <Time time ={file.upload_at}/>
    </td>
  </tr>
);



FileListItem.propTypes = {
  files: PropTypes.array
};


export default FileListItem;