const increment = document.querySelector(".increment");

setInterval(() => {
	const value = Number.parseInt(increment.textContent);
	const newValue = value + 1;
	increment.textContent = newValue;
}, 1000);
