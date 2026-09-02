let nome = "";
let menu_aberto = false
let escuro = false
function confirmar() {
    nome = document.getElementById('nome').value.trim();
    senha = document.getElementById('senha').value.trim();
    if (nome.length > 0) {
        nome = nome.charAt(0).toUpperCase() + nome.slice(1).toLowerCase();
        document.querySelector('div.modal').style.display = 'none';
        document.body.style.overflow = "auto";
        document.getElementById('msg').innerHTML = `Olá <strong>${nome}</strong>, me chamo Kauã, criei esse site para mostrar alguns esboços e também tentar reunir o que já aprendi e juntar nessa página, claro, não tem tudo, mas acredito que a grande maioria esteja aqui, aqui você também pode me conhecer um pouco, e vou tentar atualizá-la semanalmente.`
        document.querySelector("#logado").innerHTML = `<button onclick="abrir_janela()"><img src="imagens/user.png" width="30px" alt="">Seja bem vindo(a) ${nome}</button>`
    }
    }
function abrir_janela() {
    if (nome.length >= 1) {
        document.querySelector('div#logout').style.display = 'flex';
        document.body.style.overflow = "hidden";
    }
    else {
        document.querySelector('div#login').style.display = 'flex';
        document.body.style.overflow = "hidden";
    }
}
function fechar_janela() {
    document.getElementById('login').style.display = 'none'
    document.getElementById('logout').style.display = 'none'
    document.body.style.overflow = 'auto';
}
function nao() {
    document.querySelector('div#logout').style.display = 'none';
    document.body.style.overflow = "auto";
}
function sim() {
    nome = "";
    senha = "";
    document.getElementById("nome").value = "";
    document.getElementById("senha").value = "";
    document.getElementById("msg").innerHTML =`Olá, me chamo Kauã, criei esse site para mostrar alguns esboços e também tentar reunir o que já aprendi e juntar nessa página, claro, não tem tudo, mas acredito que a grande maioria esteja aqui, aqui você também pode me conhecer um pouco, e vou tentar atualizá-la semanalmente.`
    document.querySelector("#logout").style.display = "none";
    document.body.style.overflow = "auto";
    document.querySelector("#logado").innerHTML = `<button onclick="abrir_janela()"><img src="imagens/user.png" width="30px" alt=""> Login</button>`
}
function modo() {
    if (escuro) {
        document.documentElement.style.setProperty('--wallpaper','url(imagens/vice-city.jpg) center/ cover no-repeat fixed')
        document.documentElement.style.setProperty('--background_header','linear-gradient(to right, #0e2b6b,#631e97)')
        document.documentElement.style.setProperty('--background_hoverbutton2','#872db4')
        document.documentElement.style.setProperty('--background_main','rgba(6, 4, 40, 0.87)')
        escuro = false
    }
    else{
        document.documentElement.style.setProperty('--wallpaper','url(imagens/vice-city-escuro1.jpg) center/ cover no-repeat fixed')
        document.documentElement.style.setProperty('--background_header','linear-gradient(18deg, #0F0C38, #100d51 )')
        document.documentElement.style.setProperty('--background_hoverbutton2','#2d38b4')
        document.documentElement.style.setProperty('--background_main','#050721c6')
        escuro = true
    }
    }
function abrir_menu() {
    if (menu_aberto) {
        document.getElementById('barra_vertical').style.borderRadius = '0px 0px 3px 3px'
        document.getElementById('menu').style.display = 'none'
        menu_aberto = false
    }
    else{
        document.getElementById('barra_vertical').style.borderRadius = '0px 0px 0px 3px'
        document.getElementById('menu').style.display = 'block'
        menu_aberto = true
    }
}
document.getElementById('opçao').addEventListener('click', () => {
    document.getElementById('menu').classlist.toggle('fechada');
});
//var n1 = Number.parseFloat(window.prompt('Digite um número'))
//var n2 = Number.parseFloat(window.prompt('Digite um número'))
//var s = n1 + n2
//window.alert(`A soma dos dois valores é: ${s.toFixed(2)}`)