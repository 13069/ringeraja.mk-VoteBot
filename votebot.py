#Внимание: Оваа скрипта е дадена само за едукативни цели. Секоја употреба на оваа скрипта со цел автоматско гласање или која било друга форма на неовластен пристап до онлајн услуги може да ги прекрши условите за користење на целната веб-локација и потенцијално може да биде незаконска. Важно е да се почитуваат условите за користење и упатствата обезбедени од веб-локациите и онлајн платформите. Неовластен пристап или манипулација со онлајн системи може да резултира со правни последици. Корисникот на оваа скрипта е единствено одговорен за какви било последици кои произлегуваат од неговата употреба. Со користење на оваа скрипта, вие се согласувате да го обештетите и да ги држите безопасни авторот на сценариото и сите поврзани субјекти од каква било одговорност што произлегува од неговата употреба.
# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.
#Автор на оваа скрипта е: Леонид Крстевски

import requests

# URL на веб-страницата
url = "https://www.ringeraja.mk/portleti/ankete/pollVote.asp"

# Проследи на корисникот да избере опција за гласање
option = input("Изберете опција за гласање (1, 2, или 3): ")

# Провери дали избраната опција е валидна
if option not in ["1", "2", "3"]:
    print("Невалидна опција. Изберете 1, 2, или 3.")
else:
    # Податоците за гласање
    vote_data = {
        "postBack": "1",
        "ID": "1564",    # ID на анкетата
        "vote": option  # Вредност на избраната опција
    }

    # Проследи на корисникот да внесе број на гласови
    num_votes = int(input("Внесете број на гласови (од 1 до 50): "))

    # Провери дали бројот на гласови е во дозволениот опсег
    if num_votes < 1 or num_votes > 50:
        print("Невалиден број на гласови. Внесете број помеѓу 1 и 50.")
    else:
        # Проследи гласање повеќе пати
        for _ in range(num_votes):
            response_vote = requests.post(url, data=vote_data)
            
            # Провери резултат за секој глас
            if response_vote.status_code == 200:
                print("Гласот е успешен!")
            else:
                print("Гласот не е успешен.")
                

#Внимание: Оваа скрипта е дадена само за едукативни цели. Секоја употреба на оваа скрипта со цел автоматско гласање или која било друга форма на неовластен пристап до онлајн услуги може да ги прекрши условите за користење на целната веб-локација и потенцијално може да биде незаконска. Важно е да се почитуваат условите за користење и упатствата обезбедени од веб-локациите и онлајн платформите. Неовластен пристап или манипулација со онлајн системи може да резултира со правни последици. Корисникот на оваа скрипта е единствено одговорен за какви било последици кои произлегуваат од неговата употреба. Со користење на оваа скрипта, вие се согласувате да го обештетите и да ги држите безопасни авторот на сценариото и сите поврзани субјекти од каква било одговорност што произлегува од неговата употреба.
# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.
#Автор на оваа скрипта е: Леонид Крстевски
