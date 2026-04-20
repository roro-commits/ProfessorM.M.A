import React from 'react'
// import PropTypes from 'prop-types'
import Profile from './profile'
import Commit from './commits'
import Status from './status'
import ID from './id'
import HeadTimer from './headTime'
import History from './history'




const HeaderItem = ({report}) => {
    const username = report.user_name;
    const commits = report.latestCommit;
    return(
        <ul className="header-HeaderItem">
            <Profile usernames = {username} />
            <Commit commits = {commits} />
            <Status stats = {report.check} />
            <ID  id = {report.ids} />
            <HeadTimer />
            <History commits = {report.commits} />
        </ul>
    );

}

export default HeaderItem;