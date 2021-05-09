import socket

from planlekcji.utils import BaseLinks


def host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip


if __name__ == '__main__':
    bl = BaseLinks.BaseLinks()              #DZIAŁA BARDZO DOBRZE
    classes_links = bl.classes_links()      #Też działa świetnie :)
    # url = "http://plan.ckziu-elektryk.pl/plany/n76.html"
    # html = requests.get(url).text
    # print(html)
