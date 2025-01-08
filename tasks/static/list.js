let recording = false;
micBtn.onclick = (e)=>{
    e.preventDefault();
    record();
}
logoutBtn.onclick = ()=>{
    fetch(Urls['logout'](), {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken.value 
        }

    }).then(()=>{
        location.assign(Urls['home']())
    })
}

function record() {
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        if (!recording) {
            micBtn.classList.replace("btn-outline-danger", "btn-danger");

            recording = true;
        
            const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.interimResults = false;

            recognition.onresult = (event) => {
                userPrompt = event.results[event.resultIndex][0].transcript;
                micBtn.classList.replace("btn-danger", "btn-outline-danger");
                recording = false;
                submitCommand(userPrompt);
            };

            recognition.onerror = (event) => {
                if (event.error == "no-speech") {
                    micBtn.classList.replace("btn-danger", "btn-outline-danger");
                    console.log("Error: ", event.error)
                    recording = false; 
                } else {
                    console.error('Speech recognition error:', event.error);
                    recording = false;
                }
            };

            recognition.start();
        }
        
    } else {
        console.log('Speech recognition not supported in this browser.');
    }
}
function submitCommand(userPrompt){
    command.value = userPrompt;
    commandForm.submit(userPrompt)
}