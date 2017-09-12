def add(b):
	b.append(100)
	b = [10, 12]

class Car(object):
    def make_car_sound():
        print('VRooooommmm!')
b = [5]
add(b)
print(b)
Car.make_car_sound()
