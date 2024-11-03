document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        const name = document.getElementById("name").value.trim();
        if (name === "") {
            alert("Name is required.");
            event.preventDefault();
            return;
        }

        const email = document.getElementById("email").value.trim();
       
