filepath = "master_data.csv"   #input file path

outputFilePath = "outputstudent_data.csv"  # make sure the file name is unique in your directory






import csv



def read_csv_to_dict(filepath):
  """
  Reads a CSV file into a dictionary using the csv module.

  Args:
      filepath (str): Path to the CSV file.

  Returns:
      dict: A dictionary where keys are column names and values are lists of corresponding values.
  """

  try:
    with open(filepath, "r") as csvfile:
      reader = csv.reader(csvfile)
      headers = next(reader)  # Read the header row

      data_dict = []
      for row in reader:
        # Create a dictionary entry for each row using zip(headers, row)
        data_dict.append(dict(zip(headers, row)))
      print(f'Successfully read CSV file "{filepath}".')
      return data_dict

  except FileNotFoundError:
    print(f'Error: File {filepath} not found.')
    return None


students = read_csv_to_dict(filepath)


def calculateCreditPoints(gd,credit):
    if gd == '' or credit == '':
        return '0'
    return str(int(gd)*int(credit))

studentData = {}
i = 0
for student in students:
    
    id = student["ROLLNO"] + student["SEMESTER"]
    if id not in studentData:
        currentData = {
            "ORG_NAME": "National Institute of Technology Goa",
            "ORG_NAME_L": "",
            "ACADEMIC_COURSE_ID": student["STUDENTREGNO"],
            "COURSE_NAME": student["DEGREENAME"],
            "COURSE_NAME_L": "",
            "STREAM": student["BRANCH_PROGRAMME_NAME"],
            "STREAM_L": "",
            "SESSION": "",
            "REGN_NO": student["ROLLNO"],
            "RROLL": student["ROLLNO"],
            "CNAME": student["STUDENTNAME"],
            "GENDER": "",
            "DOB": "",
            "FNAME": "",
            "MNAME": "",
            "PHOTO": "",
            "MRKS_REC_STATUS": "",
            "RESULT": "",
            "YEAR": "",
            "MONTH": "",
            "DIVISION": "",
            "GRADE": "",
            "PERCENT": "",
            "DOI": "",
            "SEM": student["SEMESTER"],
            "EXAM_TYPE": "REGULAR",
            "TOT": "",
            "TOT_MRKS": "",
            "TOT_CREDIT": student["EARN_CREDITS"],
            "TOT_CREDIT_POINTS": student["EGP"],
            "TOT_GRADE_POINTS": "",
            "GRAND_TOT_MAX": "",
            "GRAND_TOT_MRKS": "",
            "GRAND_TOT_CREDIT_POINTS": student["CUMMULATIVE_CREDITS"],
            "CGPA": student["CGPA"],
            "REMARKS": "",
            "SGPA": student["SGPA"],
            "ABC_ACCOUNT_ID": "",
            "TERM_TYPE": "",
            "TOT_GRADE": "",
            "courseDetails": []
            }   
        studentData[id] = currentData
    
    count = len(studentData[id]["courseDetails"]) + 1
    studentData[id]["courseDetails"].append({
        "SUB1NM": student["COURSENAME"],
        "SUB1": student["COURSE_CODE"],
        "SUB1_TH_MAX": "",
        "SUB1_PR_MAX": "",
        "SUB1_CE_MAX": "",
        "SUB1_TH_MRKS": "",
        "SUB1_PR_MRKS": "",
        "SUB1_CE_MRKS": "",
        "SUB1_TOT": "",
        "SUB1_GRADE": student["GRADE"],
        "SUB1_GRADE_POINTS": student["GDPOINT"],
        "SUB1_CREDIT": student["CREDITS"],
        "SUB1_CREDIT_POINTS": calculateCreditPoints(student["GDPOINT"],student["CREDITS"]),
        "SUB1_REMARKS": "",
        "SUB1_CREDIT_ELIGIBILITY": "Y",
    })
    
  


data = studentData
header = ['ORG_NAME','ORG_NAME_L','ACADEMIC_COURSE_ID','COURSE_NAME','COURSE_NAME_L','STREAM','STREAM_L','SESSION','REGN_NO','RROLL','CNAME','GENDER','DOB','FNAME','MNAME','PHOTO','MRKS_REC_STATUS','RESULT', 'YEAR','MONTH','DIVISION','GRADE','PERCENT','DOI','SEM','EXAM_TYPE', 'TOT', 'TOT_MKS', 'TOT_CREDIT', 'TOT_CREDIT_POINTS', 'TOT_GRADE_POINTS','GRAND_TOT_MAX','GRAND_TOT_MRKS','GRAND_TOT_CREDIT_POINTS','CGPA','REMARKS','SGPA','ABC_ACCOUNT_ID','TERM_TYPE','TOT_GRADE']
for i in range(1, 11):                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    header.extend([f'SUB{i}NM', f'SUB{i}',f'SUB{i}_TH_MAX',	f'SUB{i}_PR_MAX',f'SUB{i}_CE_MAX',f'SUB{i}_TH_MRKS',f'SUB{i}_PR_MRKS',f'SUB{i}_CE_MRKS',f'SUB{i}_TOT',f'SUB{i}_GRADE', f'SUB{i}_GRADE_POINTS', f'SUB{i}_CREDIT',f'SUB{i}_CREDIT_POINTS',f'SUB{i}_REMARKS',f'SUB{i}_CREDIT_ELIGIBILITY'])
    if i==1:
        header.extend(['AADHAAR_NAME','ADMISSION_YEAR'])



with open(outputFilePath, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    

    for student_id, student_data in data.items():
        # Combine common student data with empty subject details
        row = [value for key,value  in student_data.items()]
        row.pop()
        course_details = student_data.get("courseDetails", [])
        i = 1
        gradePoints = 0
        for course in course_details:
            
            for key,value in course.items():
                row.append(value)
                if key=='SUB1_GRADE_POINTS':
                    gradePoints+= 0 if value=='' else int(value) 
            if i==1:
                row.extend(['',''])

            i+=1
        row[30] = str(gradePoints) 
        
        writer.writerow(row)

print("CSV file created successfully!")
