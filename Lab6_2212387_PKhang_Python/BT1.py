import pandas as pd
df = pd.read_csv(r'E:\Python\Lab6_2212387_PKhang_Python\Automobile_data.csv')
print(df) 
print(df.head(6))

print (df.tail(7))

print(df.head(11))

#df = df[['company','price']][df.price == df['price'].max()]
#print(df)

#car_Manufacturers = df.groupby('company')
#toyota = car_Manufacturers.get_group('toyota')
#print(toyota)

#print(df['company'].value_counts())

car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers[['company','price']].mean('price')
print(priceDf)