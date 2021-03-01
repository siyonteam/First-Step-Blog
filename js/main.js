$(function () {
    $('.login').click(() => {
        $('.loginForm').slideToggle(500);
    });
    $('.loginForm').mouseleave(() => {
        $('.loginForm').slideUp(500);
        $('.userInput').val('');
        $('.passInput').val('');
    });
    $('.loginBtn').click(() => {
        $('.userInput').val('');
        $('.passInput').val('');
    });
    $('.hamburger').click(() => {
        $('.hamburger').toggleClass('open');
        $('.navList').toggleClass('open');
        $('.navChilds').toggleClass('open');
    });
    $('.send_comment').click(function () {
        if (!$(this).parent('.tempFooter').next('.answerForm').is(':visible')) {
            $(this).parent('.tempFooter').next('.answerForm').slideToggle();

            $(this)
                .parent('.tempFooter')
                .next('.answerForm')
                .css('display', 'flex');
            $(this).text('X');
        } else {
            $(this)
                .parent('.tempFooter')
                .next('.answerForm')
                .slideToggle(() => {
                    $(this)
                        .parent('.tempFooter')
                        .next('.answerForm')
                        .css('display', 'none');
                    $(this).text('پاسخ');
                });
        }
    });
    $('.commentToggle').click(() => {
        if (!$('.comment').is(':visible')) {
            $('.comment').fadeToggle();
            $('.comment').css('display', 'flex');
        } else {
            $('.comment').fadeToggle(() => {
                $('.comment').css('display', 'none');
            });
        }
    });
});
