import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';


function Message()
{
  return(
    <div className="message">
      This is Less than 140 Characters 
    </div>
  )
}
function NameWithhandle (){
return(
  <span className="name-with-handle">
    <span className="name">Your Name</span>
    <span className="handle">@yourhandle</span>
  </span>
);

}

const Time = () => (
<span className="time">3h ago</span>
);

const ReplyButton =() => (
  <i className="fa fa-reply reply-button"/>
);

const RetweetButton =() => (
  <i className="fa fa-retweet retweet-button"/>
);

const LikeButton = () => (
<i className="fa fa-heart like-button" />
);

const MoreoptionsButton =() =>(
  <i className="fa fa-ellipsis-h more-options-button"></i>
);


function Avatar() 
{
  return(
    <img src="https://www.gravatar.com/avatar/c050686033f2bca3421fa701ad4f6cec" alt="avatar" className="avatar" />
  )

}

function Tweet(){
  return(
    <div className="tweet">
      <Avatar />
      <div className="content">
        <NameWithhandle/>
        <Message/>
        <div className="buttons">
          <ReplyButton/>
          <RetweetButton/>
          <LikeButton/>
          <MoreoptionsButton/>
        </div>
      </div>
      
    </div>
  );


}

ReactDOM.render(
  <Tweet/>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
