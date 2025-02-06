from django.shortcuts import render

# Create your views here.
from .models import DocumentVerificationDB
from datetime import datetime


def index(request):
    if request.method == 'POST':
        sellername = request.POST.get('sellername')
        phone_no = request.POST.get('phone_no')
        role = request.POST.get('role')
        created_at = request.POST.get('created_at')
        status = request.POST.get('status')
        
        # Check if created_at is provided and convert it to datetime object
        if created_at:
            created_at = datetime.strptime(created_at, '%d-%m-%Y')

        user = DocumentVerificationDB.objects.create(
            sellername=sellername,
            phone_no=phone_no,
            role=role,
            created_at=created_at,
            status=status
        )
        
        # Filter data based on the provided date range
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        if from_date and to_date:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
            data = DocumentVerificationDB.objects.filter(created_at__range=[from_date, to_date])
        else:
            data = DocumentVerificationDB.objects.all()
    else:
        data = DocumentVerificationDB.objects.all()
    return render(request, 'index.html', {'data': data})















# def index(request):
#     if request.method == 'POST':
#         sellername = request.POST.get('sellername')
#         phone_no = request.POST.get('phone_no')
#         role = request.POST.get('role')
#         created_at = request.POST.get('created_at')
#         status = request.POST.get('status')
        

#         user = DocumentVerification.objects.create(
#             sellername=sellername,
#             phone_no=phone_no,
#             role=role,
#             created_at=created_at,
#             status=status
#         )
#         from_date = request.POST.get('from_date')
#         to_date = request.POST.get('to_date')
#         data = DocumentVerification.objects.filter(created_at__range=[from_date, to_date])
#     else:
#         data = DocumentVerification.objects.all()
#     return render(request, 'index.html', {'data': data})