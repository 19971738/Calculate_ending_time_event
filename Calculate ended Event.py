hour = int(input("Die Anfangszeit(Stunde): "))
mins = int(input("Die Anfangszeit (minuten): "))
dura = int(input("Dauer der Veranstaltung (minuten): "))

dura1 = mins + dura
hour1 = (dura1//60) + hour #OK
hour2 = hour1 % 24
mins1 = (dura1 % 60) 

print("Die Veranstaltung endet um: ",hour2, ":",mins1," Uhr.")
