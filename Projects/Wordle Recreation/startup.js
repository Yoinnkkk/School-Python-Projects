const slist = ["main.js", "intro.js"]
// File loads all script files for cleaner html look
function loadScripts(path) {
    var header = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = "text/javascript";
    script.src = path
    header.appendChild(script);
}
i = 0
while (i < slist.length) {
    loadScripts(slist[i]);
    i++
    if (slist[i] == 'gameData.js') {
        while (gameData == undefined || gameData == null) {}
    }
}