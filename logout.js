// logout.js

function confirmLogout() {
    var result = confirm("Are you sure you want to logout?");
    if (result) {
        // Redirect to the logout page or perform logout action
        window.location.href = "/landingpage/index.html"; // Replace with your actual logout page URL
    } else {
        // User chose not to logout, do nothing
    }
}
