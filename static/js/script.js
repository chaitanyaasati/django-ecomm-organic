function openSlideMenu(){
    document.getElementById('side-menu').style.width= '190px';
}

function closeSlideMenu(){
    document.getElementById('side-menu').style.width= '0';
}

container = document.getElementsByClassName('similar-products-list')
let left = document.getElementById('left')
let right = document.getElementById('right')
left.addEventListener('click', function(){
    container[0].scrollLeft -= 160;
})

right.addEventListener('click', function(){
    console.log("right")
    container[0].scrollLeft += 160;
})

right = document.getElementById('right')

function addToCart(event){
    console.log(event.target)
}