import re
from bs4 import BeautifulSoup
import pandas as pd
def scrape(path):
    
    with open(path, 'r') as file:
        html_data = file.read()

   
    soup = BeautifulSoup(html_data, 'html.parser')

    student_results = []

    matric_numbers = [m.string for m in soup.find_all("td", string=re.compile("EU"))]
   
    for student in matric_numbers:
        student_result = {}
        student_row = soup.find("td", string=re.compile(student))
        student_parent = student_row.find_parent("tr").find_all("td", attrs={"align": "center"})
        student_courses = [td.next_element.next_element.next_element.strip().replace(" (", "") for td in student_parent]
        student_grades = [td.next_element.next_element.contents[-1].strip() for td in student_parent]
        student_result["MATRIC_NUMBER"] = student
        student_result.update(dict(zip(student_courses, student_grades)))
        student_results.append(student_result)
    
    df = pd.DataFrame(student_results)
    
    
    df.to_excel('result_data.xlsx', index=False)
    return 'result_data.xlsx'

scrape('Home_Elizade_University_Portal.html')
scrape('100l.html')
