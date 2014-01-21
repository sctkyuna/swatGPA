var submitCredentials = function(user, pin) {
	// submits given credentials to the python script
	// if credentials work, return GPA
	// else, return false
}



$(document).ready(function() {
	// Credentials handler
	/*var getCredentials = function() {
		UserID = $('input[name=user]').val();
        PIN = $('input[name=pin]').val();
        
        //TODO: figure out how to save php output to js var
        //var GPA = getGPA();
        //console.log(GPA);

        return false;
	}

	$("form[name=creds]").submit(getCredentials);*/

	// Submit button effects
	$("#submitButton").mouseover(function() {
        $(this).fadeTo("fast",1);
    });
    
    $("#submitButton").mouseout(function() {
        $(this).fadeTo("fast",0.5); 
    });
	
});


