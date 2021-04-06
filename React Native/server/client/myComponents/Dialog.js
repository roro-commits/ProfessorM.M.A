import * as React from 'react';
import { Button, Dialog, Portal } from 'react-native-paper';

const DilaogMessage = ({restart}) => {
  const [visible, setVisible] = React.useState(false);

  const hideDialog = () => setVisible(false);

  return (
    <Portal>
      <Dialog visible={visible} onDismiss={hideDialog}>
        <Dialog.Actions>
          <Button onPress={() => console.log('Cancel')}>Cancel</Button>
          <Button onPress={restart}>Restart</Button>
        </Dialog.Actions>
      </Dialog>
    </Portal>
  );
};

export default DilaogMessage;