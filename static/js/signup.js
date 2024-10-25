setTimeout(function() {
    var image = document.querySelector('.anim-image');
    var formContainer = document.querySelector('.form-container');

    if (image && formContainer) {
        image.style.height = "100vh";

        formContainer.classList.add('show');
    }
}, 1000);

const inputs = document.querySelectorAll('.input');
const button = document.querySelector('.signup-button');

const handleFocus = ({ target }) =>{
    const span = target.previousElementSibling;
    span.classList.add('span-active');
}

const handleFocusOut = ({ target }) =>{
    if (target.value === ''){
        const span = target.previousElementSibling;
        span.classList.remove('span-active');
    }
}

const handleChange = () => {
    console.log('handleChange')
    const [username, email, password, confirmPassword] = inputs;
    const isUsernameValid = username.value.length >= 3;
    const isPasswordValid = password.value.length >= 6;
    const isValidEmail = (email) => {
        return email.includes('@');
    }
    const isEmailValid = isValidEmail(email.value);
    const passwordsMatch = password.value === confirmPassword.value;
    if (isUsernameValid && isPasswordValid && isEmailValid && passwordsMatch) {
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