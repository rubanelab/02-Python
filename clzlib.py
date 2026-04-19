class SubfieldsInAI():
  def Subfields():
    fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
    print("Sub-fields in AI are:")

    for field in fields:
      print(field)

class OddEven():
  def OddEven():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
      print(number, "is even number")
    else:
      print(number, "is odd number")

class ElegiblityForMarriage():
  def marriage_eligibility(gender, age):
    if gender == "male":
      if age < 21:
        print("NOT ELIGIBLE")
      else:
        print("ELIGIBLE")
    else:
      if age < 18:
        print("NOT ELIGIBLE")
      else:
        print("ELIGIBLE")

class FindPercent():
  def percentage():
    subject1 = int(input("Subject1 = "))
    subject2 = int(input("Subject2 = "))
    subject3 = int(input("Subject3 = "))
    subject4 = int(input("Subject4 = "))
    subject5 = int(input("Subject5 = "))

    total = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = total / 5

    print("Total: ", total)
    print("Percentage: ", percentage)

class Triangle():
  def triangle(height, breadth):
    print("Height:", height)
    print("Breadth:", breadth)
    print("Area of triangle:", (height * breadth) / 2)
