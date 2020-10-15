const addButtons = document.querySelectorAll('[btn_add]');
addButtons.forEach(button => {
    button.addEventListener("click", () => {

        form = document.getElementById('MyForm');
        newform = form.cloneNode(true);
        form.parentNode.appendChild(newform);
    })

})

