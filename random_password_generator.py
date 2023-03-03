import os
import random
import string

while True:
    def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
        # Belirlenen uzunlukta bir şifre oluşturma
        password = ''
        characters = ''
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        for i in range(length):
            password += random.choice(characters)
        return password

    # Kullanıcıdan şifre uzunluğunu ve hangi karakterlerin kullanılacağını alma
    length = int(input("Şifre uzunluğunu girin: "))
    use_lowercase = input("Küçük harf kullanılsın mı? (E/H): ").lower() == 'e'
    use_uppercase = input("Büyük harf kullanılsın mı? (E/H): ").lower() == 'e'
    use_digits = input("Sayı kullanılsın mı? (E/H): ").lower() == 'e'
    use_symbols = input("Sembol kullanılsın mı? (E/H): ").lower() == 'e'
    purpose = input("Şifrenin ne için oluşturulduğunu girin: ")

    # Şifre oluşturma ve yazdırma
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    print("Oluşturulan şifre:", password)

    # Şifreyi dosyaya kaydetme
    filename = os.path.join(os.path.dirname(__file__), "pass.txt")
    with open(filename, 'a') as f:
        f.write(f"{purpose}: {password}\n")
        print(f"Oluşturulan şifre {purpose} için pass.txt dosyasına kaydedildi.")

    # Tekrar isteme
    while True:
        answer = input("Tekrar şifre oluşturmak istiyor musunuz? (E/H): ")
        if answer.lower() == 'e':
            break
        elif answer.lower() == 'h':
            exit()
        else:
            print("Geçersiz bir yanıt girdiniz. Lütfen tekrar deneyin.")
