$TTL    604800
@       IN      SOA     ns1.cafepudge.loc. root.cafepudge.loc. (
                             2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

@       IN      NS      ns1.cafepudge.loc.

ns1     IN      A       192.168.56.1  ; Указываем IP-адрес вашего DNS-сервера

server  IN      A       192.168.56.2  ; Пример записи A для server.cafepudge.loc
