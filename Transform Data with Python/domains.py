import read

df = read.load_data()

tmpcount = df['url'].value_counts()

tmpdomains_100 = tmpcount.head(100)

for name,row in tmpdomains_100.items():
    print('URL is {0} and total is {1}'.format(name,row))
    
