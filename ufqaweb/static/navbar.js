$(".navbar-expanded").animate({height: '+=34vh'},300); 

let navBarStatus = false
let w = $(window).width()


$(document).ready(function () {
    $('.navbar-expand-icon-2').click(function (e) { 
        e.preventDefault();
        if (!navBarStatus) {
            $(".navbar-expanded").animate({height: '+=34vh'},300); 
            // $(".bi-list").css({WebkitTransform: 'rotate(90deg)'},300); 
            navBarStatus = true;
        } else {
            $(".navbar-expanded").animate({height: '-=34vh'},300); 
            navBarStatus = false;
        }
    });

    $('.navbar-expand-icon').click(function (e) { 
        e.preventDefault();
        if (w < 450)
            if (!navBarStatus) {
                $(".navbar-expanded-full").animate({height: '+=90vw'},300); 
                // $(".bi-list").css({WebkitTransform: 'rotate(90deg)'},300); 
                navBarStatus = true;
            } else {
                $(".navbar-expanded-full").animate({height: '-=90vw'},300); 
                navBarStatus = false;
            }
        else {
            $('.navbar-expanded-full').fadeIn();
        }
    });

    $('.closeNavbar').click(function (e) { 
        e.preventDefault();
        if (w < 450)
            if (!navBarStatus) {
                $(".navbar-expanded-full").animate({height: '+=90vw'},300); 
                // $(".bi-list").css({WebkitTransform: 'rotate(90deg)'},300); 
                navBarStatus = true;
            } else {
                $(".navbar-expanded-full").animate({height: '-=90vw'},300); 
                navBarStatus = false;
            }
        else {
            $('.navbar-expanded-full').fadeOut();
        } 
    });
});