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
          <form>
            <div className="row">
              <div className="col-xs-8">
                <input 
                  type="text"
                  placeholder="send message"
                />
              </div>
              <div className="col-xs-4">
                <input
                  type="submit"
                />
              </div>
            </div>
          </form>
        </div>
      </div>
    );
  }
}
 
export default App;
