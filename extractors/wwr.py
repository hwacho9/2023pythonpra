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
                # print(company.string, region.string, title.string)
                job_data = {
                    "link": f"https://weworkremotely.com/{link}",
                    "company": company.string.replace(",", " "),
                    "location": region.string.replace(",", " "),
                    "position": title.string.replace(",", " ")
                }
                results.append(job_data)
        return results
