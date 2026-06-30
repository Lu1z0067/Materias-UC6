print("\nConverção de idade canina para idade humana")
age_dog = int(input("\nDigite a idade do seu cachorro: "))

if age_dog == 1:
    print("\nSeu cachorro convertido para idade humana, ele teria 15 anos")
if age_dog == 2: 
    print("\nSeu cachorro convertido para idade humana, ele teria 24 anos")
if age_dog > 2:
    age_dog = (age_dog * 5 + 24)-2
    print(f"\nSeu cachorro convertido para idade humana, ele teria {age_dog} anos")
