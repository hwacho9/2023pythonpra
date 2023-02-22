from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
    url = "https://www.indeed.com/jobs?q="
    browser.get(f"{url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", class_="css-tvvxwd", recursive=False)
    count = len(pages)
    print(count)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        url = "https://www.indeed.com/jobs"
        url_end = f"{url}?q={keyword}&start={page*10}"
        browser.get(url_end)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    "company": company.string,
                    "location": location.string,
                    "position": title,
                    "link": f"https://www.indeed.com{link}",
                }
                for _ in job_data:
                    if job_data[_] != None:
                        job_data[_] = job_data[_].replace(",", " ")
                results.append(job_data)
    return results


print(extract_indeed_jobs("python"))
