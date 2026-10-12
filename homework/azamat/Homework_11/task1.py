class Book:
    page_material = 'paper'
    text_availability = True

    def __init__(self, book_title, author, number_of_pages, ibsn, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ibsn = ibsn
        self.reserved = reserved

    def check_reserved(self):
        if self.reserved:
            return (f'Название: {self.book_title}, Автор: {self.author}, старниц: {self.number_of_pages}, '
                    f'материал: {Book.page_material}, зарезервирована')
        else:
            return (f'Название: {self.book_title}, Автор: {self.author}, старниц: {self.number_of_pages}, '
                    f'материал: {Book.page_material}')


a = Book('aaa', 'bbb', 110, 102311234, False)
b = Book('sss', 'ddd', 234, 123041223, True)
c = Book('ggg', 'hhh', 432, 456464353, False)
d = Book('www', 'eee', 90, 239928283, False)
r = Book('rrr', 'ttt', 324, 2134123214, False)

print(a.check_reserved())
print(b.check_reserved())
print(c.check_reserved())
print(d.check_reserved())
print(r.check_reserved())
