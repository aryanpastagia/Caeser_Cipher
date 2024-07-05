#Aryan Pastagia A227
choice=input("Choose Encryption or Decryption:")
result=""
if choice == "e":
    PT=input("Enter plain text:")
    for i in PT:
        if i.isalpha():
            upper=i.isupper()
            a=ord(i)
            encr=((((a - ord('A' if upper else 'a')) + 3) % 26) + ord('A' if upper else 'a'))
            result+=chr(encr)
        else:
            result+=i
    print("The cipher text is",result)

elif choice=="d":
    CT=input("Enter Cipher text:")
    for i in CT:
        if i.isalpha():
            upper=i.isupper()
            a=ord(i)
            decr=((((a - ord('A' if upper else 'a')) + 3) % 26) + ord('A' if upper else 'a'))
            result +=chr(decr)
        else:
            result +=i
    print("The plain text is ",result)
 