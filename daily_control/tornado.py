#coding=utf-8
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


http_server = HTTPServer(WSGIContainer())
http_server.listen(5000)  #flask默认的端口
IOLoop.instance().start()