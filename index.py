import os
from os.path import join
import configs
__author__ = 'a-chburrell'
#!/usr/bin/env python


def get_json_files():
    json_files = []
    listings = os.listdir(configs.entries_dir)
    for listing in listings:
        f = open(listing)
        filename = join(configs.entries_dir,f)
        if os.path.isfile(filename):
            json_files.append(filename)
    return json_files

def get_table(json_files):
    jsons = []
    for json_file in json_files:
        f = open(json_file)
        jsons.append(f.read())
        f.close()
    return from_json(jsons)

def from_json_List(jsons):
    out = "<p>No entries currently in the database</p>"
    if len(jsons) > 0:
        out = "<table><tr><th>Site Name</th><th>IP Address</th><tr>"
        for json in jsons:
            out += from_json(json)
        out +="</table>"
    return out

def from_json(json):
    mapping = eval(json)#todo - change this to JSON...
    ip_address = mapping["ip_address"]
    site_name = mapping["site_name"]
    return "<tr><td>%s</td><td>%s</td>" %(site_name,getLink(ip_address))

def getLink(ip_address):
    return "<a href=\"http:%s\">%s</a>"% (ip_address,ip_address)



json_files = get_json_files()
table = get_table(json_files)

print "Content-Type: text/html"
print
print """\
<html>
    <head>
        <title>Company-B Website</title>
    </head>
    <body>
        <h1>Listing of all registered sites</h1>
        %s
    </body>
</html>
"""   % table
