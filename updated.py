#enter the file name of the pdf that contains the grade cards
pdf_filepath = "sample.pdf"  #the grade cards should not have headers

#enter the file name of the csv output file
output_csv_filepath = 'sample2.csv' # make sure this file doesn't already exist in the directory










import PyPDF2
import fitz  # PyMuPDF library
import datetime

# date_str = "31/05/2024"
# date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")

# month_name = date_obj.strftime("%B")
# year = date_obj.year

# print(f"Month: {month_name}")
# print(f"Year: {year}")




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
def findGradePoints(grade):
  grade_points = {"s": 10, "a": 9, "b": 8, "c": 7, "d": 6, 'p': 5, 'w': 0, "f": 0}
  return grade_points.get(grade.lower(), None)


def parse_grade_report(grade_report_text):
    data = {}
    lines = grade_report_text.strip().split('\n')
    # print("line:",lines)
    data['ORG_NAME'] = 'National Institute of Technology Goa'
    data['ORG_NAME_L'] = ''
    data['COURSE_NAME_L'] = ''
    data['STREAM_L'] = ''
    data['SESSION'] = ''
    data['PROGRAMME'] = lines[1].strip().split(':')[1].strip()
    data['DISCIPLINE'] = lines[6].strip().split(':')[1].strip()
    data['NAME'] = lines[9].strip()
    data['ROLL NO'] = lines[10].strip()
    data['SEMESTER'] = lines[11].strip()
    data['YEAR'] = lines[13].strip()
    data['DATE'] = lines[12].strip()
    
    date_obj = datetime.datetime.strptime(data['DATE'], "%d/%m/%Y")

    data['GRADEMONTH'] = date_obj.strftime("%B")
    data['GRADEYEAR'] = date_obj.year

    
    grades = []
    for index,line in enumerate(lines[19::4]):
        grade = line.strip()
        if(grade=="EARNED CREDITS"):
            break
        credit = lines[19+index*4+1].strip()
        subject_name = lines[19+index*4+2].strip()
        subject_code = lines[19+index*4+3].strip()
        gradePoints = findGradePoints(grade)
        creditPoints = gradePoints * int(credit)
        grades.append((subject_name, subject_code,'','','','','','','', grade, gradePoints, credit,creditPoints,'','Y'))
        
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

# Define the header row ORG_NAME	ORG_NAME_L	ACADEMIC_COURSE_ID	COURSE_NAME	COURSE_NAME_L	STREAM	STREAM_L	SESSION	REGN_NO	RROLL	CNAME	GENDER	DOB	FNAME	MNAME	PHOTO	MRKS_REC_STATUS	RESULT	YEAR	MONTH	DIVISION	GRADE	PERCENT	DOI	SEM	EXAM_TYPE	TOT	TOT_MRKS	TOT_CREDIT	TOT_CREDIT_POINTS	TOT_GRADE_POINTS	GRAND_TOT_MAX	GRAND_TOT_MRKS	GRAND_TOT_CREDIT_POINTS	CGPA	REMARKS	SGPA	ABC_ACCOUNT_ID	TERM_TYPE	TOT_GRADE	SUB1NM	SUB1	SUB1_TH_MAX	SUB1_PR_MAX	SUB1_CE_MAX	SUB1_TH_MRKS	SUB1_PR_MRKS	SUB1_CE_MRKS	SUB1_TOT	SUB1_GRADE	SUB1_GRADE_POINTS	SUB1_CREDIT	SUB1_CREDIT_POINTS	SUB1_REMARKS	SUB1_CREDIT_ELIGIBILITY	AADHAAR_NAME	ADMISSION_YEAR	SUB2NM	SUB2	SUB2_TH_MAX	SUB2_PR_MAX	SUB2_CE_MAX	SUB2_TH_MRKS	SUB2_PR_MRKS	SUB2_CE_MRKS	SUB2_TOT	SUB2_GRADE	SUB2_GRADE_POINTS	SUB2_CREDIT	SUB2_CREDIT_POINTS	SUB2_REMARKS	SUB2_CREDIT_ELIGIBILITY	SUB3NM	SUB3	SUB3_TH_MAX	SUB3_PR_MAX	SUB3_CE_MAX	SUB3_TH_MRKS	SUB3_PR_MRKS	SUB3_CE_MRKS	SUB3_TOT	SUB3_GRADE	SUB3_GRADE_POINTS	SUB3_CREDIT	SUB3_CREDIT_POINTS	SUB3_REMARKS	SUB3_CREDIT_ELIGIBILITY	SUB4NM	SUB4	SUB4_TH_MAX	SUB4_PR_MAX	SUB4_CE_MAX	SUB4_TH_MRKS	SUB4_PR_MRKS	SUB4_CE_MRKS	SUB4_TOT	SUB4_GRADE	SUB4_GRADE_POINTS	SUB4_CREDIT	SUB4_CREDIT_POINTS	SUB4_REMARKS	SUB4_CREDIT_ELIGIBILITY	SUB5NM	SUB5	SUB5_TH_MAX	SUB5_PR_MAX	SUB5_CE_MAX	SUB5_TH_MRKS	SUB5_PR_MRKS	SUB5_CE_MRKS	SUB5_TOT	SUB5_GRADE	SUB5_GRADE_POINTS	SUB5_CREDIT	SUB5_CREDIT_POINTS	SUB5_REMARKS	SUB5_CREDIT_ELIGIBILITY	SUB6NM	SUB6	SUB6_TH_MAX	SUB6_PR_MAX	SUB6_CE_MAX	SUB6_TH_MRKS	SUB6_PR_MRKS	SUB6_CE_MRKS	SUB6_TOT	SUB6_GRADE	SUB6_GRADE_POINTS	SUB6_CREDIT	SUB6_CREDIT_POINTS	SUB6_REMARKS	SUB6_CREDIT_ELIGIBILITY	SUB7NM	SUB7	SUB7_TH_MAX	SUB7_PR_MAX	SUB7_CE_MAX	SUB7_TH_MRKS	SUB7_PR_MRKS	SUB7_CE_MRKS	SUB7_TOT	SUB7_GRADE	SUB7_GRADE_POINTS	SUB7_CREDIT	SUB7_CREDIT_POINTS	SUB7_REMARKS	SUB7_CREDIT_ELIGIBILITY	SUB8NM	SUB8	SUB8_TH_MAX	SUB8_PR_MAX	SUB8_CE_MAX	SUB8_TH_MRKS	SUB8_PR_MRKS	SUB8_CE_MRKS	SUB8_TOT	SUB8_GRADE	SUB8_GRADE_POINTS	SUB8_CREDIT	SUB8_CREDIT_POINTS	SUB8_REMARKS	SUB8_CREDIT_ELIGIBILITY

header = ['ORG_NAME','ORG_NAME_L','ACADEMIC_COURSE_ID','COURSE_NAME','COURSE_NAME_L','STREAM','STREAM_L','SESSION','REGN_NO','RROLL NO','CNAME','GENDER','DOB','FNAME','MNAME','PHOTO','MRKS_REC_STATUS','RESULT', 'YEAR','MONTH','DIVISION','GRADE','PERCENT','DOI','SEM','EXAM_TYPE', 'TOT', 'TOT_MKS', 'TOT_CREDIT', 'TOT_CREDIT_POINTS', 'TOT_GRADE_POINTS','GRAND_TOT_MAX','GRAND_TOT_MRKS','GRAND_TOT_CREDIT_POINTS','CGPA','REMARKS','SGPA','ABC_ACCOUNT_ID','TERM_TYPE','TOT_GRADE']
for i in range(1, 11):
    header.extend([f'SUB{i}NM', f'SUB{i}',f'SUB{i}_TH_MAX',	f'SUB{i}_PR_MAX',f'SUB{i}_CE_MAX',f'SUB{i}_TH_MRKS',f'SUB{i}_PR_MRKS',f'SUB{i}_CE_MRKS',f'SUB{i}_TOT',f'SUB{i}_GRADE', f'SUB{i}_GRADE_POINTS', f'SUB{i}_CREDIT',f'SUB{i}_CREDIT_POINTS',f'SUB{i}_REMARKS',f'SUB{i}_CREDIT_ELIGIBILITY'])
    if i==1:
        header.extend(['AADHAAR_NAME','ADMISSION_YEAR'])
#SUB1NM	SUB1	SUB1_TH_MAX	SUB1_PR_MAX	SUB1_CE_MAX	SUB1_TH_MRKS	SUB1_PR_MRKS	SUB1_CE_MRKS	SUB1_TOT	SUB1_GRADE	SUB1_GRADE_POINTS	SUB1_CREDIT	SUB1_CREDIT_POINTS	SUB1_REMARKS	SUB1_CREDIT_ELIGIBILITY
#Operating System	CS300								A	9	4	36	*	Y

# Open the CSV file for writing
with open(output_csv_filepath, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(header)

    # Write student data to the CSV file
    for student in student_data:
        row = [
            'National Institute of Technology Goa',
            '',
            student['ROLL NO'],
            student['PROGRAMME'], 
            '',
               student['DISCIPLINE'], 
               '',
               '',
               student['ROLL NO'], 
               student['ROLL NO'], 
               student['NAME'], 
               '',
               '',
               '',
               '',
               '',
               'O',
               '',
               student['GRADEYEAR'],
               student['GRADEMONTH'],
               '','','','',
               student['SEMESTER'], 
               'REGULAR','','',
               student['EARNED CREDITS'], 
               student['TOTAL EARNED CREDITS'], 
               student['EARNED GRADE POINTS'],
               '','',
               student['TOTAL EARNED GRADE POINTS'],
               student['CGPA'], '',
               student['SGPA'],  '','','',
               
               ]


        # Add subject information to the row

        for i, subject in enumerate(student['GRADES']):
            row.extend([subject[0], subject[1], subject[2], subject[3],subject[4], subject[5], subject[6], subject[7],subject[8], subject[9], subject[10], subject[11],subject[12], subject[13], subject[14]])
            if i==0:
                row.extend(['',''])

        # Fill remaining subject cells with empty strings
        remaining_cells = (10 - len(student['GRADES'])) * 4
        row.extend([''] * remaining_cells)

        # Write the row to the CSV file
        writer.writerow(row)