import webbrowser as wb


def web_automation():
    chrome_path = '/usr/bin/firefox'
    URLS = ('stackoverflow.com', 'github.com', 'google.com', 'gmail.com', 'cnn.com/news')

    for url in URLS:
        print('Opening: ' + url)
        wb.get(chrome_path).open(url)


web_automation()
