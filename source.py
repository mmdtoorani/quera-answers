from Exception import *
import hashlib

class Site:
    register_users = []
    active_users = []
    def __init__(self, url):
        self.url = url
        
    def show_users(self):
        pass

    def register(self, user):
        if user in self.register_users:
            raise AlreadyRegistered("user already registered")
        else:
            self.register_users.append(user)
            return "register successful"

    def login(self, **kwargs):
        if (kwargs.get('username') is not None) and (kwargs.get('password') is not None) and (kwargs.get('email') is not None):
            pass
        elif (kwargs.get('username') is not None) and (kwargs.get('password') is not None):
            pass
        elif (kwargs.get('password') is not None) and (kwargs.get('email') is not None):
            pass
        
    def logout(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            return "logout successful"
        else:
            return "user is not logged in"

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        if self.username_validation(username):
            self.username = username
            
        p = password
        if self.password_validation(p):
            self.password = self.set_new_password(p)
        
        if self.id_validation(user_id):
            self.user_id = user_id
        else:
            raise InvalidCodeMelli("Invalid code melli")
        
        if self.phone_validation(phone):
            self.phone = phone
        else:
            raise InvalidPhoneNumber("Invalid phone number")
        
        if self.email_validation(email):
            self.email = email

    def set_new_password(self, password): #DONE!
        return hashlib.sha256(password.encode('utf8')).hexdigest()

    def username_validation(self, username): # DONE!
        if '_' not in username or len(username.split('_')) > 2:
            raise InvalidUsername("Invalid username")
        else:
            return True

    def pass_has_num(self, password):
        type_list = []
        for i in password:
            try:
                i = int(i)
                type_list.append("int")
            except:
                type_list.append("str")
        return "int" in type_list

    def is_pass_utf8(self, password):
        try:
            password.encode('utf-8')
            return True
        except UnicodeEncodeError:
            return False
    
    def password_validation(self, password): # DONE!
        if len(password) < 8 :
            raise InvalidPassword("Invalid password")
        
        elif password.islower() or password.isupper() or password.isnumeric() or not self.pass_has_num(password):
            raise InvalidPassword("Invalid password")
        
        elif not self.is_pass_utf8(password):
            raise InvalidPassword("Invalid password")
        
        else:
            return True
            
        
    def id_validation(self, id):
        total = 0
        pos = 10
        for i in id:
            total += int(i) * pos
            pos -= 1
            if pos == 1:
                break
                
        remains = total % 11
        if remains < 2:
            if remains == int(id[-1]):
                return True
        else:
            if remains == 11 - int(id[-1]):
                return True
            
        return False

    def phone_validation(self, phone):
        if phone[0:4] == '+989':
            if len(phone) == 13:
                return True
        
        elif phone[0:2] == '09':    
            if len(phone) == 11:
                return True
        
        return False

    def email_validation(self, email):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        valid_chars = "0123456789-_."
            
        first_part = email.split('@')[0]
        second_part = email.split('@')[1].split('.')[0]
        third_part = email.split('.')[-1]
        print(first_part, second_part, third_part)
        
        for i in first_part:
            if i not in valid_chars + alphabet:
                raise InvalidEmail("Invalid email")
        
        for i in second_part:
            if i not in valid_chars + alphabet:
                raise InvalidEmail("Invalid email")
            
        for i in third_part:
            if i not in alphabet:
                raise InvalidEmail("Invalid email")
        
        if len(third_part) < 2 or 5 < len(third_part):
            raise InvalidEmail("Invalid email")
        
        return True

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func): #DONE!
    def wrapper(username):
        new_username = username.replace("_", " ")
        if len(new_username) > 15:
            return new_username[:15] + "..."
        else:
            return func(new_username)
    return wrapper
        
def verify_change_password(func):
    pass

@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)

@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")

# print(welcome("salib_alibabaeei"))