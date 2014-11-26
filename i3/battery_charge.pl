#!/usr/bin/perl

$discharging = `acpi -b | awk '{print \$3}' | tr -d '\n' | grep -c Discharging`;
$charging = `acpi -b | awk '{print \$3}' | tr -d '\n' | grep -c Charging`;
$charged = `acpi -b | awk '{print \$3}' | tr -d '\n' | grep -c 'Full'`;
$percent = `sh battery.sh`;

if ($discharging == 1) {
	print 1;
}
elsif ($charging == 1 && $percent < 99) {
	print 2;
}
elsif ($charged == 1 || ($charging == 1 && $percent >= 99)) {
	print 3;
}
else {
	print 4;
}
