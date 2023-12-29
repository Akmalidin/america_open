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


function closeModal(e) {
    $(".container-modal").removeClass("show");
    return $(e).closest('.container-modal').removeClass('show');
}
