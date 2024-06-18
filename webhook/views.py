import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import Application


@csrf_exempt
@require_POST
def jotform_webhook(request):
    try:
        raw_request = request.POST.get('rawRequest')
        if not raw_request:
            return JsonResponse({"error": "rawRequest not found"}, status=400)

        data = json.loads(raw_request)

        full_name = data.get('q3_fullName', {})
        first_name = full_name.get('first', '')
        last_name = full_name.get('last', '')
        contact_number = data.get('q4_contactNumber', {}).get('full', '')
        email = data.get('q5_emailAddress', '')
        what_date = data.get('q13_whatDate13', {}).get('implementation', '')
        other_specific_date = data.get('q12_anyOther', {})
        what_services = data.get('q10_whatServices', '')

        if not email:
            return JsonResponse({"error": "Email not provided"}, status=400)

        username = f"{first_name}_{last_name}".lower()
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(User.objects.make_random_password())
            user.save()

        application, app_created = Application.objects.update_or_create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            what_date=what_date,
            other_specific_date=other_specific_date,
            what_services=what_services
        )

        response_data = {
            "status": "success",
            "user_created": created,
            "application_created": app_created
        }

        return JsonResponse(response_data, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
