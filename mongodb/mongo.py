#!/usr/bin/python 

import sys
import subprocess
import json

if len(sys.argv) > 1:
    if sys.argv[1] == "config":
        print "graph_title MongoDB Monitoring"
        print "graph_vlabel Count"
        print "graph_category mongodb"

        print "command.label commands"
        print "conn.label connections"
        print "delete.label deletes"
        print "flushes.label flushes"
        print "getmore.label getmore"
        print "insert.label inserts"
        print "query.label queries"
        print "update.label updates"

        sys.exit(0)
    elif sys.argv[1] == "autoconfig":
        print('yes')
        sys.exit(0)

p = subprocess.Popen(['/usr/bin/mongostat', '-n', '1', '--json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()

#print out
json = json.loads(out)

print "command.value ",json['{{inventory_hostname_short}}']['command'].split('|')[0]
print "conn.value ",json['{{inventory_hostname_short}}']['conn'].replace('*', '')
print "delete.value ",json['{{inventory_hostname_short}}']['delete'].replace('*', '')
print "flushes.value ",json['{{inventory_hostname_short}}']['flushes'].replace('*', '')
print "getmore.value ",json['{{inventory_hostname_short}}']['getmore'].replace('*', '')
print "insert.value ",json['{{inventory_hostname_short}}']['insert'].replace('*', '')
print "query.value ",json['{{inventory_hostname_short}}']['query'].replace('*', '')
print "update.value ",json['{{inventory_hostname_short}}']['update'].replace('*', '')

