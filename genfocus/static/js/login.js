document.addEventListener('DOMContentLoaded', function(){
    const inputs = document.querySelectorAll('.input');
    const button = document.querySelector('.login-button');

    if (inputs.length > 0 && button) {
        inputs.forEach((input) => input.addEventListener('focus', handleFocus));
        inputs.forEach((input) => input.addEventListener('focusout', handleFocusOut));
        inputs.forEach((input) => input.addEventListener('input', handleChange));
    }
    function handleFocus({target}){
        const span = target.previousElementSibling;
        span.classList.add('span-active');
    }

    function handleFocusOut({ target }) {
        if (target.value === ''){
            const span = target.previousElementSibling;
            span.classList.remove('span-active');
        }
    }

    function handleChange() {
        const [username, password] = inputs;
        const isUsernameValid = username.value.length >= 3;
        const isPasswordValid = password.value.length >= 6;
        if (isUsernameValid && isPasswordValid) {
            button.removeAttribute('disabled');
        } else {
            button.setAttribute('disabled', '');
        }
    }
})

