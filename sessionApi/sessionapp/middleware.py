from django.http import HttpResponse

class MiddleWareCycle:
    def __init__(self, get_response):
        print('INIT METHOD')
        self.get_response = get_response


    def __call__(self, request):
        print('Before the view is executed')
        response = self.get_response(request)
        # go to seetings.py to middleware
        print('After the view is excuted')
        return response


class ExceptionHandingMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response


    def __call__(self, request):
        
        return self.get_response(request)
        # go to seetings.py to middleware
        
    def process_exception(self,request,exception):
        print(exception.__class__.__name__)
        print(exception)
        return HttpResponse("<b>We are currently face a issue we will get back </b>")