from django.shortcuts import render,HttpResponse
import logging

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)


# Create your views here.
def index(request):
    try:
        logger.warning('Line 26 may causes error')
        a = 10/0
    except:
        logger.error("Divide by Zero")
        return HttpResponse("Error")
   


def hello_reader(request):
    logger.warning('Homepage was accessed at ')
    return HttpResponse("<h1>Hello FreeCodeCamp.org Reader :)</h1>")
