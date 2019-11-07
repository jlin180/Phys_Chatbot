import React, { Component } from 'react';
import './App.css';
import User from './User';
import WatsonBot from './WatsonBot';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      
    };
  }

  render() {
    return (  
        <table className="table">
          <tbody>
            <tr>
              <td><User /></td>
            </tr>
            <tr>
              <td><WatsonBot /></td>
            </tr>
            <tr>
              <td><User /></td>
            </tr>
          </tbody>
        </table>
    );
  }
}
 
export default App;
