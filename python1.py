start = int(input("Current Time:"))
interval = int(input("Alarm after:"))
end = (start + interval) % 24
print("Alarm rings at", end)
