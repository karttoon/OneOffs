<?php

/*
	Author  - Jeff White [karttoon]
	Email   - karttoon@gmail.com
	Version - 1.0.0
	Date    - 02NOV2015

	This PHP is designed to pass back specific values when various commands are received, as to elicit malware to perform various functions. Designed for one specific malware but can be used across any that have this type of communication.
*/

if (($_GET['command']) == 'getid') {
	echo "123456789";
} elseif (($_GET['command']) == 'getip') {
	echo "192.168.60.50";
} elseif (($_GET['command']) == 'update') {
	echo "ok";
} elseif (($_GET['command']) == 'update2') {
	echo "ok";
} elseif (($_GET['command']) == 'ghl') {
	echo "aHR0cDovLzE5Mi4xNjguNjAuMjAwL2JhZC5waHAK";
} elseif (($_GET['command']) == 'dl') {
	echo "fA==";
} elseif (($_GET['command']) == 'version') {
	echo "MS45fGh0dHA6Ly8xOTIuMTY4LjYwLjIwMC8xOS5leGUK";
} elseif (($_GET['command']) == 'getbackconnect') {
	echo "192.168.60.200:1337";
} else {
	echo "Go Away?";
}

?>
