import './App.css';
import Box from './component/box'
import Header from './component/header'



function App({threads}) {
  return (
    <div className="App">
      <Header />
      {
        threads.map(threads => 
         <Box threads = {threads} />
        )}
      
    </div>
  );
}

export default App;
