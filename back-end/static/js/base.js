/**
 * Created by amourlee on 15/8/9.
 */

$(function(){
    $("#SubPassword").click(function () {
        var carDetail = {
            password: $('#password').val(),
            confirm_password: $('#confirm_password').val(),
            current_password: $('#current_password').val()

        }

        for(var i in carDetail){
            if (carDetail[i] === ""){
                alert("请填写完全！")
                //break;
                return false;
            }
        }

        console.log(carDetail)
        var url = "#"; //修改为表单发送地址

        $.ajax({
                type: "POST",
                url: url,
                data: carDetail,
                success: function (data) {
                    if (data.status == 200) {
                        alert(data.message);
                        window.location.href="/";
                    } else if (data.status == 500) {
                        alert(data.message);
                    } else {
                        alert("意外");
                    }
                }
            }
        );
        return false;
    });

    $("#login").click(function () {
        var carDetail = {
            password: $('#login_password').val(),
            username: $('#login_username').val(),

        }

        for(var i in carDetail){
            if (carDetail[i] === ""){
                alert("请填写完全！")
                //break;
                return false;
            }
        }

        console.log(carDetail)
        var url = "#"; //修改为表单发送地址

        $.ajax({
                type: "POST",
                url: url,
                data: carDetail,
                success: function (data) {
                    if (data.status == 200) {
                        window.location.href="/"+data.redirect;
                    } else if (data.status == 500) {
                        alert(data.message);
                    } else {
                        console.log(data);
                        alert("意外");
                    }
                }
            }
        );
        return false;
    });

})
