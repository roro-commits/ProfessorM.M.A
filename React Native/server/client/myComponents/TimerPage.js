import React, { PureComponent } from 'react';
import { View, StyleSheet } from 'react-native';
import { TabViewAnimated, TabBar, SceneMap } from 'react-native-tab-view';
import {TImer} from './Timer'
import Constants from 'expo-constants';
import {SetTimer} from './Timer'






const FirstRoute = () => {
  return (
    <React.Fragment>
      <View style={styles.containerTimer}>
        <TImer/>
      </View>
    </React.Fragment>
)
}
const SecondRoute = () => {
  return (
    <React.Fragment>
      <View style={styles.containerTimer}>
        <SetTimer/>
      </View>
    </React.Fragment>
)
}


export default class TimerTab extends PureComponent {
  state = {
    index: 1,
    routes: [
      { key: '1', title: 'Timer' },
      { key: '2', title: 'Set Timer' },
    ],
  };

  _handleIndexChange = index => this.setState({ index });

  _renderHeader = props => <TabBar {...props} />;

  _renderScene = SceneMap({
    '1': FirstRoute,
    '2': SecondRoute,
  });

  render() {
    return (
      <TabViewAnimated
        style={styles.container}
        navigationState={this.state}
        renderScene={this._renderScene}
        renderHeader={this._renderHeader}
        onIndexChange={this._handleIndexChange}
      />
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  containerTimer: {
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
      marginTop:40

  },
});