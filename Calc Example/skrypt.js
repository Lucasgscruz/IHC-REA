$(document).ready(function() {
    var $display = $("#display");

    var buttonID = "";
    var expression = "";
   



    $('.btnClick').unbind('click').click(function() {
       
        buttonID = ($(this).find('span')).attr('id');
        number = ($(this).find('span').text());
        console.log(number);
    
        switch (buttonID) {

            case "clc":
                clc();
                break;
            case "ce":
                ce();
                break;
            case "divide":
                divide();
                break;
            case "multiple":
                multiple();
                break;
            case "minus":
                minus();
                break;
            case "plus":
                plus();
                break;
            case "equal-sign":
                equal();
                break;
            case "dot":
                dot();
                break;
            default:
               calc(number);
               break;
        }



    });
    function calc(numb) {
      
        expression += parseInt(numb, 10);
        $display.html(expression);
        console.log(expression);
    }

    function clc() {
        expression = "";
        $display.html(expression);
        console.log("clc");
    }

    function ce() {
        expression = expression.substring(0, expression.length-1);
        $display.html(expression);
        console.log("ce");
    }

    function divide() {
        expression += "/";
        $display.html(expression);
        console.log("divide");
    }

    function multiple() {
        expression += "*";
        $display.html(expression);
        console.log("multiple");
    }

    function minus() {
        expression += "-";
        $display.html(expression);
        console.log("minus");
    }

    function plus() {
        expression += "+";
        $display.html(expression);
        console.log('plus');
    }

    function equal() {
        if (!expression) {
            return;
        }
        try {

        $display.html(parseFloat((eval(expression)).toFixed(5)));
        expression = parseFloat((eval(expression)).toFixed(5));
        console.log("equal");
    }
    catch (e) {
        $display.html("Syntax ERROR");
    }
    }

    function dot() {
        expression += ".";
         $display.html(expression);
        console.log("dot");
    }
});
