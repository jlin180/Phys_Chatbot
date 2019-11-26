import React, { Component } from 'react';
import './App.css';
import User from './User';
import WatsonBot from './WatsonBot';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      userInputs:[],
    };
  
    this.bodyStyle = {
      width: '100vw',
      display: 'block',
      maxHeight: '80vh',
      overflowY: 'auto',
    }

  }

  onEnterPress(event){
    if(event.keyCode === 13 && event.shiftKey === false){
      let message = event.target.value;
      let timeStamp = new Date();
      this.handleNewSubmission(message,timeStamp);
      event.target.value = '';
    }
  }

  handleNewSubmission(message, timeStamp){
    let inputs = [...this.state.userInputs];
    // inputs.push({
    //   message,
    //   timeStamp,
    // })
    fetch('http://127.0.0.1:5000/check', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      "Access-Control-Allow-Origin" : "*", 
      "Access-Control-Allow-Headers" : "*",
      "Access-Control-Allow-Credentials" : true 
    },
    body: JSON.stringify({
      'input': message,
    }),
    })
    .then(response => response.json())
    .then(response => {
      console.log(response)
      let output = response.message;
      inputs.push({
        message,
        timeStamp,
        output,
      });
      this.setState({userInputs: inputs});
    })
  }

  render() {
    const { userInputs } = this.state;
    return (  
      <div className="overflow-auto table-responsive">
        <table className="table table-hover">
          <tbody style={this.bodyStyle}>
            {userInputs.map((user,index) =>{
              return(
                <React.Fragment>
                  <tr key={index}>
                    <User 
                      message = {user.message}
                      timeStamp = {user.timeStamp}
                    />
                  </tr>
                  <tr key={-index}>
                    <WatsonBot
                      message = {user.output}
                      timeStamp = {user.timeStamp}
                    />
                </tr>
              </React.Fragment>
              );
            })}
          </tbody>
        </table>
        <div>
          <form name="sendMessage" className="form-inline">
            <textarea
              id="message"
              name="message"
              rows="3"
              maxLength="400"
              placeholder="Send message"
              onKeyDown={e => this.onEnterPress(e)}
              style={{width:'100vw',}}
            />
          </form>
        </div>
      </div>
    );
  }
}
 
export default App;
