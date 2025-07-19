weather_input= input("What's the weather like today? (sunny/rainy/cold):")
if weather_input.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_input.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_input.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("I don't have recommendations for this weather.")