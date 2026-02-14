from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class Command(BaseCommand):
    help = 'Test email configuration by sending a test email'

    def add_arguments(self, parser):
        parser.add_argument('--to', type=str, help='Email address to send test email to')

    def handle(self, *args, **options):
        to_email = options.get('to')
        
        if not to_email:
            self.stdout.write(
                self.style.ERROR('Please provide an email address using --to flag')
            )
            return

        try:
            # Test booking context
            booking_context = {
                'customer_name': 'Test User',
                'booking_date': '2025-10-15',
                'booking_slots': ['6-7 pm', '7-8 pm'],
                'total_amount': 1400,
                'turf_name': 'JP Sports Arena',
                'turf_address': 'Survey No. 25, Kothrud, Near COEP College, Pune, Maharashtra 411038',
                'booking_id': 'TEST_12345',
                'booking_time': '14:30:00',
                'contact_phone': '+91 9999999999',
                'contact_email': 'support@surftheturf.com'
            }
            
            # Render email template
            message_html = render_to_string('booking_confirmation_email.html', booking_context)
            message_plain = strip_tags(message_html)
            
            # Send test email
            send_mail(
                'Test Booking Confirmation - SurfTheTurf',
                message_plain,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
                html_message=message_html,
                fail_silently=False
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Test email sent successfully to {to_email}')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to send test email: {str(e)}')
            )
            self.stdout.write(
                self.style.WARNING('Check your email settings in settings.py')
            )