
console.log("Script Running...")

// btn class clicked event handling
document.querySelector(".btn")?.addEventListener('click', async function () {
    console.log("Clicked");
    let key = document.getElementById('key').value;
    let country = document.getElementById("con").value;

    try {
        const csrftoken = getCookie('csrftoken'); 
        
        const response = await fetch('/generate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken, 
            },
            body: `key=${encodeURIComponent(key)}&con=${encodeURIComponent(country)}`,
        });

        if (response.ok) {
            const result = await response.json();
            console.log("Result: ", result);
        } else {
            console.error("Error: ", response.statusText);
        }
    } catch (error) {
        console.error("Error: ", error);
    }
});

// Function to get CSRF token from cookie
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    
    return null;
}
