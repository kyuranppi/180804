from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'landi1/post_list.html', {}) #post_list라는 함수는 request를 넘겨 받아 render method를 호출한다 이 함수는 호출하여 받은(return) blog/post_list.html template를 보여준다.