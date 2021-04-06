import * as React from 'react';
import { Button } from 'react-native-paper';


const StartButton = ({props ,text,icon}) => (
    <Button icon={icon} mode="contained" onPress={props} >
     {text}
    </Button>
  );
  
  export default StartButton;