var trigger = false
function button() {
    const button = document.getElementById("button1")
    if (trigger == true) {
        button.style.borderStyle = "dotted";
        trigger = false;
        } else {
            button.style.borderStyle = "solid";
            trigger = true
        }
}