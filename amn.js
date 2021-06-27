$(function() {
  // #
  $('a:not([href^="#"]):not([target])').on('click', function(e){
    e.preventDefault(); 
    url = $(this).attr('href'); 
    if (url !== '') {
      $('body').addClass('fadeout');  // class="fadeout"
      setTimeout(function(){
        window.location = url;  // 0.8
      }, 800);
    }
    return false;
  });
});
