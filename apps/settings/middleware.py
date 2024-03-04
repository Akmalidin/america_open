from django.contrib.sessions.models import Session
from django.utils import timezone
from django.shortcuts import render

class OneDevicePerProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Получаем текущую сессию пользователя
            session_key = request.session.session_key

            # Если у пользователя еще нет сессии, создаем ее
            if not session_key:
                request.session.save()
                session_key = request.session.session_key

            # Получаем все активные сессии для пользователя
            active_sessions = Session.objects.filter(
                expire_date__gte=timezone.now(),
                session_data__contains=request.user.pk
            ).exclude(session_key=session_key)

            # Закрываем все другие сессии пользователя
            for session in active_sessions:
                session_data = session.get_decoded()
                if session_data.get('_auth_user_id') == str(request.user.pk):
                    session.delete()

        response = self.get_response(request)
        return response

class ServerErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            return render(request, 'errors/500.html', status=500)
        return response