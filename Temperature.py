class Temperature:
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

# Example usage:
temp = Temperature()
temp.convertFahrenheit(30)  # Convert 30 Celsius to Fahrenheit
temp.convertCelsius(86)     # Convert 86 Fahrenheit to Celsius
