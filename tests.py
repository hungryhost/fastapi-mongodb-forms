from urllib import request, parse
data = parse.urlencode({}).encode()

query = 'work_easdmail=yuiborodin@miem.hse.ru&employasdment_startdate=2020-02-02&dasdas=asdasdasdadssad'
req = request.Request("http://127.0.0.1:8000/get_form?{}".format(query), data=data)
resp = request.urlopen(req)
print(resp.read())