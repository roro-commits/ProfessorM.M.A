import React from 'react'
import PropTypes from 'prop-types'



function GetUserNames({usernames}){

    return(
        <li className="username">
            {usernames}
        </li>
    )
}


export default GetUserNames;