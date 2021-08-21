const modalBtns = [...document.getElementsByClassName("modal-button")]
const strtBtn = document.getElementById("start-button")
const modalBody = document.getElementById("model-body-confirm")

modalBtns.forEach(modalBtn=> modalBtn.addEventListener("click", ()=>{
    const pk = modalBtn.getAttribute("data-pk")
    const name = modalBtn.getAttribute("data-quiz")
    const questions = modalBtn.getAttribute("data-questions")
    const difficulty = modalBtn.getAttribute("data-difficulty")
    const time = modalBtn.getAttribute("data-time")
    const scoreToPass = modalBtn.getAttribute("data-pass")

    modalBody.innerHTML = `
        <div>Are you sure to take exam of "<b>${name}</b>"?</div>
        <ul>
            <li>Difficulty: ${difficulty}</li>
            <li>number of questions: ${questions}</li>
            <li>score to pass: ${scoreToPass}</li>
            <li>time: ${time}</li>
        <</ul>
    `
    strtBtn.addEventListener("click", ()=>{
        window.location.href = url +pk
    })
}))