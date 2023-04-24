from src import route1

def post_http():
    http_message = {
        "HTTP_method": "POST",
        "HTTP_header": [
            ("token", "Bearer kjshdfkljsdh34343"),
            ("origin", "http://somthing.other.org")
        ],
        "HTTP_body": [
            ("name", "Marcos"),
            ("message", "hello world")
        ]
    }

    route1(http_message)