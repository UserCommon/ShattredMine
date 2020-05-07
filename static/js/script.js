
$(document).ready(function() {
 // executes when HTML-Document is loaded and DOM is ready
console.log("document is ready");


  $( ".card" ).hover(
  function() {
    $(this).addClass('shadow').css('cursor', 'pointer');
  }, function() {
    $(this).removeClass('shadow');
  }
);

// document ready
});

const left = document.getElementsByClassName("left")
const right = document.getElementsByClassName("right")

function scroll(left, right) {

}

scroll()