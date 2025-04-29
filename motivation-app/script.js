function updateQuote(mood) {
    const quoteBox = document.getElementById('quote');
    quoteBox.textContent = "Loading...";

    console.log("Fetching quote for mood:", mood);

    fetch(`http://127.0.0.1:5000/get_quote/${mood}`)  
        .then(function(response) {
            console.log("Response status:", response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(function(data) {
            console.log("Quote data received:", data);
            quoteBox.textContent = data.quote;
        })
        .catch(function(error) {
            console.error("Error fetching quote:", error);
            quoteBox.textContent = "Oops! Could not fetch quote. Try again.";
        });
       
        
        
}
