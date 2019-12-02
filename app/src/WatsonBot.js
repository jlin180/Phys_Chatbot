import React, { Component } from 'react';
class WatsonBot extends Component {
    constructor(props){
        super(props);
        this.state = {
            name: 'Watson Bot',
        };
    }

    formatTime(){
        const { timeStamp } = this.props;
        let hour = timeStamp.getHours()%12===0 ? '12': timeStamp.getHours()%12;
        let minute = timeStamp.getMinutes();
        let period = timeStamp.getHours()/12 >= 1 ? 'PM' : 'AM';
        return `${hour}:${minute}${period}`;
    }

    render() { 
        const { name } = this.state;
        const { message } = this.props;
        return (
            <td>
                <strong>{name}</strong> {this.formatTime()}
                <br/>
                {message}
            </td>
        );
    }
}
 
export default WatsonBot;