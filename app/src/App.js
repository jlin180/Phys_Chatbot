import React, { Component } from 'react';
import './App.css';
import User from './User';
import WatsonBot from './WatsonBot';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      
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
      event.preventDefault();
      document.sendMessage.submit();
    }
  }

  render() {
    return (  
      <div className="overflow-auto">
        <table className="table">
          <tbody style={this.bodyStyle}>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><WatsonBot /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
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
