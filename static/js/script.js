$('.sidebar-item').hover(function () {
    $(this).prev().addClass('border-hidden');
}, function () {
    $('.sidebar-item').removeClass('border-hidden');
});

if ($('.sidebar-item').hasClass('active')) {
    $('.sidebar-item.active').prev().addClass('active-border-hidden');
}

$('.phone').mask("+996 (xxx)-xxx-xxx");

function enableDisableRegisterButton() {
    let confirmRules = document.getElementById(`confirm_policy`)
    let registerButton = document.getElementById(`register-btn`)

    if (confirmRules.checked) {
        return registerButton.disabled = false
    } else {
        return registerButton.disabled = true
    }
}

$(document).ready(function () {
    $(".tabs").click(function () {
        $(".tabs").removeClass("active");
        $(this).addClass("active");

        let current_fs = $(".active");
        let next_fs = $(this).attr('id');
        next_fs = "#" + next_fs + "1";

        $("fieldset").removeClass("show");
        $(next_fs).addClass("show");

        current_fs.animate({}, {
            step: function () {
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({
                    'display': 'block'
                });
            }
        });
    });
});

function clearInvalidFeedback() {
    $(".invalid-feedback").css("display", 'none');
    $(".invalid-feedback").text("");
    $(".is-invalid").removeClass('is-invalid');
}

function openUserResetPassword() {
    $('#myModal').modal('hide');

    setTimeout(() => {
        $('#userResetPasswordModal').modal('show');
    }, 500)
}

function closeModal(e) {
    $(".container-modal").removeClass("show");
    return $(e).closest('.container-modal').removeClass('show');
}

$(function () {
    $("#registerForm").submit(function (e) {
        e.preventDefault();

        let phone = $(this).find("#register-phone").val();
        let fullName = $(this).find("#register-full_name").val();
        let email = $(this).find("#register-email").val();
        let password = $(this).find("#register-password").val();
        let confirmPolicy = $(this).find("#confirm_policy").val();
        let subjectFirst = $(this).find("#subject_first").val();
        let subjectSecond = $(this).find("#subject_second").val();
        let _token = $('meta[name="csrf-token"]').attr('content');

        $(".loader").addClass("loading");
        clearInvalidFeedback()

        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            type: "POST",
            data: {
                '_token': _token,
                'full_name': fullName,
                'phone': phone,
                'email': email,
                'password': password,
                'subject_first': subjectFirst,
                'subject_second': subjectSecond,
                'confirm_policy': confirmPolicy,
            },
            success: function (res) {
                $(".loader").removeClass("loading");
                alertModal('Сіз сәтті тіркелдіңіз!');
                setTimeout(() => {
                    window.location.reload()
                }, 1500)
            },
            error: function (err) {
                $(".loader").removeClass("loading");
                let response_text = JSON.parse(err.responseText);
                if (response_text.errors && typeof response_text.errors == 'object') {
                    Object.entries(response_text.errors).forEach(([key, value]) => {
                        $('#error-register-' + key).text(value[0]);
                        $('#error-register-' + key).css('display', 'block');
                        $('#register-' + key).addClass('is-invalid');
                    })
                }
            }
        });
    });

    $('#loginForm').submit(function (e) {
        e.preventDefault();

        let phone = $(this).find("#login-phone").val();
        let password = $(this).find('#login-password').val();
        let _token = $('meta[name="csrf-token"]').attr('content');
        $(".loader").addClass("loading");

        clearInvalidFeedback()

        $.ajax({
            url: $(this).attr('action'),
            type: "GET",
            data: {
                'phone': phone,
                'password': password,
                '_token': _token
            },
            success: function (res) {
                $(".loader").removeClass("loading");
                if (res.data && res.data.success) {
                    window.location.reload();
                }
            },
            error: function (err) {
                console.log(err)

                $(".loader").removeClass("loading");

                let response_text = JSON.parse(err.responseText);

                if (response_text.errors && typeof response_text.errors == 'object') {
                    Object.entries(response_text.errors).forEach(([key, value]) => {
                        $('#error-login-' + key).text(value[0]);
                        $('#error-login-' + key).css('display', 'block');
                        $('#login-' + key).addClass('is-invalid');
                    })
                }
            }
        });
    });

    $('#userUpdateForm').submit(function (e) {
        e.preventDefault();

        let phone = $(this).find('#update-phone').val();
        let full_name = $(this).find("#update-full_name").val();
        let email = $(this).find("#update-email").val();
        let _token = $('meta[name="csrf-token"]').attr('content');
        $(".loader").addClass("loading");

        clearInvalidFeedback()

        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data: {
                'phone': phone,
                'full_name': full_name,
                'email': email,
                '_token': _token
            },
            success: function (res) {
                $(".loader").removeClass("loading");
                if (res && res.success) {
                    alertModal('Сәтті өзгертілді!');
                    setTimeout(() => {
                        window.location.reload()
                    }, 1500)
                }
            },
            error: function (err) {
                $(".loader").removeClass("loading");
                let response_text = JSON.parse(err.responseText);
                if (response_text.errors && typeof response_text.errors == 'object') {
                    Object.entries(response_text.errors).forEach(([key, value]) => {
                        $('#error-update-' + key).text(value[0]);
                        $('#error-update-' + key).css('display', 'block');
                        $('#update-' + key).addClass('is-invalid');
                    })
                }
            }
        });
    });

    $('#userPasswordUpdateForm').submit(function (e) {
        e.preventDefault();

        let password = $(this).find("#update-password").val();
        let password_confirmation = $(this).find('#update-password_confirmation').val();
        let _token = $('meta[name="csrf-token"]').attr('content');
        $(".loader").addClass("loading");

        clearInvalidFeedback()

        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data: {
                'password': password,
                'password_confirmation': password_confirmation,
                '_token': _token
            },
            success: function (res) {
                $(".loader").removeClass("loading");
                if (res && res.success) {
                    alertModal('Сәтті өзгертілді!');
                    setTimeout(() => {
                        window.location.reload()
                    }, 1500)
                }
            },
            error: function (err) {
                $(".loader").removeClass("loading");
                let response_text = JSON.parse(err.responseText);
                if (response_text.errors && typeof response_text.errors == 'object') {
                    Object.entries(response_text.errors).forEach(([key, value]) => {
                        $('#error-update-' + key).text(value[0]);
                        $('#error-update-' + key).css('display', 'block');
                        $('#update-' + key).addClass('is-invalid');
                    })
                }
            }
        });
    });

    $('#userResetPasswordForm').submit(function (e) {
        e.preventDefault();

        let email = $('#reset_password_email').val();
        let _token = $('meta[name="csrf-token"]').attr('content');

        $(".loader").addClass("loading");
        clearInvalidFeedback()

        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            type: "GET",
            data: {
                'email': email,
                '_token': _token
            },
            success: function (res) {
                $(".loader").removeClass("loading");
                if (res.data.status) {
                    $('#userResetPasswordModal').modal('hide');
                    alertModal('Электрондық поштаңызды тексеріңіз', 3000);
                }
            },
            error: function (err) {
                $(".loader").removeClass("loading");

                let response_text = JSON.parse(err.responseText);
                if (response_text.errors && typeof response_text.errors == 'object') {
                    Object.entries(response_text.errors).forEach(([key, value]) => {
                        $('#error-reset_password-' + key).text(value[0]);
                        $('#error-reset_password-' + key).css('display', 'block');
                        $('#reset_password_email').addClass('is-invalid');
                    })
                }
            }
        });
    });
});


