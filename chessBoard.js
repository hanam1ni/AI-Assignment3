function decreaseButton() {
    var inputVal = parseInt($("#input-nQueen").val());
    if (inputVal > 4) {
        $("#input-nQueen").val(inputVal - 1);
        renderTable(inputVal - 1)
        $('.text-error').css({'display': 'none'});
    }
}

function increaseButton() {
    var inputVal = parseInt($("#input-nQueen").val());
    if (inputVal < 10) {
        $("#input-nQueen").val(inputVal + 1);
        renderTable(inputVal + 1)
        $('.text-error').css({'display': 'none'});
    }
}

function fillTable(nTable) {
    for (row = 0; row < nTable ; row++) {
        col = Math.floor(Math.random() * nTable)
        queenClass = 'queen-piece row-' + row
        queenImg = '<img class="' + queenClass +'" src="static/img/queen-chess.svg">'
        $('#chess-board').append(queenImg)
        posTop = row * 100 / nTable
        posLeft = col * 100 / nTable
        queenClass = '.queen-piece.row-' + row
        $(queenClass).css({'top': posTop + '%'});
        $(queenClass).css({'left': posLeft + '%'});
    }
}

function placeQueen(position) {
    nTable = position.length
    position.forEach(function(pos) {
        queenClass = '.queen-piece.row-' + pos.posY
        posLeft = pos.posX * 100 / nTable
        t = pos.posX * 100 / nTable
        $(queenClass).animate({
            left: posLeft + '%'
        }, 39)
    })
}

function movingQueen(nQueen) {
    for(row = 0; row < nQueen; row++) {
        queenClass = '.queen-piece.row-' + row
        posLeft = Math.floor(Math.random() * nQueen) * 100 / nQueen
        $(queenClass).animate({
            left: posLeft + '%'
        }, 39)
    }
}

function renderTable(nTable) {
    var rowTable = ""
    $(".row-table").remove();
    $(".queen-piece").remove();
    for (row = 0; row < nTable; row++){
        rowClass = "row-" + row
        rowTable += "<tr class='row-table " + rowClass + "'>"
        for (col = 0; col < nTable; col++) {
            cellClass = " col-" + col
            rowTable += "<td class='cell-table " + rowClass + cellClass + "'></td>" 
        }
        rowTable += "</tr>"
    }
    $("#chess-board").append(rowTable);
    fillTable(nTable)
}

$(document).ready(renderTable(5))