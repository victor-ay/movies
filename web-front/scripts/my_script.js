
console.log("Inside my script")

function showAlert(){
    window.alert("loaded")
}

function changeHeader() {
    elem = document.getElementById('my-header')
    elem.style.color = 'red'
}

function switchColor(className) {
    elements = document.getElementsByClassName(className)
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index]
        let currClass = null
        if (element.classList.contains('btn-primary')) {
            currClass = 'btn-primary'
            newClass = 'btn-danger'
        }else{
            currClass = 'btn-danger'
            newClass = 'btn-primary'
        }
        element.classList.replace(currClass, newClass)
    }
}

function loadCompletedHandler() {
    window.getElementById("hello_btn").onclick = () => {
        console.log("Pressed hello_btn")
        document.getElementById("my-p").innerHTML = `${date.getDate()}-${date.getMonth()+1}`
    }
}