import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import SwipeableViews from 'react-swipeable-views';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Grid from '@material-ui/core/Grid';

import Post from "../posts"
import SearchBar from "../searchBar"
import APIClient from '../apiClient'
import listing from '../listing'

const styles = theme => ({
 root: {
   marginTop: 30
 },
 paper: {
   padding: theme.spacing(2),
   textAlign: 'center',
   color: theme.palette.text.secondary,
 },
});

class Home extends React.Component {
     post={
        Body:0,
        Title:0,
        Id:0,
         ViewCount:-1,
         Score:-1
    }
    state = {
    posts:[], scoreOrViewCount:-1,
     searchTerm:""
 };

 async componentDidMount() {
   this.apiClient = new APIClient("");
   this.apiClient.getposts().then((data) => this.setState({ ...this.state, posts:data})
   );
 }

 resetPosts= posts => this.setState({ ...this.state, posts:posts })
 onSearch = (event) => {
   const target = event.target;
   if (!target.value || this.searchTerm==target.value) { this.setState({searchTerm:""}); return }
   this.setState({searchTerm: event.target.value});
   this.onRefresh();

 }
onListTypeChange = (event) => {

     this.setState({scoreOrViewCount: event.target.value});
 }

 onRefresh = (event) => {
     listing.getJSONListing(this.state.searchTerm,this.state.scoreOrViewCount)
     .then((response) => {
        this.setState({ ...this.state, posts:response});

     })
 }
 renderpost = (posts) => {
   if (!posts) { return [] }
   return posts.map((post) => {
       return (
         <Grid key={post.Id}>
             <Post post={post} />
         </Grid>
     );
   })
 }
 render() {
   return (
     <div className={styles.root}>
       <SearchBar onSearch={this.onSearch} onListingTypeChanged={this.onListTypeChange} onRefresh={this.onRefresh} />
       {/* <Tabs*/}
       {/*  indicatorColor="primary"*/}
       {/*  textColor="primary"*/}
       {/*  fullWidth*/}
       {/*>*/}
       {/*  <Tab label="posts" />*/}
       {/*</Tabs>*/}
           { this.renderpost(this.state.posts)}
     </div>
   );
 }
}

export default withStyles(styles)(Home);