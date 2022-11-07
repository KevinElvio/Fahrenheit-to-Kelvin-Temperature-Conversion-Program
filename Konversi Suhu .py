#Program Konversi suhu Farenheit ke Kelvin dan sebaliknya
fahrenheit = float(input("Masukan Nilai Fahrenheit: "))
celcius = (fahrenheit -32) * (5/9)
kelvin = celcius + 273
print("Nilai kelvin",kelvin,("kelvin"))

kelvin = float(input("Masukan Nilai Kelvin: "))
celcius = (kelvin - 273)
fahrenheit = (celcius * (9/5)) + 32
print("Nilai Fahrenheit",fahrenheit,("fahrenheit"))
