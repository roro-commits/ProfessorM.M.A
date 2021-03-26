import './App.css';
import {makeStyles} from "@material-ui/core/styles";
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import SimpleTabs from './nav'



const useStyle = makeStyles((theme)=>({
grid: {
  width: '100px',
  height:'100px',
  margin: '0px'
},
paper: {
  padding: theme.spacing(2),
  textAlign: 'center',
  color: theme.palette.text.secondary,
  background: theme.palette.success.light,
}
}));

function App() {
  const classes = useStyle();

  return (
    
    <div className={classes.root}>

      <Paper className={classes.paper}><SimpleTabs/></Paper>
  
    </div>
  );
}

export default App;
