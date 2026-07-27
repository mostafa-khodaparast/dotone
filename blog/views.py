from django.http import HttpResponse


def post_list(restonse):
    return HttpResponse("All posts here...")


def post_detail(response, post_id):
    return HttpResponse(f"Post detail of {post_id}")
