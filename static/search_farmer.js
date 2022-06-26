let search_input = document.getElementById('datatable-search-input');
search_input.addEventListener("input", function() {
    let farmer_name = search_input.value.toLowerCase()
    let farmer = document.getElementsByClassName('farmers');
    for (let i = 0; i < farmer.length; i++) {
        let farmers = document.getElementsByClassName('farmer_name')[i].innerText.toLowerCase();
        let farmer_mobile = document.getElementsByClassName('farmer_mobile')[i].innerText.toLowerCase();
        if (farmers.includes(farmer_name) || farmer_mobile.includes(farmer_name)) {
            farmer[i].style.display = '';
        }
        else {
            farmer[i].style.display = 'none';
        }
    }
})