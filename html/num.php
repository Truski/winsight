<?php


header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

$string = file_get_contents("C:/Users/Sapphire/Desktop/winsight/build/darknet/x64/angle.txt");
$arr = explode("\n", $string);
$oldNumber = $arr[0];
$angle = $arr[1];
while(true){
	$string = file_get_contents("C:/Users/Sapphire/Desktop/winsight/build/darknet/x64/angle.txt");
	$arr = explode("\n", $string);
	$num = $arr[0];
	$angle = $arr[1];
	if($oldNumber == $num){
		sleep(2);
		continue;
	}
	$oldNumber = $num;
	echo "data: $angle" . PHP_EOL;
	echo PHP_EOL;
	ob_flush();
	flush();
	sleep(2);
}