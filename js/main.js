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
});
