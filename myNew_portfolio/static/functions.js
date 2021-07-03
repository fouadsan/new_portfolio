const date = new Date().getFullYear();
let copyrightEl = document.getElementById('copyright-el')
function getCopyDate() {
    copyrightEl.innerHTML = `&copy; Copyright <strong><span>${date}</span></strong>. All Rights Reserved`
}

getCopyDate()


const handleAlerts = (position, title, msg, type, boolConfirmBtn, timer) => {
    Swal.fire({
        position: position,
        title: title,
        text: msg,
        icon: type,
        showConfirmButton: boolConfirmBtn,
        timer: timer,
        confirmButtonText: 'Ok'
    })
}
