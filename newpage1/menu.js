$(function() {
            /*SP*/
            function toggleNav() {
                var body = document.body;
                var hamburger = document.getElementById('nav_btn');
                var blackBg = document.getElementById('nav_bg');
                hamburger.addEventListener('click', function() {
                    body.classList.toggle('nav_open'); 
                });
                blackBg.addEventListener('click', function() {
                    body.classList.remove('nav_open'); 
                });
            }
            toggleNav();
        });
