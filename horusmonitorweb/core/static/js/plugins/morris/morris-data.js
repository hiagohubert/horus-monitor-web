
var dataCPU = [];
var dataMemory = [];
var graphCPU;
var graphMemory;
var machine = $("#machine_id").val();

function convertDate(datetime) {
    var datetime = datetime.replace("Z", "");
    return datetime;
}
function formatDate(datetime){
    return datetime.getFullYear()+"-"+(datetime.getMonth()+1)+"-"+datetime.getDate()+" "+datetime.getHours()+":"+datetime.getMinutes()+":"+datetime.getSeconds();
}


function getCPUDATA(today = false){
    var d = new Date();
    var hour_ago = new Date();
    hour_ago.setHours(d.getHours()-1);

    if(today){
      var uri = "/api/cpu/?machine="+machine;
    }else{
      var uri = "/api/cpu/?start_date="+formatDate(hour_ago)+"&end_date="+formatDate(d)+"&machine="+machine;
    }

    $.ajax({
       url: uri,
       dataType: "json",
       success: function(response) {
            $.each(response, function(key, value){
                 obj = {date: convertDate(value.inserted_at), used: value.percent_used};
                 dataCPU.push(obj);
            });
            graphCPU = Morris.Line({
                            element: 'morris-line-chart',
                            data: dataCPU ,
                            xkey: 'date',
                            ykeys: ['used'],
                            labels: ['% Usado'],
                            ymax: 100,
                            smooth: false,
                            resize: true
                        });
        }
   });


}

function updateCPU(today = false){
    var d = new Date();
    var hour_ago = new Date();
    hour_ago.setHours(d.getHours()-1);

    if(today){
      var uri = "/api/cpu/?machine="+machine;
    }else{
      var uri = "/api/cpu/?start_date="+formatDate(hour_ago)+"&end_date="+formatDate(d)+"&machine="+machine;
    }
    
    $.ajax({
       url: uri,
       dataType: "json",
       success: function(response) {
            $.each(response, function(key, value){
                 obj = {date: convertDate(value.inserted_at), used: value.percent_used};
                 dataCPU.push(obj);
            });
            graphCPU.setData(dataCPU);
        }
   });
    
}

function getMemoryDATA(today = false){
    var d = new Date();
    var hour_ago = new Date();
    hour_ago.setHours(d.getHours()-1);

    if(today){
      var uri = "/api/memory/?machine="+machine;
    }else{
      var uri = "/api/memory/?start_date="+formatDate(hour_ago)+"&end_date="+formatDate(d)+"&machine="+machine;
    }

    $.ajax({
       url: uri,
       dataType: "json",
       success: function(response) {
            $.each(response, function(key, value){
                 obj = {date: convertDate(value.inserted_at), used: value.percent_used};
                 dataMemory.push(obj);
            });
            graphMemory = Morris.Line({
                element: 'morris-bar-chart',
                data: dataMemory ,
                xkey: 'date',
                ykeys: ['used'],
                labels: ['% Usado'],
                ymax: 100,
                smooth: false,
                resize: true
            });
        }
   });

}

function updateMemory(today = false){
    var d = new Date();
    var hour_ago = new Date();
    hour_ago.setHours(d.getHours()-1);

    if(today){
      var uri = "/api/memory/?machine="+machine;
    }else{
      var uri = "/api/memory/?start_date="+formatDate(hour_ago)+"&end_date="+formatDate(d)+"&machine="+machine;
    }

    $.ajax({
       url: uri,
       dataType: "json",
       success: function(response) {
            $.each(response, function(key, value){
                 obj = {date: convertDate(value.inserted_at), used: value.percent_used};
                 dataMemory.push(obj);
            });
            graphMemory.setData(dataMemory);
        }
   });
    
}


