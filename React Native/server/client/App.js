import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MyComponent from './myComponents/mainFrame'

export default function App() {
  

  return (
    
    <React.Fragment>
      <MyComponent/>
    </React.Fragment>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
