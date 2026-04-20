import React,{useState} from 'react'
import Header from "../components/ui/Header"
import {ThemeProvider} from '@material-ui/core/styles';
import {BrowserRouter,Route,Switch}  from 'react-router-dom'
import  theme from "./ui/Theme"
import ProfessorMMA from "./ui/fighterPage";
import Statistics from "./ui/statistics";


function App() {
  const [value, setValue] = useState(0);

  return (
   <ThemeProvider theme ={theme}>
     <BrowserRouter>
     <Header value={value} setValue={setValue}  />
      <Switch>
      {/* <LandingPage /> */}
        <Route exact path="/" component={()=> <div style={{height: "2000px"}} >Landing page</div>}/>
        <Route exact path="/Project" component={ProfessorMMA }/>
        <Route exact path="/chart" component={Statistics}/>
        <Route exact path="/contact" component={()=> <div style={{height: "2000px"}} >contact</div> }/>
      </Switch>
     </BrowserRouter>
   </ThemeProvider>
      
  
  );
}

export default App;
