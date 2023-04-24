from src import route1

def post_http():
    
    http_message = {
        "method": "POST",
        "header": {
            "token": "Bearer kjhaskjdhkajsh2323",
            "origin": "http://somthing.other.org"
        },
        "body": {
            "name": "Marcos",
            "message": "hello world"
        }
    }

    route1(http_message)
