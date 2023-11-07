// logout.js

function confirmLogout() {
    var result = confirm("Are you sure you want to logout?");
    if (result) {
        // Redirect to the logout page or perform logout action
        window.location.href = "{% url 'library-index' %}"; 
    } else {
        // User chose not to logout, do nothing
    }
}
