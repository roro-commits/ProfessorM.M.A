let $select = $('#Name');

let script = document.currentScript;
let fullUrl = script.src;
let jsonUrl = fullUrl.replace("data2.js", "fighterDataset2.json") // hard coded jsonUrl




$.getJSON(jsonUrl, function (datas) {
    // $select.html('');

    const name =  $('li.name1').text();
    const height = $('li.height1').text();
    const weight = $('li.weight1').text();
    const reach = $('li.reach1').text();
    const stance = $('li.stance1').text();
    const dob = $('li.dob1').text();
    const name1 =  $('li.name2').text();
    const height1 = $('li.height2').text();
    const weight1 = $('li.weight2').text();
    const reach1 = $('li.reach2').text();
    const stance1 = $('li.stance2').text();
    const dob1 = $('li.dob2').text();

    // const sLpM = data['SLpM']
    // const strAcc = data['Str. Acc..']
    // const sApM = data['SApM']
    // const strDef = data['Str. Def']
    // const tdAvg = data['TD Avg']
    // const tdAcc = data['TD Acc']
    // const tdDef = data['TD Def.']
    // const subAvg = data['Sub. Avg']


    let data_list =[]
    let name_set = []
    let name_set2 = []
    let fighter_one = []
    let fighter_two = []
    let radar_one = []
    let radar_two = []



// && name !== null
//             console.log(name[7+5])

    for (let i = 0; i < 3582; i++) {
        if (typeof datas[i] !== 'undefined')
        {
            data_list.push(datas[i]);

        }
    };

    console.log("data", data_list[9]);
    console.log("data", data_list.length );

    for (let i = 0; i < data_list.length; i++) {
        $('#Name').append('<option id="' + i + '">' + data_list[i].NAME + '</option>');
        $('#Name2').append('<option id="' + i + '">' + data_list[i].NAME + '</option>');
        name_set.push(data_list[i].NAME);
        name_set2.push(data_list[i].NAME);

    }

        $(".Document").ready(function() {
            $('#Name2').select2( )
            $('#Name').select2( )

        })
       



      $('#Name').change(function(){
        $('#Name').select2( (name_set))

        let fighter_id = $(this).children(":selected").attr("id");

            $('li.height1').text(height+ data_list[fighter_id].HEIGHT);
            $('li.weight1').text(weight+ data_list[fighter_id].WEIGHT);
            $('li.reach1').text(reach+ data_list[fighter_id].REACH);
            $('li.stance1').text(stance+ data_list[fighter_id].STANCE);
            $('li.dob1').text(dob+ data_list[fighter_id].DOB);
            // $('#fighter-attributea').css('width','300px');

 
            if ($('#Name').children(":selected").attr("value") !== 'none'
                && $('#Name2').children(":selected").attr("value") !== 'none') {

            let fighter_id = $('#Name').children(":selected").attr("id");
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
            // $('#data').val('');
            // $('#submit_value').click()
            let radar_one = []
            let radar_two = []
            radar_one.push(fighter_one.slice(1,2).concat(fighter_one.slice(3 ,4)).concat(fighter_one.slice(6,13)));
            radar_two.push(fighter_two.slice(1,2).concat(fighter_two.slice(3 ,4)).concat(fighter_two.slice(6,13)));
            radar_one[0][0] = radar_one[0][0] * 30
            radar_two[0][0] = radar_two[0][0] * 30
            radar_one[0][2] = radar_one[0][2] * 10
            radar_two[0][2] = radar_two[0][2] * 10
            radar_one[0][4] = radar_one[0][4] * 10
            radar_two[0][4] = radar_two[0][4] * 10
            radar_one[0][6] = radar_one[0][6] * 10
            radar_two[0][6] = radar_two[0][6] * 10

            // radar_one.push()
        
            console.log(radar_one[0])
            
            function convertRange( value, min , max) { 
                
                for (let i = 0; i < value[0].length; i++) 
                {
                    if(max - min === 0) return 1;
                    value[0][i] = (value[0][i] - min) / (max - min);

                }
                return value;
            };
            // var num = scale(.25, 0, 1, 0, 100);

                // ChartJS Chart Modified to fit my code 

            let chart = convertRange(radar_one ,2 ,10)
            let chart2 = convertRange(radar_two ,2 ,10)
            console.log(chart ,"kk")

                var ctx = $("#chart-line");
                var myLineChart = new Chart(ctx, {
                    type: 'radar',
                    data: {
                        labels: ['HEIGHT', 'REACH', 'SLpM', 'StrAcc', 'SApM', 'StrDef', 'TDAvg','TDAcc','TDDef','SubAvg'],
                        fontStyle: "bold",
                        fontColor: 'red',
                        datasets: [{
                            data: chart[0],
                            label: "FAVOURITE",
                            borderColor: "#458af7",
                            backgroundColor: '#e0d316',
                            fill: true,
                            fontColor: 'black',
                            pointHoverBorderColor: '#eb4034',
                        }, {
                            data: chart2[0],
                            label: "UNDERDOG",
                            borderColor: "#f54242",
                            fill: true,
                            backgroundColor: '#3cba9f'
                        }]
                    },
                    options: {
                        
                            legend: false,
                            gridLines: {
                               display: false,
                            },
                            labels: {
                                // This more specific font property overrides the global property
                                fontColor: 'red',
                                defaultFontSize: 13
                            },
                            scale: {
                              angleLines: {
                                color: 'white'
                              },
                              gridLines: {
                                color: 'white'
                              },
                              pointLabels :{
                                fontColor: '#333',
                                fontFamily: "'Raleway', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                                fontSize: 12,
                                fontStyle: 600,
                              },
                              ticks: {
                                suggestedMin: 0,
                                suggestedMax: 10,
                                display: false,
                                maxTicksLimit: 5
                              }
                            }
                          
                        
                    
                    }
                });

        }
      })



     $('#Name2').change(function(){
        $('#Name2').select2( (name_set2))
        let fighter_id = $(this).children(":selected").attr("id");
            

            $('li.height2').text(height1+ data_list[fighter_id].HEIGHT);
            $('li.weight2').text(weight1+ data_list[fighter_id].WEIGHT);
            $('li.reach2').text(reach1+ data_list[fighter_id].REACH);
            $('li.stance2').text(stance1+ data_list[fighter_id].STANCE);
            $('li.dob2').text(dob1+ data_list[fighter_id].DOB);

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
            // $('#data').val('');
            // $('#submit_value').click()
            let radar_one = []
            let radar_two = []
            radar_one.push(fighter_one.slice(1,2).concat(fighter_one.slice(3 ,4)).concat(fighter_one.slice(6,13)));
            radar_two.push(fighter_two.slice(1,2).concat(fighter_two.slice(3 ,4)).concat(fighter_two.slice(6,13)));
            radar_one[0][0] = radar_one[0][0] * 30
            radar_two[0][0] = radar_two[0][0] * 30
            radar_one[0][2] = radar_one[0][2] * 10
            radar_two[0][2] = radar_two[0][2] * 10
            radar_one[0][4] = radar_one[0][4] * 10
            radar_two[0][4] = radar_two[0][4] * 10
            radar_one[0][6] = radar_one[0][6] * 10
            radar_two[0][6] = radar_two[0][6] * 10

            // radar_one.push()
        
            console.log(radar_one[0])
            
            function convertRange( value, min , max) { 
                
                for (let i = 0; i < value[0].length; i++) 
                {
                    if(max - min === 0) return 1;
                    value[0][i] = (value[0][i] - min) / (max - min);

                }
                return value;
            };
            // var num = scale(.25, 0, 1, 0, 100);



                let chart = convertRange(radar_one ,2 ,10)
                let chart2 = convertRange(radar_two ,2 ,10)
                console.log(chart ,"kk")
                // ChartJS Chart Modified to fit my code 
                var ctx = $("#chart-line");
                var myLineChart = new Chart(ctx, {
                    type: 'radar',
                    data: {
                        labels: ['HEIGHT', 'REACH', 'SLpM', 'StrAcc', 'SApM', 'StrDef', 'TDAvg','TDAcc','TDDef','SubAvg'],
                        datasets: [{
                            data: chart[0],
                            label: "A Team",
                            borderColor: "#458af7",
                            backgroundColor: '#e0d316',
                            fill: true,
                            fontColor: 'black',
                            pointHoverBorderColor: '#eb4034',
                        }, {
                            data: chart2[0],
                            label: "B Team",
                            borderColor: "#f54242",
                            fill: true,
                            backgroundColor: '#3cba9f'
                        }]
                    },
                    options: {
                        title: {
                            display: true,
                            text: ''
                        },
                        font: {
                            size: 14,
                        }
                    }
                });
            

                }
            })

   
        console.log("new_value",$('#data').val())

        $('#submit_value').click(function(){

            // if ($('data').val().length > 14){

            //     $('#form_value').submit();
            // }
            
            let fight_data = fighter_one.concat(fighter_two);
            // console.log(fight_data)
    
            if ( fight_data.length  >14){
                $('#data').val(fight_data);
                $('#form_value').submit();
            }
            
      
           
    
    
        console.log(jsonUrl);
    
    
    })

    })

   