import os
import re

urls = list()

# Read XML files
with open('sitemap_set_0.xml') as f:
    lines_1 = f.read().splitlines()
with open('sitemap_set_1.xml') as f:
    lines_2 = f.read().splitlines()
lines = lines_1+lines_2

# Extract URLS
for line in lines:
    if 'set?id' in line:
        #print line
        line = line.replace("<loc>", " ")
        line = line.replace("</loc>", " ")
        lurls = re.findall(r'(https?://[^\s]+)', line)
        urls.extend(lurls)

# Print URLS
with open('polyvore-sets.txt', 'w') as f:
    f.write("\n".join(urls))
