const form = document.querySelector('#chat-form');
const chatbox = document.querySelector('.chatbox');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const userInput = document.querySelector('#user-input').value;
  if (userInput) {
    displayMessage(userInput, 'user');
    sendRequest(userInput);
    document.querySelector('#user-input').value = '';
  }
});

function displayMessage(message, sender) {
  const div = document.createElement('div');
  div.classList.add(sender);
  div.innerHTML = message;
  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function sendRequest(message) {
  fetch("")
    .then(response => response.json())
    .then(data => {
      const response = data.response;
      displayMessage(response, 'bot');
    })
    .catch(error => console.error(error));
}
