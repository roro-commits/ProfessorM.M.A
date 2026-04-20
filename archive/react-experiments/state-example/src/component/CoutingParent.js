import React from 'react'
import Child from './Child'



export default class Countingparent extends React.Component {
    //state
    state =
    {
        actionCount :0,
        text:''
    }
    
    // Action function
    handleAction = (action) => 
    {
        console.log('Child says', action);
        //actionCount is incremeneted
        // the new count replades the hold one
        this.setState({
            actionCount : this.state.actionCount +1
        });

        console.log(this.state)
    };

    // action 2 

    handleChange = ( event) =>{
        this.setState({
            text: event.target.value
        });
    };

    // render Actions 
    render(){

            return (
                <div>
                    <Child onAction = {this.handleAction} />
                    <p>Clicked {this.state.actionCount} times</p>
                    <input type = 'text' value ={this.state.text} onChange={this.handleChange} />
                    <p>{this.state.text}</p>
                </div>
            );
    }
}

