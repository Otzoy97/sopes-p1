import React from 'react'
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import Posts from '../pages/posts'
import Stats from '../pages/stats'
import NotFound from '../pages/404'

const App = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/posts" component={Posts}/>
            <Route exact path="/stats" component={Stats}/>
            <Route exact path="/" component={null}/>
            <Route component={NotFound} />
        </Switch>
    </BrowserRouter>
)

export default App