feet_inches = input("enter feet and inches: ")

def convert(feet_inches):
    result = [x for x in feet_inches.strip().split(" ")]
    feet = float(result[0])
    inches = float(result[-1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches= feet_inches)
if result < 1:
    print("Kid can't user slider")
else:
    print("Kid can use slider")