var planting_history_menu = document.getElementById("planting_history_menu");
var soil_test_menu = document.getElementById("soil_test_menu");
var planting_history = document.getElementById("planting_history");
var soil_test = document.getElementById("soil_test");

soil_test_menu.addEventListener("click", function soil_test_func() {
  soil_test.style.display = 'block';
  planting_history.style.display = 'none';
  soil_test_menu.style.backgroundColor = '#e4fff5';
  planting_history_menu.style.backgroundColor = 'white';
})

planting_history_menu.addEventListener("click", function planting_history_func() {
  planting_history.style.display = 'block';
  soil_test.style.display = 'none';
  planting_history_menu.style.backgroundColor = '#e4fff5';
  soil_test_menu.style.backgroundColor = 'white';
})