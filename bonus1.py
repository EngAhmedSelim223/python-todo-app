feet_inches = input("enter feet and inches: ")
def parse(feet_inches):
    result = [x for x in feet_inches.strip().split(" ")]
    feet = float(result[0])
    inches = float(result[-1])
    return (feet, inches)

def convert(feet, inches):
    
    meters = feet * 0.3048 + inches * 0.0254
    return meters
feet, inches = parse(feet_inches)
result = convert(feet , inches)
if result < 1:
    print(f"tall: {result} => Kid can't user slider")
else:
    print(f"tall: {result} => Kid can use slider")