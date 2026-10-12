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


class Peschool(Book):
    def __init__(self, book_title, author, number_of_pages, ibsn, reserved,
                     subject, class_school, task):
            super().__init__(book_title, author, number_of_pages, ibsn, reserved)

            self.subject = subject
            self.class_school = class_school
            self.task = task

    def check_reserved(self):
        if self.reserved:
            return (f'Название: {self.book_title}, Автор: {self.author}, старниц: {self.number_of_pages}, '
                f'предмет: {self.subject}, класс: {self.class_school}, зарезервирована')
        else:
            return (f'Название: {self.book_title}, Автор: {self.author}, старниц: {self.number_of_pages}, '
                f'предмет: {self.subject}')


a = Peschool('Алгебра', 'Иванов', 250, 123456789, True, 'Математика', 7, True)

print(a.check_reserved())



