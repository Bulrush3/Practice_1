from bs4 import BeautifulSoup
import csv

items = list()

with open('text_5_var_60', encoding='utf-8') as file:
    lines = file.readlines()
    html = ''
    for line in lines:
        html += line

    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    rows = soup.find_all('tr')
    print(rows)
    rows = rows[1:]
    for row in rows:
        cells = row.find_all("td")
        print
        item = {
            'company': cells[0].text,
            'contact': cells[1].text,
            'country': cells[2].text,
            'price': cells[3].text,
            'item': cells[4].text
        }
        items.append(item)

with open('r_text_5.csv', 'w', encoding="utf-8", newline='') as result:
    writer = csv.writer(result, delimiter=',', quotechar='*', quoting=csv.QUOTE_MINIMAL)

    for item in items:
        writer.writerow(item.values())
