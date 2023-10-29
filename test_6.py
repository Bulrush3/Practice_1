from bs4 import BeautifulSoup
import json

str_json = ''
with open('r_text_6_v2.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        str_json += line

data = json.loads(str_json)
data = data['data']

soup = BeautifulSoup("""<table>
    <tr>
        <th>symbol</th>
        <th>open</th>
        <th>high</th>
        <th>low</th>
        <th>close</th>
        <th>amount</th>
        <th>vol</th>
        <th>count</th>
        <th>bid</th>
        <th>bidSize</th>
        <th>ask</th>
        <th>askSize</th>
    </tr>
</table>""",  "html.parser")

table = soup.contents[0]

# print(table)

for tick in data:
    tr = soup.new_tag("tr")
    for key, val in tick.items():
        td = soup.new_tag("td")
        td.string = str(val)
        tr.append(td)
    table.append(tr)

# # print(soup.prettify())


with open('r_text_6_v2.html', 'w') as result:
    result.write(soup.prettify())
    result.write("\n")