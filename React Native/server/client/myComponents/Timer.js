import * as React from 'react';
import { Text, View, StyleSheet, Animated } from 'react-native';
import Constants from 'expo-constants';
import { CountdownCircleTimer } from 'react-native-countdown-circle-timer'
import StartButton from './startButton'
import DilaogMessage from './Dialog'
import { ToggleButton,DefaultTheme, Provider as PaperProvider } from 'react-native-paper';
import {Picker} from '@react-native-picker/picker';
import {timeLineData} from './mainFrame'
import moment from 'moment';
import axios from 'axios'



let values  = 10;
let job = 'cloudOS';


const children = ({ remainingTime }) => {
    const hours = Math.floor(remainingTime / 3600)
    const minutes = Math.floor((remainingTime % 3600) / 60)
    const seconds = remainingTime % 60
  
    return `${hours}:${minutes}:${seconds}`
  };

  const theme = {
    ...DefaultTheme,
    roundness: 2,
    colors: {
      ...DefaultTheme.colors,
      primary: '#3498db',
      accent: '#dbc834',
    },
  };


const SetTimer = () => {
    const [value, setValue] = React.useState(10);
    const [selectedLanguage, setSelectedLanguage] = React.useState('cloudOS');

    return (
      <React.Fragment>
        <View  style={styles.view} >
         <Text style ={styles.text}> Pick Time </Text>
         <Text style ={styles.text2}> 10sec | 1min| 5min| 50min </Text>
         {/* <React.Fragment>  
         <Text style ={styles.text2}> 10sec </Text>
         <Text style ={styles.text2}>  1min </Text>
         <Text style ={styles.text2}>  5min </Text>
         <Text style ={styles.text2}>  30min </Text>
         </React.Fragment> */}

        <ToggleButton.Row style={styles.color} onValueChange={value => setValue(value)} value={value}>
            <ToggleButton size ={40} icon="timer-10" onPress={() => {values = 10}} value={10} />
            <ToggleButton size ={40} icon="clock-time-six" onPress={() => {values = 60}} value="1 min" />
            <ToggleButton size ={40} icon="timelapse" onPress={() => {values = 300}} value="5 min" />
            <ToggleButton size ={40} icon="clock-time-twelve-outline" onPress={() => {values = 3000}} value="30 min" />
      </ToggleButton.Row>

      <Text style ={styles.text}> Select Subject </Text>
         <View  >
         <ToggleButton.Row  style={styles.color} size={80} onValueChange={selectedLanguage => setSelectedLanguage(selectedLanguage)} value={selectedLanguage}>
            <ToggleButton size ={40} icon="cloud-check" onPress={() => {job = 'cloudOS Computing'}} value='cloudOS' />
            <ToggleButton size ={40} icon="code-json" onPress={() => {job = 'C++ Programing'}} value="C++" />
            <ToggleButton size ={40} icon="math-integral-box" onPress={() => {job = 'Mathematics'}} value="Math" />
            <ToggleButton size ={40} icon="cannabis" onPress={() => {job = 'Recreation'}} value="plus" />
      </ToggleButton.Row>
      
         </View>
      </View>
      </React.Fragment>
     
    );
  };




class TImer extends React.Component {
    constructor(props) {       
        super(props);
       
                 //line 2
        this.state = {     //line 3
          start : false,
          time: 10,
          done:false ,
          key:0,

         
       };
       
      

       this.onselectstart = () =>{
        this.setState({time: values})
        console.log("pressed");
        this.setState({ start:true });
        this.setState({ done:true });
    }

    this.onReset =() =>{
        console.log(this.state.done);
        this.setState({ key: this.state.key+1 });
        this.setState({time: values})

        console.log(timeLineData.length)

    }

    this.getTime =() =>{

      console.log("testing")
      console.log(job)
      
    }

    this.submit = (event) => {
      // event.preventDefault();
        let data = job
        let val = values
        let description =''
        let dotColor = ''


        var date = moment()
        .utcOffset('+1')
        .format('hh:mm a');

        // 'cloudOS Computing'}} value='cloudOS' />
        //     > {job = ' C++ Programing'}} value="C++" />
        //     <=>  { job = 'Mathematics'}} value="Math" />
        //      'Recreation'}} value="plus" 

        if (job === 'cloudOS Computing'){
          description =' Studying Cloud Computing .....'
          dotColor = 'green'
         }
         if (job === 'C++ Programing'){
          description =' Programming in C++, Programmer rule the world .....'
          dotColor = 'red'
         }
         if (job === 'Mathematics'){
          description = 'In real life, I assure you, there is no such thing as algebra'
          dotColor = 'brown'
         }
         if (job === 'Recreation'){
          description = 'Herb is the healing of a nation, alcohol is the destruction.  —Bob Marley '
          dotColor = 'brown'
         }
          
    const payload = {
        title: job,
        time: date,
        description: description,
        dotColor: dotColor,
    }

      axios({
          url: '/api/save',
          method:'POST',
          data: payload,
      })
      .then (() =>{
        console.log("File has been sent to the server ")
      })
      .catch(() =>{
        console.log("internal Server Error")
      });;

    }
  }
     
       

        

       render(){
           return(
            <React.Fragment>
                <View style={styles.container}>
                    <CountdownCircleTimer
                    key={this.state.key}
                    isPlaying={this.state.start.valueOf()}
                    duration={this.state.time}
                    colors={[
                    ['#004777', 0.4],
                    ['#F7B801', 0.4],
                    ['#A30000', 0.2],
                    ]}
                    size = {250}
                    // onComplete	
                    ariaLabel ={"keep going!!"}
                    onComplete ={() => {this.state.done = true},this.submit}
                    
                    >
                    {({ remainingTime, animatedColor }) => (
                    <Animated.Text style={{ color: animatedColor }, styles.remainingTime}>
                        {children({remainingTime})}
                    </Animated.Text>
                    )}
            
                    </CountdownCircleTimer>

                    <View style={styles.startButton}>
                    <React.Fragment>
                        <StartButton  icon={'clock-start'}  props={this.state.done === false ? this.onselectstart : this.onReset} text={this.state.done === false ? 'Start Timer !!!': "Restart!!!"}  />
                    </React.Fragment>
                </View>
                  
                </View>
            
             
            
            </React.Fragment>

           )
       }
}


const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      // paddingTop: Constants.statusBarHeight,
      backgroundColor: 'white',
      padding: 8,
      marginTop:0
    },
    remainingTime: {
      fontSize: 60,
    },
    startButton:{
        marginTop:65

    },
    color:{
      // backgroundColor:'blue'
    },
    text:{
      marginBottom:40,
      marginTop:40

    },
    text2:{
      marginBottom:40
    },
    view:{
      justifyContent: 'center',
      alignItems: 'center',
    },
  });

export{
  SetTimer,
  TImer,
}
