const div = document.querySelector("#menssagem")

div.addEventListener("load", ()=>{
    setTimeout(() => {
        div.style.display = 'none';
     },3000);
})