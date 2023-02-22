from bs4 import BeautifulSoup
import requests


def wage_k(name):
    class_name = ''
    if name.attrs.get('class'):
        class_name = name.attrs.get('class')[0]
        if name.string == 'k':
            return name


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here

        jobs = soup.find_all('table', {'id': "jobsboard"})
        for jobs_section in jobs:
            job_posts = jobs_section.find_all('tr', class_='job')
            for post in job_posts:
                job_infos = post.find_all('td')
                info = job_infos[1]
                title = info.find('h2')
                company = info.find('h3')
                location = info.find_all("div", class_="location")
                wage = location[-1]
                regions = location[:-1]
                regions = regions['location']

                # print(title.string, company.string, wage.string)
                title = title.string
                title = title.strip()

                company = company.string
                company = company.strip()

                job_data = {"title": title,
                            "company": company,
                            "regions": regions,
                            "wage": wage.string
                            }
                results.append(job_data)
        for result in results:
            print(result)
            print("////////////////////")
    else:
        print("Can't get jobs.")


keyword = input("Write the keyword thay you want to find = ")
extract_jobs(f"{keyword}")
