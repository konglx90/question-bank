/**
 * Created by jxuan on 15-10-22.
 */
$(document).ready(function() {
    boxrightsty();

    //控制面板右侧样式
    function boxrightsty() {
        var $windowhei = $(window).height();
        $("#boxright").css("min-height", $windowhei - 90);
    }
});