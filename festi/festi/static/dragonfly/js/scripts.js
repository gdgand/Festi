/*
 * Theme name: Dragonfly
 * Description: Additional scripts
 * Version: 1.5
 * Last update: September 6 2014
 * Author: Jiri Cermak
 * */

$(document).ready(function() {

    /*
     * ===================================
     * Back To Top
     * ===================================
     * */

    var offset = 220,
        duration = 500;
    $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
            $('.back-to-top').fadeIn(duration);
        } else {
            $('.back-to-top').fadeOut(duration);
        }
    });

    $('.back-to-top').click(function(event) {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, duration);
        return false;
    });


    /*
     * ===================================
     * Smooth scroll - from href to id
     * ===================================
     * */

    // Must add the class "scroll" to the link - <a href="#someID" class="scroll">
    $('a.scroll').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });

    /*
     * ===================================
     * Removing conflicts
     * ===================================
     * */

    // example: when click on filter menu, it will be removed class of loading animation

    $(".filter").on("click", function() {
        $(".hover-content").removeClass("easeUp easePulse switchOnTv wow animated");
    });



    /*
     * ===================================
     * Sidebar
     * ===================================
     * */


    /* close sidebar */
    $("#sidebar-close").click(function() {
        $(".sidebar-off").removeClass("sidebar-on");
    });
    $('html').click(function() {
        $(".sidebar-off").removeClass("sidebar-on");
    });

    $(".sidebar-off").click(function(event) {
        event.stopPropagation();
    });

    /* open sidebar */
    $("#sidebar-btn").on("click", function(event) {
        event.stopPropagation();
        event.preventDefault();
        $(".sidebar-off").toggleClass("sidebar-on");
    });



    /*
     * ===================================
     * Smooth scrolling
     * ===================================
     * */

    //not active for Internet Explorer (version 9 and 10), only for version 11 and higher
    var $noIE = $("html").hasClass("ie");
    if ($noIE) {
        $("#IEremove").remove();
        $("html").css({
            "overflow": "visible"
        });
    } else {

        //setting for smooth scrolling
        $("html").niceScroll({
            cursorcolor: "#999",
            cursorwidth: "8px",
            cursorborder: "none",
            cursorborderradius: "0px",
            scrollspeed: 60,
            mousescrollstep: 15 * 3,
            hwacceleration: true,
            background: "#ddd",
            preservenativescrolling: true,
            bouncescroll: true,
            spacebarenabled: true,
            disableoutline: true,
            smoothscroll: true,
            sensitiverail: true,
            hidecursordelay: 500,
            cursordragspeed: 0.3,
            zindex: 999999
        });
    }



    /*
     * ===================================
     * Style Switcher
     * ===================================
     * */


    //=== show/hide style-switcher by the class "active" ===//
    $(".switcher-icon").on("click", function() {
        $(".style-switcher").toggleClass("active");
    });


    //=== navigation settings ===//

    //dark, light or transparent
    var navbar = $("#navbarSettings"),
        navbarSpace = $("#navbarSpaceBottom");

    $("#navDark").click(function() {
        navbar.removeStyle("background-color");;
        navbar.removeClass("navbar-default navbar-trn").addClass("navbar-inverse");
        if (navbar.hasClass("navbar-fixed-top")) {
            navbarSpace.css({
                "height": "70px"
            });
        } else {
            navbarSpace.removeStyle("height");
        }
    });
    $("#navLight").click(function() {
        navbar.removeStyle("background-color");
        navbar.removeClass("navbar-inverse navbar-trn").addClass("navbar-default");
        if (navbar.hasClass("navbar-fixed-top")) {
            navbarSpace.css({
                "height": "70px"
            });
        } else {
            navbarSpace.removeStyle("height");
        }
    });
    $("#navTrn").click(function() {
        navbarSpace.removeStyle("height");
        navbar.removeClass("navbar-inverse navbar-default").addClass("navbar-trn");
    });


    // Fixed or relative position of navbar
    $("#navRelative").click(function() {
        navbar.removeClass("navbar-fixed-top");
        navbarSpace.removeStyle("height");
    });
    $("#navFixed").click(function() {
        if (navbar.hasClass("navbar-trn")) {
            navbarSpace.removeStyle("height");
        } else {
            navbarSpace.css({
                "height": "70px"
            });
        }
        navbar.addClass("navbar-fixed-top");
    });



    /*=== Colors Themes ===*/

    var $knobs = $("#GreenKnobs, #YellowKnobs, #RedKnobs, #LightBlueKnobs, #BlueKnobs");
    //gKnob = green knob - when you choose a color theme, this function will hide all other ID of the knobs

    $(".light-blue").on("click", function() {
        $("#colors").attr("href", "assets/css/themes/light-blue.css");
        $knobs.hide();
        $("#LightBlueKnobs").show();
        return false;
    });

    $(".blue").on("click", function() {
        $("#colors").attr("href", "assets/css/themes/blue.css");
        $knobs.hide();
        $("#BlueKnobs").show();
        return false;
    });
    $(".red").on("click", function() {
        $("#colors").attr("href", "assets/css/themes/red.css");
        $knobs.hide();
        $("#RedKnobs").show();
        return false;
    });
    $(".yellow").on("click", function() {
        $("#colors").attr("href", "assets/css/themes/yellow.css");
        $knobs.hide();
        $("#YellowKnobs").show();
        return false;
    });
    $(".green").on("click", function() {
        $("#colors").attr("href", "assets/css/themes/green.css");
        $knobs.hide();
        $("#GreenKnobs").show();
        return false;
    });

    /*=== Transparent navigation ===*/

    // add background color to transparent navbar after scrolling 90px
    $(window).scroll(function() {
        var $navbarTrn = $(".navbar-trn"),
            $nav = $(".navbar");
        if (navbar.hasClass("navbar-fixed-top")) {
            if ($(window).scrollTop() > 150) {
                $navbarTrn.css({
                    "background-color": "rgba(0, 0, 0, 0.8)"
                });
            } else {
                $navbarTrn.css({
                    "background-color": "transparent"
                });
            }
        } else {
            $navbarTrn.css({
                "background-color": "transparent"
            });
        }
        // add box-shadow
        if (navbar.hasClass("navbar-fixed-top")) {
            if ($(window).scrollTop() > 150) {
                $nav.css({
                    "box-shadow": "0 2px 5px rgba(0, 0, 0, 0.2)"
                });
            } else {
                $nav.css({
                    "box-shadow": "none"
                });
            }
        } else {
            $nav.css({
                "box-shadow": "none"
            });
        }
    });



    /*
     * ===================================
     * Settings for plugins
     * ===================================
     * */


    /*=== WOW - Loading animations ===*/
    new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 0,
        mobile: false
    }).init();


    /*=== Mixitup - Filterable portfolio ===*/
    $('#Grid').mixitup();


    /*=== Slippry Slideshow in frame of Macbook Pro - using on Services III ===*/
    var thumbs = $('#mb-slideshow').slippry({
        // general elements & wrapper
        slideWrapper: '<div class="frame sy-slides-wrap" />',
        slippryWrapper: '<div class="slippry_box thumbnails" />',
        // options
        transition: 'horizontal',
        pager: false,
        auto: true,
        onSlideBefore: function(el, index_old, index_new) {
            $('.thumbs a img').removeClass('active');
            $('img', $('.thumbs a')[index_new]).addClass('active');
        }
    });

    $('.thumbs a').click(function() {
        thumbs.goToSlide($(this).data('slide'));
        return false;
    });


    /*=== Slippry Slideshow - using on the page About us I ===*/
    $('#slider-aboutUs').slippry({
        slideWrapper: '<div class="normal sy-slides-wrap" />',
        transition: 'fade',
        auto: true,
        useCSS: true,
        pause: 5000
    });


    /*=== Sticky - Make every elements sticky, just set a class or ID ===*/
    $(".sticker").sticky({
        topSpacing: 0
    });


    /*=== Knobs - our skills ===*/

    // Light Blue Knob
    $(".lbKnob").knob({
        fgColor: "#1eb9c1",
        min: 0,
        max: 100,
        step: 5,
        angleOffset: 0,
        angleArc: 360,
        stopper: true,
        readOnly: true,
        cursor: false,
        lineCap: 'none',
        thickness: '0.03',
        width: 150,
        displayInput: true,
        displayPrevious: true,
        inputColor: '#999999',
        font: 'Lato',
        fontWeight: 'normal',
        bgColor: '#EEEEEE',
        draw: function() {
            if (this.$.data('skin') == 'tron') {
                var a = this.angle(this.cv), // Angle

                    sa = this.startAngle, // Previous start angle

                    sat = this.startAngle, // Start angle

                    ea, // Previous end angle
                    eat = sat + a, // End angle

                    r = 1;
                this.g.lineWidth = this.lineWidth;
                this.o.cursor && (sat = eat - 0.3) && (eat = eat + 0.3);
                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor && (sa = ea - 0.3) && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }
                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();
                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();
                return false;
            }

        }
    });

    //Blue Knob
    $(".bKnob").knob({
        fgColor: "#1a99aa",
        min: 0,
        max: 100,
        step: 5,
        angleOffset: 0,
        angleArc: 360,
        stopper: true,
        readOnly: true,
        cursor: false,
        lineCap: 'none',
        thickness: '0.03',
        width: 150,
        displayInput: true,
        displayPrevious: true,
        inputColor: '#999999',
        font: 'Lato',
        fontWeight: 'normal',
        bgColor: '#EEEEEE',
        draw: function() {
            if (this.$.data('skin') == 'tron') {
                var a = this.angle(this.cv), // Angle

                    sa = this.startAngle, // Previous start angle

                    sat = this.startAngle, // Start angle

                    ea, // Previous end angle
                    eat = sat + a, // End angle

                    r = 1;
                this.g.lineWidth = this.lineWidth;
                this.o.cursor && (sat = eat - 0.3) && (eat = eat + 0.3);
                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor && (sa = ea - 0.3) && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }
                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();
                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();
                return false;
            }

        }
    });

    // Green Knob
    $(".gKnob").knob({
        fgColor: "#3c948b",
        min: 0,
        max: 100,
        step: 5,
        angleOffset: 0,
        angleArc: 360,
        stopper: true,
        readOnly: true,
        cursor: false,
        lineCap: 'none',
        thickness: '0.03',
        width: 150,
        displayInput: true,
        displayPrevious: true,
        inputColor: '#999999',
        font: 'Lato',
        fontWeight: 'normal',
        bgColor: '#EEEEEE',
        draw: function() {
            if (this.$.data('skin') == 'tron') {
                var a = this.angle(this.cv), // Angle

                    sa = this.startAngle, // Previous start angle

                    sat = this.startAngle, // Start angle

                    ea, // Previous end angle
                    eat = sat + a, // End angle

                    r = 1;
                this.g.lineWidth = this.lineWidth;
                this.o.cursor && (sat = eat - 0.3) && (eat = eat + 0.3);
                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor && (sa = ea - 0.3) && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }
                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();
                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();
                return false;
            }

        }
    });

    // Red Knob
    $(".rKnob").knob({
        fgColor: "#df6c4f",
        min: 0,
        max: 100,
        step: 5,
        angleOffset: 0,
        angleArc: 360,
        stopper: true,
        readOnly: true,
        cursor: false,
        lineCap: 'none',
        thickness: '0.03',
        width: 150,
        displayInput: true,
        displayPrevious: true,
        inputColor: '#999999',
        font: 'Lato',
        fontWeight: 'normal',
        bgColor: '#EEEEEE',
        draw: function() {
            if (this.$.data('skin') == 'tron') {
                var a = this.angle(this.cv), // Angle

                    sa = this.startAngle, // Previous start angle

                    sat = this.startAngle, // Start angle

                    ea, // Previous end angle
                    eat = sat + a, // End angle

                    r = 1;
                this.g.lineWidth = this.lineWidth;
                this.o.cursor && (sat = eat - 0.3) && (eat = eat + 0.3);
                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor && (sa = ea - 0.3) && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }
                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();
                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();
                return false;
            }

        }
    });

    // Yellow Knob
    $(".yKnob").knob({
        fgColor: "#ecd06f",
        min: 0,
        max: 100,
        step: 5,
        angleOffset: 0,
        angleArc: 360,
        stopper: true,
        readOnly: true,
        cursor: false,
        lineCap: 'none',
        thickness: '0.03',
        width: 150,
        displayInput: true,
        displayPrevious: true,
        inputColor: '#999999',
        font: 'Lato',
        fontWeight: 'normal',
        bgColor: '#EEEEEE',
        draw: function() {
            if (this.$.data('skin') == 'tron') {
                var a = this.angle(this.cv), // Angle

                    sa = this.startAngle, // Previous start angle

                    sat = this.startAngle, // Start angle

                    ea, // Previous end angle
                    eat = sat + a, // End angle

                    r = 1;
                this.g.lineWidth = this.lineWidth;
                this.o.cursor && (sat = eat - 0.3) && (eat = eat + 0.3);
                if (this.o.displayPrevious) {
                    ea = this.startAngle + this.angle(this.v);
                    this.o.cursor && (sa = ea - 0.3) && (ea = ea + 0.3);
                    this.g.beginPath();
                    this.g.strokeStyle = this.pColor;
                    this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sa, ea, false);
                    this.g.stroke();
                }
                this.g.beginPath();
                this.g.strokeStyle = r ? this.o.fgColor : this.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth, sat, eat, false);
                this.g.stroke();
                this.g.lineWidth = 2;
                this.g.beginPath();
                this.g.strokeStyle = this.o.fgColor;
                this.g.arc(this.xy, this.xy, this.radius - this.lineWidth + 1 + this.lineWidth * 2 / 3, 0, 2 * Math.PI, false);
                this.g.stroke();
                return false;
            }

        }
    });
});