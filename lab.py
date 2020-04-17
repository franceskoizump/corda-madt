from madt_lib.network import Network


def main():
    net = Network('15.0.0.0/8')
    # create a local network that will connect all those nodes
    server = net.create_node('server', image='roastario/notary-and-network-map:4.0',entrypoint='sh -c "/start.sh && while true; do sleep 1000; done"',ports={'10200/tcp': 10200, '8080/tcp': 8080}, privileged=True)
    client1 = net.create_node('client1', image='party-a', entrypoint='sh -c "/run-corda.sh && while true; do sleep 1000; done"',ports={'2222/tcp': 2221}, privileged=True)
    client2 = net.create_node('client2', image='party-b', entrypoint='sh -c "/run-corda.sh && while true; do sleep 1000; done"',ports={'2222/tcp': 2222}, privileged=True)
    client3 = net.create_node('client3', image='party-c', entrypoint='sh -c "/run-corda.sh && while true; do sleep 1000; done"',ports={'2222/tcp': 2223}, privileged=True)
    
    net.create_subnet('net_corda54675', (server, client1, client2, client3))
    
    net.configure(verbose=True)
   
    server.add_options(environment=['PUBLIC_ADDRESS=notary-and-network-map', 'MY_PUBLIC_ADDRESS=notary-and-network-map'])
    
    # save lab
    net.render('../madt/labs/corda-yo', verbose=True)


if __name__ == "__main__":
    main()
