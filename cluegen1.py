import requests_ftp

s=requests_ftp.FTPSession()
resp = s.list('ftp://salabim.org', auth=('ruudvander', 'rthvdh'))
print(resp.status_code)

resp = s.stor("ftp://salabim.org/a53.py", auth=("ruudvander", "rthvdh"), files={"file": open("a53.py", "rb")})
