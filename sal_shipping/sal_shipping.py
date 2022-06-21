# weight of package for ground shipping 
ground_weight = 41.5

#Ground shipping rate
if ground_weight <= 2:
  ground_price = 20 + (ground_weight * 1.50)
elif ground_weight <= 6:
  ground_price = 20 + (ground_weight * 3)
elif ground_weight <= 10:
  ground_price = 20 + (ground_weight * 4)
else:
  ground_price = 20 + (ground_weight * 4.75)

print(ground_price)

#premium ground shipping
premium_ground_shipping = 125
print("Ground Shipping Premium is $",premium_ground_shipping) 

#Weight of package for drone shipping 
drone_weight = 41.5
if drone_weight <= 2:
  drone_price = 4.50 * drone_weight 
elif drone_weight <= 6:
  drone_price = 9 * drone_weight
elif drone_weight <= 10:
  drone_price = 12 * drone_weight
else:
  drone_price = 14.25 * drone_weight 

print(drone_price)



