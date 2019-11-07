import React, { Component } from 'react';
class WatsonBot extends Component {
    constructor(props){
        super(props);
        this.state = {
            message: 'smd',
            name: 'Watson Bot',
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
 
export default WatsonBot;