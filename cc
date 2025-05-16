$TTL    604800
@       IN      SOA     ns1.local.lan. root.local.lan. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

@       IN      NS      ns1.local.lan.

server  IN      A       192.168.56.2



  $TTL    604800
@       IN      SOA     ns1.local.lan. root.local.lan. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

@       IN      NS      ns1.local.lan.
2       IN      PTR     server.local.lan.
