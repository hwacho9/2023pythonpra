from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

app = Flask("JobScrapper")


@app.route("/")  # decorator 함수 바로 위에 위치해야 한다
def home():
    return render_template("home.html", name="nico")


db = {}
# 가짜 데이터베이스 서버가 켜져있을 때만 메모리에 저장된다


@app.route("/search")
def search():
    keyword = request.args.get("keyword")  # request의 args 에서 keyword 를 가져온다
    # URL의 물음표 뒤에 있는 qrguments 에서 keyword를 가져와서 search.html에 보낸다
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr  # list
        db[keyword] = jobs  # dictonary 에 접근
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:  # 사용자가 keyword 없이 export로 이동하면 홈페이지로 돌아간다
        return redirect("/")
    if keyword not in db:  # 만약 keyword가 데이터베이스에 없으면
        return redirect(f"/search?keyword={keyword}")
    # 사용자를 search 페이지로 redirect 하고 사용자가 내보내려는 keyword를 전달한다
    save_to_file(keyword, db[keyword])
    # as_attachment 는 다운로드가 실행되도록
    return send_file(f"{keyword}.csv", as_attachment=True)


if __name__ == "__main__":
    app.run("0.0.0.0")
