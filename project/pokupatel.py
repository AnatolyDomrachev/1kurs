from roditel import Roditel

class Pokupatel(Roditel):
    path = []

P = Pokupatel('spisok.conf')
P.read_file(P.path, 'path.confi')
P.print_spisok()

