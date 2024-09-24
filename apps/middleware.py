from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class CommingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request):
        # Code to be executed for each request before the view (and later middleware) are called.

        # List of routes that should be redirect to the home page because it is in construction mode
        redirect_routes = {
            reverse('activity'): 'Activity',
            reverse('contact'): 'Contact',
            reverse('feedback'): 'Feedback',
            reverse('resume'): 'Resume',
        }

        # for key, value in redirect_routes.items():
        #     print(f"{key}: {value}")


        for path, page_name in redirect_routes.items():
            if request.path_info == path:
                messages.info(request, f"{page_name} Page Under development, Coming soon.")
                return redirect('home') 
            
        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response