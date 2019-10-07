import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket


 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        temperature  = 25
        humidity = 50
        # Reverse Message and send it back
        if message == 'Temperature':
            self.write_message("Current Temperature: " + str(temperature))
        if message == 'Humidity':
            self.write_message("Current Humidity: " + str(humidity))
        else:
            pass
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])








if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
 
