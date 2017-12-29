/**
 * Created by amourlee on 15/8/8.
 */
$(function(){

    function asd(){
        var a = 1 + parseInt(Math.random() * 9);
        var b = parseInt(Math.random() * 10);
        var c = parseInt(Math.random() * 10);
        var d = parseInt(Math.random() * 10);

        var yanzheng = a * 1000 + b * 100 + c * 10 + d;


        $(".yanzhengma").html(yanzheng);
    }

    asd();

    $(".yanzhengma").click(function(){
        asd();
    })

    $(".cao").focus(function(){
        $(".nimeimei span").html(" ");
        console.log(123);
    })
    $(".cao").blur(function(){
        var $value = $(this).val();
        console.log($value);
        if($value == $(".yanzhengma" ).html()){
            console.log("true");
            $(".caocao").removeAttr("disabled");
        }
        else {
            $(".nimeimei span").html("*验证码错误");
        }
    })

})