window.addEventListener("scroll", function () {
  const header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 0);
});

function menuToggle() {
  const menuToggle = document.querySelector(".menuToggle");
  const navigation = document.querySelector(".navigation");
  menuToggle.classList.toggle("active");
  navigation.classList.toggle("active");
}

// OWL CAROUSEL
$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    // autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    center: true,
    navText: [
      "<i class='fa fa-angle-left'></i>",
      "<i class='fa fa-angle-right'></i>",
    ],
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 1,
      },
      1000: {
        items: 3,
      },
    },
  });
});
