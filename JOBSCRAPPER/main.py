from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"  # python은 바꿀 수 있다.

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
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
            company, kind, region = anchor.find_all('span', class_="company")
            # find 는 결과를 가져오고 find_all은 list를 가져온다
            title = anchor.find("span", class_="title")
            print(company.string, region.string, title.string)
            job_data = {
                "company": company.string,
                "region": region.string,
                "position": title.string
            }
            results.append(job_data)
    for result in results:
        print(result)
        print("/////")

    """list_of_numbers = [1,2,3]
    first, second, third = list_of_nunmber
    print(first, second, third)  =>> 1, 2, 3 이 출력된다
    """
