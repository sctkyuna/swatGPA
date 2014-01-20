var submitCredentials = function(user, pin) {
	// submits given credentials to the python script
	// if credentials work, return GPA
	// else, return false
}

$(document).ready(function() {
	// Credentials handler
	var getCredentials = function() {
		var UserID = $('input[name=user').val();
        var PIN = $('input[name=pin').val();
        
        var GPA = {
        	<?php 
	        	$handle=proc_open('python test.py', 'r');
	        	echo "$handle'; " . gettype($handle) . "\n";
	        	echo $read;
	        	pclose($handle);
        	?>
        }


        return false;
	}

	$("form[name=creds]").submit(getCredentials);

	// Submit button effects
	$("#submitButton").mouseover(function() {
        $(this).fadeTo("fast",1);
    });
    
    $("#submitButton").mouseout(function() {
        $(this).fadeTo("fast",0.5); 
    });
	
});