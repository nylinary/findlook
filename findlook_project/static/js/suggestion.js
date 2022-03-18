function createPItem(text) {
    let p = document.createElement('p')
    p.setAttribute('class', 'm-auto ta-center');
    p.textContent = text;
    return p
}
document.addEventListener("DOMContentLoaded", function(){
    let btn = document.querySelector("input[type=submit]");
    btn.addEventListener("click", async function(e){
        e.preventDefault();
        let response = await fetch("/suggestion", {
            method: "POST",
            body: new FormData(document.querySelector("form"))
        })
        let response_json = await response.json();
        let container = document.getElementById("sg-Wrapper");
        if (response_json.success){
            container.innerHTML='';
            container.appendChild(createPItem("Ваш отзыв отправлен!"));
            document.addEventListener("click", function(){
                window.open("/", "_self");
            })
        }
        else {
            let warning = document.getElementById("WarningMessage");
            warning.style.color = "red";
            warning.textContent = "Некорректные данные!";
        }

    })
})