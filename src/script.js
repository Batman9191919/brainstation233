function searchBooks() {
  const searchInput = document.getElementById('searchInput').value.toLowerCase().trim();
  const cards = document.querySelectorAll('.book-card');

  cards.forEach(card => {
    const bookTitleElement = card.querySelector('.book-title');
    const bookAuthorElement = card.querySelector('.book-author');

    // Get the book title and author, handle missing elements
    const bookTitle = bookTitleElement ? bookTitleElement.textContent.toLowerCase().trim() : "";
    const bookAuthor = bookAuthorElement ? bookAuthorElement.textContent.toLowerCase().trim() : "";

    // Show or hide books based on the search query
    if (bookTitle.includes(searchInput) || bookAuthor.includes(searchInput)) {
      card.style.display = ''; // Show the book
    } else {
      card.style.display = 'none'; // Hide the book
    }
  });
}


function typeWriterEffect(elementId, text, speed) {
  let i = 0;
  const element = document.getElementById(elementId);
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  type();
}

// Run the typewriter effect when the page loads
window.onload = function () {
  typeWriterEffect("typewriter-text", "Where Books Come to Life", 150); // Adjust speed as needed
};

