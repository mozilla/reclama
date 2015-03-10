jQuery(document).ready(function ($) {
    Tabzilla.disableEasterEgg();

    /* Navigation Menu */

    // Collapse Nav menu when user clicks outside the dropdown
    function collapseNavMenu() {
        $("#nav-main-menu").hide();
        $("#nav-main-menu").removeClass("open");
        $("#outer-wrapper").off("click", collapseNavMenu);
    }

    // Expand Nav menu
    function expandNavMenu(e) {
        var $menu = $("#nav-main-menu");
        e.stopPropagation();

        $menu.toggle();
        $menu.toggleClass("open");

        // If the nav is open listen for clicks outside the dropdown
        if ($menu.hasClass("open")) {
            $("#outer-wrapper").on("click", collapseNavMenu);
        } else {
            $("#outer-wrapper").off("click", collapseNavMenu);
        }
    }

    // Nav menu trigger (Mobile)
    $(".toggle").on("click", function(e) {
        expandNavMenu(e);
    });
});
