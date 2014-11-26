#!/bin/sh
# Demonstrated for fun by guys at ihaveapc.com
# Ping a standard website with output suppressed, if ping completes then display success else failure

if [ "$(ping -c 1 google.com)" ]; then
	echo 1
fi
