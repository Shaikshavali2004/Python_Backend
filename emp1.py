employees=[{"eid":1,"ename":"Glory","gender":"Non-binary"},
{"eid":2,"ename":"Micah","gender":"Male"},
{"eid":3,"ename":"Job","gender":"Genderqueer"},
{"eid":4,"ename":"Opalina","gender":"Female"},
{"eid":5,"ename":"Roderick","gender":"Male"},
{"eid":6,"ename":"Jameson","gender":"Male"},
{"eid":7,"ename":"Isidro","gender":"Male"},
{"eid":8,"ename":"Bret","gender":"Male"},
{"eid":9,"ename":"Estelle","gender":"Female"},
{"eid":10,"ename":"Molly","gender":"Female"},
{"eid":11,"ename":"Sherlocke","gender":"Agender"},
{"eid":12,"ename":"Wilfred","gender":"Male"},
{"eid":13,"ename":"Lucais","gender":"Male"},
{"eid":14,"ename":"Foster","gender":"Male"},
{"eid":15,"ename":"Reg","gender":"Male"},
{"eid":16,"ename":"Iolande","gender":"Female"},
{"eid":17,"ename":"Tobias","gender":"Male"},
{"eid":18,"ename":"Colline","gender":"Female"},
{"eid":19,"ename":"Valene","gender":"Female"},
{"eid":20,"ename":"Tremaine","gender":"Male"},
{"eid":21,"ename":"Minne","gender":"Genderqueer"},
{"eid":22,"ename":"Casandra","gender":"Female"},
{"eid":23,"ename":"Sydney","gender":"Female"},
{"eid":24,"ename":"Bette","gender":"Female"},
{"eid":25,"ename":"Yolande","gender":"Female"},
{"eid":26,"ename":"Shannan","gender":"Male"},
{"eid":27,"ename":"Gavan","gender":"Genderfluid"},
{"eid":28,"ename":"Vlad","gender":"Agender"},
{"eid":29,"ename":"Barnabas","gender":"Male"},
{"eid":30,"ename":"Annadiane","gender":"Female"},
{"eid":31,"ename":"Broddy","gender":"Male"},
{"eid":32,"ename":"Estell","gender":"Female"},
{"eid":33,"ename":"Chantal","gender":"Female"},
{"eid":34,"ename":"Ludwig","gender":"Male"},
{"eid":35,"ename":"Kania","gender":"Female"},
{"eid":36,"ename":"Brandon","gender":"Male"},
{"eid":37,"ename":"Garth","gender":"Male"},
{"eid":38,"ename":"Mireielle","gender":"Female"},
{"eid":39,"ename":"Binnie","gender":"Female"},
{"eid":40,"ename":"Sebastiano","gender":"Male"},
{"eid":41,"ename":"Lana","gender":"Female"},
{"eid":42,"ename":"Bevin","gender":"Male"},
{"eid":43,"ename":"Garrard","gender":"Male"},
{"eid":44,"ename":"Gilli","gender":"Female"},
{"eid":45,"ename":"Cletis","gender":"Male"},
{"eid":46,"ename":"Rhonda","gender":"Female"},
{"eid":47,"ename":"Chet","gender":"Male"},
{"eid":48,"ename":"Hilary","gender":"Male"},
{"eid":49,"ename":"Alain","gender":"Male"},
{"eid":50,"ename":"Bridgette","gender":"Female"},
{"eid":51,"ename":"Odie","gender":"Male"},
{"eid":52,"ename":"Lishe","gender":"Female"},
{"eid":53,"ename":"Jacinthe","gender":"Female"},
{"eid":54,"ename":"Lucinda","gender":"Female"},
{"eid":55,"ename":"Doralin","gender":"Female"},
{"eid":56,"ename":"Baily","gender":"Male"},
{"eid":57,"ename":"Bud","gender":"Male"},
{"eid":58,"ename":"Antin","gender":"Male"},
{"eid":59,"ename":"Sayre","gender":"Female"},
{"eid":60,"ename":"Debora","gender":"Female"},
{"eid":61,"ename":"Chryste","gender":"Female"},
{"eid":62,"ename":"Broddy","gender":"Agender"},
{"eid":63,"ename":"Billi","gender":"Female"},
{"eid":64,"ename":"Evita","gender":"Female"},
{"eid":65,"ename":"Ingar","gender":"Male"},
{"eid":66,"ename":"Alejoa","gender":"Male"},
{"eid":67,"ename":"Arden","gender":"Bigender"},
{"eid":68,"ename":"Cassie","gender":"Male"},
{"eid":69,"ename":"Farrell","gender":"Male"},
{"eid":70,"ename":"Noreen","gender":"Female"},
{"eid":71,"ename":"Berton","gender":"Male"},
{"eid":72,"ename":"Lula","gender":"Female"},
{"eid":73,"ename":"Mady","gender":"Female"},
{"eid":74,"ename":"Prue","gender":"Female"},
{"eid":75,"ename":"Elia","gender":"Male"},
{"eid":76,"ename":"Rowan","gender":"Male"},
{"eid":77,"ename":"Arlyn","gender":"Female"},
{"eid":78,"ename":"Marmaduke","gender":"Male"},
{"eid":79,"ename":"Caz","gender":"Male"},
{"eid":80,"ename":"Mattie","gender":"Female"},
{"eid":81,"ename":"Dannie","gender":"Male"},
{"eid":82,"ename":"Norri","gender":"Female"},
{"eid":83,"ename":"Tricia","gender":"Female"},
{"eid":84,"ename":"Pauly","gender":"Male"},
{"eid":85,"ename":"Jo-ann","gender":"Female"},
{"eid":86,"ename":"Obadiah","gender":"Male"},
{"eid":87,"ename":"Christalle","gender":"Female"},
{"eid":88,"ename":"Derby","gender":"Male"},
{"eid":89,"ename":"Calley","gender":"Female"},
{"eid":90,"ename":"Ammamaria","gender":"Female"},
{"eid":91,"ename":"Christel","gender":"Female"},
{"eid":92,"ename":"Oswell","gender":"Male"},
{"eid":93,"ename":"Reynolds","gender":"Male"},
{"eid":94,"ename":"Sergent","gender":"Male"},
{"eid":95,"ename":"Farand","gender":"Female"},
{"eid":96,"ename":"Ursa","gender":"Bigender"},
{"eid":97,"ename":"Cassandry","gender":"Female"},
{"eid":98,"ename":"Park","gender":"Polygender"},
{"eid":99,"ename":"Cordula","gender":"Female"},
{"eid":100,"ename":"Nevil","gender":"Bigender"}]

# display only employee names using for and while

"""for emp in employees:
    #print(employees)
    print(emp['ename'])
"""
"""i=0
while i<=len(employees)-1:
    print(employees[i]['ename'])
    i=i+1
"""

"""for emp in employees:
    if emp['gender'] == 'Male':
         print(emp['ename'])"""

"""i=0
while i<=len(employees)-1:
    if employees[i]['gender'] == 'Female':
         print(employees[i]['ename'])
    i=i+1"""

"""no_of_male_emp = 0
for emp in employees:
    if emp['gender'] == 'Male':
        #no_of_male_emp = no_of_male_emp + 1
        no_of_male_emp += 1

print(len(employees))
print(no_of_male_emp )"""


i=0
no_of_female_emp = 0
while i<=len(employees)-1:
    if employees[i]['gender'] == 'Female':
        #no_of_female_emp += 1
        no_of_female_emp = no_of_female_emp + 1

    i=i+1
print(len(employees))
print(no_of_female_emp)

