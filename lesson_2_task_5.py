def month_to_season(n_month):
    if n_month in (12 , 1, 2):
        print("Зима")
    elif n_month in (3, 4, 5):
            print("Весна")
    elif n_month in (6, 7, 8):
            print("Лето")
    elif n_month in (9, 10, 11):
            print ("Осень")
    else : return("неверная цифра года")
month_to_season (int(input()))