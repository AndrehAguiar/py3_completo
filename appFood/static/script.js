var userLogged = "";
var userBasket = {}
var basket = {}
var basketLoaded = null


function chkBtnCheckout(){
  var btn = document.getElementById('btn-chkout')
  if(basketLoaded["userBasket"] !== undefined & window.location.pathname !== "/checkout"){
    btn.disabled = false;
  }else{
    btn.disabled = true;
  }
}

function setBasket(basket){
  localStorage.setItem('userBasket', JSON.stringify(basket));
}

function getBasket(){
  return JSON.parse(localStorage.getItem('userBasket')) ;
}

function loadBasket(basketLoaded){

  var content = document.getElementById('basket-items');

  if(basketLoaded["userLogged"] === userLogged & basketLoaded["userBasket"] !== undefined){
    content.innerHTML = ""
    var userDict = {};
    var shop = {};
    console.log(Object.keys(basketLoaded["userBasket"]).length);
    for(var i = 0; i < Object.keys(basketLoaded["userBasket"]).length; i++){
      var item = basketLoaded["userBasket"][i]["item"];
      var qtd = basketLoaded["userBasket"][i]["qtd"];
      var price = basketLoaded["userBasket"][i]["price"];
      var image = basketLoaded["userBasket"][i]["image"];

      content.innerHTML += `<div id='basket-item-${i}'>${image} <div id='item-${i}-descr'><span>${item} </span> <span>qtd. <small>${qtd}:<br /> R$ </small> ${(price*qtd).toFixed(2)}</span></div></div>`;

      shop[i] = {'item':item, 'qtd':qtd, 'price':price};
    }
    userDict["userLogged"] = userLogged;
    userDict['userBasket'] = shop;
    document.querySelector('#shop').value = JSON.stringify(userDict);
    chkBtnCheckout();
  }
}

function subItem(id){
  var dvQtd = document.getElementById(`item-${id}-qtd`)
  var qtd = parseInt(dvQtd.innerHTML);
  if (qtd === 1){
    document.getElementById(`sub-${id}`).disabled = true;
    document.getElementById(`item-${id}-add`).disabled = true;
  }
  qtd-=1;
  dvQtd.innerHTML = qtd;
}

function sumItem(id){
  var dvQtd = document.getElementById(`item-${id}-qtd`)
  var qtd = parseInt(dvQtd.innerHTML);
  if (qtd === 0){
    document.getElementById(`sub-${id}`).disabled = false;
    document.getElementById(`item-${id}-add`).disabled = false;
  }
  qtd+=1;
  dvQtd.innerHTML = qtd;
}

function showBasket(){
  var dvBasket = document.getElementById('dv-basket');

  if (dvBasket.style.display === "block"){
    dvBasket.style.display = "none";
  }else{
    dvBasket.style.display = "block";
  }
}

function addItem(id){
  var spUser = document.getElementById(`sp-client`);
  if(spUser.innerHTML === ""){
    window.location.href = "/client";
  }else{
    if(basketLoaded['userBasket'] === undefined){
      loadBasket(basketLoaded);
      basketLoaded['userBasket'] = {};
    }

    var user = spUser.innerHTML;
    var content = document.getElementById('basket-items');
    var item = document.getElementById(`item-${id}-name`);
    var image = document.getElementById(`item-${id}-image`).innerHTML;
    var price = document.getElementById(`item-${id}-price`).innerHTML;
    var qtd = document.getElementById(`item-${id}-qtd`).innerHTML;
    var name = item.getElementsByTagName("H3")[0].innerHTML;

    var idBasket = Object.keys(basketLoaded['userBasket']).length;
    basketLoaded['userBasket'][idBasket]={'item':name,'qtd':qtd,'price':price,'image':image};

    if (content.innerHTML === "Nenhum item adicionado!"){
      content.innerHTML = "";
      document.getElementById('btn-chkout').disabled = false;
    }
    var item = document.getElementById(`item-${id}-name`).innerHTML
    content.innerHTML += `<div id='basket-item-${id}'>${image} <div id='item-${id}-descr'><span>${name} </span> <span>qtd. <small>${qtd}:<br /> R$ </small> ${(price*qtd).toFixed(2)}</span></div></div>`
    showBasket();

    setBasket(basketLoaded);
    document.querySelector('#shop').value = JSON.stringify(basketLoaded);
    setTimeout(function(){showBasket();}, 3000);
  }
}

window.addEventListener('load', function(e) {

  var basket;
  var logged = false;
  var user = document.getElementById(`sp-client`).innerHTML;
  if (user !== ""){
    userLogged = user.split(" | ")[0];
    logged = true;
  }
  basketLoaded = getBasket();
  if (basketLoaded === null || basketLoaded["userLogged"] !== userLogged) {
    setBasket({userLogged});
    basketLoaded = getBasket();
    console.log(basketLoaded)

  }else if(basketLoaded["userBasket"] !== undefined){
      loadBasket(basketLoaded);
  }
  if(logged){
      userBasket = basketLoaded;
  }
  document.getElementById("loader").remove();
  document.getElementById("dvLoader").remove();
});
