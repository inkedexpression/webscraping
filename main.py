from operator import index

import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
job_list = []
for page in range(1,803):
    web = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={page}&startPage=1').text
    soup = BeautifulSoup(web,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
            company_name = job.find('h3',class_='joblist-comp-name').text.strip()
            skills = job.find('div',class_='srp-skills').text
            skills = ' '.join(skills.split())
            skills = skills.replace(" ", ", ")
            more_info = job.header.h2.a['href']

            # print(f'company name : {company_name}')
            # print(f'skills required : {skills}')
            # print(f'more info : {more_info}')
            # print('')
            job_list.append({'comapany':company_name,'skills':skills,'more_info':more_info})
df = pd.DataFrame(job_list)
print(df)
df.to_csv('Jobs 2025',index=False)
print('sucessfull')
