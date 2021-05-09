import socket

from planlekcji.utils import BaseLinks
from planlekcji.models import DataRooms


def host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip


if __name__ == '__main__':
    dr = DataRooms.DataRoom(1, [DataRooms.OneCell('Adams', '1PTN', 'Matematyka'),
                                DataRooms.OneCell('Adams', '2PTN', 'Bazy danych')])
    print(dr)
    # bl = BaseLinks.BaseLinks()              #DZIAŁA BARDZO DOBRZE
    # classes_links = bl.classes_links()      #Też działa świetnie :)
    # url = "http://plan.ckziu-elektryk.pl/plany/n76.html"
    # html = requests.get(url).text
    # print(html)
