console.log("working")

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

// Accessing the dom elements 
let pressure_result = document.getElementById("pressure_result"); 
let temp_input_value = document.getElementById("temp_value_input"); 
let submit_btn = document.getElementById("convert_to_pressure_btn"); 
let temperature_value;
let pressure_value;

// Adding event listener 
submit_btn.addEventListener("click", (event) => {
    // 
    temperature_value = temp_input_value.value || 0.00
    data = JSON.stringify({ "temp_value": temperature_value })

    // Using Ajax to send the data to the server 
    $.ajax({
        // Setting up the ajax configurations 
        type: "POST", 
        url: "/pressure/prediction", 
        dataType: "json", 
        contentType: "application/json", 
        data: data 
    }) 
    // 
    .done((data) => {
        // 
        console.log(data); 
    })

})