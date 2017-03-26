import urllib2 as urllib
import re

HOSTS_URL = "https://raw.githubusercontent.com/tommyanthony/block-spotify-ads/master/hosts"

def write_hosts_file(output_filename):
    output = open(output_filename, "w")
    infile = urllib.urlopen(HOSTS_URL)
    for line in infile:
        output.write(line)
    output.close()

if __name__ == "__main__":
    write_hosts_file("/etc/hosts")
