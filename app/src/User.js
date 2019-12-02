import React, { Component } from 'react';
class User extends Component {
    constructor(props){
        super(props);
        this.state = {
            name: 'Jefferson',
        };

        this.style = {
            width: '100vw',
            float: 'right',
        }
    }


    formatTime(){
        const { timeStamp } = this.props;
        let hour = timeStamp.getHours()%12===0 ? '12': timeStamp.getHours()%12;
        let minute = timeStamp.getMinutes()<10 ? '0'+timeStamp.getMinutes() : timeStamp.getMinutes();
        let period = timeStamp.getHours()/12 >= 1 ? 'PM' : 'AM';
        return `${hour}:${minute}${period}`;
    }

    render() {
        const { name } = this.state;
        const { message } = this.props;
        return (
            <td style={this.style}>
                <div>
                    <strong>{name}</strong> {this.formatTime()}
                    <br/>
                    {message}
                </div>
            </td>
        );
    }
}
 
export default User;