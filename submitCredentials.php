<html>
<head>
    <meta charset="UTF-8">
	<link rel='stylesheet' type= "text/css" href='stylesheet.css'/>
</head>
<body>
<span id="gpa">
<?php

$descriptorspec = array(
  	0 => array("pipe", "r"),
	1 => array("pipe", "w"),
	2 => array("pipe", "w")
);

$run = "python test.py {$_POST['user']} {$_POST['pin']}"; //TODO: Change this to 

$process = proc_open($run, $descriptorspec, $pipes);

//$read = fread($process, 8);
//echo $read;

if (is_resource($process)) {
  
	echo stream_get_contents($pipes[1]);
	fclose($pipes[1]);
	fclose($pipes[0]);
	pclose($process);


//	$handle = proc_open($run, 'r');
//	echo "$handle; " . gettype($handle) . "\n";
//	$read = fread($handle, 8);
//	echo $read;
	pclose($handle);

}

?>;
</span>
</body>
<html>


<!--escapeshellcmd(string $command) , escapeshellarg(string $command), htmlspecialchars()-->
 
