$(document).ready(function() {
    $('.slider').slider();
    $(window).scroll(function() { // check if scroll event happened
        if ($(document).scrollTop() > 10) { // check if user scrolled more than 50 from top of the browser window
            $(".nav-wrapper").css("background-color", "rgba(36,49,60,0.7)"); // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
        } else {
            $(".nav-wrapper").css("background-color", "transparent"); // if not, change it back to transparent
        }
    });
    $('ul.tabs').tabs();
    $('.modal').modal();

    // footer animations added
    var social_holder_classes = ['#social-icon-holder-1', '#social-icon-holder-2', '#social-icon-holder-3', '#social-icon-holder-4'];
    var social_holder_animation = 'animated rubberBand';
    // loop through the classes one by one
    for (var i = 0; i < social_holder_classes.length; i++) {
        $(social_holder_classes[i]).hover(function() {
            $(this).addClass(social_holder_animation);
        }, function() {
            $(this).removeClass(social_holder_animation);
        });
    }

    var content_container_anim = ['animated pulse', 'animated flipInY'];
    // var content_scroll_length = [20, 30];
    $(window).scroll(function() { // check if scroll event happened
        if ($(document).scrollTop() > 20) { // check if user scrolled more than 50 from top of the browser window
            $('#content_container-1').addClass(content_container_anim[0]); // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
        } else {
            $('#content_container-1').removeClass(content_container_anim[0]); // if not, change it back to transparent
        }
    });

    $(window).scroll(function() { // check if scroll event happened
        if ($(document).scrollTop() > 40) { // check if user scrolled more than 50 from top of the browser window
            $('#content_container-2').addClass(content_container_anim[0]); // if yes, then change the color of class "navbar-fixed-top" to white (#f8f8f8)
        } else {
            $('#content_container-2').removeClass(content_container_anim[0]); // if not, change it back to transparent
        }
    });

    var ctrg_exp_icon_anim = 'animated pulse';
    $('#category_explore_icon').hover(function() {
      /* Stuff to do when the mouse enters the element */
      $(this).addClass(ctrg_exp_icon_anim);
    }, function() {
      /* Stuff to do when the mouse leaves the element */
      $(this).removeClass(ctrg_exp_icon_anim);
    });

    $('.dropdown-button').dropdown({
      inDuration: 100,
      outDuration: 300,
      constrainWidth: false, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'left', // Displays dropdown with edge aligned to the left of button
      stopPropagation: false // Stops event propagation
    }
  );


});
