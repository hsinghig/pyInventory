$(function(){
    $('#btnExportExtruderCSV').on('click',  function(){
        fetch('/dashboard/processextruder', {
            method: 'GET'
        }).then(response => {          
            // do something with file create a hyperlink and download the file
            return response.blob();
        }).then(data => {
            let a = document.createElement("a");
            a.href = window.URL.createObjectURL(data);
            a.download = 'extruderData.csv';
            a.click();
        }).catch(e => {           
            console.log(e);
        });
    });

    $('#btnExportCrossPlyCSV').on('click', function(){
        alert('Clicked Cross Ply Export CSV');
    });

});