
// var trigger = false
// function button() {
//     const button = document.getElementById("button1")
//     if (trigger == true) {
//         button.style.borderStyle = "dotted";
//         trigger = false;
//         } else {
//             button.style.borderStyle = "solid";
//             trigger = true
//         }
// }

var timer = 1000
setInterval(() => {
    timer = timer/2
    document.getElementById("button").innerHTML = timer+"ms"
}, timer);