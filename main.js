searchForm = document.querySelector('.search-form');
document.querySelector('#search-btn').onclick = ()=>{
        searchForm.classList.toggle('active');
}

let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () =>{
        loginForm.classList.toggle('active');
}

let search = document.querySelector('.search-box');

document.querySelector('#search-icon').onclick = () => {
        search.classList.toggle('active');
}
let header = document.querySelector('header');

window.addEventListener('scroll' ), () => {
        header.classList.toggle('shadow', window.scrollY > 0);
}