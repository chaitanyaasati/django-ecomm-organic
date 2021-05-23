function openSlideMenu(){
    document.getElementById('side-menu').style.width= '190px';
}

function closeSlideMenu(){
    document.getElementById('side-menu').style.width= '0';
}

container = document.getElementsByClassName('similar-products-list')
console.log(container)
console.log(document.getElementById('left'))
let left = document.getElementById('left')
let right = document.getElementById('right')
left.addEventListener('click', function(){
    console.log("left");
    container[0].scrollLeft -= 160;
})

right.addEventListener('click', function(){
    console.log("right")
    container[0].scrollLeft += 160;
})

right = document.getElementById('right')