import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

result = requests.get(URL)


def extract_indeed_pages():

  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  pages = pagination.find_all('a')

  spans = []

  for page in pages[0:-1]:
    spans.append(int(page.find("span").string))

  max_page = spans[-1]  #max_page = range(0, 5)

  return max_page


def extract_job(html_title, html_company):
  html_title = html_title.find("a")['title']

  if html_company.find("a") is not None:
   html_company = html_company.find("a").string
   type_tag = "anchor"
 
  elif html_company.find("span") is not None:

    if html_company.find("span", class_= "company") is not None:#.string 이 있어서 span-tag에서 None이 필터링 되지 못했다. 그 결과 Location으로 넘어가지 못했다.
      html_company =  html_company.find("span", class_= "company").string
      type_tag = "span"        
    
    elif html_company.find("span", class_= "location accessible-contrast-color-location") is not None:
      html_company = html_company.find("span", class_= "location accessible-contrast-color-location").string
      type_tag = "Location"

  else:
    html_company = "error"
    type_tag = "error"

  html_company = html_company.strip()
   
  return {'title': html_title, 'company': html_company}


def extract_indeed_jobs(last_page):
  jobs = []

  for page in range(last_page):
    result_request = requests.get(f"{URL}&start={page*LIMIT}")#1
    soup = BeautifulSoup(result_request.text, "html.parser")#2
    title_results = soup.find_all("h2", {"class": "title"})#3-1
    company_results = soup.find_all("div", {"class": "sjcl"})#3-2

    for i, j in zip(title_results, company_results):
      job= extract_job(i, j)

    jobs.append(job)
    
  return jobs
