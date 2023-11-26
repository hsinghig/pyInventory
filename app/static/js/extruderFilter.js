$(function(){
    $('#colorFilterForm').on('change keyup paste', function(){    
        var select_button_text = $('#colorFilterForm option:selected')
                .toArray().map(item => item.text);  
        $('#labelFilterColor').text(select_button_text)
    });   
    $('#widthFilterForm').on('change keyup paste', function(){    
        var select_button_text = $('#widthFilterForm option:selected')
                .toArray().map(item => item.text);  
        $('#labelFilterWidth').text(select_button_text)
    });   
});