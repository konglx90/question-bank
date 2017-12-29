/**
 * Created by kong90 on 16-3-13.
 */
$(document).ready(function(){
    //调用datetimepicker时间插件
    $("#date1, #date2").datetimepicker({format: 'yyyy-mm-dd hh:ii'});

    $("#in").click(function () {
        var carDetail = {
            date1: $('#date1').val(),
            date2: $('#date2').val(),

        }

        for(var i in carDetail){
            if (carDetail[i] === ""){
                alert("请填写完全！")
                //break;
                return false;
            }
        }

        var url = "/car_manage/make_excel/?da=in"; //修改为表单发送地址

        var da_1 = carDetail.date1,
            da_2 = carDetail.date2;
        window.location.href = "/car_manage/make_excel/?da=in&date1="+da_1+"&date2="+da_2;

    });

    $("#out").click(function () {
        var carDetail = {
            date1: $('#date1').val(),
            date2: $('#date2').val(),

        }

        for(var i in carDetail){
            console.log(typeof i)
            if (carDetail[i] === ""){
                alert("请填写完全！")
                //break;
                return false;
            }
        }

        console.log(carDetail)
        var url = "/car_manage/make_excel/?da=out"; //修改为表单发送地址

        var da_1 = carDetail.date1,
            da_2 = carDetail.date2;
        window.location.href = "/car_manage/make_excel/?da=out&date1="+da_1+"&date2="+da_2;

    });

});
//