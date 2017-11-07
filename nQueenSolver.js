moveInterval = null;

function queenSolveRequest() {
    var nQueen = $("#input-nQueen").val()
    var initTemp = $("#input-temp").val()
    var coolRate = $("#input-rate").val()
    if(initTemp !== '' && coolRate !== '') {
        $('#time-result').css({'visibility': 'hidden'});
        $('.text-error').css({'display': 'none'});
        var requestData = {
            'nQueen': nQueen,
            'initTemp': initTemp,
            'coolRate': coolRate
        }
        $('.input-box').prop('disabled', true)
        $('#queen-submit').prop('disabled', true)
        moveInterval = setInterval(function(){
                movingQueen(nQueen)
            }, 90);
        $.ajax({
            url: "http://127.0.0.1:5000/queen",
            data: JSON.stringify(requestData), 
            type: 'POST',
            contentType: "application/json",
            success: function(data) {
                jsonData = JSON.parse(data)
                clearInterval(moveInterval)
                placeQueen(jsonData.solution)
                timeElapsed = Math.round(jsonData.timeElapsed * 10000000) / 10000000                
                resultText = "Time Elasped " + timeElapsed + " Seconds"
                document.getElementById("time-result").innerHTML = resultText;
                $('#time-result').css({'visibility': 'visible'});
                $('.input-box').prop('disabled', false)
                $('#queen-submit').prop('disabled', false)
            },
            error: function() {
                $('.input-box').prop('disabled', false)
                $('#queen-submit').prop('disabled', false)
                clearInterval(moveInterval)
            }
        })
    } else {
        $('.text-error').css({'display': 'inline'});
    }
}