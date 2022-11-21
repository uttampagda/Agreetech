var pesticide_dose_menu = document.getElementById("pesticide_dose_menu");
var fertilizer_menu = document.getElementById("fertilizer_menu");
var water_irrigation_menu = document.getElementById("water_irrigation_menu");
var harvesting_menu = document.getElementById("harvesting_menu");
var selling_menu = document.getElementById("selling_menu");
var pesticide_dose = document.getElementById("pesticide_dose");
var fertilizer = document.getElementById("fertilizer");
var water_irrigation = document.getElementById("water_irrigation");
var harvesting = document.getElementById("harvesting");
var selling = document.getElementById("selling");

pesticide_dose_menu.addEventListener("click", function fertilizer_func() {
  fertilizer.style.display = "none";
  water_irrigation.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "none";
  pesticide_dose.style.display = "block";
  pesticide_dose_menu.style.backgroundColor = "#e4fff5";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "white";
});

fertilizer_menu.addEventListener("click", function fertilizer_func() {
  fertilizer.style.display = "block";
  water_irrigation.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "none";
  pesticide_dose.style.display = "none";
  pesticide_dose_menu.style.backgroundColor = "white";
  fertilizer_menu.style.backgroundColor = "#e4fff5";
  water_irrigation_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "white";
});

water_irrigation_menu.addEventListener(
  "click",
  function water_irrigation_func() {
    water_irrigation.style.display = "block";
    fertilizer.style.display = "none";
    harvesting.style.display = "none";
    selling.style.display = "none";
    pesticide_dose.style.display = "none";
    pesticide_dose_menu.style.backgroundColor = "white";
    fertilizer_menu.style.backgroundColor = "white";
    water_irrigation_menu.style.backgroundColor = "#e4fff5";
    harvesting_menu.style.backgroundColor = "white";
    selling_menu.style.backgroundColor = "white";
  }
);

harvesting_menu.addEventListener("click", function harvesting_menu_func() {
  water_irrigation.style.display = "none";
  fertilizer.style.display = "none";
  harvesting.style.display = "block";
  selling.style.display = "none";
  pesticide_dose.style.display = "none";
  pesticide_dose_menu.style.backgroundColor = "white";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "#e4fff5";
  selling_menu.style.backgroundColor = "white";
});
selling_menu.addEventListener("click", function selling_func() {
  water_irrigation.style.display = "none";
  fertilizer.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "block";
  pesticide_dose.style.display = "none";
  pesticide_dose_menu.style.backgroundColor = "white";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "#e4fff5";
});
