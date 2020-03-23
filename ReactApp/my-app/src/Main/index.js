import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'
//import { Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';

// import Login from '../Login'
import Home from '../Home'

class Main extends Component {
 render() {
   return (
       // for Login page and authoentication not needed to render for now --selection GSOC2020
     <Router path="/" component={Home}>
         <Home> </Home>
       {/*<Security*/}
       {/*  issuer={yourOktaDomain}*/}
       {/*  client_id={yourClientId}*/}
       {/*  redirect_uri={'http://localhost:8080/implicit/callback'}*/}
       {/*  scope={['openid', 'profile', 'email']}>*/}
       {/*  <Switch>*/}
       {/*    <Route exact path="/" component={Login} />*/}
       {/*    <Route path="/implicit/callback" component={ImplicitCallback} />*/}
       {/*    <SecureRoute path="/" component={Home} />*/}
       {/*  </Switch>*/}
       {/*</Security>*/}
     </Router>
   );
 }
}

export default Main;