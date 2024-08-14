import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)
            full_name = data.get('fullName')
            phone_number = data.get('phoneNumber')
            email = data.get('email')
            reason = data.get('reason')
            message = data.get('message')

            # Basic validation to ensure all fields are provided
            if not full_name or not phone_number or not email or not reason or not message:
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Create email subject and message content
            subject = f"New Contact Form Submission: {reason}"
            email_message = f"""
            Name: {full_name}
            Phone: {phone_number}
            Email: {email}
            Message: {message}
            """

            # Send the email using the user's email as the sender
            send_mail(
                subject,
                email_message,
                email,  # From email (user's email)
                ['nikhilrai662@gmail.com'],  # To email (your email)
                fail_silently=False,
            )

            # Return a success response
            return JsonResponse({"message": "Form submitted successfully!"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({"error": "Invalid request method."}, status=400)


import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def haveaproject(request):
    if request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)
            name = data.get('name')
            subject = data.get('subject')
            email = data.get('email')
            message = data.get('message')

            # Basic validation to ensure all fields are provided
            if not name or not subject or not email or not message:
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Create email subject and message content
            email_subject = f"Have A Project - {subject}"
            email_message = f"""
            Name: {name}
            Email: {email}
            Message: {message}
            """

            # Send the email using the user's email as the sender
            send_mail(
                email_subject,
                email_message,
                email,  # From email (user's email)
                ['nikhilrai662@gmail.com'],  # To email (your email)
                fail_silently=False,
            )

            # Return a success response
            return JsonResponse({"message": "Message sent successfully!"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({"error": "Invalid request method."}, status=400)