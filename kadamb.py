
from pprint import pprint
import re

str_1 = "Hi, my name is Kadamb Kaluskar. I live in India."

str_2 = "Hi, my name is {{first_name}} {{last_name}}. I live in {{country_name}}."

opening_curlies = [m.start() for m in re.finditer('{{', str_2)]
opening_curlies = opening_curlies + [len(str_2)]
closing_curlies = [m.end() for m in re.finditer('}}', str_2)]
closing_curlies = [0] +closing_curlies

templates = [str_2[closing_curlies[idx]:opening_curlies[idx]].strip() for idx in range(len(opening_curlies)) if (str_2[closing_curlies[idx]:opening_curlies[idx]]!=' ' and str_2[closing_curlies[idx]:opening_curlies[idx]]!='')]

str_1_trimmed = str_1
str_2_trimmed = str_2
for template in templates:
    str_1_trimmed = str_1_trimmed.replace(template,'').replace('  ',' ').strip()
    str_2_trimmed = str_2_trimmed.replace(template, '').replace('  ',' ').strip()
vals = str_1_trimmed.strip().split(' ')
keys = str_2_trimmed.strip().split(' ')

output_param = {}
for item_idx in range(len(keys)):
    output_param[keys[item_idx]] = vals[item_idx]

pprint (output_param)
