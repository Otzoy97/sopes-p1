import React, { Fragment } from 'react'
import LineChart from '../components/graph'
import { serverA, serverB } from '../config'

class Stats extends React.Component {

    render() {
        return (
            <Fragment>
                <div className="row align-items-center justify-content-between mt-2">
                    <div className="col-auto">
                        <h1>Métricas</h1>
                    </div>
                </div>
                <div className="row mt-1 mb-2">
                    <div className="col">
                        <div className="list-group list-group-horizontal-md" id="list-tab" role="tablist">
                            <a class="list-group-item list-group-item-action active" id="serverA-list" data-toggle="list" href="#serverA" role="tab" aria-controls="serverA">Servidor A</a>
                            <a class="list-group-item list-group-item-action" id="serverB-list" data-toggle="list" href="#serverB" role="tab" aria-controls="serverB">Servidor B</a>
                        </div>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <div className="tab-content" id="nav-tabContent">
                            <div className="card shadow  bg-white tab-pane fade show active" id="serverA" role="tabpanel" aria-labelledby="serverA-list">
                                <div className="card-header">
                                    <div className="row">
                                        <div className="col align-self-center">Servidor A</div>
                                    </div>
                                </div>
                                <LineChart key={"graphA"} server={serverA} />
                            </div>
                            <div className="card shadow bg-white tab-pane fade" id="serverB" role="tabpanel" aria-labelledby="serverB-list">
                                <div className="card-header">
                                    <div className="row">
                                        <div className="col align-self-center">Servidor B</div>
                                    </div>
                                </div>
                                <LineChart key={"graphB"} server={serverB} />
                            </div>
                        </div>
                    </div>
                </div>
            </Fragment >
        )
    }
}
export default Stats
