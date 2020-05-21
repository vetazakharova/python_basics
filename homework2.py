def data(city, email, name, surname, birth, phone):
    str1 = "Your name is " + name + " " + surname + " and you were born in " + birth + ". You live in " + city + " and your contact info is " + email + " " + phone
    return str1

namee = input("What is your name? ")
surnamee = input("What is your surname? ")
birthh = input("Which year were you born? ")
cityy = input("In which city do you live? ")
emaill = input("What is your email? ")
phonee = input("What is your phone number? ")
print(data(name = namee, surname = surnamee, city = cityy, birth = birthh, email = emaill, phone = phonee ))
