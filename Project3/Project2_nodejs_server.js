var mysql = require('mysql');
const http = require('http');
const WebSocketServer = require('websocket').server;

USER="satya"
PASWWD="satya123"
DATABASE="example"
TABLE="environment"

const server = http.createServer();
server.listen(9898);

const wsServer = new WebSocketServer({
    httpServer: server
});

var con = mysql.createConnection({
  host: "localhost",
  user: USER,
  password: PASWWD,
  database: DATABASE
});

con.connect(function(err) {
	if (err) throw err;
	console.log("Connected!");
}); 

wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
    
    connection.on('message', function(message) {
      if(message.utf8Data == "Refresh") {
	con.query("SELECT * FROM environment ORDER BY id DESC LIMIT 1", function (err, result, fields) {
		if (err) throw err;
		var send_json = JSON.stringify(result);
		connection.sendUTF(send_json);
	});
      }
      else if(message.utf8Data == "Table") {
	con.query("SELECT * FROM environment ORDER BY id DESC LIMIT 10", function (err, result, fields) {
		if (err) throw err;
		var send_json = JSON.stringify(result);
		connection.sendUTF(send_json);
	});
      }
    });
    connection.on('close', function(reasonCode, description) {
        console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
    });
});


