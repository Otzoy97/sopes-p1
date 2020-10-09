import React/*, { useState }*/ from 'react'

class Posts extends React.Component {
    render() {
        return (
            <div className="row align-items-center justify-content-between">
                <div className="col-auto mr-auto">
                    <h1>Publicaciones</h1>
                </div>
                <div className="col-auto">
                    <div className="dropdown">
                        <button type="button" className="btn btn-primary dropdown-toggle" data-display="static" id="server" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Servidor
                        </button>
                        <div className="dropdown-menu dropdown-menu-right" aria-labelledby="server">
                            <button className="dropdown-item active" type="button">Servidor A</button>
                            <button className="dropdown-item" type="button">Servidor B</button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Posts