import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import SwipeableViews from 'react-swipeable-views';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Grid from '@material-ui/core/Grid';

import posts from "../posts"
import SearchBar from "../searchBar"
import APIClient from '../apiClient'
import listing from '../listing'

const styles = theme => ({
 root: {
   flexGrow: 1,
   marginTop: 30
 },
 paper: {
   padding: theme.spacing.unit * 2,
   textAlign: 'center',
   color: theme.palette.text.secondary,
 },
});

class Home extends React.Component {
 state = {
    posts: [],
    scoreOrViewCount:-1,
     searchTerm:""
 };

 async componentDidMount() {
     console.log("HI from home")
   this.apiClient = new APIClient("");
   this.apiClient.getposts().then((data) =>
     this.setState({...this.state, posts: data})
   );
 }






 resetPosts= posts => this.setState({ ...this.state, posts })
 onSearch = (event) => {
   const target = event.target;
   if (!target.value) { this.setState({searchTerm:""}); return }
   this.setState({searchTerm: event.target.value});

 }
onListTypeChange = (event) => {
     this.setState({value: event.target.value});
 }
 onRefresh = (event) => {
     listing.getJSONListing(this.state.searchTerm,this.state.scoreOrViewCount)
     .then((response) => {
       this.setState({ ...this.state});
       this.resetPosts(response.items);
     })
 }

 render() {
   return (
     <div className={styles.root}>
       <SearchBar onSearch={this.onSearch} onListingTypeChanged={this.onListTypeChange} onRefres={this.onRefresh} />
       {/* <Tabs*/}
       {/*  indicatorColor="primary"*/}
       {/*  textColor="primary"*/}
       {/*  fullWidth*/}
       {/*>*/}
       {/*  <Tab label="posts" />*/}
       {/*</Tabs>*/}

       <SwipeableViews
         axis={'x-reverse'}
       >
         <Grid container spacing={16} style={{padding: '20px 0'}}>
           { this.state.posts }
         </Grid>
       </SwipeableViews>
     </div>
   );
 }
}

export default withStyles(styles)(Home);