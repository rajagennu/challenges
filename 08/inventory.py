room_name = []

def get_names():

	global room_name
	rooms_count = int(input("Enter how many rooms are there in your house: "))
	while rooms_count > 0 :
		room_name.append(str(input("Enter room name and press enter: ")))
		rooms_count = rooms_count -  1 

	return room_name 









print(get_names())
#print_names()
#load_items()






