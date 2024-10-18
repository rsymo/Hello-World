document.write("Hello, world!");

// create a function to convert celcius to farenheit
function celsiusToFarenheit(celsius) {
  return celsius * 9 / 5 + 32;
}

// create a function to convert farenheit to celcius
function farenheitToCelsius(farenheit) {
  return (farenheit - 32) * 5 / 9;
}

// create an array of months in the year
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

// create an array of months in the year in german
const monthsInGerman = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"];

// create a function to get the month in the year
function getMonthName(month) {
  return months[month - 1];
}



