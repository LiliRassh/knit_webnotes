"use strict";

$(document).ready(() => {
    let correct = false;
    $("#id_name").blur(() => {
        let name = $("#id_name").val();
        // Проверка занятости названия узора:
        $.ajax({
            url: "/patterns/ajax_name",
            data: "name=" + name,
            success: function (result) {
                if (result.message == "Есть узор с таким названием!") {
                    $("#name_mess").html(result.message).css('color', 'red');
                    correct = false;
                } else {
                    $("#name_mess").html("");
                    correct = true;
                }
            }
        });
    });

    $("#save").click(() => {
        if (correct == true) {
            $("#pattern").attr("onsubmit", "return true");
            $("#save_mess").html("");
        } else {
            $("#pattern").attr("onsubmit", "return false");
            let save_mess = "Отправка данных заблокированна!";
            $("#save_mess").html(save_mess).css('color', 'red');
        }
    });
});