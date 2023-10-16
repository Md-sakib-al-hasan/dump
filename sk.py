class StarCinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall_obj):
        self._hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

    def view_show_list(self):
        return self._show_list

    
    def book_seats(self, show_id, seats_to_book):
        
