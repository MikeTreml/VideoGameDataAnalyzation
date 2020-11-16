var slideIndex = 0;
showSlides();
var slideIndex2 = 0;
showSlides2();
var slideIndex3 = 0;
showSlides3();
var slideIndex4 = 0;
showSlides4();

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
  
    setTimeout(showSlides4, 6000); // Change image every 2 seconds
  }