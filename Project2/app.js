// Node.js WebSocket server script

const http = require('http');
const WebSocketServer = require('websocket').server;
const server = http.createServer();
server.listen(9898);
const wsServer = new WebSocketServer({
    httpServer: server
});

//Mysql functionality initialization
var mysql = require('mysql');
var con = mysql.createConnection({
  host: "localhost",
  user: "pi",
  password: "letmein",
  database: "exampledb"
});


//Mysql retrive data setup
con.connect(function(err) {
	if (err) throw err;
	console.log("Connected!");
	con.query("SELECT temperature, humidity FROM environment ORDER BY ID DESC LIMIT 1", function (err, result, fields) {
	  if (err) throw err;
	  console.log(result);
//	  connection.sendUTF(result);
	});
});


//Websocket setup
wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
    connection.on('message', function(message) {
      console.log('Received Message:', message.utf8Data);
      connection.sendUTF('Hi this is WebSocket server!');
    });
    connection.on('close', function(reasonCode, description) {
        console.log('Client has disconnected.');
    });
});



