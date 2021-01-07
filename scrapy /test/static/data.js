let $select = $('#Name');

let script = document.currentScript;
let fullUrl = script.src;
let jsonUrl = fullUrl.replace("data.js", "fighterDataset.json") // hard coded jsonUrl

$.getJSON(jsonUrl, function (data) {
    // $select.html('');

    const name = data['Name']
    const height = data['HEIGHT']
    const weight = data['WEIGHT']
    const reach = data['REACH']
    const stance = data['STANCE']
    const dob = data['DOB']
    const sLpM = data['SLpM']
    const strAcc = data['Str. Acc..']
    const sApM = data['SApM']
    const strDef = data['Str. Def']
    const tdAvg = data['TD Avg']
    const tdAcc = data['TD Acc']
    const tdDef = data['TD Def.']
    const subAvg = data['Sub. Avg']

    let name_list = []
    let height_list = []
    let weight_list = []
    let reach_list = []
    let stance_list = []
    let dob_list = []
    let sLpM_list = []
    let strAcc_list = []
    let sApM_list = []
    let strDef_list = []
    let tdAvg_list = []
    let tdAcc_list = []
    let tdDef_list = []
    let subAvg_list = []

// && name !== null
            console.log(name[7+5])

    for (let i = 2; i < 3582; i++) {
        if (typeof name[i] !== 'undefined')
        {
            name_list.push(name[i]);
            height_list.push(height[i]);
            weight_list.push(weight[i]);
            reach_list.push(reach[i]);
            stance_list.push(stance[i]);
            dob_list.push(dob[i]);
            sLpM_list.push(sLpM[i]);



            // unexplained reason for the index of before mixed up
            // index was different by  5


            strAcc_list.push(strAcc[i]);
            sApM_list.push(sApM[i]);
            strDef_list.push(strDef[i]);
            tdAvg_list.push(tdAvg[i]);
            tdAcc_list.push(tdAcc[i]);
            tdDef_list.push(tdDef[i]);
            subAvg_list.push(subAvg[i]);

        }


    }

    for (let i = 2; i < name_list.length; i++) {
        $('#Name').append('<option id="' + i + '">' + name_list[i] + '</option>')
        $('#Name2').append('<option id="' + i + '">' + name_list[i] + '</option>')
    }

    if ($('#Name').id) {


    }


    console.log(jsonUrl);
    // console.log(data);

    // hard code fix for index bug above
     let x = 5;
    console.log(name_list[9], height_list[9], weight_list[9], reach_list[9], stance_list[9], dob_list[9], sLpM_list[8], strAcc[8+x], sApM[8+x], strDef[7+x], tdAvg[8+x], tdAcc[8+x], tdDef[9+x], subAvg[7+x]);


})