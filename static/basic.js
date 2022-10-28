function deshboard_button() {
  var side_menu_button = document.getElementsByClassName("side_menu_boxes");
  var side_deshboard_button = document.getElementById("side_box_1");

  for (let i = 0; i < side_menu_button.length; i++) {
    side_menu_button[i].style.backgroundColor = "white";
    side_deshboard_button.style.backgroundColor = "#cdffc1";
  }
}

function farmers_button() {
  var side_menu_button = document.getElementsByClassName("side_menu_boxes");
  var side_deshboard_button = document.getElementById("side_box_2");

  for (let i = 0; i < side_menu_button.length; i++) {
    side_menu_button[i].style.backgroundColor = "white";
    side_deshboard_button.style.backgroundColor = "#cdffc1";
  }
}

function search_button() {
  var side_menu_button = document.getElementsByClassName("side_menu_boxes");
  var side_deshboard_button = document.getElementById("side_box_3");

  for (let i = 0; i < side_menu_button.length; i++) {
    side_menu_button[i].style.backgroundColor = "white";
    side_deshboard_button.style.backgroundColor = "#cdffc1";
  }
}

function default_parameters_button() {
  var side_menu_button = document.getElementsByClassName("side_menu_boxes");
  var side_deshboard_button = document.getElementById("side_box_4");

  for (let i = 0; i < side_menu_button.length; i++) {
    side_menu_button[i].style.backgroundColor = "white";
    side_deshboard_button.style.backgroundColor = "#cdffc1";
  }
}

function createuser_button() {
  var side_menu_button = document.getElementsByClassName("side_menu_boxes");
  var side_deshboard_button = document.getElementById("side_box_5");

  for (let i = 0; i < side_menu_button.length; i++) {
    side_menu_button[i].style.backgroundColor = "white";
    side_deshboard_button.style.backgroundColor = "#cdffc1";
  }
}
// if (window.location.href == 'http://127.0.0.1:8000') {
//     deshboard_button()
// }

if (window.location.href == "http://127.0.0.1:8000/farmers") {
  farmers_button();
}

if (window.location.href == "http://127.0.0.1:8000/search") {
  search_button();
}

if (window.location.href == "http://127.0.0.1:8000/default_parameters") {
  default_parameters_button();
}

if (window.location.href == "http://127.0.0.1:8000/createuser") {
  createuser_button();
}

let menu_btn = document.getElementById("menu_btn");
// menu_btn.addEventListener('click', function hide_side_menu(){
//     let side_menu = document.getElementById('side_menu');
//     let main_content = document.getElementById('main_content')
//     if(side_menu.style.display != 'none'){
//         side_menu.style.display = 'none';
//         main_content.style.marginLeft = '0';
//     }else{
//         side_menu.style.display = 'block';
//         main_content.style.marginLeft = '360px';

//     }
// })
menu_btn.addEventListener("mouseover", function hide_side_menu() {
  menu_btn.innerText = `home`;
});

menu_btn.addEventListener("mouseout", function hide_side_menu_() {
  menu_btn.innerText = `apps`;
});

let hide_unhide_logout_btn = document.getElementById("hide_unhide_logout_btn");
hide_unhide_logout_btn.addEventListener(
  "click",
  function hide_unhide_logout_box() {
    let logout_btn = document.getElementById("logout_btn");
    if (logout_btn.style.display != "block") {
      logout_btn.style.display = "block";
    } else {
      logout_btn.style.display = "none";
    }
  }
);



