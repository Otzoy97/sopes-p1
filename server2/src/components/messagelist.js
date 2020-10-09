import React from 'react'
import Message from './message'

const MessageList = (props) => {
    return (
        <div className="row">
            <div className="col">
                {props.msgs.map((msg) => {
                    return (
                        <Message title={msg.autor}
                            paragraph={msg.oracion} />
                    )
                })}
            </div>

        </div>
    )
}

export default MessageList