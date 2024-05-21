# Bookstore Inventory Management System

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
    ```bash
    git clone https://github.com/SklCandy420/Bookstore.git
    cd bookstore
    ```

2. Build and start the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```

3. Access the API documentation at `http://localhost:8000/docs`.

### API Endpoints

#### Books
- `GET /books/`: Retrieve a list of all books.
- `GET /books/{book_id}`: Retrieve details of a specific book by its ID.
- `POST /books/`: Create a new book.
- `PUT /books/{book_id}`: Update details of a specific book by its ID.
- `DELETE /books/{book_id}`: Delete a specific book by its ID.

#### Authors
- `GET /authors/`: Retrieve a list of all authors.
- `GET /authors/{author_id}`: Retrieve details of a specific author by their ID.
- `POST /authors/`: Create a new author.
- `PUT /authors/{author_id}`: Update details of a specific author by their ID.
- `DELETE /authors/{author_id}`: Delete a specific author by their ID.

#### Genres
- `GET /genres/`: Retrieve a list of all genres.
- `GET /genres/{genre_id}`: Retrieve details of a specific genre by its ID.
- `POST /genres/`: Create a new genre.
- `PUT /genres/{genre_id}`: Update details of a specific genre by its ID.
- `DELETE /genres/{genre_id}`: Delete a specific genre by its ID.

### Testing

1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:
    ```bash
    pytest
    ```

### Authentication

1. Register a user and obtain a JWT token:
    ```bash
    POST /auth/token
    ```

2. Use the token to access restricted endpoints:
    ```bash
    Authorization: Bearer <token>
    ```
