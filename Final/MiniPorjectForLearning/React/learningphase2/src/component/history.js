import React from 'react'


const History = ({commits}) => {
    return(
        <span className="history">
            <span >
                <i class="fa fa-history"> {commits} commits</i>
                
            </span>
        </span>
    )
}

export default History;