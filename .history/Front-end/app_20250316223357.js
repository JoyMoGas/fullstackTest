async function fetchBooks() {
  try {
      const response = await fetch('http://127.0.0.1:5000/api/get');
      if (!response.ok) throw new Error('Error al obtener datos');
      
      const books = await response.json();
      const bookList = document.getElementById('book-list');

      books.forEach(book => {
          const bookCard = document.createElement('div');
          bookCard.classList.add('card');
          bookCard.innerHTML = `
              <h2>${book.title}</h2>
              <p><strong>Autor:</strong> ${book.author}</p>
              <img src="${book.image}" alt="${book.title}">
          `;
          bookList.appendChild(bookCard);
      });
  } catch (error) {
      console.error('Error al obtener los libros:', error);
  }
}

fetchBooks();
