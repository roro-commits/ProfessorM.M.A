import * as React from 'react';
import {StyleSheet, TextPropTypes, View} from 'react-native'
import { BottomNavigation, Text} from 'react-native-paper';
import { MyTimeLine } from './MyTimeLine';
import TopBar from './TitleAppBar';
import Constants from 'expo-constants';
import TimerTab from './TimerPage'
import TimerTabs from './TimerPageTwo'
import PostData from './data/post.json'
import axios from 'axios'
import StartButton from './startButton'
import Refresh from './setTimer'
import { mdiTimelineClockOutline } from '@mdi/js';







let datas =[];
export {datas}

let timeLineData = [
    {time: '09:00', title: 'Event 10', lineColor:'#009688',},
    {time: '10:45', title: 'Event 2', description: 'Event 2 Description'},
    {time: '12:00', title: 'Event 3', description: 'Event 3 Description'},
    {time: '14:00', title: 'Event 44', description: 'Event 4 Description'},
    {time: '16:30', title: 'Event 55', description: 'Event 5 Description'}
];

export {timeLineData}



class  MyComponent extends React.Component{
  
    state = {

      index: 0,
      routes:[ 
          { key: 'TimeLine', title: 'TimeLine', icon: 'timeline-clock-outline' },
          { key: 'Timer', title: 'Timer', icon: 'timer' },
          
      ],
    };

 
  //  FriendsRoute = () => {
  //     return(
  //         <React.Fragment>
  //           <TopBar title = "LeaderBoard " subtitle="Ranks" />
            

  //         </React.Fragment>

  //     )

  //  }

    TimerRoute = () =>  {
    return(
        <React.Fragment >
            <TopBar title = "Timer " subtitle="clock" />
              <TimerTabs/>
        </React.Fragment>
    );
    }


   TimeLineRoute = () => {
      return(
          <React.Fragment>
              <TopBar title = "Time Line" subtitle="Today"/>
              <React.Fragment >
                  <Refresh data={timeLineData}/>
              </React.Fragment>
             
          </React.Fragment>
      );
      }




    _handleIndexChange = index => this.setState({ index });
   renderScene = BottomNavigation.SceneMap({
    TimeLine: this.TimeLineRoute,
    Timer: this.TimerRoute,
    // Friend: this.FriendsRoute,
  });

 

 render (){ return (
    <BottomNavigation
      navigationState={this.state}
      onIndexChange={this._handleIndexChange}
      renderScene={this.renderScene}
    />
  );}
  
};


const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      paddingTop: Constants.statusBarHeight,
      backgroundColor: '#ecf0f1',
      padding: 8,
    },
    remainingTime: {
      fontSize: 46,
    },
    startButton:{
        marginTop:'40px'

    },
  });





export default MyComponent;

