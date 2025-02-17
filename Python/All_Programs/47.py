print('Welcome to CarDekho, where you get your dream car!')
minimum_price = 10000
maximum_price = 1000000
carDetails = {
    'Tata': { 
        'price': 200000,
        'type': 'CNG'
    },
    'SUV': {
        'price': 500000,
        'type': 'Diesel'
    }
}

try:
    car_model = input("Enter the car model (Tata/SUV): ")
    car_price = int(input('Enter price range of your choice:'))
   
    if car_price < minimum_price:
        raise ('Enter price greater than 10000')
     
    if car_model in carDetails:
        print(f"Details for {car_model}:")
        print(f"Price: ₹{carDetails[car_model]['price']}")
        print(f"Fuel Type: {carDetails[car_model]['type']}")

    else:
        raise ValueError("Invalid car name")  


except ValueError as e:
    print(e)  
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
