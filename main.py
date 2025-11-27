# main.py

class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None
class BookList:
    def __init__(self):
        self.head = None

    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"✅ Book '{title}' added successfully.")

    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp and temp.book_id != book_id:
            prev = temp
            temp = temp.next

        if not temp:
            print("❌ Book not found.")
            return

        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next

        print(f"🗑️ Book '{temp.title}' deleted successfully.")

    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"\n📘 Book Found:\nID: {temp.book_id}\nTitle: {temp.title}\nAuthor: {temp.author}\nStatus: {temp.status}")
                return temp
            temp = temp.next
        print("❌ Book not found.")
        return None

    def displayBooks(self):
        if not self.head:
            print("📚 No books available in the library.")
            return
        print("\n📚 Current Books in Library:")
        temp = self.head
        while temp:
            print(f"ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {temp.status}")
            temp = temp.next
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        if self.isEmpty():
            print("🕓 No transactions yet.")
            return
        print("\n🔁 Recent Transactions:")
        for t in reversed(self.stack):
            print(t)
class TransactionSystem:
    def __init__(self):
        self.books = BookList()
        self.transactions = Stack()

    def issueBook(self, book_id):
        book = self.books.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transactions.push(("issue", book_id))
            print(f"📕 Book '{book.title}' has been issued.")
        else:
            print("❌ Book not available or already issued.")

    def returnBook(self, book_id):
        book = self.books.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transactions.push(("return", book_id))
            print(f"📗 Book '{book.title}' has been returned.")
        else:
            print("❌ Book not issued or not found.")

    def undoTransaction(self):
        if self.transactions.isEmpty():
            print("❌ No transaction to undo.")
            return

        action, book_id = self.transactions.pop()
        book = self.books.searchBook(book_id)
        if not book:
            print("❌ Book not found for undo operation.")
            return

        if action == "issue":
            book.status = "Available"
            print(f"↩️ Undo successful: Book '{book.title}' marked as Available again.")
        elif action == "return":
            book.status = "Issued"
            print(f"↩️ Undo successful: Book '{book.title}' marked as Issued again.")

    def viewTransactions(self):
        self.transactions.display()
def main():
    system = TransactionSystem()

    while True:
        print("\n=== 📚 Library Book Management System ===")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bid = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            system.books.insertBook(bid, title, author)

        elif choice == '2':
            bid = int(input("Enter Book ID to delete: "))
            system.books.deleteBook(bid)

        elif choice == '3':
            bid = int(input("Enter Book ID to search: "))
            system.books.searchBook(bid)

        elif choice == '4':
            system.books.displayBooks()

        elif choice == '5':
            bid = int(input("Enter Book ID to issue: "))
            system.issueBook(bid)

        elif choice == '6':
            bid = int(input("Enter Book ID to return: "))
            system.returnBook(bid)

        elif choice == '7':
            system.undoTransaction()

        elif choice == '8':
            system.viewTransactions()

        elif choice == '9':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
