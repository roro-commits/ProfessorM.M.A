
import React, { Component, useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View
} from 'react-native';
import Timeline from 'react-native-timeline-flatlist';

export const MyTimeLine = (props) => {
  
  const [data, setData] = useState([props.theData]);
  
  useEffect(() => {
    setData(props.theData);
  }, [props.theData]);

  return (
    <View style={styles.container}>
      <Timeline
        style={styles.list}
        data={data}
      />
    </View>

  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
		paddingTop:65,
		backgroundColor:'white'
  },
  list: {
    flex: 1,
    marginTop:20,
  },
});
