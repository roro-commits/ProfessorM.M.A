import React from 'react';

const Nav = ({activeTab, onTabChange, Item}) => 
(
    <nav className="App-nav">
        <ul>
            <li className={`App-nav-item ${activeTab === 0 && 'selected'}`}><a onClick={()=> onTabChange(0)}> Items</a></li>
            <li className={`App-nav-item ${activeTab === 1 && 'selected'}`}><a onClick={()=> onTabChange(1)}> Cart</a></li>
            <li className={`App-nav-item ${activeTab === 1 && 'selected'} basket`}><a onClick={()=> onTabChange(1)}> 
            <i class="fa fa-shopping-basket" > {Item}</i>
            </a></li>

        </ul>
    </nav>
)

export default Nav;