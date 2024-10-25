const inputs = document.querySelectorAll('.input');
const button = document.querySelector('.signup-button');

const handleFocus = ({ target }) =>{
    const span = target.previousElementSibling;
    span.classList.add('span-active');
}

const handleFocusOut = ({ target }) =>{
    if (target.value == ''){
        const span = target.previousElementSibling;
        span.classList.remove('span-active');
    }
}

const handleChange = () => {
    console.log('handleChange')
    const [username, password] = inputs;
    const isUsernameValid = username.value.length >= 3;
    const isPasswordValid = password.value.length >= 6;
    if (isUsernameValid && isPasswordValid) {
        button.removeAttribute('disabled');
    } else {
        button.setAttribute('disabled', '');
    }
}

inputs.forEach((input) =>
    input.addEventListener('focus', handleFocus)
);
inputs.forEach((input) =>
    input.addEventListener('focusout', handleFocusOut)
);

inputs.forEach((input) =>
    input.addEventListener('input', handleChange)
);

