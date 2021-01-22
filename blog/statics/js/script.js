function addBootstrapClass(){

    const fields = [
        document.getElementById("id_nome"),
        document.getElementById("id_marca"),
        document.getElementById("id_descricao"),
        document.getElementById("id_quantidade"),
        document.getElementById("id_preco"),
        document.getElementById("id_usuario"),
        document.getElementById("id_status"),
        document.getElementById("id_username"),
        document.getElementById("id_password"),
        document.getElementById("id_first_name"),
        document.getElementById("id_last_name"),
        document.getElementById("id_email"),
        document.getElementById("id_password1"),
        document.getElementById("id_password2")
    ]

    for(let i = 0; i < fields.length; i++){
        if(fields[i] !== null) {
            console.log(fields[i].classList)
            if (fields[i].classList) fields[i].classList.add('form-control')
            else fields[i].className += 'form-control'
        }
    }
}
addBootstrapClass()

