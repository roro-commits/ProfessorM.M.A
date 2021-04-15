/* eslint-disable no-use-before-define */
import React,{useEffect,useState} from 'react';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import axios from 'axios'
import FighterData from '../Data/fighterDataset.json'
import { Button } from '@material-ui/core';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardActionArea from '@material-ui/core/CardActionArea';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box'

import { Radar, RadarChart, PolarGrid, Legend, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts';






      // abstract Grid

     const Grids = (props) => <Grid container {...props} />
     const GridCol = (props) => <Grid container direction ='column'{...props} />
     const GridRow = (props) => <Grid container direction ='row'{...props} />
     const Item = (props) => <Grid item {...props} />




const useStyle = theme => ({
  toolbarMargin: {
    ...theme.mixins.toolbar,
    marginBottom: "1em",
    [theme.breakpoints.down("xs")]:{
      marginBottom: "1.5em",

    },
  },
  logo: {
    // height:"100px",
    width: "16em",
    [theme.breakpoints.down("md")]:{
      height: "5em",
      width: "17em",
    },
    [theme.breakpoints.down("xs")]:{
      height: "5.5em",
      width: "19em",

    },

  },
  paper:{
     display: "flex",
    flexWrap: "wrap",
    "& > *": {
       marginTop:theme.spacing(200),
      margin: theme.spacing(30),
      width: theme.spacing(300),
      height: theme.spacing(16)
    }
  },
   root: {
      backgroundColor: '#FAFAFA',
    minWidth: 200,
     minHeight:300,
  },
  Win: {
      backgroundColor: '#BCE6DA',
    minWidth: 200,
     minHeight:300,
  },
 Loss: {
  backgroundColor:'#F0A89C',
minWidth: 200,
 minHeight:300,
},
    draw:{
        backgroundColor: '#F0E79C',
        minWidth: 200,
        minHeight:300,

    },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});






class Statistics extends React.PureComponent {
constructor(props){
    super(props)
    this.state = {
      selectOptionsNames : [],
      height: [],
      DOB:[],
      SApM:[],
      SLpM:[],
      REACH:[],
      STANCE:[],
      WEIGHT:[],
      strikeAccuracy:[],
      strDef:[],
      tdAcc:[],
      subAvg:[],
      tdDef:[],
      tdAvg:[],
      FighterA:[],
      FighterB:[],
      Response:false,
      Response1:false,
      Favourite: '',
      UnderDog: '',
      favWin:false,
      undWin:false,
      draw:false,
    }
    this.getFighterA = this.getFighterA.bind(this);

  }


  async getOptions(){
    const res = await axios.get('http://127.0.0.1:5000/static/fighterDataset2.json')
    const data = res.data
    const nameData =[]
    const heightData =[]
    const StrikeAcc =[]
    const DOB =[]
    const SApM =[]
    const SLpM =[]
    const REACH =[]
    const STANCE =[]
    const WEIGHT =[]
    const strDef =[]
    const tdAcc =[]
    const subAvg =[]
    const tdDef =[]
    const tdAvg =[]


    for(let i =0; i< 6000 ;i++){
      // console.log(FighterData.Name[i])
      if (FighterData.Name[i] !== undefined){
        nameData.push({ "Name" : FighterData.Name[i]})
        heightData.push({"Height": FighterData.HEIGHT[i]})
        StrikeAcc.push({"StrAcc": FighterData["Str. Acc.."][i]})
        DOB.push({"DOB":FighterData.DOB[i]})
        SApM.push({"SApM":FighterData.SApM[i]})
        SLpM.push({"SLpM":FighterData.SLpM[i]})
        REACH.push({"REACH":FighterData.REACH[i]})
        STANCE.push({"STANCE":FighterData.STANCE[i]})
        WEIGHT.push({"WEIGHT":FighterData.WEIGHT[i]})
        strDef.push({"strDef":FighterData["Str. Def"][i]})
        tdAcc.push({"tdAcc":FighterData["TD Acc"][i]})
        subAvg.push({"subAvg":FighterData["Sub. Avg"][i]})
        tdDef.push({"tdDef":FighterData["TD Def."][i]})
        tdAvg.push({"tdAvg":FighterData["TD Avg"][i]})


      }
    }

    this.setState({selectOptionsNames: nameData})
    this.setState({height: heightData})
    this.setState({strikeAccuracy: StrikeAcc})
    this.setState({DOB: DOB})
    this.setState({SLpM: SLpM})
    this.setState({REACH: REACH})
    this.setState({STANCE: STANCE})
    this.setState({WEIGHT: WEIGHT})
    this.setState({strDef: strDef})
    this.setState({tdAcc: tdAcc})
    this.setState({subAvg: subAvg})
    this.setState({tdDef: tdDef})
    this.setState({tdAvg: tdAvg})
    this.setState({SApM: SApM})




  }
    componentDidMount(){
      this.getOptions()
  }



  getFighterA(param){
    const indexA = this.state.selectOptionsNames.indexOf(param);
    const FighterA=[]


    if(indexA !== -1 ){
      // this.setState({FighterA:[]}) // reset array before setting new data
      FighterA.push(this.state.selectOptionsNames[indexA].Name)
      FighterA.push(this.state.height[indexA].Height)
      FighterA.push(this.state.WEIGHT[indexA].WEIGHT)
      FighterA.push(this.state.REACH[indexA].REACH)
      FighterA.push(this.state.STANCE[indexA].STANCE)
      FighterA.push(this.state.DOB[indexA].DOB)
      FighterA.push(this.state.SLpM[indexA].SLpM)
      FighterA.push(this.state.strikeAccuracy[indexA].StrAcc)
      FighterA.push(this.state.SApM[indexA].SApM)
      FighterA.push(this.state.strDef[indexA].strDef)
      FighterA.push(this.state.tdAvg[indexA].tdAvg)
      FighterA.push(this.state.tdAcc[indexA].tdAcc)
      FighterA.push(this.state.tdDef[indexA].tdDef)
      FighterA.push(this.state.subAvg[indexA].subAvg)
    }
    this.setState({FighterA:FighterA})
    this.setState({Response:false});
    this.setState({favWin:false});
    this.setState({undWin:false});
    this.setState({draw:false});



  }







     // const Grids = (props) => <Grid container {...props} />
     // const GridCol = (props) => <Grid container direction ='column'{...props} />
     // const GridRow = (props) => <Grid container direction ='row'{...props} />
     // const Item = (props) => <Grid item {...props} />


  render(){
      const { classes } = this.props;
      const bull = <span className={classes.bullet}>•</span>;
    return (

    <React.Fragment>
       <Box p={5}>
           <GridCol>
                <GridCol direction="column" justify="center" alignItems="center">
                    <Item xs={12}>
                      <GridRow spacing={10}>

                            <Item xs={12} lg={6}>

                              <GridRow>
                                  <Item >
                                      <Box p={1.5}>
                                          <Paper  styles={classes.paper}>

                                             <Autocomplete
                                              id="FighterA"
                                              options={this.state.selectOptionsNames}
                                              getOptionLabel={(option) => option.Name}
                                              style={{ width: 500 }}
                                              onChange={(event, value) => this.getFighterA(value)} // sends Index of selected Item Fighter A
                                              renderInput={(params ) => <TextField {...params}  label="Fighters" variant="outlined" />}
                                            />
                                        </Paper>
                                      </Box>

                                </Item>

                              </GridRow>
                          </Item>




                      </GridRow>
                </Item>

                </GridCol>

                  <Box p={10}>
                      <Item xs={12} lg={12}>
                               <GridCol  justify="center" alignItems="center">
                                   <Item>
                                        <Card  elevation={3} className={this.state.Response1?  this.state.draw ?  classes.draw : this.state.undWin ? classes.Win: classes.Loss : classes.root}>
                                    <CardActionArea>
                                        <CardActions>
                                            <CardContent>
                                                <Typography variant="h7" component="h1">
                                                   Radar Chart
                                                 </Typography>

                                            </CardContent>
                                        </CardActions>
                                         <GridRow justify="center" alignItems="center">
                                        <Item xs={12}>
                                             <ResponsiveContainer width={1200} height={500}>
                                                <RadarChart cx="50%" cy="50%" outerRadius="80%" data={data}>
                                                  <PolarGrid />
                                                  <PolarAngleAxis dataKey="subject" />
                                                  <PolarRadiusAxis angle={30} domain={[0, 150]} />
                                                  <Radar name="Mike" dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.3} />
                                                  <Radar name="Lily" dataKey="B" stroke="#82ca9d" fill="#82ca9d" fillOpacity={0.3} />
                                                  <Legend />
                                                </RadarChart>
                                            </ResponsiveContainer>
                                        </Item>
                                     </GridRow>
                                    </CardActionArea>
                                </Card>
                                   </Item>

                               </GridCol>
                      </Item>
                  </Box>

                  <Box p={20}>
                      <Item xs={12} lg={12}>
                               <GridCol  justify="center" alignItems="center">
                                   <Item>
                                        <Card  elevation={3} className={this.state.Response1?  this.state.draw ?  classes.draw : this.state.undWin ? classes.Win: classes.Loss : classes.root}>
                                    <CardActionArea>
                                        <CardActions>
                                            <CardContent>
                                                <Typography variant="h7" component="h1">
                                                   Bar Chart
                                                 </Typography>

                                            </CardContent>
                                        </CardActions>
                                         <GridRow justify="center" alignItems="center">
                                        <Item xs={12}>
                                             <ResponsiveContainer width={1200} height={500}>
                                                <RadarChart cx="50%" cy="50%" outerRadius="80%" data={data}>
                                                  <PolarGrid />
                                                  <PolarAngleAxis dataKey="subject" />
                                                  <PolarRadiusAxis angle={30} domain={[0, 150]} />
                                                  <Radar name="Mike" dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
                                                  <Radar name="Lily" dataKey="B" stroke="#82ca9d" fill="#82ca9d" fillOpacity={0.6} />
                                                  <Legend />
                                                </RadarChart>
                                            </ResponsiveContainer>
                                        </Item>
                                     </GridRow>
                                    </CardActionArea>
                                </Card>
                                   </Item>

                               </GridCol>
                      </Item>
                  </Box>



            </GridCol>

       </Box>

    </React.Fragment>

  );
  }
}

const data = [
  {
    subject: 'Math',
    A: 120,
    B: 110,
    fullMark: 150,
  },
  {
    subject: 'Chinese',
    A: 98,
    B: 130,
    fullMark: 150,
  },
  {
    subject: 'English',
    A: 86,
    B: 130,
    fullMark: 150,
  },
  {
    subject: 'Geography',
    A: 99,
    B: 100,
    fullMark: 150,
  },
  {
    subject: 'Physics',
    A: 85,
    B: 90,
    fullMark: 150,
  },
  {
    subject: 'History',
    A: 65,
    B: 85,
    fullMark: 150,
  },
];


// export default class ComboBox
export default withStyles(useStyle)(Statistics)

