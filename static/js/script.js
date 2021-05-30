console.log("iamhere")

function addToCart(event){
    console.log(event.target)
}

function openSlideMenu(){
    document.getElementById('side-menu').style.width= '190px';
}

function closeSlideMenu(){
    document.getElementById('side-menu').style.width= '0';
}

// container = document.getElementsByClassName('similar-products-list')
// let left = document.getElementById('left')
// let right = document.getElementById('right')
// left.addEventListener('click', function(){
//     container[0].scrollLeft -= 160;
// })

// right.addEventListener('click', function(){
//     container[0].scrollLeft += 160;
// })

buttons=document.getElementsByClassName('fruit-btn')
for(let i=0;i<buttons.length;i++){
    buttons[i].addEventListener('click',function addToCart(event){
        var btn = event.target
        var container= btn.parentElement
        var stockid = container.getElementsByClassName('stockid')[0]
        stockidlist=localStorage.getItem('cartstock')
        if(stockidlist==null){
            stockidlist=[]
        }
        else{
        var stockidlist = JSON.parse("[" + stockidlist + "]");
        }
        if(!stockidlist.includes(parseInt(stockid.textContent))){
            stockidlist.push(stockid.textContent)
        }
        localStorage.setItem('cartstock',stockidlist)
    })
}

console.log("iamhere")