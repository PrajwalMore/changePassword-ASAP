import webbrowser

print("Application launched")
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

setOfUrl={"google":"google password change url here"}


def addLink(urlName,url):
    setOfUrl[urlName]=url
addLink("github","https://github.com/password_reset")
addLink("Google","https://myaccount.google.com/intro/security")
#addLink("","")
#addLink("","")
#addLink("","")
# ^ multiple links to open.

for url in setOfUrl:
          webbrowser.get('chrome').open_new(setOfUrl[url])
