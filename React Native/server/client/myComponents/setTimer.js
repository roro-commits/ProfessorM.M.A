/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

 import React, { Component } from 'react';
 import {
   StyleSheet,
   Text,
   View,
   RefreshControl,
   ActivityIndicator
 } from 'react-native';
 import Timeline from 'react-native-timeline-flatlist'
 import axios from 'axios'
import StartButton from './startButton'
 
 export default class Refresh extends Component {
   constructor(){
     super()
     this.onEndReached = this.onEndReached.bind(this)
     this.renderFooter = this.renderFooter.bind(this)
     this.onRefresh = this.onRefresh.bind(this)
 
     this.data = [
       {time: '09:00', title: 'Archery Training', description: 'The Beginner Archery and Beginner Crossbow course does not require you to bring any equipment, since everything you need will be provided for the course. '},
       {time: '10:45', title: 'Play Badminton', description: 'Badminton is a racquet sport played using racquets to hit a shuttlecock across a net.'},
       {time: '12:00', title: 'Lunch'},
       {time: '14:00', icon:'camera',title: 'Watch Soccer', description: 'Team sport played between two teams of eleven players with a spherical ball. '},
       {time: '16:30', icon: require('./icon/cannabis.png') }
     ]
 
     this.state = {
       isRefreshing: false,      
       waiting: false,
       data: this.data,
       getTimeData:[],

     }
   }

   componentWillMount=() =>{
    console.log("before MOunt Set Timer")

    this.getTimeData();

  }

    getTimeData =() =>{
        let data;

        axios.get('/api') 
        .then((response) => {
            data = response.data
            
            console.log('Data has been recived');
            // changing  the revive file for icon 
          this.setState({getTimeData:data})
            

          //   let data =data.find((o, i) => {
          //     if (o.icon) {
          //         arr[i] = { icon : require('./icon/cannabis.png')};
          //         return true; // stop searching
          //     }
          // });

          // // datas = data

        })

        .catch(()=>{
            console.log('data is not recived')
        })
  
         return data

    }
 
   onRefresh(){
     this.setState({isRefreshing: true});
     this.getTimeData();
     //refresh to initial data
     setTimeout(() => {
       //refresh to initial data
       this.setState({
         data: this.data,
         isRefreshing: false
       });
     }, 2000);
   }
 
   onEndReached() {
     if (!this.state.waiting) {
         this.setState({waiting: true});
         this.onRefresh();
 
         //fetch and concat data
         setTimeout(() => {
 
           //refresh to initial data
           var data = this.props.data.concat(
             [
               {time: '18:00', title: 'Load more data', description: 'append event at bottom of timeline'},
               {time: '18:00', title: 'Load more data', description: 'append event at bottom of timeline'},
               {time: '18:00', title: 'Load more data', description: 'append event at bottom of timeline'},
               {time: '18:00', title: 'Load more data', description: 'append event at bottom of timeline'},
               {time: '18:00', title: 'Load more data', description: 'append event at bottom of timeline'}
             ]
             )
 
           this.setState({
             waiting: false,
             data: data,
           });
         }, 2000);
     }
   }
 
 renderFooter() {
     if (this.state.waiting) {
         return <ActivityIndicator />;
     } else {
         return <Text>~</Text>;
     }
   }
 
   render() {
     //'rgb(45,156,219)'
     return (
       <React.Fragment>

         <View style={styles.container}>
              <View>
              <Timeline 
                  style={styles.list}
                  data={this.state.getTimeData }
                  circleSize={30}
                  circleColor='rgb(45,156,219)'
                  lineColor='rgb(45,156,219)'
                  timeContainerStyle={{minWidth:52, marginTop: -5}}
                  timeStyle={{textAlign: 'center', backgroundColor:'#ff9797', color:'white', padding:5, borderRadius:13}}
                  descriptionStyle={{color:'gray'}}
                  options={{
                    style:{paddingTop:5},
                    refreshControl: (
                      <RefreshControl
                        refreshing={this.state.isRefreshing}
                        onRefresh={this.onRefresh}
                      />
                    ),
                    renderFooter: this.renderFooter,
                    //  onEndReached: this.onEndReached
                  }}
                  innerCircle={'dot'}
                />
              </View>

            <View >
          <StartButton icon={"reload"} text ={"load"}  props={this.onRefresh} />
          </View>  

       </View>

              

       </React.Fragment>
       
     );
   }
 }
 
 const styles = StyleSheet.create({
   container: {
     flex: 1,
     padding: 10,
         paddingTop:20,
     backgroundColor:'white'
   },
   list: {
     flex: 1,
     marginTop:10,
   },
 });