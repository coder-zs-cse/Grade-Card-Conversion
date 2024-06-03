
### Enter the relative file path of the pdf file you want to extract grade card information from

pdf_filepath = "sample.pdf"


### Enter the name of the output csv file. 
#Make sure it is unique and such a file does not exist already in your directory

output_csv_filepath = 'sample.csv'






import PyPDF2
import fitz  # PyMuPDF library


def read_pdf_text(filepath):
  """
  Reads all recognized text from a PDF file and prints it.

  Args:
    filepath: Path to the PDF file.
    
  """
  student_data = []
  try:

    with fitz.open(filepath) as pdf_file:
      for i in range(pdf_file.page_count):
        pdf_reader = pdf_file[i].get_text("text")
        student_data.append(pdf_reader)
      return student_data

  except FileNotFoundError:
    print(f"Error: PDF file not found at {filepath}")


# # Example usage
# pdf_filepath = "mergedPDF.pdf"
# extractedText = read_pdf_text(pdf_filepath)


def parse_grade_report(grade_report_text):
    data = {}
    lines = grade_report_text.strip().split('\n')
    # print("line:",lines)
    data['PROGRAMME'] = lines[1].strip().split(':')[1].strip()
    data['DISCIPLINE'] = lines[6].strip().split(':')[1].strip()
    data['NAME'] = lines[9].strip()
    data['ROLL NO'] = lines[10].strip()
    data['SEMESTER'] = lines[11].strip()
    data['YEAR'] = lines[13].strip()

    grades = []
    for index,line in enumerate(lines[19::4]):
        grade = line.strip()
        if(grade=="EARNED CREDITS"):
            break
        credit = lines[19+index*4+1].strip()
        subject_name = lines[19+index*4+2].strip()
        subject_code = lines[19+index*4+3].strip()
        grades.append((subject_code, subject_name, credit, grade))
        
    # print(grades)
    # print(data)
    data['GRADES'] = grades
    data['REGISTERED CREDITS'] = lines[-7].strip()
    data['EARNED CREDITS'] = lines[-9].strip()
    data['EARNED GRADE POINTS'] = lines[-4].strip()
    data['SGPA'] = lines[-5].strip()
    data['TOTAL EARNED CREDITS'] = lines[-8].strip()
    data['TOTAL EARNED GRADE POINTS'] = lines[-3].strip()
    data['CGPA'] = lines[-6].strip()

    return data



extractedText = read_pdf_text(pdf_filepath)

student_data = []
for student in extractedText:
    student_data.append(parse_grade_report(student))



import csv

# Define the header row
header = ['PROGRAMME','DISCIPLINE','NAME', 'ROLL NO', 'SEMESTER', 'YEAR', 'SGPA', 'CGPA', 'REGISTERED CREDITS','EARNED CREDITS', 'TOTAL EARNED CREDITS', 'EARNED GRADE POINTS','TOTAL EARNED GRADE POINTS']
for i in range(1, 11):
    header.extend([f'course{i}_code', f'course{i}_name', f'course{i}_grade', f'course{i}_credit'])

# Open the CSV file for writing
with open(output_csv_filepath, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(header)

    # Write student data to the CSV file
    for student in student_data:
        row = [student['PROGRAMME'], student['DISCIPLINE'], student['NAME'], student['ROLL NO'], student['SEMESTER'], student['YEAR'], student['SGPA'], student['CGPA'], student['REGISTERED CREDITS'], student['EARNED CREDITS'], student['TOTAL EARNED CREDITS'], student['EARNED GRADE POINTS'],student['TOTAL EARNED GRADE POINTS']]

        # Add subject information to the row
        for i, subject in enumerate(student['GRADES'], start=1):
            row.extend([subject[0], subject[1], subject[3], subject[2]])

        # Fill remaining subject cells with empty strings
        remaining_cells = (10 - len(student['GRADES'])) * 4
        row.extend([''] * remaining_cells)

        # Write the row to the CSV file
        writer.writerow(row)




