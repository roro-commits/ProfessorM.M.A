import React from 'react'
import './App.css';
import ListContainer from './component/list-container'
import Option from './component/option'

function App({list}) {
  return (
    <div className ='app'>
        <li className='title top'>Phone Features  
        </li>
        <Option />

      {
        list.map( list =>
          <div className="App">
          <ListContainer key = {list.id} list ={list.message} />
         </div>
        )
       
      }
        <li className='title'>Add a card...</li>


    </div>
  );
}




export default App;
