let $select = $('#Name');

let script = document.currentScript;
let fullUrl = script.src;
let jsonUrl = fullUrl.replace("data2.js", "fighterDataset2.json") // hard coded jsonUrl

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

    let data_list =[]
    let dataset = []
    let fighter_one = []
    let fighter_two = []




// && name !== null
//             console.log(name[7+5])

    for (let i = 0; i < 3582; i++) {
        if (typeof data[i] !== 'undefined')
        {
            data_list.push(data[i]);

        }
    };

    console.log("data", data_list[9]);
    console.log("data", data_list.length );

    for (let i = 0; i < data_list.length; i++) {
        $('#Name').append('<option id="' + i + '">' + data_list[i].NAME + '</option>');
        $('#Name2').append('<option id="' + i + '">' + data_list[i].NAME + '</option>');
    }




      $('#Name').change(function(){
            if ($('#Name').children(":selected").attr("value") !== 'none'
                && $('#Name2').children(":selected").attr("value") !== 'none') {

            let fighter_id = $(this).children(":selected").attr("id");
            let fighter_id2 = $('#Name2').children(":selected").attr("id");
            console.log("fighter one :",data_list[fighter_id])
            console.log("fighter two :",data_list[fighter_id2])
            fighter_one = []
            fighter_two = []
            fighter_one.push(data_list[fighter_id].NAME )
            fighter_one.push(data_list[fighter_id].HEIGHT )
            fighter_one.push(data_list[fighter_id].WEIGHT )
            fighter_one.push(data_list[fighter_id].REACH )
            fighter_one.push(data_list[fighter_id].STANCE )
            fighter_one.push(data_list[fighter_id].DOB )
            fighter_one.push(data_list[fighter_id].SLpM )
            fighter_one.push(data_list[fighter_id].StrAcc)
            fighter_one.push(data_list[fighter_id].SApM )
            fighter_one.push(data_list[fighter_id].StrDef)
            fighter_one.push(data_list[fighter_id].TDAvg)
            fighter_one.push(data_list[fighter_id].TDAcc)
            fighter_one.push(data_list[fighter_id].TDDef)
            fighter_one.push(data_list[fighter_id].SubAvg)
            fighter_two.push(data_list[fighter_id2].NAME )
            fighter_two.push(data_list[fighter_id2].HEIGHT )
            fighter_two.push(data_list[fighter_id2].WEIGHT )
            fighter_two.push(data_list[fighter_id2].REACH )
            fighter_two.push(data_list[fighter_id2].STANCE )
            fighter_two.push(data_list[fighter_id2].DOB )
            fighter_two.push(data_list[fighter_id2].SLpM )
            fighter_two.push(data_list[fighter_id2].StrAcc)
            fighter_two.push(data_list[fighter_id2].SApM )
            fighter_two.push(data_list[fighter_id2].StrDef)
            fighter_two.push(data_list[fighter_id2].TDAvg)
            fighter_two.push(data_list[fighter_id2].TDAcc)
            fighter_two.push(data_list[fighter_id2].TDDef)
            fighter_two.push(data_list[fighter_id2].SubAvg)
            $('#data').val('');


        }
      })



     $('#Name2').change(function(){
            if ($('#Name').children(":selected").attr("value") !== 'none'
                && $('#Name1').children(":selected").attr("value") !== 'none') {

            let fighter_id2 = $('#Name2').children(":selected").attr("id");
            let fighter_id = $('#Name').children(":selected").attr("id");
            console.log("fighter one :",data_list[fighter_id])
            console.log("fighter two:",data_list[fighter_id2])
            fighter_one = []
            fighter_two = []
            fighter_one.push(data_list[fighter_id].NAME )
            fighter_one.push(data_list[fighter_id].HEIGHT )
            fighter_one.push(data_list[fighter_id].WEIGHT )
            fighter_one.push(data_list[fighter_id].REACH )
            fighter_one.push(data_list[fighter_id].STANCE )
            fighter_one.push(data_list[fighter_id].DOB )
            fighter_one.push(data_list[fighter_id].SLpM )
            fighter_one.push(data_list[fighter_id].StrAcc)
            fighter_one.push(data_list[fighter_id].SApM )
            fighter_one.push(data_list[fighter_id].StrDef)
            fighter_one.push(data_list[fighter_id].TDAvg)
            fighter_one.push(data_list[fighter_id].TDAcc)
            fighter_one.push(data_list[fighter_id].TDDef)
            fighter_one.push(data_list[fighter_id].SubAvg)
            fighter_two.push(data_list[fighter_id2].NAME )
            fighter_two.push(data_list[fighter_id2].HEIGHT )
            fighter_two.push(data_list[fighter_id2].WEIGHT )
            fighter_two.push(data_list[fighter_id2].REACH )
            fighter_two.push(data_list[fighter_id2].STANCE )
            fighter_two.push(data_list[fighter_id2].DOB )
            fighter_two.push(data_list[fighter_id2].SLpM )
            fighter_two.push(data_list[fighter_id2].StrAcc)
            fighter_two.push(data_list[fighter_id2].SApM )
            fighter_two.push(data_list[fighter_id2].StrDef)
            fighter_two.push(data_list[fighter_id2].TDAvg)
            fighter_two.push(data_list[fighter_id2].TDAcc)
            fighter_two.push(data_list[fighter_id2].TDDef)
            fighter_two.push(data_list[fighter_id2].SubAvg)
            $('#data').val('');

        }
      })

    $('#submit_value').click(function(){
        dataset =[];
        let fight_data = fighter_one.concat(fighter_two);
        // console.log(fight_data)

        if ( fight_data.length  >14){
            $('#data').val(fight_data);
            $('#form_value').submit();
        }

        console.log("new_value",$('#data').val())

      })


    console.log(jsonUrl);


})