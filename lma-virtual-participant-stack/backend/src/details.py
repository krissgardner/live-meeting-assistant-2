
import os

meeting_platform = os.environ['MEETING_PLATFORM']
meeting_id = os.environ['MEETING_ID']
meeting_password = os.environ['MEETING_PASSWORD']
meeting_name = os.environ['MEETING_NAME']

email_sender = os.getenv('EMAIL_SENDER', '')
email_receiver = os.getenv('EMAIL_RECEIVER', '')

lma_user = os.getenv('LMA_USER', 'unknown user')

intro_message = os.environ['INTRO_MESSAGE'].replace('{LMA_USER}', lma_user)
start_recording_message = os.environ['START_RECORDING_MESSAGE'].replace(
    '{LMA_USER}', lma_user)
stop_recording_message = os.environ['STOP_RECORDING_MESSAGE'].replace(
    '{LMA_USER}', lma_user)
exit_message = os.environ['EXIT_MESSAGE'].replace('{LMA_USER}', lma_user)


scribe_name = "Live Meeting Assistant"
scribe_identity = f"{scribe_name} ({lma_user})"

waiting_timeout = 300000  # 5 minutes
meeting_timeout = 21600000  # 6 hours

start = True

start_command = "START"
pause_command = "PAUSE"
end_command = "END"

intro_messages = [
    intro_message
]
start_messages = [
    start_recording_message
]
pause_messages = [
    stop_recording_message
]
exit_messages = [
    exit_message
]

messages = []
attachments = {}
captions = []
speakers = []
