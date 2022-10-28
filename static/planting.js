var fertilizer_menu = document.getElementById("fertilizer_menu");
var water_irrigation_menu = document.getElementById("water_irrigation_menu");
var pesticide_menu = document.getElementById("pesticide_menu");
var harvesting_menu = document.getElementById("harvesting_menu");
var selling_menu = document.getElementById("selling_menu");
var fertilizer = document.getElementById("fertilizer");
var water_irrigation = document.getElementById("water_irrigation");
var pesticide = document.getElementById("pesticide");
var harvesting = document.getElementById("harvesting");
var selling = document.getElementById("selling");

fertilizer_menu.addEventListener("click", function fertilizer_func() {
  fertilizer.style.display = "block";
  water_irrigation.style.display = "none";
  pesticide.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "none";
  fertilizer_menu.style.backgroundColor = "#e4fff5";
  water_irrigation_menu.style.backgroundColor = "white";
  pesticide_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "white";
});

water_irrigation_menu.addEventListener(
  "click",
  function water_irrigation_func() {
    water_irrigation.style.display = "block";
    fertilizer.style.display = "none";
    pesticide.style.display = "none";
    harvesting.style.display = "none";
    selling.style.display = "none";
    fertilizer_menu.style.backgroundColor = "white";
    water_irrigation_menu.style.backgroundColor = "#e4fff5";
    pesticide_menu.style.backgroundColor = "white";
    harvesting_menu.style.backgroundColor = "white";
    selling_menu.style.backgroundColor = "white";
  }
);

pesticide_menu.addEventListener("click", function pesticide_func() {
  pesticide.style.display = "block";
  water_irrigation.style.display = "none";
  fertilizer.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "none";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  pesticide_menu.style.backgroundColor = "#e4fff5";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "white";
});

harvesting_menu.addEventListener("click", function harvesting_menu_func() {
  pesticide.style.display = "none";
  water_irrigation.style.display = "none";
  fertilizer.style.display = "none";
  harvesting.style.display = "block";
  selling.style.display = "none";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  pesticide_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "#e4fff5";
  selling_menu.style.backgroundColor = "white";
});
selling_menu.addEventListener("click", function selling_func() {
  pesticide.style.display = "none";
  water_irrigation.style.display = "none";
  fertilizer.style.display = "none";
  harvesting.style.display = "none";
  selling.style.display = "block";
  fertilizer_menu.style.backgroundColor = "white";
  water_irrigation_menu.style.backgroundColor = "white";
  pesticide_menu.style.backgroundColor = "white";
  harvesting_menu.style.backgroundColor = "white";
  selling_menu.style.backgroundColor = "#e4fff5";
});