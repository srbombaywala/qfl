// Toggle to show and hide navbar menu
const navbarMenu = document.getElementById("menu");
const burgerMenu = document.getElementById("burger");

burgerMenu.addEventListener("click", () => {
  navbarMenu.classList.toggle("is-active");
  burgerMenu.classList.toggle("is-active");
});

// Toggle to show and hide dropdown menu
const dropdown = document.querySelectorAll(".dropdown");

dropdown.forEach((item) => {
  const dropdownToggle = item.querySelector(".dropdown-toggle");

  dropdownToggle.addEventListener("click", () => {
    const dropdownShow = document.querySelector(".dropdown-show");
    toggleDropdownItem(item);

    // Remove 'dropdown-show' class from other dropdown
    if (dropdownShow && dropdownShow != item) {
      toggleDropdownItem(dropdownShow);
    }
  });
});

// Function to display the dropdown menu
const toggleDropdownItem = (item) => {
  const dropdownContent = item.querySelector(".dropdown-content");

  // Remove other dropdown that have 'dropdown-show' class
  if (item.classList.contains("dropdown-show")) {
    dropdownContent.removeAttribute("style");
    item.classList.remove("dropdown-show");
  } else {
    // Added max-height on active 'dropdown-show' class
    dropdownContent.style.height = dropdownContent.scrollHeight + "px";
    item.classList.add("dropdown-show");
  }
};

// Fixed dropdown menu on window resizing
window.addEventListener("resize", () => {
  if (window.innerWidth > 992) {
    document.querySelectorAll(".dropdown-content").forEach((item) => {
      item.removeAttribute("style");
    });
    dropdown.forEach((item) => {
      item.classList.remove("dropdown-show");
    });
  }
});

// Fixed navbar menu on window resizing
window.addEventListener("resize", () => {
  if (window.innerWidth > 992) {
    if (navbarMenu.classList.contains("is-active")) {
      navbarMenu.classList.remove("is-active");
      burgerMenu.classList.remove("is-active");
    }
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const heroText = document.querySelector(".hero-text");
  
  // Add the show class after a brief delay for the loading animation
  setTimeout(() => {
      heroText.classList.add("show");
  }, 300); // Adjust the delay as necessary
});


const galleryScroll = document.querySelector('.gallery-scroll');
let scrollAmount = 0;
let scrollSpeed = 1; // Adjust the scroll speed
let scrollInterval;

// Function to duplicate the gallery images for a looping effect
function duplicateGallery() {
    const images = Array.from(galleryScroll.children);
    images.forEach(image => {
        const clone = image.cloneNode(true); // Clone each image
        galleryScroll.appendChild(clone);    // Append the clone
    });
}

// Scroll the gallery continuously
function scrollGallery() {
    scrollAmount += scrollSpeed; // Increment scroll position

    // Reset to the beginning when the scroll reaches halfway (original set)
    if (scrollAmount >= galleryScroll.scrollWidth / 2) {
        galleryScroll.style.transform = `translateX(0)`; // Jump back to start without visible jump
        scrollAmount = 0;
    } else {
        galleryScroll.style.transform = `translateX(-${scrollAmount}px)`; // Continue scrolling
    }
}

// Start the automatic scrolling
function startScrolling() {
    scrollInterval = setInterval(scrollGallery, 20); // Adjust the interval for speed
}

// Pause scrolling when hovering over the gallery
galleryScroll.addEventListener('mouseover', () => {
    clearInterval(scrollInterval); // Stop scrolling
});

// Resume scrolling when the mouse leaves the gallery
galleryScroll.addEventListener('mouseout', () => {
    startScrolling(); // Restart scrolling
});

// Initialize by duplicating the gallery images and starting the scroll
duplicateGallery();
startScrolling();