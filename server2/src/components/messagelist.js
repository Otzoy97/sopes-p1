import React from 'react'
import Message from './message'

function MessageList(props) {
    return (
        props.data.map((msg, idx) => {
            return (
                <Message key={idx} title={msg.autor}
                    paragraph={msg.oracion} />
            )
        })
    )
}

export default MessageList