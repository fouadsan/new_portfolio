const contactUrl = window.location.href + 'contact';

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendEmailForm = document.getElementById('send-email-form')

const nameInput = document.getElementById('name-input')
const emailInput = document.getElementById('email-input')
const subjectInput = document.getElementById('subject-input')
const messageInput = document.getElementById('message-input')

const sendBox = document.getElementById('send-box')
const spinnerBox = document.getElementById('spinner-box')

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const sendEmail = () => {
    $.ajax({
        type: 'POST',
        url: contactUrl,
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'name': nameInput.value,
            'email': emailInput.value,
            'subject': subjectInput.value,
            'message': messageInput.value,
        },
        dataType: 'json',
        beforeSend: function () {
            sendBox.classList.add('not-visible')
            spinnerBox.classList.remove('not-visible')
        },
        success: function (response) {
            setTimeout(() => {
                spinnerBox.classList.add('not-visible')
                sendBox.classList.remove('not-visible')

                nameInput.value = ""
                emailInput.value = ""
                subjectInput.value = ""
                messageInput.value = ""

            }, 150);
            console.log(response.msg)
            handleAlerts('center', 'Email Status', response.msg, response.type, response.confirmation)
        },
        error: function (error) {
            handleAlerts('center', 'Error!', 'Oops...something went wrong', 'error', true)
        }
    })
}

sendEmailForm.addEventListener('submit', e => {
    e.preventDefault()
    sendEmail()
})
