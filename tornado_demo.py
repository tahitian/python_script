#! /usr/bin/python
import logging
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.concurrent import run_on_executor

class TrackHandler(tornado.web.RequestHandler):
    # executor = ThreadPoolExecutor(thread_pool_size*4)
    # @run_on_executor()
    def post(self):
        data = 'hello'
        self.write(data)

def main():
    logging.basicConfig(level=logging.INFO)
    formatter = logging.Formatter("[%(name)s] [%(asctime)s] [%(levelname)s] \"%(message)s\"")
    filehandler = logging.handlers.RotatingFileHandler('../../log/tornado.log', mode = "a", maxBytes = 1073741824, backupCount = 4)
    filehandler.setFormatter(formatter)
    logging.getLogger().addHandler(filehandler)
    # tornado.options.logging = None
    # tornado.options.define('logging', default='info')
    # tornado.options.define('log_file_prefix', default='../../log/tornado.log')
    # tornado.options.define('log_rotate_mode', default='size')
    # tornado.options.define('log_file_max_size', default=100*1024*1024)
    # tornado.options.define('log_file_num_backups', default=5)
    # tornado.options.parse_command_line()
    app = tornado.web.Application([
        ("/track", TrackHandler)
        ])
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
