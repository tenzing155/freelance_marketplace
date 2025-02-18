from rest_framework import generics, permissions
from .models import Job, Bid
from .serializers import JobSerializer, BidSerializer
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
        serializer.save(client=self.request.user)  # ✅ Fixed: Automatically sets 'client'

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]  # <- Requires login

class BidListCreateView(generics.ListCreateAPIView):
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Bid.objects.filter(job_id=job_id)  # Get all bids for a specific job

    def perform_create(self, serializer):
        job = Job.objects.get(pk=self.kwargs['job_id'])
        serializer.save(freelancer=self.request.user, job=job)

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
