// Function to toggle visibility of the reviews and ratings section
function toggleReviewsSection() {
	var reviewsSection = document.querySelector('.reviews-section');
	reviewsSection.classList.toggle('show');
}

// Function to handle form submission
document.getElementById('reviewForm').addEventListener('submit', function(event) {
	event.preventDefault(); // Prevent default form submission
	
	// Retrieve review and rating values
	var review = document.getElementById('review').value;
	var rating = document.getElementById('rating').value;
	
	// You can now send this data to your backend using AJAX or any other method
	
	// For now, let's just display the submitted review
	var reviewsContainer = document.getElementById('reviewsContainer');
	var reviewItem = document.createElement('div');
	reviewItem.innerHTML = '<p><strong>Rating:</strong> ' + rating + '</p><p><strong>Review:</strong> ' + review + '</p>';
	reviewsContainer.appendChild(reviewItem);
	
	// Clear form fields after submission
	document.getElementById('review').value = '';
	document.getElementById('rating').value = '1';
});

// Function to retrieve existing reviews and display them
function displayExistingReviews() {
	// You can fetch existing reviews from your backend here
	// For now, let's just simulate some existing reviews
	var existingReviews = [
		
		// Add more existing reviews as needed
	];

	// Display each existing review
	var reviewsContainer = document.getElementById('reviewsContainer');
	existingReviews.forEach(function(reviewData) {
		var reviewItem = document.createElement('div');
		reviewItem.innerHTML = '<p><strong>Rating:</strong> ' + reviewData.rating + '</p><p><strong>Review:</strong> ' + reviewData.review + '</p>';
		reviewsContainer.appendChild(reviewItem);
	});
}

// Call the function to display existing reviews when the page loads
displayExistingReviews();