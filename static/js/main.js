// let likeCount = document.querySelectorAll('.likeButtonCount').innerText;
// let count = 0;
// let likeButton = document.querySelectorAll('.likeButton');
// let button = $('.fa-heart');
// console.log(button);

// for (let i = 0; i < likeButton.length; i++) {
//     button[i].addEventListener('click', () => {
//         const toggleClass = (el, className) => el.classList.toggle(className);
//         toggleClass(button[i], 'animateLike');
//         if (count % 2 == 0) {
//             likeCount[i]--;
//             likeCount[i].text(x);
//         } else {
//             likeCount[i]++;
//             likeCount[i].text(x);
//         }
//     });
// }
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
        $(this).parent('.tempFooter').next('.answerForm').slideToggle();
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
    // $('.send_comment').c((index) => {
    //     $(this).on('click', () => {
    //         $('.commenting').each((index) => {
    //             $(this).slideToggle();
    //         });
    //     });
    // });
});
