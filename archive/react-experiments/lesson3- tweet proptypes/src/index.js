import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import  moment from 'moment';
import PropTypes from 'prop-types';


function Message({text})
{
  return(
    <div className="message">
     {text}
    </div>
  )
}

Message.propTypes = {
  text: PropTypes.string
};

function NameWithhandle ({author}){
  const {name,handle} = author;
return(
  <span className="name-with-handle">
    <span className="name">{name}</span>
    <span className="handle">@{handle}</span>
  </span>
);

}

NameWithhandle.propTypes = {

  author: PropTypes.shape({
    name: PropTypes.string.isRequired,
    handle: PropTypes.string.isRequired
  }).isRequired
};

const Time = ({time}) => {
  const timeString = moment(time).fromNow();
  return(
<span className="time">
  {timeString}
</span>

);
}

Time.propTypes = {
  time: PropTypes.string
};



const ReplyButton =() => (
  <i className="fa fa-reply reply-button"/>
);

function getRetweetCount (count){
  if(count > 0){
    return (
      <span className="retweet-count">
        {count}
      </span>
    );
  }else {
    return null;
  }
}

const RetweetButton =({count}) => (
  <span className="retweet-button">
  <i className="fa fa-retweet"/>
  { getRetweetCount(count)}m
  </span>
);


RetweetButton.propTypes = {
  count: PropTypes.number
};

const LikeButton = ({count}) => (
  <span className="like-button">
    <i className="fa fa-heart" />
    {
      count > 0 &&
      <span className="like-count">
        {count}m
      </span>}
  </span>
);

LikeButton.propTypes = {
  count: PropTypes.number
};

const MoreoptionsButton =() =>(
  <i className="fa fa-ellipsis-h more-options-button"></i>
);


function Avatar({hash}) 
{
  var url  = "https://www.gravatar.com/avatar/${hash}";
  {/*https://www.gravatar.com/avatar/c050686033f2bca3421fa701ad4f6cec*/}
  return(
    <img src= {url} alt="avatar" className="avatar" />
  )

}

Avatar.propTypes = {
  hash: PropTypes.string
};

function Tweet({tweet}){
  return(
    <div className="tweet">
      <Avatar hash={tweet.gravatar} />
      <div className="content">
        <NameWithhandle author ={tweet.author}/><Time time={tweet.timestamp}/>
        <Message text={tweet.message}/>
        <div className="buttons">
          <ReplyButton/>
          <RetweetButton count ={tweet.retweets}/>
          <LikeButton count ={tweet.likes}/>
          <MoreoptionsButton/>
        </div>
      </div>
      
    </div>
  );
}

Tweet.propTypes ={

  tweet: PropTypes.shape(
    {
      gravatar: PropTypes.string,
      message: PropTypes.string,
      author: PropTypes.shape({
        handle: PropTypes.string,
        name: PropTypes.string
      }),
      likes : PropTypes.number,
      retweets: PropTypes.number,
      timestamp: PropTypes.string

      })
    }


  



var  testTweet  ={
  message: "It's been four years since we successfully lunched now with over 1B users .",
  gravatar: "c050686033f2bca3421fa701ad4f6cec",
  author: {
    handle: "rotimiAwoniran",
    name:"Sage-Blacc - Clavem"
  },
  likes:6,
  retweets: 2,
  timestamp: "2016-07-30 21:24:37"
};


ReactDOM.render(
  <Tweet tweet={testTweet} />,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
