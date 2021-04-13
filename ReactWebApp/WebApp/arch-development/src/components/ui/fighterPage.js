/* eslint-disable no-use-before-define */
import React,{useEffect,useState} from 'react';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import {json} from 'd3'
import axios from 'axios'
import FighterData from '../Data/fighterDataset.json'
import { Button } from '@material-ui/core';




        // FighterData.DOB
        // FighterData.SApM
        // FighterData.SLpM
        // FighterData.REACH
        // FighterData.STANCE
        // FighterData.WEIGHT
        // FighterData["Str. Acc.."]
        // FighterData["Str. Def"]
        // FighterData["TD Acc"]
        // FighterData["Sub. Avg"]
        // FighterData["TD Def."]
        // FighterData["TD Avg"]

export default class ComboBox extends React.Component {
constructor(props){
    super(props)
    this.state = {
      selectOptionsNames : [],
      height: [],
      DOB:[],
      SApM:[],
      SLpM:[],
      REACH:[],
      STANCE:[],
      WEIGHT:[],
      strikeAccuracy:[],
      strDef:[],
      tdAcc:[],
      subAvg:[],
      tdDef:[],
      tdAvg:[],
      FighterA:[],
      FighterB:[],
    }
    this.getFighterA = this.getFighterA.bind(this);
    this.getFighterB = this.getFighterB.bind(this);
    this.postData = this.postData.bind(this);

  }

  async getOptions(){
    const res = await axios.get('http://127.0.0.1:5000/static/fighterDataset2.json')
    const data = res.data
    const nameData =[]
    const heightData =[]
    const StrikeAcc =[]
    const DOB =[]
    const SApM =[]
    const SLpM =[]
    const REACH =[]
    const STANCE =[]
    const WEIGHT =[]
    const strDef =[]
    const tdAcc =[]
    const subAvg =[]
    const tdDef =[]
    const tdAvg =[]


    for(let i =0; i< 6000 ;i++){
      // console.log(FighterData.Name[i])
      if (FighterData.Name[i] !== undefined){
        nameData.push({ "Name" : FighterData.Name[i]})
        heightData.push({"Height": FighterData.HEIGHT[i]})
        StrikeAcc.push({"StrAcc": FighterData["Str. Acc.."][i]})
        DOB.push({"DOB":FighterData.DOB[i]})
        SApM.push({"SApM":FighterData.SApM[i]})
        SLpM.push({"SLpM":FighterData.SLpM[i]})
        REACH.push({"REACH":FighterData.REACH[i]})
        STANCE.push({"STANCE":FighterData.STANCE[i]})
        WEIGHT.push({"WEIGHT":FighterData.WEIGHT[i]})
        strDef.push({"strDef":FighterData["Str. Def"][i]})
        tdAcc.push({"tdAcc":FighterData["TD Acc"][i]})
        subAvg.push({"subAvg":FighterData["Sub. Avg"][i]})
        tdDef.push({"tdDef":FighterData["TD Def."][i]})
        tdAvg.push({"tdAvg":FighterData["TD Avg"][i]})

        // FighterData.DOB
        // FighterData.SApM
        // FighterData.SLpM
        // FighterData.REACH
        // FighterData.STANCE
        // FighterData.WEIGHT
        // FighterData["Str. Acc.."]
        // FighterData["Str. Def"]
        // FighterData["TD Acc"]
        // FighterData["Sub. Avg"]
        // FighterData["TD Def."]
        // FighterData["TD Avg"]
      }
    }
    // const SApM =[]
    // const SLpM =[]
    // const REACH =[]
    // const STANCE =[]
    // const WEIGHT =[]
    // const strAcc =[]
    // const strDef =[]
    // const tdAcc =[]
    // const subAvg =[]
    // const tdDef =[]
    // const tdAvg =[]

    this.setState({selectOptionsNames: nameData})
    this.setState({height: heightData})
    this.setState({strikeAccuracy: StrikeAcc})
    this.setState({DOB: DOB})
    this.setState({SLpM: SLpM})
    this.setState({REACH: REACH})
    this.setState({STANCE: STANCE})
    this.setState({WEIGHT: WEIGHT})
    this.setState({strDef: strDef})
    this.setState({tdAcc: tdAcc})
    this.setState({subAvg: subAvg})
    this.setState({tdDef: tdDef})
    this.setState({tdAvg: tdAvg})
    this.setState({SApM: SApM})




  }
    componentDidMount(){
      this.getOptions()
  }

  handleChange(e){
   this.setState({name:e.label})
  }

    // FighterB.push(this.state.selectOptionsNames[indexB].Name)
    //   FighterB.push(this.state.height[indexB].Height)
    //   FighterB.push(this.state.SLpM[indexB].SLpM)
    //   FighterB.push(this.state.DOB[indexB].DOB)
    //   FighterB.push(this.state.strikeAccuracy[indexB].StrAcc)
    //   FighterB.push(this.state.REACH[indexB].REACH)
    //   FighterB.push(this.state.STANCE[indexB].STANCE)
    //   FighterB.push(this.state.WEIGHT[indexB].WEIGHT)
    //   FighterB.push(this.state.strDef[indexB].strDef)
    //   FighterB.push(this.state.tdAcc[indexB].tdAcc)
    //   FighterB.push(this.state.subAvg[indexB].subAvg)
    //   FighterB.push(this.state.tdDef[indexB].tdDef)
    //   FighterB.push(this.state.tdAvg[indexB].tdAvg)
    //   FighterB.push(this.state.SApM[indexB].SApM)

  getFighterA(param){
    const indexA = this.state.selectOptionsNames.indexOf(param);
    const FighterA=[]


    if(indexA !== -1 ){
      // this.setState({FighterA:[]}) // reset array before setting new data
      FighterA.push(this.state.selectOptionsNames[indexA].Name)
      FighterA.push(this.state.height[indexA].Height)
      FighterA.push(this.state.WEIGHT[indexA].WEIGHT)
      FighterA.push(this.state.REACH[indexA].REACH)
      FighterA.push(this.state.STANCE[indexA].STANCE)
      FighterA.push(this.state.DOB[indexA].DOB)
      FighterA.push(this.state.SLpM[indexA].SLpM)
      FighterA.push(this.state.strikeAccuracy[indexA].StrAcc)
      FighterA.push(this.state.SApM[indexA].SApM)
      FighterA.push(this.state.strDef[indexA].strDef)
      FighterA.push(this.state.tdAvg[indexA].tdAvg)
      FighterA.push(this.state.tdAcc[indexA].tdAcc)
      FighterA.push(this.state.tdDef[indexA].tdDef)
      FighterA.push(this.state.subAvg[indexA].subAvg)
    }
    this.setState({FighterA:FighterA})



  }

  getFighterB(param){
    const indexB = this.state.selectOptionsNames.indexOf(param);
    const FighterB=[]
    if(indexB!== -1 ){
      // this.setState({FighterB:[]}) // reset array before setting new data
      FighterB.push(this.state.selectOptionsNames[indexB].Name)
      FighterB.push(this.state.height[indexB].Height)
      FighterB.push(this.state.WEIGHT[indexB].WEIGHT)
      FighterB.push(this.state.REACH[indexB].REACH)
      FighterB.push(this.state.STANCE[indexB].STANCE)
      FighterB.push(this.state.DOB[indexB].DOB)
      FighterB.push(this.state.SLpM[indexB].SLpM)
      FighterB.push(this.state.strikeAccuracy[indexB].StrAcc)
      FighterB.push(this.state.SApM[indexB].SApM)
      FighterB.push(this.state.strDef[indexB].strDef)
      FighterB.push(this.state.tdAvg[indexB].tdAvg)
      FighterB.push(this.state.tdAcc[indexB].tdAcc)
      FighterB.push(this.state.tdDef[indexB].tdDef)
      FighterB.push(this.state.subAvg[indexB].subAvg)

    }
    this.setState({FighterB:FighterB})

  }


  postData(){
  let predictData ;



    if(this.state.FighterA.length > 0 && this.state.FighterB.length > 0){
        predictData = this.state.FighterA.concat(this.state.FighterB);
    }

    const axios = require('axios')

  axios.post('http://localhost:5000/predict', predictData)
    .then(function (response) {
      console.log(response);
    })



    console.log(predictData);

  }


  render(){
    return (
    <React.Fragment>

      <Autocomplete
      id="combo-box-demo"
      options={this.state.selectOptionsNames}
      getOptionLabel={(option) => option.Name}
      style={{ width: 300 }}
      onChange={(event, value) => this.getFighterA(value)} // sends Index of selected Item Fighter A
      renderInput={(params ) => <TextField {...params}  label="Combo box" variant="outlined" />}
    />
       <Autocomplete
      id="combo-box-demo"
      options={this.state.selectOptionsNames  }
      getOptionLabel={(option) => option.Name}
      style={{ width: 300 }}
      onChange={(event, value) => this.getFighterB(value)} // sends Index of selected Item Fighter B
      renderInput={(params) => <TextField {...params} label="Combo box" variant="outlined" />}
    />
       <label htmlFor="contained-button-file">
        <Button variant="contained" color="primary" onClick={this.postData} component="span">
          Upload
        </Button>
      </label>

      {/*{*/}
      {/*  console.log("--****************A")*/}
      {/*}*/}
      {/*{*/}
      {/*          console.log("FighterA",this.state.FighterA)*/}

      {/*}*/}
    </React.Fragment>

  );
  }


}


