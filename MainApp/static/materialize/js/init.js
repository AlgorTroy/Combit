$(document).ready(function() {
    $('.slider').slider();

    $(window).scroll(function() { // check if scroll event happened
        if ($(document).scrollTop() > 10) { // check if user scrolled more than 50 from top of the browser window
          $(".nav-wrapper").css("background-color", "rgba(36,49,60,0.7)"); // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
        } else {
          $(".nav-wrapper").css("background-color", "transparent"); // if not, change it back to transparent
        }
      });
});
