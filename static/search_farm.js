let group_by = document.getElementsByClassName('dropdown-item');
group_by[0].addEventListener('click', function GroupBy() {
    let farm_space = document.getElementsByClassName('farm_space');
    let card = document.getElementsByClassName('card')
    for(let i = 0; i < farm_space.length; i++){
        if(farm_space[i].innerText > 0){
            card[i].style.display = 'block';
        }
        else{
            card[i].style.display = 'none';
        }
    }
});

group_by[1].addEventListener('click', function GroupBy() {
    let farm_space = document.getElementsByClassName('farm_space');
    let card = document.getElementsByClassName('card')
    for(let i = 0; i < farm_space.length; i++){
        if(farm_space[i].innerText > 40){
            card[i].style.display = 'block';
        }
        else{
            card[i].style.display = 'none';
        }
    }
});

group_by[2].addEventListener('click', function GroupBy() {
    let farm_space = document.getElementsByClassName('farm_space');
    let card = document.getElementsByClassName('card')
    for(let i = 0; i < farm_space.length; i++){
        if(farm_space[i].innerText <= 40 && farm_space[i].innerText > 20){
            card[i].style.display = 'block';
        }
        else{
            card[i].style.display = 'none';
        }
    }
});

group_by[3].addEventListener('click', function GroupBy() {
    let farm_space = document.getElementsByClassName('farm_space');
    let card = document.getElementsByClassName('card')
    for(let i = 0; i < farm_space.length; i++){
        if(farm_space[i].innerText <= 20){
            card[i].style.display = 'block';
        }
        else{
            card[i].style.display = 'none';
        }
    }
});