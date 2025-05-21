document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('user-data-form');
    const insightData = document.getElementById('insight-data');

    // // Fetch and display insights when the page loads
    // fetch('/analytics')
    //     .then(response => response.json())
    //     .then(insights => {
    //         displayInsights(insights);
    //     })
    //     .catch(error => {
    //         insightData.textContent = 'Error fetching insights.';
    //     });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/api/submit-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            displayInsights(data.insights);
        })
        .catch(error => {
            insightData.textContent = 'Error fetching insights.';
        });
    });

    function displayInsights(insights) {
        if (!insights) {
            insightData.textContent = 'No user data available.';
            return;
        }
        let html = '';
        for (const [key, value] of Object.entries(insights)) {
            html += `${key}: ${value}<br>`;
        }
        insightData.innerHTML = html;
    }
});