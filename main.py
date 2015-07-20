import webapp2

from handlers import main_controller

app = webapp2.WSGIApplication([
    ('/', main_controller.MainController),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()