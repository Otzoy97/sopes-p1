import React from 'react'

const Message = ({ title, paragraph }) => {
    <div className="row">
        <div className="col">
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title font-weight-bold">{title}</h5>
                    <p className="card-text">{paragraph}</p>
                </div>
            </div>
        </div>
    </div>
}

export default Message