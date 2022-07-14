duration = int(input("Секунды: "))
hour = duration // 3600
duration %= 3600
minutes = duration // 60
duration %= 60
print(f"{hour:02}:{minutes:02}:{duration:02}")
