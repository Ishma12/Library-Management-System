// profile.js

// Function to show/hide the user dropdown menu
function toggleUserDropdown() {
    console.log("toggleUserDropdown called");
    var dropdown = document.getElementById('user-dropdown');
    if (dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
    } else {
        dropdown.style.display = 'block';
    }
}

// Add an event listener for the user avatar click
document.getElementById('user-avatar').addEventListener('click', toggleUserDropdown);
