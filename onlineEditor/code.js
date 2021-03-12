const textArea = document.getElementById("textArea");
const loadInput = document.getElementById("loadInput");
const download = document.getElementById("download");   
const runButton = document.getElementById("runbtn");
const testButton = document.getElementById("testbtn");
const saveButton = document.getElementById("savebtn");
const loadButton = document.getElementById("loadbtn");
const clearButton = document.getElementById("clearbtn");
const consoleText = document.getElementById("consoleOutput");

const codeSkeleton = 
`from helpers import subsets, choose

def perfect_matchings(graph):
    pass

def hamiltonian_cycles(graph):
    pass`

const editor = setupCodeMirror();

function setupCodeMirror() {
    const config = {
        mode: "python",
        theme: "darcula",
        lineNumbers: true,
        autoCloseBrackets: true,
        matchBrackets: true 
    };

    textArea.innerHTML = codeSkeleton;
    return CodeMirror.fromTextArea(textArea, config);
}

pypyjs.stdout = printToConsole;
pypyjs.stderr = printToConsole;
pypyjs.ready().then(function() {
     // Show loading before this
});

runButton.addEventListener("click", e => runCode(editor.getValue()));
testButton.addEventListener("click", e => testCode(editor.getValue()));
saveButton.addEventListener("click", e => saveFile());
loadButton.addEventListener("click", e => loadInput.click());
clearButton.addEventListener("click", e => clearConsole());
loadInput.addEventListener("change", e => loadCodeFromFile(e.target.files[0]));

function runCode(code) { 
    pypyjs.exec(editor.getValue()).then(
        () => {}, 
        err => {
            pypyjs.stderr("ERROR: "+err.name+": "+err.message+"!\n"); 
            pypyjs.stderr(err.trace);
        });
    reset();
}

function testCode() {
    // TODO implement this
    // execute user code
    // invoke test script
}

// TODO make this more efficient
function printToConsole(str) {
    consoleText.innerText += str;
}

function clearConsole() {
    consoleText.innerText = "";
}

// Remove user defined variables and functions from interpreter
function reset() {
    pypyjs.exec(
        "for var in dir():\n" +
        "   if not var.startswith('__'):\n" + 
        "       del globals()[var]"
    );
}

function saveFile() {
    var file = new Blob([editor.getValue()]);
    download.download = "assignment5.py";
    download.href = window.URL.createObjectURL(file);
    download.click();
}

function loadCodeFromFile(file) {
    let reader = new FileReader();
    reader.onload = e => {
        let str = e.target.result;
        editor.setValue(str);
    }
    reader.readAsText(file);
}