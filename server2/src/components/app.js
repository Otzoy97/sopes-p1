import React from 'react'
import {BrowserRouter, Route, Switch} from 'react-router-dom'

const app = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path="/posts"></Route>
            <Route exact path="/stats"></Route>
            <Route component={NotFound}></Route>
        </Switch>
    </BrowserRouter>
)