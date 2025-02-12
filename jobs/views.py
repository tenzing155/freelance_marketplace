from rest_framework import generics, permissions 
from .models import Job
from .serializers import JobSerializer
import stripe 
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)  # ✅ Automatically sets 'posted_by'

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]  # <- Requires login

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': 'Freelance Service'},
                        'unit_amount': 5000,  # $50.00
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/",
        )
        return JsonResponse({'checkout_url': session.url})  # ✅ Return the correct URL
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

