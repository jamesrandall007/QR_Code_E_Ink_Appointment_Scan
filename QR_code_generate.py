# pip install "qrcode[pil]"
import qrcode
from icecream import ic
from datetime import datetime, timedelta

# Get input from user
date_appt = input('Enter date and time of appointment: YYYMMDD ')
time_appt = datetime.strptime(input('Time of appointment: HHMM '), "%H%M")
duration_appt = timedelta(minutes=int(input('Duration of appointment: default is 15 minutes: ') or 15))
ic(date_appt, time_appt, duration_appt)
end_time = time_appt + duration_appt
# Convert end_time back to string in HHMM format
end_time_str = end_time.strftime("%H%M")

ic(end_time)
ic(end_time_str)

physician_name = input('Enter physician name: default is Kassay ') or 'Kassay'
reason = input('Enter reason for appointment: ')

# Create event details
event_details = (f'DTSTART:{date_appt}T{time_appt.strftime("%H%M")}00',
                 f'DTEND:{date_appt}T{end_time_str}00')

ic(event_details)
qr = qrcode.QRCode(version=1, box_size=10, border=5)
# Start the QR code data with the BEGIN:VEVENT line
qr_data = 'BEGIN:VEVENT\n'

# Add the SUMMARY and LOCATION lines
qr_data += f'SUMMARY:{reason} with {physician_name}\n'
qr_data += 'LOCATION: 12511 SW 68th Ave Suite 200 Portland OR 97223\n'

# Loop through each line in event_details and add it to the QR code data
for line in event_details:
    qr_data += f'{line}\n'

# Add the END:VEVENT line
qr_data += 'END:VEVENT'

# Add the QR code data to the QR code
qr.add_data(qr_data)

# # Generate QR code
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(f'BEGIN:VEVENT'
#             f'SUMMARY:{reason} with {physician_name}'
#             f'LOCATION: 12511 SW 68th Ave Suite 200 Portland OR 97223'
#             f'{event_details}'
#             f'END:VEVENT')

# qr.add_data(f'cal:/event?details={event_details}')
qr.make(fit=True)

# Save QR code as image
image = qr.make_image(fill='black', back_color='white')

# Format the current date and time as a string
current_datetime_str = datetime.now().strftime("%Y%m%d%H%M")

filename = f'QR_appointment_{current_datetime_str}.png'
image.save(filename)

print(f'QR code generated successfully as {filename}!')
