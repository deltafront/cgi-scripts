import cgi
import hashlib
import os
import cgitb
cgitb.enable()

__author__ = 'a-chburrell'
import configs

def get_values_from_request():
    fields = os.environ
    username = fields[configs.user_auth_header_name]
    password = fields[configs.pass_auth_header_name]
    timestamp = fields[configs.timestamp_header_name]
    ip_address =cgi.escape(fields["REMOTE_ADDR"])
    try:
        request_body_size = int(fields['CONTENT_LENGTH', 0])
    except (ValueError):
        request_body_size = 0
    request_body = fields['wsgi.input'].read(request_body_size)
    site_name= cgi.parse_qs(request_body)
    return {"userame":username,"password":password,"timestamp":timestamp,"site_name":site_name,"ip_address":ip_address}


def to_json(ip_address,site_name):
    return "{\"ip_address\":\%s\",\"site_name\":\"%s\"}" % (ip_address,site_name)

def verify(username,password,timestamp):
    if configs.auth_enabled:
        pre_hash = "%s%s%s%s" % (configs.auth_salt,configs.pass_value,username,str(timestamp))
        master_hash = hashlib.md5(pre_hash).hexdigest
        return password == master_hash
    else:
        return True

def write_entry(site_name,json):
    filename = "%s.%s" % (site_name,configs.entriesFile)
    f = open(filename)
    f.write(json)
    f.close()

mapping = get_values_from_request()
username = mapping["username"]
password = mapping["password"]
timestamp = mapping["timestamp"]
site_name = mapping["site_name"]
ip_address = mapping["ip_address"]
out = None
if verify(username=username,password=password,timestamp=timestamp):
    json = to_json(site_name=site_name,ip_address=ip_address)
    write_entry(site_name=site_name,json=json)
    out = "Entry Written"
else:
    out = "Authentication failed!"
print out


