sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, Please use numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.00) * (fr * 0.5)
    xp = reg + otp
else:
    xp = float(sh) * float(sr)
print("pay:", xp)