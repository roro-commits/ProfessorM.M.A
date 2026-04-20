import React from 'react'
import PropTypes from 'prop-types'
import FileListItem from './FileList'
import Header from './table_head'




const FileList = ({files,report}) => 
 {   
   return (
     <div className="total">
      <Header  report = {report}/>
      <table className="file-list ">
    <tbody>
      {files.map(file  => 
        
           
          <FileListItem key={file.id} file = {file} />
      )}
    </tbody>
    </table>

     </div>
    )
  }
  
  FileList.propTypes = {
    files: PropTypes.array
  };
  

  export default FileList;