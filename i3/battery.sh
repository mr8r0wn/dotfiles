#!/bin/sh
acpi -b | awk '{ split($5,a,":"); print $4}' | tr -d ',' | tr -d '%' #| tr '\n' '+' | tr -d '%' #| sed 's/\(.*\)+$/\(\1\)\/2/' | { cat; echo; } | bc
