import React, { Component } from 'react';
class User extends Component {
    constructor(props){
        super(props);
        this.state = {
            message: 'Hello',
            name: 'Jefferson',
            timeStamp: new Date(),
        };
    }

    formatTime(){
        const { timeStamp } = this.state;
        let hour = timeStamp.getHours()%12===0 ? '12': timeStamp.getHours()%12;
        let minute = timeStamp.getMinutes();
        let period = timeStamp.getHours()/12 >= 1 ? 'PM' : 'AM';
        return `${hour}:${minute}${period}`;
    }

    render() { 
        const { name, message } = this.state;
        return (
            <div>
                {name} {this.formatTime()}
                <br/>
                {message}
            </div>
        );
    }
}
 
export default User;