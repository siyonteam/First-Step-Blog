$(function () {
    // functions for readability
    let stateIconFont = (className) => {
        let string = "fas " + className;
        return string;
    };
    let formLoginChange = () => {
        loginForm.slideDown();
        registerForm.fadeOut();
        stateText.text("ورود");
        stateIcon.removeClass();
        stateIcon.addClass(stateIconFont("fa-sign-in-alt"));
    };
    let formRegisterChange = () => {
        registerForm.fadeIn();
        loginForm.slideToggle();
        stateText.text("ثبت نام");
        stateIcon.removeClass();
        stateIcon.addClass(stateIconFont("fa-user-plus"));
    };
    let prevDefault = () => {
        let buttonsPrevDefault = $(".buttons-JS");
        buttonsPrevDefault.click((event) => {
            event.preventDefault();
        });
    };
    // preventDefault buttons
    prevDefault();
    // Vars for login register transforms
    let count = 0;
    let angleRight = $(".angleRight");
    let angleLeft = $(".angleLeft");
    let loginForm = $("#login");
    let registerForm = $("#register");
    let stateText = $(".state__text");
    let stateIcon = $(".stateIcon");

    // angles onclick functions
    angleRight.click(() => {
        if (count % 2 === 1) {
            formRegisterChange();
            count++;
        } else {
            formLoginChange();
            count++;
        }
    });
    angleLeft.click(() => {
        if (count % 2 === 1) {
            formRegisterChange();
            count++;
        } else {
            formLoginChange();
            count++;
        }
    });
});
