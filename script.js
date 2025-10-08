async function predict() {
  const f1 = parseFloat(document.getElementById('f1').value) || 0;
  const f2 = parseFloat(document.getElementById('f2').value) || 0;
  const f3 = parseFloat(document.getElementById('f3').value) || 0;
  const f4 = parseFloat(document.getElementById('f4').value) || 0;

  const response = await fetch('/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({features: [f1, f2, f3, f4]})
  });

  const data = await response.json();
  document.getElementById('result').innerHTML = 
    `<b>Prediction:</b> ${data.prediction}<br>${data.details}`;
}
