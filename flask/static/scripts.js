function showDiv(tag){
  var el = document.getElementById(`dv-${tag}`)
  el.style.display = "block"
  console.log(el.parentElement)
  for(child in el.parentElement.children){
    var id = el.parentElement.children[child].id
    console.log("SHOW",id)
    if(id !== `dv-${tag}` & id !== undefined){
      hideDiv(id)
    }
  }
}
function hideDiv(id){
  console.log("HIDE",id)
  document.getElementById(id).style.display = "none"
}
function showRawCode(){
  document.getElementById("raw-code").style.display="block";
  document.getElementById("summary").style.display="none";
  document.getElementById("content").style.display="none";
  document.getElementById("cont-words").style.display="none";
}
function showSummary(){
  document.getElementById("raw-code").style.display="none";
  document.getElementById("summary").style.display="block";
  document.getElementById("content").style.display="block";
  document.getElementById("cont-words").style.display="none";
}
function showWords(){
  document.getElementById("raw-code").style.display="none";
  document.getElementById("summary").style.display="none";
  document.getElementById("content").style.display="none";
  document.getElementById("cont-words").style.display="block";
}
