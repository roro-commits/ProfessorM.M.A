import React from 'react';
import PropTypes from 'prop-types';
import Item from './Item'
import './ItemPages.css';

function ItemPage ({items, onAddToCart}){
return(
 <ul className="ItemPage-items">
    {
        items.map(item =>
            <li key={item.id}className="ItemPage-item">
                <Item item={item}
                onAddToCart= {()=> onAddToCart(item)} >
                    <button className="Item-addToCart"   onClick = { () => onAddToCart(item)} >
                        Add to cart
                    </button>

                </Item>
                </li>
            )
    }
    
</ul>
);

}
ItemPage.propTypes = {
    Items: PropTypes.array.isRequired
};

export default ItemPage;