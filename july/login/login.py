from login_oop_db import check_data, add_data

class Login:
    def __init__(self, user, password):
        self.user = user
        self.__password = password


    @property
    def password(self):
        return self.__password
    
    def cek(self):
        c = check_data(self.user, self.password)
        if not c:
            print("Username/password tidak ditemukan. Silakan daftar dulu.")
            daftar = signUp(self.user, self.password)
            daftar.register()
            return False
        else:
            print("Login berhasil!")
            return True


class signUp(Login):
    def __init__(self, user, password):
        super().__init__(user, password)
        
    def register(self):
        print(f"Mendaftarkan user {self.user}")
        add_data(self.user, self.password)
        print("registrasi berhasil")

def main():
    print("=====REGISTRASI=====")
    username = input("username: ")
    password = input("password: ")
    reg = Login(username, password)
    reg.cek()
    

if __name__ == "__main__":
    main()