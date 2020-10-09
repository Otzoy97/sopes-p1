import React, { Fragment } from 'react'
import MessageList from '../components/messagelist'
import {serverA, serverB} from '../config'

class Posts extends React.Component {

    constructor(props) {
        super(props)


        this.state = {
            serverA: {
                button: "dropdown-item active"
            },
            serverB: {
                button: "dropdown-item"
            }
        }
    }

    async componentDidMount() {
        this.bindMessages(serverA + '/getMsgs')
    }

    bindMessages = async(url) =>{
        let res = await fetch(url, {method:'GET'})
        console.log(res)
        let data = await  res.json()
        console.log(data)         
    }

    handleClickA = () => {
        this.setState({
            serverB: {
                button: "dropdown-item"
            },
            serverA: {
                button: "dropdown-item active"
            }
        })
    }

    handleClickB= () => {
        this.setState({
            serverA: {
                button: "dropdown-item"
            },
            serverB: {
                button: "dropdown-item active"
            }
        })
    }

    render() {
        return (
            <Fragment>
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
                                <button onClick={this.handleClickA} className={this.state.serverA.button} type="button">Servidor A</button>
                                <button onClick={this.handleClickB} className={this.state.serverB.button} type="button">Servidor B</button>
                            </div>
                        </div>
                    </div>
                </div>
                {/* <MessageList data = {this.state.msgs} /> */}
            </Fragment>
        )
    }
}

export default Posts