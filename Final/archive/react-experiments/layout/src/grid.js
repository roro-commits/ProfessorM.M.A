import React from 'react';
import {makeStyles} from '@material-ui/core';
import {Grid} from '@material-ui/core';
import {Paper} from '@material-ui/core';
import {Chip} from '@material-ui/core';
import {Typography} from '@material-ui/core';
import {Hidden} from '@material-ui/core'
const useStyle = makeStyles((theme)=>({
    grid: {
          overflow: true,
      width: '100%',
      // height:'100%',
      margin: '0px'
    },
    paper: {
      padding: theme.spacing(2),
      textAlign: 'center',
      color: theme.palette.text.secondary,
      background: theme.palette.success.light,
      height: '100px'
    }
    }));

const Item = (props) => <Grid item {...props} />
const Container = props => <Grid container {...props} />


function Grids () {

  const classes = useStyle();

    return(

        <Grid container className={classes.grid} spacing={1}>
          <Grid item  xs ={12} sm={6} md ={4}>
                <Paper className={classes.paper}>
                    xs =12 sm = 6 md =3  
                </Paper>
          </Grid>

          <Grid item  xs ={12} sm={6} md ={4}>
                <Paper className={classes.paper}>
                    xs =12 sm = 6 md =3  
                </Paper>
          </Grid>

          <Grid item  xs ={12} sm={12} md ={4}>
                <Paper className={classes.paper}>
                    xs =12 sm = 6 md =3  
                </Paper>
          </Grid>

          <Grid item  xs ={12} sm={9} md ={9}>
                <Paper className={classes.paper} height="300px" >
                    <Grid container spacing={4}  justify ="space-between">
                      <Grid item    xs ={12} sm={3} md ={4}>
                            <Paper >
                                  <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                       <Grid item    xs ={12} sm={3} md ={4}>
                            <Paper >
                                  <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                       <Grid item >
                            <Paper >
                                 <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                    </Grid>
                    <Grid container spacing={3}  justify ="space-between">
                      <Grid item >
                            <Paper >
                                  <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                       <Grid item >
                            <Paper >
                                  <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                       <Grid item >
                            <Paper >
                                 <Chip label =" xs =12 sm = 6 md =3" />
                            </Paper>
                       </Grid>
                    </Grid>
                    
                </Paper>
          </Grid>

<Hidden smDown>

<Item item  xs ={12} sm={3} md ={3}>
                  <Paper className ={classes.paper}  >
                        <Item item  xs ={12} sm={3} md ={3}>
                              <Container direction = "column" spacing={2}>
                                   <Item>
                                          <Item>
                                                      <Paper>
                                                            <Typography>One</Typography>
                                                      </Paper>
                                          </Item>
                                          <Item>
                                                      <Paper>
                                                            <Typography>TWo</Typography>
                                                      </Paper>
                                          </Item>
                                   </Item>
                                   <Item>
                                          <Item>
                                                      <Paper>
                                                            <Typography>One</Typography>
                                                      </Paper>
                                          </Item>
                                          <Item>
                                                      <Paper>
                                                            <Typography>TWo</Typography>
                                                      </Paper>
                                          </Item>
                                   </Item>
                              </Container>
                     
                        </Item>
                  </Paper>
            </Item>
</Hidden>
        </Grid>

        
   
    )
}

export default Grids;