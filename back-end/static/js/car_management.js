/**
 * Created by jxuan on 15-12-1.
 */
$(function () {

    var src;

    $("#apply").click(function () {
        src = ""; //TODO 修改为apply_form的地址
        getBoxright(src);
    });

    //$("#check").click(function () {
    //    src = ""; //TODO 修改为申请列表的地址
    //    getBoxright(src);
    //});

    $("#check").click(function () {
        $("#status").show();
    });

    $("#result").click(function () {
        src = ""; //TODO 修改为申请结果列表页面
        getBoxright(src);
    });

    $("#campus").change(function () {
        var campus = $(this).val();
        if (campus == "清水河校区") {
            $(".shahe").hide().siblings(".qingshui").show();
        } else if (campus == "沙河校区") {
            $(".qingshui").hide().siblings(".shahe").show();
        }
    });

    $("#timebegin, #timeend, #timebegin_end, #timeend_end").datetimepicker({format: 'yyyy-mm-dd hh:ii'});

    $("#nopass").click(function () {
        var $feedback = $("#feedback");
        if ($feedback.length == 0) {
            var template = '<div class="form-group col-sm-6 col-md-4" id="feedback">\
            <p class="col-sm-5 col-md-6 control-label">原因:</p>\
            <div class="col-sm-7 col-md-6">\
            <textarea class="form-control" autofocus name="feedback_reason"></textarea>\
            </div>\
            </div>';
            $("#Sbtn_parent").before(template);
            return false;
        } else if ($("textarea").val() == "") {
            alert("请填写拒绝原因！");
            return false;
        } else {
            $("#judge").val("1");
        }
    });

    $("#pass").click(function () {
        $("#judge").val("0");
        if ($("#feedback").length !== 0) {
            $("#feedback").remove();
        }
    })

    //var carDetail = {
    //    car_id: $('#car_id').val(),
    //    timebegin: $('#timebegin').val(),
    //    timeend: $('#timeend').val(),
    //    department: $('#department').val(),
    //    campus: $('#campus').val(),
    //    reason: $('#reason').val(),
    //    note: $('#note').val()
    //}

    $("#abroad_btn").click(function () {
        var carDetail = {
            car_id: $('#car_id').val(),
            name: $('#name').val(),
            timebegin: $('#timebegin').val(),
            timeend: $('#timeend').val(),
            timebegin_end: $('#timebegin_end').val(),
            timeend_end: $('#timeend_end').val(),
            interviewer_workplace: $('#interviewer_workplace').val(),
            campus: $('#campus').val(),
            reason: $('#reason').val(),
            note: $('#note').val(),
            interviewer_name: $('#interviewer_name').val(),
            number: $('#number').val(),
            phone: $('#phone').val(),
            user_workplace: $('#user_workplace').val(),
            user_job: $('#user_job').val(),
            interviewer_phone: $('#interviewer_phone').val(),

        }

        for (var i in carDetail) {
            console.log(typeof i)
            if (carDetail[i] === "" && (i !== "note" && i !== "interviewer_name" && i != "interviewer_phone")) {
                alert("请填写完全！")
                //break;
                return false;
            }
        }

        console.log(carDetail)
        var url = "/car_manage/car_apply"; //修改为表单发送地址

        $.ajax({
                type: "POST",
                url: url,
                data: carDetail,
                success: function (data) {
                    if (data.status == 200) {
                        alert(data.message);
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


    (function () {
        var $change_num = $("#change_num");
        $change_num.click(function () {
            $(this).val("保存").attr("type", "submit").attr("id", "save_num");
            $("#limits_form input").removeAttr('disabled');
        })
    })();

});

function getBoxright(src) {
    var template = "<iframe style='width:100%;height:100%;' frameborder='none' src='" + src + "'></iframe>";
    var $boxright = $("#boxright");
    $boxright.empty().append(template);
}

