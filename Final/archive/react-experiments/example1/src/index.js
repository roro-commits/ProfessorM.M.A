import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

const Stamp  = () => (  
  <i className="fas fa-mail-bulk"></i>
);


const Sender = ({sender}) => {

  const {name,address} = sender;

  return (
    
      <span>
        <span>
         {name}
        </span>
        <br/>
        <span> {address}</span>
      </span>
  ); 
 
}

function Reciever ({reciever}) {
 const  {name,address} = reciever;
  return(
      <span>
        <span className="rev address">{name}</span>
        <br/>
        <span className="rev address">{address}</span>
      </span>
  );

}

function Envbody ({letter}) {

  return(
      <div className="envbody">
      <Stamp/>
      <Sender sender = {letter.sender} />
      <div className="receiver">
        <div className="child">
           <Reciever reciever = {letter.reciever} />
        </div>
      </div>
      </div>

  );

}

const letter = {
  reciever: {
    name:"John Doe",
    address:"faker street"
  },

  sender: {
    name:"Mrs Doe",
    address:"123 Baker Street"
  }
}

ReactDOM.render(
 <Envbody letter={letter}/>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
