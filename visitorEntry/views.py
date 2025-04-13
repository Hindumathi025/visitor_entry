from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
def visitor_entry(request):
    
    return render(request, "index.html")

@csrf_exempt  # For API endpoint (use proper auth in production)
def verify_phone_email(request):
    if request.method == 'POST':
        try:
            print("........................verify")
            # Get JSON URL from request
            data = json.loads(request.body)
            print("data",data)
            user_json_url = data.get('user_json_url')

            # Fetch user data from Phone.Email
            with urllib.request.urlopen(user_json_url) as url:
                user_data = json.loads(url.read().decode())

            # Extract user information
            user_country_code = user_data["user_country_code"]
            user_phone_number = user_data["user_phone_number"]
            user_first_name = user_data.get("user_first_name", "")
            user_last_name = user_data.get("user_last_name", "")
            print("user phone number",user_phone_number)
            # Here you would typically:
            # 1. Create or update user in your database
            # 2. Implement login logic
            # 3. Set session/cookie for authenticated user

            return JsonResponse({
                'success': True,
                'message': 'Verification successful',
                'user_data': {
                    'phone': f"{user_country_code}{user_phone_number}",
                    'name': f"{user_first_name} {user_last_name}".strip()
                }
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
 