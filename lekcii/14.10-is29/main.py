import etc
import path_to_market
import path_from_market
import pokupka

spisok = []
etc.read_file(spisok,'spisok.conf')

path = []
etc.read_file(path,'path.conf')

path_to_market.path_to_market(path)
print()
pokupka.pokupka(spisok)
print()
path_from_market.path_from_market(path)


