var slideIndex = 0;
showSlides();
var slideIndex2 = 0;
showSlides2();
var slideIndex3 = 0;
showSlides3();
var slideIndex4 = 0;
showSlides4();
var slideIndex5 = 0;
showSlides5();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  slides[slideIndex-1].style.display = "block";  

  setTimeout(showSlides, 8000); // Change image every 2 seconds
}

function showSlides2() {
    var i;
    var slides = document.getElementsByClassName("mySlides2");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex2++;
    if (slideIndex2 > slides.length) {slideIndex2 = 1}    
    slides[slideIndex2-1].style.display = "block";  
  
    setTimeout(showSlides2, 10000); // Change image every 2 seconds
  }
  function showSlides3() {
    var i;
    var slides = document.getElementsByClassName("mySlides3");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex3++;
    if (slideIndex3 > slides.length) {slideIndex3 = 1}    
    slides[slideIndex3-1].style.display = "block";  
  
    setTimeout(showSlides3, 7000); // Change image every 2 seconds
  }

  function showSlides4() {
    var i;
    var slides = document.getElementsByClassName("mySlides4");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex4++;
    if (slideIndex4 > slides.length) {slideIndex4 = 1}    
    slides[slideIndex4-1].style.display = "block";  
  
    setTimeout(showSlides4, 9000); // Change image every 2 seconds
  }

  function showSlides5() {
    var i;
    var slides = document.getElementsByClassName("mySlides5");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex5++;
    if (slideIndex5 > slides.length) {slideIndex5 = 1}    
    slides[slideIndex5-1].style.display = "block";  
  
    setTimeout(showSlides5, 6000); // Change image every 2 seconds
  }

  $( function() {
    $( "#draggable" ).draggable();
});
function mOver(obj){

	$("#details__title-grid").html($(obj).find('.name-data').text());
	$("#details__year-grid").html($(obj).find('.year-data').text());
	$("#details__publisher-grid").html($(obj).find('.publisher-data').text());
    $("#details__genre-grid").html($(obj).find('.genre-data').text());
	$("#details__platform-grid").html($(obj).find('.platform-data').text());
    $("#details__rank-grid").html($(obj).find('.rank-data').text());
    $("#details__globals-grid").html($(obj).find('.globalsales-data').text());
    $("#details__title-grid").attr("href", "/chartdetails?name="+$(obj).find('.name-data').text());
};
function mOut(obj){
}