# a.
# getting familiar with print() and its formating capabilities(end and sep)
print("Hello, world!")
print("Python", "is an interpreted", "language", sep='-', end=" ...")
print("python3 is the latest Python programming language release\n")

#b.
print("     *")
print("     *")
print("    * *")
print("   *   *")
print("  *     *")
print("**       **")
print("*         *")
print("*         *")
print("***********")


banner = """
   ____                   _      ____  _     _
  / ___| ___   ___   __ _| |__  / ___|| |__ (_)_ __   __ _
 | |  _ / _ \ / _ \ / _` | '_ \| |   | '_ \| | '_ \ / _` |
 | |_| | (_) | (_) | (_| | | | | |___| | | | | | | | | (_| |
  \____|\___/ \___/ \__, |_| |_|\____|_| |_|_|_| |_|\__, |
                   |___/                            |___/
"""

print(banner)



















# a leap year is a year that contains an extra day, Feb 29th.
# rules for determing a leap year: divisibility by 4,

# leap_year: determine if year is leap or not
# @year - year to determine
# return - True if leap year or False if not leap year
def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

print(leap_year(2020))
print(leap_year(1990))

test_data = [2020, 2034, 5989, 6960, 2001, 2003]
test_results = [True, False]

for x in test_data:
    yr = leap_year(x)
    for i in test_results:
        if yr == i:
            print(f"{x} is a leap year")
        else:
            print(f"{x} is not a leap year")

