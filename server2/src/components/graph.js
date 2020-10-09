import React, { Fragment } from 'react'
import { Line, defaults } from 'react-chartjs-2'
defaults.global.animation = false

class LineChart extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            config: {
                labels: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
                datasets: [
                    {
                        label: 'CPU(%)',
                        data: [],
                        borderColor: ['rgba(255,206,86,0.5)'],
                        backgroundColor: ['rgba(255,206,86,0.5)'],
                        pointBackgroundColor: ['rgba(255,206,86,0.5)'],
                        pointBorderColor: ['rgba(255,206,86,0.5)'],
                    },
                    {
                        label: 'RAM(%)',
                        data: [],
                        borderColor: ['rgba(54,162,235,0.5)'],
                        backgroundColor: ['rgba(54,162,235,0.5)'],
                        pointBackgroundColor: ['rgba(54,162,235,0.5)'],
                        pointBorderColor: ['rgba(54,162,235,0.5)'],
                    }
                ]
            },
            lastCpu: 0,
            lastRam: 0
        }
    }


    componentDidMount() {
        this.interval = setInterval(async () => {
            await this.bindInfo(this.props.server + '/getInfo')
        }, 5000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }


    bindInfo = async (url) => {
        let res = await fetch(url, { method: 'GET' })
        let data = await res.json()
        // ----
        let info = data.res
        let cpu = this.state.config.datasets[0].data
        let ram = this.state.config.datasets[1].data
        if (cpu.length === 13) {
            cpu.pop()
            ram.pop()
        }
        cpu.unshift( ((info.cpu.total - info.cpu.idle) * (100 / info.cpu.total)).toFixed(8) )
        ram.unshift( ((info.ram.total - info.ram.free - info.ram.buffer - info.ram.cached) * (100 / info.ram.total)).toFixed(8))
        this.setState({
            config: {
                labels: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
                datasets: [
                    {
                        label: 'CPU(%)',
                        data: cpu,
                        borderColor: ['rgba(255,206,86,0.5)'],
                        backgroundColor: ['rgba(255,206,86,0.5)'],
                        pointBackgroundColor: ['rgba(255,206,86,0.5)'],
                        pointBorderColor: ['rgba(255,206,86,0.5)'],
                    },
                    {
                        label: 'RAM(%)',
                        data: ram,
                        borderColor: ['rgba(54,162,235,0.5)'],
                        backgroundColor: ['rgba(54,162,235,0.5)'],
                        pointBackgroundColor: ['rgba(54,162,235,0.5)'],
                        pointBorderColor: ['rgba(54,162,235,0.5)'],
                    }
                ]
            },
            lastCpu: cpu[0],
            lastRam: ram[0]
        })
    }

    render() {

        return (
            <Fragment>
                <div className="card-body">
                <Line data={this.state.config} redraw />
                </div>
                <div className="card-footer">
                    <div className="row">
                        <div className="col">
                            CPU(%): {this.state.lastCpu}
                        </div>
                        <div className="col">
                            RAM(%): {this.state.lastRam}
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default LineChart