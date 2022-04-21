import mechanize

def viewpage(url):
    browser=mechanize.Browser()
    page=browser.open(url)
    source_code=page.read()
    print(source_code)

