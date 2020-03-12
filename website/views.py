from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def home(request):
	return render(request, 'home.html', {})



def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send a email
		send_mail(
			'message from ' + message_name, # Subject
			message, # message
			message_email, # From Email
			["tom.nyone@outlook.com"], # To Email, you can add more email to the list for copy.
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def blog_details(request):
	return render(request, 'blog-details.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_day = request.POST['your-day']
		your_message = request.POST['your-message']


		# send a email
		appointment = "Message from: " + your_name + "\n Phone: " + your_phone + "\n Email: " + your_email + "\n Address: " + your_address + "\n Schedule: " + your_schedule + "\n Day: " + your_day + "\n Message: " + your_message
		send_mail(
			'appointment from ' + your_name, # Subject
			appointment, # message
			your_email, # From Email
			["tom.nyone@outlook.com"], # To Email, you can add more email to the list for copy.
			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_day': your_day,
			'your_message': your_message,
			})

	else:
		return render(request, 'home.html', {})
