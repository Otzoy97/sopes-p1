import React from 'react'
import Message from './message'

const MessageList = ({msgs}) => {
    return (
        <div className="row">
            <div className="col">
                {msgs.map((msg) => {
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