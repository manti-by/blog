from django.http import HttpResponse


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Profiles with test key")
    return HttpResponse("Profiles view")
