<!--HTML page for GPA Calc web app-->
<html>
<head>
	<link rel='stylesheet' type= "text/css" href='stylesheet.css'/>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="text/javascript" src='script.js'></script>

</head>

<body background="squared_metal.png">
	<div id="intro">
		<h1> Swarthmore GPA Calculator </h1>
		<p> Enter your mySwat credentials to calculate your GPA. </p>
	</div>
		
	<form name="creds"><fieldset>
		<legend>Credentials</legend>
		<h3>User ID:</h3> <input type="text" name="user" required> <br/>
		<h3>PIN:</h3> <input type="password" name="pin" required> <br/>

		<p> To calculate your major GPA, select your major(s). </p>
		<!--TODO: Add more majors-->
		<select multiple>
  			<option value="cs">Computer Science</option>
  			<option value="bio">Biology</option>
  			<option value="psych">Psychology</option>
		</select> <br/>

		<input type="submit" id="submitButton">
	</fieldset></form>

</body>
</html>