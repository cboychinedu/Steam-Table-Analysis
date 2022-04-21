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

// Debug 
console.log("working")

// Accessing the dom elements 
let temperature_result = document.getElementById("temperature_result");
let pressure_input_value = document.getElementById("pressure_value_input"); 
let submit_btn = document.getElementById("convert_to_temperature_btn")
let temperature_value; 
let pressure_value; 

// Adding an event listener for the submit button 
submit_btn.addEventListener("click", (event) => {
    // 
    pressure_value = pressure_input_value.value || 0.00 
    data = JSON.stringify({ "pressure_value": pressure_value })

    // Using Ajax to send the data to the server 
    $.ajax({
        // Setting up the ajax configurations 
        type: "POST", 
        url: "/temperature/prediction", 
        dataType: "json", 
        contentType: "application/json", 
        data: data
    })
    // On response from the server, execute the block of code below 
    .done((data) => {
        // If the prediction was a success 
        if (data.message === "success" ) {
            // Getting the predicted temperature value 
            temperature_value = data.result.predictedTemp;
            
            // Displaying the predicted temperature 
            temperature_result.innerText = `${temperature_value} °C`; 
        }

        // If the message is an error message 
        else if (data.message === "error" ) {
            // Execute the code block below 
            temperature_value.innerText = data.result; 
        }
    })
})