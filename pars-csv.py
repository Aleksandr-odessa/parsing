import  csv

FILE_NAME='rabota.csv'
text = []
with open('vacancies.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f,delimiter = ",",skipinitialspace = True)
    for row in reader:
        text.append(row) 
with open(FILE_NAME,'w', encoding="utf-8") as files:
    for i in range(len(text)):
        for j in range(len(text[i])):
            text[i][j]=text[i][j].replace('\n', '').replace('  ', '').replace('\xa0', ' ')
            files.write(text[i][j])
            print(text[i][j])
            with open(FILE_NAME,'w', encoding="utf-8") as f:
                writer = csv.writer(f, delimiter ='\n')
                writer.writerow(text[i][j])
                print('success')