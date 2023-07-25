res = bs4.BeautifulSoup(url.text,"html.parser")
# now you want 2 files one for text content of the web and secondly the code of the web
saveFile1 = open("Web_Text.txt","a") # with a append mode
for i in res.select('p'):
    saveFile1.write(i.getText())
saveFile1.close() # most impact never forget to close your file after opening

saveFile2 = open("Web_Code.txt","a") # with a append mode
for i in res.select('p'):
    saveFile2.write(res.prettify())
saveFile2.close()

#TODO: pasting code from another file 
soup = BeautifulSoup(url.text, 'html.parser')

table = soup.find('tbody')
print(table)

A = []
B = []
C = []
D = []
E = []
F = []

for row in table.findAll('tr'):
    cells = row.findAll('td')
    A.append(cells[0].text)
    B.append(cells[1].text)
    C.append(cells[2].text)
    D.append(cells[3].text)
    E.append(cells[4].text)
    F.append(cells[5].text)
df = pd.DataFrame(A, columns=['Country'])
df['Gold'] = B
df['Silver'] = C
df['Bronze'] = D
df['Total Medals'] = E
df['2021 Population'] = F
print(df)

df.to_csv('data.csv')
os.startfile('.\\data.csv')
