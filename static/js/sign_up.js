"use strict";

$(document).ready(() => {
    let correct1 = false;
    let correct2 = true;
    let correct3 = true;
    let correct4 = true;
    // Логин
    let regExp1 = /^[a-zA-Z][a-zA-Z0-9_\-]{5,15}$/;
    // Пароль
    let regExp2 = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[_\-\$#&])[A-Za-z0-9_\-\$#&]{8,}$/;
    // Email
    let regExp3 = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
    
    $("#login").blur(() => {
        let loginX = $("#login").val();
        if (regExp1.test(loginX)) {
            // Проверка занятости логина:
            $.ajax({
                url: "/accounts/ajax_reg",
                data: "login=" + loginX,
                success: function (result) {
                    if (result.message == "Логин занят") {
                        $("#login_mess").html(result.message);
                        correct1 = false;
                    } else {
                        $("#login_mess").html("");
                        correct1 = true;
                    }
                }
            });
        } else {
            correct1 = false;
            $("#login_mess").html("Логин не соответствует шаблону безопасности!")
        }
        //$("#login_mess").html(loginX);
    });

    $("#submit").click(() => {
        if (correct1 == true && correct2 == true && correct3 == true && correct4 ==true) {
            $("#form1").attr("onsubmit", "return true");
        } else {
            $("#form1").attr("onsubmit", "return false");
            alert("Форма содержит не корректные данные! \nОтправка данных заблокированна!")
        }
    });
});