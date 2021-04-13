const express = require('express');
const router = express.Router();

const getTimer = require('../Models/getTimer')


//routes 

router.get('/', (req, res) => {
   
    getTimer.find({})
    .then((data) => {
        // console.log(data)
        res.json(data);

    })
    .catch((error) => {
        console.log('error', dearrorta)
    })
});


router.post('/save', (req, res) => {
   
     // console.log(data)
     console.log('Body', req.body);

     const data = req.body;

    // calling Model
    const timer = getTimer(data);

    //saving to data base 
    timer.save((error)=>{
        if(error){
                res.status(500).json({msg:'Sorry Data not saved Internal Server Error '})
        }else{
            //
            res.json({
                msg:"Data Saved to DataBase"
            });

        }

    });

     
    
});



router.get('/name', (req, res) => {
    const data = {
        username: 'koko',
        age: 5

    };
    res.json(data);
});





module.exports = router;