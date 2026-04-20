import React from 'react'
import PropTypes from 'prop-types'
import HeaderItem from './headerItem'





function Header ({report}) 
{

    return(
        <div className="Header">
            <HeaderItem  report = {report}/>
        </div>
    )


}





export default Header;