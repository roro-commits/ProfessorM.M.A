import React from 'react'
import ListItem from './listItem'


function ListContainer ({list}) {
   return(
    <div className="container">
    <ul className="list-con">
        <li className = 'li-item'>
            <ListItem item ={list}/>

        </li>
    </ul>
     </div>
   )


}

export default ListContainer;