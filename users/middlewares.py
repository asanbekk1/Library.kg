from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = request.POST.get('experience', 0)
            try:
                experience = int(experience)
            except (ValueError, TypeError):
                experience = 0

            # Логика расчета зарплаты
            if experience < 1:
                salary = 30000
            elif 1 <= experience < 3:
                salary = 50000
            elif 3 <= experience < 5:
                salary = 70000
            else:
                salary = 100000

            # Сохраняем зарплату в запросе
            request.salary = salary
            request.session['salary'] = salary  # Сохраняем в сессии

        elif request.path == '/register/' and request.method == 'GET':
            request.salary = 'Зарплата не определена'