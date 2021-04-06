
const mongoose = require('mongoose');



//schema 
const Schema = mongoose.Schema;

const timeStoreSchema = new Schema({

        time:String,
        title:String,
        description:String,
        icon:String,
        dotColor:String,
});

//Model 

const getTimer = mongoose.model('getTime', timeStoreSchema)

module.exports = getTimer;