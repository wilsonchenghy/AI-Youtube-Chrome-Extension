document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('button').addEventListener('click', function() {
        generateSummary()
    })
})

function generateSummary() {

    let inputURL = document.querySelector('input').value

    document.querySelector('.loading').style.display = 'flex';

    fetch(`http://localhost:8000/summary?inputURL=${inputURL}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let summaryElement = document.getElementById('summary')
            summaryElement.innerHTML = data.summary
            console.log(document.body.style.height )
            document.body.style.height = summaryElement.offsetHeight + 'px'

            let wrapper = document.querySelector('.summary-wrapper');

            if (data.summary) {
                wrapper.style.display = 'flex';
                wrapper.style.height = summaryElement.offsetHeight + 'px';
            } else {
                wrapper.style.display = 'none';
            }

            document.querySelector('.loading').style.display = 'none';
        })
        .catch(error => {
            console.error('Error: ', error)
            document.querySelector('.loading').style.display = 'none';
        })

    console.log("Successful")
}