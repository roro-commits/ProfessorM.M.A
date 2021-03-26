import React from 'react'
import PropTypes from 'prop-types'


const Profile =({usernames},{commits}) => {
    return(
        <div className='profile-details'>
        <li className="profile">
            <i className="fa fa-user-circle"></i>
        </li>
        <span className="userName">
            {usernames}
        </span>
       
        </div>
    )
}

export default Profile;