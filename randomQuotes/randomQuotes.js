var express = require('express'),
	http =  require('http'),
	redis = require('redis'),
	db = redis.createClient(),
	app = express();

// Dunno why I chose this port
app.set('port', 8888);

// Display the html file
app.get('/', function (req, res) {
	res.sendfile('./randomMessages.html');
});

// Uploads quotes to the db
app.get('/submitQuotes', function (req, res) {
	if (req.query.userMessage1 !== "") {
		db.sadd("randomQuotes", req.query.userMessage1); }	
	if (req.query.userMessage2 !== "") {
		db.sadd("randomQuotes", req.query.userMessage2); }
	res.redirect("/getQuotes");
	if (req.query.userMessage3 !== "") {
		db.sadd("randomQuotes", req.query.userMessage3); }
});

// Displays a random quote from the db on browser reload
app.get('/getQuotes', function (req, res) {
	db.srandmember("randomQuotes", function (err, reply) {
		var body = '<html>'+
		'<head>'+
		'<meta http-equiv="Content-Type" content="text/html"; '+
		'charset=UTF-8 />'+
		'</head>'+
		'<body>'+
		"<h2> Here's a random quote: </h2>"+
		'<h2>'+reply+'</h2>'+
		"<h2> Refresh your page for another one ;)</h2>"+
		"<form action='/' method='get'>"+
		"<input type='submit' value='Manage Quotes!'/>"+
		"</form>"+
		'</body>'+
		'</html>';

		res.writeHead(200, {"Content-Type": "text/html"});
		res.write(body);
		res.end(); 
	});
});

// Deletes all current quotes in the db
app.get('/deleteQuotes', function (req, res) {
	db.scard("randomQuotes", function (err, reply) {
		for (var i = 0; i < reply; i++) {
			db.spop("randomQuotes");
		};
	});
});

// Creates the server itself
http.createServer(app).listen(app.get('port'), function () {
	console.log("Express server listening on port " + app.get('port'));
});