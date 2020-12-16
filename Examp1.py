
#Its coding for Restaurant's Geust Examaple
guest_list = ['Ibtihaj', 'Jumaimah', 'Ahil']
masg = 'Please join my diner party'
#Give the name in three lines
#print(f"{masg.title()} \nIbtihaj\nJumaimah\nAhil." )

print(f"{masg.title()} Ibtihaj." )
print(f"{masg.title()} Jumaimah." )
print(f"{masg.title()} Ahil." )
#One guest unable to join
print("oh! We miss Ahil, he can't make it! I will invite Marjia instead :)")
#Modify my gest list
#del guest_list[2]
#print(guest_list)
#Add somebody in guest list
#guest_list.append("Marjia")
#print(guest_list)
#****Another way to add
guest_list[2] = "Marjia"
print(f"New Guest List is {guest_list}")
print(f"{masg.title()} Ibtihaj." )
print(f"{masg.title()} Jumaima." )
print(f"{masg.title()} Marjia." )

#Add Three more Guest

print("Oh Just found that I have more space for three more Guests! Lets invite more :) ")
#guest_list.append("Ayaz")
#guest_list.append("Ayan")
#guest_list.append("Tutu")
#print(guest_list)

#Add there more guest by using inserting method

guest_list.insert(0, "Ayaz")
guest_list.insert(2, "Ayan")
guest_list.append("Tutu")
print(guest_list)

# Cut the list shorter using pop() function
print("Hello Guys! Sorry to say that My new table didn't arrive, So I can invite Only Two guest!")
final_list = guest_list.pop(4)
print("Sorry! Marjia, see you next time!")
print(guest_list)
final_list2 = guest_list.pop(2)
print("Sorry! Ayan, see you next time!")
print(guest_list)
print("Sorry! Ayaz, see you next time!")
final_list3 = guest_list.pop(0)
print(guest_list)
#len(guest_list)
print(len(guest_list))

print("So guys I have invited total: " "+ guest_list + ")

#print("Sorry! Ayan, see you next time!")
#print(guest_list)
#guest_list.append("Jumaimah")
#print(guest_list)






