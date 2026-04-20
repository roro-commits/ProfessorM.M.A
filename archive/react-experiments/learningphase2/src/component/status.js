import React from 'react'


const Status = ({stats}) => {
    let icon = ''

    if({stats} == 'pass')
    {
        icon = 'fa fa-check'

    }
    else{
        icon = 'fa fa-times';

    }
    return (
        <span className="status">
            <i className={`${icon}`}></i>
        </span>
    )
}


export default Status;