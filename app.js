const button = document.querySelector(".btn");
const divElement = document.querySelector(".value");

button.addEventListener("click", (e) => {
	const value = Number.parseInt(divElement.textContent);
	const newValue = value + 1;
	divElement.textContent = newValue;
});


// script.js
document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value;
    alert('You searched for: ' + query);
    // Here you can add more functionality, like redirecting to a search results page
});
