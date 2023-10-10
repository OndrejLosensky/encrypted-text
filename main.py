from cryptography.fernet import Fernet
import time

def OPEN():
    print("Načítám soubor...")

    # otevře textový soubor
    with open('vlozenyText.txt', 'r') as file:
        lines = file.readlines()

    # vytvoří string z jednotlivých řádků
    global text
    text = ''.join(lines)

# zašifruje soubor zprava.txt a uloží do encrypted.txt
def ENCRYPT():
    print("Otevírám soubor 'zprava.txt'")
    print("Otevřeno!")

    time.sleep(1)
    print("šifruji")

    # tímto lze nastavit počet znaků na jeden řádek
    pocet_znaku_na_radku = 50

    lines = [encrypted_message[i:i+pocet_znaku_na_radku] for i in range(0, len(encrypted_message), pocet_znaku_na_radku)]

    with open('encrypted.txt', 'wb') as file:
        for line in lines:
            file.write(line + b'\n')
       

    print("Zašifrovaná zpráva se uložila do souboru: 'encrypted.txt'")

# dešifruje soubor encrypted.txt
def DECRYPT():
    print("Načítám soubor 'encrypted.txt'")
    time.sleep(1)
    print("Načteno!")
    time.sleep(0.5)

    print("dešifruji")
    
    with open('encrypted.txt', 'r') as file:
        lines = file.readlines()

    # Zobrazí obsah textu
    global enc_text
    enc_text = ''.join(lines)

    print(enc_text)

    print("Dešifrovaná zpráva se uložila do souboru: 'decrypted.txt'")

# hlavní funkce
def MAIN():
    global key
    global fernet
    # klíč pro šifrování
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # otevírá soubor s textem
    OPEN()

    global encrypted_message
    global decrypted_message
    encrypted_message = fernet.encrypt(text.encode())
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    
    print("Chcete zašifrovat soubor nebo dešifrovat? \n Pro šifrování stiskněte 1 | Pro dešifrování stiskněte 2")
    vyberMoznosti = input("")
    if vyberMoznosti == "1":
       ENCRYPT()
    elif vyberMoznosti == "2":
        DECRYPT()
    else:
        pass

# Zavolá funkci Main
MAIN()