from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:  # httlp 를 제대로 가져오는지 확인 status_code
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)  # job_posts 의 list에서 마지막 항목을 삭제한다
            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]
                link = anchor["href"]
                company, kind, region = anchor.find_all(
                    'span', class_="company")
                """list_of_numbers = [1,2,3]
                first, second, third = list_of_nunmber
                print(first, second, third)  =>> 1, 2, 3 이 출력된다
                """
                # find 는 결과를 가져오고 find_all은 list를 가져온다
                title = anchor.find("span", class_="title")
                print(company.string, region.string, title.string)
                job_data = {
                    "link": f"https://weworkremotely.com/{link}",
                    "company": company.string,
                    "location": region.string,
                    "position": title.string
                }
                results.append(job_data)
        return results


def get_page_count(keyword):
    driver = webdriver.Chrome()
    driver.get(
        f'https://kr.indeed.com/jobs?q={keyword}')

    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0")
    if pagination == None:
        return 1  # 스크래핑 해야 할 페이지 수를 나타낸다
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    elif count == 0:
        return 1
    else:
        return count - 1


def extract_indeed_jobs(keyword):
    driver = webdriver.Chrome()
    final_url = f'https://kr.indeed.com/jobs?q={keyword}&start='
    # print("Requesting = ", final_url)
    driver.get(final_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    # recursive=False 은 ul 바로 아래 있는 li 만 찾아준다
    jobs = job_list.find_all('li', recursive=False)
    results = []
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            # select 는 css selector 로 접근할 수 있게 해준다
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")
            job_data = {
                "link": f"https://kr.indeed.com{link}",
                "company": company.string,
                "locations": location.string,
                "position": title
            }
            results.append(job_data)
    return results


print(extract_indeed_jobs("python"))
