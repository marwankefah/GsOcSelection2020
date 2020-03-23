import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import CardActions from '@material-ui/core/CardActions';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import FavoriteIcon from '@material-ui/icons/Favorite';


const styles = theme => ({
  card: {
  },
  media: {
    height: 0,
    paddingTop: '56.25%', // 16:9
  },
  actions: {
    display: 'flex',
  }
});

class posts extends React.Component {
  // handleClick = (event) =>  {
  //   this.props.----(this.props.repo)
  // }
  renderTitle= (title) => {
      if(title==null){
          return "NO TITLE";
      }
      else{return title;}
  }
    renderInfo= (score,viewCount) => {
      console.log(score)
          return "Score :"+score+" View Count :"+ viewCount;
  }
  render() {
    const { classes } = this.props;
    return (
      <Card className={classes.card}>
        <CardHeader
          title={this.renderTitle(this.props.post.Title)}
        />

        <CardContent>
            <div>Score : {this.props.post.Score} </div>
            <div>View Count :{ this.props.post.ViewCount}</div>
            <div dangerouslySetInnerHTML={{__html: this.props.post.Body}}/>
        </CardContent>
      </Card>
    );
  }
}

export default withStyles(styles)(posts);