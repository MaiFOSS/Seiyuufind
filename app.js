const button = document.querySelector(".btn");
const divElement = document.querySelector(".value");

button.addEventListener("click", (e) => {
	const value = Number.parseInt(divElement.textContent);
	const newValue = value + 1;
	divElement.textContent = newValue;
});
