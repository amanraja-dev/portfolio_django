from .models import Profile

def user_context(request):
    data = Profile.objects.get(mobile='9155244224' )
    return {'data': data}
