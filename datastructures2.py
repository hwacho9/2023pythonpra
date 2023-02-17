websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com"
)

for website in websites:  # website의 단어는 내가 정하는 거
    if website.startswith("https://"):
        print("good to go")
    else:
        print("we have to fix it")
