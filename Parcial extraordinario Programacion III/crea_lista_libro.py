def create_book_dict() -> dict:
    book_dict = {
        "titulo": "",
        "autor": "",
        "año": 0
    }
    book_dict["género"] = ""
    return book_dict

book = create_book_dict()
book["titulo"] = "To Kill a Mockingbird"
book["autor"] = "Harper Lee"
book["año"] = 1960
book["género"] = "Fiction"

print(book)