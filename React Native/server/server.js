//import npm packages

const  express = require('express');
const  mongoose = require('mongoose');
const  morgan = require('morgan');
const  path = require('path');
const  cors = require('cors');

const { stringify } = require('querystring');

const app = express();
const PORT = 8081||process.env.PORTS;
const prod = true;

const routes = require('./routes/api')


mongoose.connect(process.env.MONGODB_URI||process.env.MONGODB_URIS||'mongodb://localhost/getTimer',{
    useNewUrlParser:true,
    useUnifiedTopology: true,
});

mongoose.connection.on('connected', () => {
    console.log('Mongoose is connected!!!!!');
})


if (prod){
    app.use(express.static('client/web-build'));
}


app.use(function(req, res, next) {
    const allowedOrigins = ['http://127.0.0.1:19000', 'http://192.168.43.234:19000', 'http://0.0.0.0:9006', 'http://localhost:9006'];
    const origin = req.headers.origin;
    if (allowedOrigins.includes(origin)) {
       res.setHeader('Access-Control-Allow-Origin', origin);
    }
    // res.header("Access-Control-Allow-Origin", "http://localhost:19006"); // update to match the domain you will make the request from
    // res.header("Access-Control-Allow-Origin", "exp://127.0.0.1:19000"); // update to match the domain you will make the request from
    // res.header("Access-Control-Allow-Origin", "exp://192.168.43.234:19000"); // update to match the domain you will make the request from
    // res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header('Access-Control-Allow-Methods', 'GET, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.header('Access-Control-Allow-Credentials', true);
    next();
  });

//middle  for data passed to  express for parsing 
app.use(express.json());
app.use(express.urlencoded({extended: false}))

// cross platform origin 
app.use(cors());

//HTTP request logger
app.use(morgan('tiny'));

app.use('/api',routes)




app.listen( PORT, console.log(`Server ios starting at ${PORT}`))