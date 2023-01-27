Student = { 
  'UE183001': 'Avish', 
  'UE183002': 'Bhavya', 
  'UE183003': 'Tanya',
  'UE183004': 'John',
  'UE183005': 'Jane',
  'UE183006': 'Mike',
  'UE183007': 'Sara',
  'UE183008': 'David',
  'UE183009': 'Emily',
  'UE183010': 'Jessica',
}
Marks = [
  ('UE183001', 'CS', 92 ), 
  ('UE183002', 'CS', 61 ), 
  ('UE183001', 'RV', 90), 
  ('UE183002', 'CS', 74), 
  ('UE183003', 'CS', 64),
  ('UE183004', 'CS', 81),
  ('UE183005', 'RV', 77),
  ('UE183006', 'CS', 94),
  ('UE183007', 'RV', 63),
  ('UE183008', 'CS', 79),
  ('UE183009', 'RV', 80),
  ('UE183010', 'CS', 66),
]

student_marks = {}


for roll_no, subject, marks in Marks:
    # Check if the roll number already exists in the dictionary
    if roll_no in student_marks:
        # If it does, add the marks to the existing value
        student_marks[roll_no] += marks
    else:
        # If it doesn't, add the roll number as a key and the marks as the value
        student_marks[roll_no] = marks


for roll_no, total_marks in student_marks.items():
    print(f"{Student[roll_no]}: {total_marks}")
