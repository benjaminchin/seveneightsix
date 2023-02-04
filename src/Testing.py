import pycurl

url = 'https://www.reddit.com/r/webdev/comments/42g4rq/tool_to_check_how_much_data_is_needed_to_fully/'
c = pycurl.Curl()
c.setopt(c.URL, url)
c.perform()
print c.getinfo(c.CONTENT_LENGTH_DOWNLOAD)