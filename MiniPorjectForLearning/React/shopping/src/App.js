import React from 'react';
import Nav from './Nav';
import './App.css'
import { items } from './static-data';
import ItemPage from './itempage'
import CartPage from './CartPage'



class App extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      activeTab: 0,
      cart: [],
  
    };
  
  }


  handleTabChange = (index) => {
    this.setState(
      {
        activeTab: index
      }
    );
  }
  handleAddtoCart = (item) => {
    this.setState(
      {
        cart: [...this.state.cart, item.id]
      }
    );
  }

  handleRemoveOne = (item) =>{
    let index = this.state.cart.indexOf(item.id);
    this.setState({
      cart:[
        ...this.state.cart.slice(0, index),
        ...this.state.cart.slice(index + 1)
      ]
    })


  }
  



  renderContent() {
    switch (this.state.activeTab) {
      default:
      case 0: return <ItemPage
        items={items}
        onAddToCart={this.handleAddtoCart} />
      case 1: return  this.renderCart();
    }
  }



  renderCart (){
    // Count how many of each item is in the cart
    let itemCounts = this.state.cart.reduce((itemCounts, itemId) => {
      itemCounts[itemId] = itemCounts[itemId] || 0;
      itemCounts[itemId]++;
      return itemCounts;
    }, {});
    // Create an array of items
    let cartItems = Object.keys(itemCounts).map(itemId => {
      // Find the item by its id
      var item = items.find(item =>
        item.id === parseInt(itemId, 10)
      );
      // Create a new "item" that also has a 'count' property
      return {
        ...item,
        count: itemCounts[itemId]
      }
    });
    return (
      <CartPage items={cartItems} 
      onAddOne={this.handleAddtoCart}
      onRemoveOne={this.handleRemoveOne} />
    );
  }




  render() {
    let { activeTab } = this.state;

    return (

      <div className="App">
        <div>
      </div>
        <Nav activeTab={activeTab} onTabChange={this.handleTabChange} Item ={ this.state.cart.length} />
        <main className="app-content">
          {this.renderContent()}
        </main>
      </div>
    )
  }
}





export default App;
