
def default_context(request):
    #return {'user_fullname': "--"}
    return {'user_fullname': request.user.username if request.user.is_authenticated else "--"}