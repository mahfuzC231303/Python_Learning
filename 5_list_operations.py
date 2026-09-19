bikes=['Honda','Yamaha','Suzuki']
print(bikes)
bikes[0]='Hero'
print(bikes)

bikes.append('Ducati')
bikes.append('Kawaasaki')
bikes.append('Ducati')
print(bikes)

bikes.insert(1,'Honda')
print(bikes)

del bikes[2]
print(bikes)

pop_value=bikes.pop(1)
print(bikes)
print(pop_value)

bikes.remove('Ducati')
print(bikes)