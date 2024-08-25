import React, { useState, useEffect } from 'react';

const BookLibrary = () => {
  const [books, setBooks] = useState([]);
  const [newBook, setNewBook] = useState({ title: '', author: '' });

  useEffect(() => {
    // Загрузка книг при монтировании компонента
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/books/');
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();
      setBooks(data);
    } catch (error) {
      console.error('Error fetching books:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewBook({ ...newBook, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/books/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newBook),
      });
      if (!response.ok) throw new Error('Failed to add book');
      await fetchBooks(); // Обновляем список книг
      setNewBook({ title: '', author: '' }); // Очищаем форму
    } catch (error) {
      console.error('Error adding book:', error);
    }
  };

  return (
    <div>
      <h1>Book Library</h1>
      
      <h2>Add New Book</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          value={newBook.title}
          onChange={handleInputChange}
          placeholder="Book Title"
          required
        />
        <input
          type="text"
          name="author"
          value={newBook.author}
          onChange={handleInputChange}
          placeholder="Author Name"
          required
        />
        <button type="submit">Add Book</button>
      </form>

      <h2>Book List</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>{book.title} by {book.author}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookLibrary;