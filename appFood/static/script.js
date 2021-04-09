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
    var content = document.getElementById('basket-items');
    var item = document.getElementById(`item-${id}-name`);
    var image = document.getElementById(`item-${id}-image`).innerHTML;
    var price = document.getElementById(`item-${id}-price`).innerHTML;
    var qtd = document.getElementById(`item-${id}-qtd`).innerHTML;
    var name = item.getElementsByTagName("H3")[0].innerHTML;
    console.log(name)
    if (content.innerHTML === "Nenhum item adicionado!"){
      content.innerHTML = "";
      document.getElementById("btn-chkout").disabled = false;
    }
    var item = document.getElementById(`item-${id}-name`).innerHTML
    content.innerHTML += `<div id='basket-item-${id}'>${image} <div id='item-${id}-descr'><span>${name} </span> <span>qtd. <small>${qtd}:<br /> R$ </small> ${(price*qtd).toFixed(2)}</span></div></div>`
    showBasket();
    setTimeout(function(){showBasket();}, 5000);
  }
}
