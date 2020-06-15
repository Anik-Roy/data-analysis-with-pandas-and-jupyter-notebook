import requests
from requests.compat import quote_plus
import pandas as pd
import json
import time

BASE_URL = 'https://www.lus.ac.bd/wp-admin/admin-ajax.php'

# Create your views here.
def index():
    student_id = '1512020284'
    birth_date = '1996-12-04'

    all_results = pd.DataFrame()
    
    my_data = {
        'student_id':student_id,
        'birth_date':birth_date,
        'action': 'get-result'
    }

    x = requests.post(BASE_URL, data = my_data)
    #print(x.content)
    data = x.json()

    if( data['success'] ):
        print(data['success'])
        print(data['student']['name'])
        print(data['student']['id'])
        print(data['student']['grade'])
        print(data['student']['cgpa'])

        result = pd.DataFrame(
                    {
                        'Student ID':[data['student']['id']],
                        'Student Name':[data['student']['name']],
                        'Grade':[data['student']['grade']],
                        'CGPA':[data['student']['cgpa']]
                    },
                    columns=["Student ID", "Student Name", "Grade", "CGPA"],
                    index=[1]
                )
        
        print(result)

    # for year in range(1993, 1997):
    #     for month in range(1, 13):
    #         for date in range(1, 31):
    #             birth_year = str(year)
    #             birth_month = ''
    #             birth_date2 = ''

    #             if month < 10:
    #                 birth_month = '0'.join(str(month))
    #             else:
    #                 birth_month = str(month)

    #             if date < 10:
    #                 birth_date2 = '0'.join(str(date))
    #             else:
    #                 birth_date2 = str(date)
                
    #             birth_date = birth_year+'-'+birth_month+'-'+birth_date2

    #             for id in range(1522020012, 1522020050):
    #                 student_id = str(id)
    #                 print(student_id)

    #                 my_data = {
    #                     'student_id':student_id,
    #                     'birth_date':birth_date,
    #                     'action': 'get-result'
    #                 }

    #                 x = requests.post(BASE_URL, data = my_data)
    #                 #print(x.content)
    #                 data = x.json()
                    
    #                 if( data['success'] ):
    #                     print(data['success'])
    #                     # print(data['student']['name'])
    #                     # print(data['student']['id'])
    #                     # print(data['student']['grade'])
    #                     # print(data['student']['cgpa'])

    #                     result = pd.DataFrame(
    #                                 {
    #                                     'Student ID':[data['student']['id']],
    #                                     'Student name':[data['student']['name']],
    #                                     'Grade':[data['student']['grade']],
    #                                     'CGPA':[data['student']['cgpa']]
    #                                 },
    #                                 columns=["Student ID", "Student Name", "Grade", "CGPA"]
    #                             )
    #                     result.set_index('Student ID')
    #                     print(result)

    #                     all_results = all_results.append(result, ignore_index = True)

    #                 time.sleep(1)
    # print(all_results)
    # all_results.to_csv('all_result.csv')
    #return render(request, 'base.html')

index()