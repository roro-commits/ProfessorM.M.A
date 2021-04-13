import * as React from 'react';
import { Appbar } from 'react-native-paper';

const TopBar = ({title,subtitle}) => (
    <Appbar.Header>
       <Appbar.Content title={title} subtitle={subtitle} />
    </Appbar.Header>
);

export default TopBar;