(function($) {
    'use strict';
    $(function() {
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
<<<<<<< HEAD
                window.history.back();  // Go back if not a popup.
=======
                window.history.back(); // Go back if not a popup.
>>>>>>> d78f511d3327b2f39c6bc7fb78199ecff1f054ca
            } else {
                window.close(); // Otherwise, close the popup.
            }
        });
    });
})(django.jQuery);
