import datetime
import logging
__author__ = 'a-chburrell'

entriesFile = "entries.json"
entries_dir = "entries"
user_auth_header_name = "CG-AUTH-USER"
user_value = "CompanyB"
pass_auth_header_name = "CG-AUTH-PASS"
pass_value = "Gab0ll!S3attl3"
auth_salt = "Ax!a!969"
timestamp_header_name = "CG-TIMESTAMP-HEADER"
logging_file_name = "" % datetime.datetime.now().strftime("")
logging_level = logging.DEBUG
auth_enabled = False
