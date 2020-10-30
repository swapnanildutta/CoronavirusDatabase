import json
import sqlite3

conn = sqlite3.connect("coronavirusdb.sqlite")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS COVID19_Toll;
    CREATE TABLE COVID19_Toll (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        country    TEXT UNIQUE,
        tot_cases      TEXT,
        new_cases      TEXT,
        tot_death      TEXT,
        new_death      TEXT,
        tot_recovery   TEXT,
        active_cases   TEXT,
        serious_cases   TEXT,
        cases_per_M   TEXT,
        death_per_M   TEXT,
        tot_test      TEXT,
        test_per_M    TEXT
    );
    ''')

with open('worldwide.json', 'r') as fh:
    data = json.load(fh)

# print("Country \t Cases \t Per Million \t Recovered \t Death")
for key in data.keys():

    # print(key,"\t",data[key]['Cnf'],"\t",data[key]['CpM'],
    #      "\t",data[key]['Rec'],"\t",data[key]['Dth'])

    cur.execute(('INSERT OR IGNORE INTO COVID19_Toll (country, tot_cases, new_cases, tot_death,'
                 ('new_death, tot_recovery, active_cases, serious_cases, cases_per_M, death_per_M,')
                 ('tot_test, test_per_M) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?')),
                (key, data[key]['TC'], data[key]['NC'], data[key]['TD'], data[key]['ND'],
                 data[key]['TR'], data[key]['AC'], data[key]['SC'], data[key]['TCpM'], data[key]['DpM'], data[key]['TT'], data[key]['TpM']), )

conn.commit()
