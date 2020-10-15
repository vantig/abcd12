var doc=document,elem=doc.createElement("div")
const addButtons = document.querySelectorAll('[btn_add]');
addButtons.forEach(button => {
    button.addEventListener("click", () => {

        content=doc.createTextNode(content);
        elem.appendChild(content)

        }

    })
