borrowed_books = ["book A", "book B", "book C"]

print("Initial borrowed books:", borrowed_books)

borrowed_books.append("Book D")
print("after borrow book:", borrowed_books)

borrowed_books.extend(["book E", "book F"])
print("after another borrow books:", borrowed_books)

borrowed_books.insert(1, "Reference Book")
print("After inserting reference book:", borrowed_books)

print("\nFinal Borrowed Books List:", borrowed_books)
