print("сеодня лето?")
summer = input()
if summer == "да":
    print("сегодня жарко?")
elif summer == "нет":
    print("сегодня зима?")
    winter = input()
    if winter == "да":
        print("ветер сильный?")
    elif winter == "нет":
        print("сегодня осень?")
        autumn = input()
    elif autumn == "нет":
        print("сегодня весна?")
    spring = input()
    if spring == "да":
        print("одень кофту и штаны")
        if autumn == "да":
            print("Одень штану и кофту")
    wind = input()
    if wind == "да":
        print("одень кофту, куртку, штаны, шапку, шарф")
    elif wind == "нет":
        print("одень кофту, куртку, штаны, шапку")
    temp = input()
    if temp == "да":
        print("одень шорты и майку")
elif temp == "нет":
    print("одень тонкую кофту и штаны")



