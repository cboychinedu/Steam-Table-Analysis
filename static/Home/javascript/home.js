console.log("Working")

// When the user scrools the page, execute myFunction
window.onscroll = function() {staticScroll()};

// Get the header id
let header = document.getElementById("main_nav");

// Get the offset position of the navbar
let sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scrool position. Remove
// "sticky" when you leave the scroll position
function staticScroll()
{
    // Code execution
    if ( window.pageYOffset > sticky )
    {
        // if the condition is met, execute the code below
        header.classList.add("sticky");
    }

    // Else condition
    else
    {
        // code execution
        header.classList.remove("sticky");
    }
};