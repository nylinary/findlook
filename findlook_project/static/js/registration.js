function createPItem(text) {
    let p = document.createElement('p')
    p.textContent = text;
    return p
}
document.addEventListener("DOMContentLoaded", function(){
    let btn = document.querySelector("input[type=submit]");
    btn.addEventListener("click", async function(e){
        e.preventDefault();
        let response = await fetch("/main/register/", {
            method: "POST",
            body: new FormData(document.querySelector("form"))
        })
        let response_json = await response.json();
        let container = document.querySelector("div[class=container]");
        if (response_json.error){
            let warning = document.querySelector("p[id=warning]");
            warning.style.color = "red";
            warning.textContent = "Некорректные данные!";            
        }
        else {
            container.innerHTML='';
            container.appendChild(createPItem("Вы успешно прошли регистрацию."));
            document.addEventListener("click", function(){
                window.open("/", "_self");
            })
        }

    })
})