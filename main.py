import random
import string


class PasswordManager():
    pw_bank = []  # Need to be a database with verified access. SQLite should be good.
    
    def __init__(self) -> None:
        pass
    
    def generate_pw(self, length=16):
        """Generate a random password of the specified length."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    
    def email_mng(self):
        service_name = input('Service/Domain: ')        
        
        domains = ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']
        user_email = input('Email: ')
            
        validation = [True if domain in user_email else False for domain in domains ]      
        
        if True in validation:
            return {service_name: user_email}
        else:
            raise ValueError

    def create_login(self):
        service = self.email_mng()
        pw = self.generate_pw()
        login = [service, pw]
        self.pw_bank.append(login)        

if __name__ == '__main__':
    final = PasswordManager()
    final.create_login()
    print(final.pw_bank)