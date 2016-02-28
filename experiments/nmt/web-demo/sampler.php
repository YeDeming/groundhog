<?php

# make sure that only one script at a time accesses the sampling server
$fp = fopen('/tmp/flock', 'w');
if (flock($fp, LOCK_EX)) 
{
	$source=$_GET["source"];
	$url = 'http://127.0.0.1:8000/limjcst/?source='.urlencode($source);
	$out = file_get_contents($url);

	echo urldecode($out);
}
else
{
	echo "Server timeout! Try again later.";
}

?>

