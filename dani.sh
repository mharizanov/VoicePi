#!/bin/bash

if [ "$1" = "deny" ]
then
	ssh root@192.168.1.1 'iptables -I grp_3 -m mac --mac-source AB:CD:EF:AB:CD:EF -j DROP'
else
	ssh root@192.168.1.1 'iptables -D grp_3 -m mac --mac-source AB:CD:EF:AB:CD:EF -j DROP'
fi
#ssh root@192.168.1.1 'iptables --list'
