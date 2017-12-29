/**
 * Created by jxuan on 15-10-22.
 */
$(document).ready(function() {
    slidebar_control();

    function slidebar_control() {
        $(".nav .slidebar_btn").each(function() {
            $(this).click(function() {
                $(this).addClass("active")
                    .children(".detailnav").slideDown(100)
                    .parent().parent().siblings().children(".slidebar_btn").removeClass("active")
                    .children(".detailnav").slideUp(100);
            });
        });

        $(".nav .detailnav li").each(function() {
            $(this).click(function() {
                $(this).addClass("navli")
                    .siblings().removeClass("navli");
            })
        })
    }
});