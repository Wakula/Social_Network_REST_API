def update_last_user_activity(get_response):
    def middleware(request):
        response = get_response(request)
        if request.user.is_authenticated:
            request.user.update_last_activity()
        return response
    return middleware
