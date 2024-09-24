document.addEventListener('DOMContentLoaded', function () {
    // Check if the current page is the index.html page
    if (window.location.pathname === '/') {
        // Text to be animated
        const professionText = "Full Stack Developer";
        // Element where text will be displayed
        const professionElement = document.getElementById('profession');

        // Function to animate text
        function animateText() {
            let index = 0;
            // Calculate speed of typing animation
            const speed = 5000 / professionText.length; // Adjust the speed to achieve desired duration

            // Function to add each character of text
            function addCharacter() {
                if (index < professionText.length) {
                    // Append character to text element
                    professionElement.textContent += professionText.charAt(index);
                    index++;
                    // Schedule next character addition
                    setTimeout(addCharacter, speed); // Adjust the speed of typing animation here (in milliseconds)
                } else {
                    // Clear text content and restart animation after delay
                    setTimeout(function () {
                        professionElement.textContent = "";
                        animateText();
                    }, 2000); // Wait for 2 seconds before restarting the animation
                }
            }

            // Start the typing animation
            addCharacter();
        }

        // Start the animation only if it's the index.html page
        animateText();
    }
});







//window onclick other menu items
document.addEventListener('DOMContentLoaded', function () {
    // Get menu toggle button
    let menuToggle = document.getElementById('menuToggle');

    // Get window menu
    let windowMenu = document.getElementById('windowMenu');

    // Add click event listener to menu toggle button
    menuToggle.addEventListener('click', function (event) {
        // Prevent the default action of the anchor tag
        event.preventDefault();

        // Toggle 'active' class on window menu
        windowMenu.classList.toggle('open');
    });

});






// Scroll to top button functionality
document.addEventListener('DOMContentLoaded', function () {

    // Dynamically add scroll-to-top button
    let scrollToTopHTML = '<button id="scrollToTopBtn" onclick="scrollToTop()">' +
        '<span class="material-symbols-outlined">pan_tool_alt</span>' +
        '</button>';
    document.body.insertAdjacentHTML('beforeend', scrollToTopHTML);

    // Function to handle scrolling
    function handleScroll() {
        const scrollToTopButton = document.getElementById("scrollToTopBtn");
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollToTopButton.style.display = "block";
        } else {
            scrollToTopButton.style.display = "none";
        }
    }

    // Add scroll to top button when DOM is loaded
    let scrollToTopButton = document.getElementById("scrollToTopBtn");
    window.onscroll = function () {
        handleScroll();
    };

});

// Function to scroll to top
function scrollToTop() {
    if (document.documentElement.scrollTop > 0) {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    } else {
        document.body.scrollTop = 0; // For Safari
    }
}





// Open navigation drawer
function openNav() {
    document.getElementById("mobileNav").style.left = "0";
    document.body.classList.add("drawer-open");
}





// Close navigation drawer
function closeNav() {
    document.getElementById("mobileNav").style.left = "-110%";
    document.body.classList.remove("drawer-open");
}

document.addEventListener("DOMContentLoaded", function () {
    let loader = document.querySelector(".loader");

    // Prevent scrolling while loader is displayed
    document.body.classList.add("no-scroll");

    // Hide loader when page content is fully loaded, with a minimum 1-second delay
    window.addEventListener("load", function () {
        setTimeout(function () {
            loader.style.display = "none";
            document.body.classList.remove("no-scroll"); 
        }, 1000);
    });
});





// Get the current URL path
let path = window.location.pathname;

// Function to set active menu item
function setActiveMenuItem(menuItems) {
    menuItems.forEach(function (item) {
        item.classList.remove("active");
        if (item.getAttribute("href") === path) {
            item.classList.add("active");
        }
    });
}
document.addEventListener("DOMContentLoaded", function () {
    // Get menu items and call setActiveMenuItem function
    let mobileMenuItems = document.querySelectorAll(".mobile a");
    setActiveMenuItem(mobileMenuItems);

    let windowMenuItems = document.querySelectorAll(".window a");
    setActiveMenuItem(windowMenuItems);

    let windowBoxMenuItems = document.querySelectorAll(".window-menu a");
    setActiveMenuItem(windowBoxMenuItems);
});
