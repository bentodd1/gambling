import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import psycopg2
import sys

def connect():
        conn_string = "host='localhost' dbname='sports' user='btodd' password='F1shF1sh&&'"
        sql = "insert into public.\"Game\"(\"Date\",\"Team1\",\"Team2\",\"Score1\",\"Score2\") VALUES(%s, %s, %s, %s, %s)"
        conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries

        return conn

def insertTeam(id,name,cursor1):
        sql = "insert into public.\"Team\"(\"Id\",\"Name\",\"Season\") VALUES(%s, %s, %s) ON CONFLICT DO NOTHING"
        values = [id,name,1]
        cursor1.execute(sql,values)

def insertGame(gameId,date,team1, teadm2,score1,score2, cursor1):
        date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into public.\"Game\"(\"Date\",\"Team1\",\"Team2\",\"Score1\",\"Score2\",\"Id\") VALUES(%s, %s, %s, %s, %s,%s )"
        values = [date,team1, teadm2,score1,score2, gameId]
        cursor1.execute(sql,values)

def insertLine(casino,team1, spread1, gameId, cursor1):
        sql = "insert into public.\"Line\"(\"Casino\",\"Team1\",\"Spread1\",\"Game\") VALUES(%s, %s, %s, %s )"
        values = [casino,team1, spread1, gameId]
        cursor1.execute(sql,values)


def calculateScore(scorePieces):
        scoreMap = {}
        for piece in scorePieces:
                currentScore = 0
                partId = piece['partid']
                if partId in scoreMap:
                        currentScore = int(scoreMap[partId])

                newScore = int(piece['val']) + currentScore
                scoreMap[partId] = newScore
        print(scoreMap)
        return scoreMap



#url = 'https://www.sportsbookreview.com/ms-odds-v2/odds-v2-service?query=%7B+eventsByDateByLeagueGroup(+leagueGroups:+[%7B+mtid:+401,+lid:+14,+spid:+5+%7D],+providerAcountOpener:+3,+hoursRange:+25,+showEmptyEvents:+true,+marketTypeLayout:+%22PARTICIPANTS%22,+ic:+false,+startDate:+1521985600000,+timezoneOffset:+-4,+nof:+true,+hl:+true,+sort:+%7Bby:+[%22lid%22,+%22dt%22,+%22des%22],+order:+ASC%7D+)+%7B+events+%7B+eid+lid+spid+des+dt+es+rid+ic+ven+tvs+cit+cou+st+sta+hl+seid+writeingame+consensus+%7B+eid+mtid+bb+boid+partid+sbid+paid+lineid+wag+perc+vol+tvol+wb+sequence+%7D+plays(pgid:+2,+limitLastSeq:+3,+pgidWhenFinished:+-1)+%7B+eid+sqid+siid+gid+nam+val+tim+%7D+scores+%7B+partid+val+eid+pn+sequence+%7D+participants+%7B+eid+partid+psid+ih+rot+tr+sppil+sppic+startingPitcher+%7B+fn+lnam+%7D+source+%7B+...+on+Player+%7B+pid+fn+lnam+%7D+...+on+Team+%7B+tmid+lid+nam+nn+sn+abbr+cit+%7D+...+on+ParticipantGroup+%7B+partgid+nam+lid+participants+%7B+eid+partid+psid+ih+rot+source+%7B+...+on+Player+%7B+pid+fn+lnam+%7D+...+on+Team+%7B+tmid+lid+nam+nn+sn+abbr+cit+%7D+%7D+%7D+%7D+%7D+%7D+marketTypes+%7B+mtid+spid+nam+des+settings+%7B+sitid+did+alias+layout+format+template+sort+url+%7D+%7D+currentLines(paid:+[20,+3,+10,+8,+9,+44,+29,+38,+16,+65,+92,+28,+83,+84,+82,+15,+35,+45,+54,+22,+18,+5,+36,+78,+93])+openingLines+eventGroup+%7B+egid+nam+%7D+statistics(sgid:+3,+sgidWhenFinished:+4)+%7B+val+eid+nam+partid+pid+typ+siid+sequence+%7D+league+%7B+lid+nam+rid+spid+sn+settings+%7B+alias+rotation+ord+shortnamebreakpoint+matchupline+%7D+%7D+%7D+maxSequences+%7B+events:+eventsMaxSequence+scores:+scoresMaxSequence+currentLines:+linesMaxSequence+statistics:+statisticsMaxSequence+plays:+playsMaxSequence+consensus:+consensusMaxSequence+%7D+%7D+%7D'
def hitApi(date,cursor):
        firstString = 'https://www.sportsbookreview.com/ms-odds-v2/odds-v2-service?query=%7B+eventsByDateByLeagueGroup(+leagueGroups:+[%7B+mtid:+401,+lid:+14,+spid:+5+%7D],+providerAcountOpener:+3,+hoursRange:+25,+showEmptyEvents:+true,+marketTypeLayout:+%22PARTICIPANTS%22,+ic:+false,+startDate:+'
        secondString =',+timezoneOffset:+-4,+nof:+true,+hl:+true,+sort:+%7Bby:+[%22lid%22,+%22dt%22,+%22des%22],+order:+ASC%7D+)+%7B+events+%7B+eid+lid+spid+des+dt+es+rid+ic+ven+tvs+cit+cou+st+sta+hl+seid+writeingame+consensus+%7B+eid+mtid+bb+boid+partid+sbid+paid+lineid+wag+perc+vol+tvol+wb+sequence+%7D+plays(pgid:+2,+limitLastSeq:+3,+pgidWhenFinished:+-1)+%7B+eid+sqid+siid+gid+nam+val+tim+%7D+scores+%7B+partid+val+eid+pn+sequence+%7D+participants+%7B+eid+partid+psid+ih+rot+tr+sppil+sppic+startingPitcher+%7B+fn+lnam+%7D+source+%7B+...+on+Player+%7B+pid+fn+lnam+%7D+...+on+Team+%7B+tmid+lid+nam+nn+sn+abbr+cit+%7D+...+on+ParticipantGroup+%7B+partgid+nam+lid+participants+%7B+eid+partid+psid+ih+rot+source+%7B+...+on+Player+%7B+pid+fn+lnam+%7D+...+on+Team+%7B+tmid+lid+nam+nn+sn+abbr+cit+%7D+%7D+%7D+%7D+%7D+%7D+marketTypes+%7B+mtid+spid+nam+des+settings+%7B+sitid+did+alias+layout+format+template+sort+url+%7D+%7D+currentLines(paid:+[20,+3,+10,+8,+9,+44,+29,+38,+16,+65,+92,+28,+83,+84,+82,+15,+35,+45,+54,+22,+18,+5,+36,+78,+93])+openingLines+eventGroup+%7B+egid+nam+%7D+statistics(sgid:+3,+sgidWhenFinished:+4)+%7B+val+eid+nam+partid+pid+typ+siid+sequence+%7D+league+%7B+lid+nam+rid+spid+sn+settings+%7B+alias+rotation+ord+shortnamebreakpoint+matchupline+%7D+%7D+%7D+maxSequences+%7B+events:+eventsMaxSequence+scores:+scoresMaxSequence+currentLines:+linesMaxSequence+statistics:+statisticsMaxSequence+plays:+playsMaxSequence+consensus:+consensusMaxSequence+%7D+%7D+%7D'
        url = firstString +str(date)+secondString
        print(url)
        resp = requests.get(url=url)
        data = resp.json()

       # print(data['data']['eventsByDateByLeagueGroup']['events'][0]['openingLines'][0]['adj'])

        for event in data['data']['eventsByDateByLeagueGroup']['events']:
                teamId1 = event['participants'][0]['source']['tmid']
                teamId2 = event['participants'][1]['source']['tmid']
                print(event['participants'][0]['source']['sn'])
                insertTeam(event['participants'][0]['source']['tmid'],event['participants'][0]['source']['sn'],cursor)
                print(event['participants'][1]['source']['sn'])
                insertTeam(event['participants'][1]['source']['tmid'],event['participants'][1]['source']['sn'],cursor)
                print('Opening Lines')
                scoreMap = calculateScore(event['scores'])
                realDate = int(str(date)[:-2])

                insertGame(event['eid'],realDate,teamId1,teamId2,scoreMap[teamId1],scoreMap[teamId2],cursor )
                print(event['openingLines'][0]['adj'])
                print(event['openingLines'][1]['adj'])

                for line in event['currentLines']:

                        print('casino')
                        insertLine(line['paid'],line['partid'],line['adj'],line['eid'],cursor)
                        print(line['paid'])
                        print('line')
                        print(line['adj'])
#page = requests.get('https://www.sportsbookreview.com/betting-odds/ncaa-basketball/pointspread/?date=20180314')
conn = connect()
cursor = conn.cursor()
#soup = BeautifulSoup(page.text, 'html.parser')
#print(len(soup))
#mydivs = soup.findAll("div", {"class": "_1Y3rN _308Yc"})

#date = 1521985600000
date =  1520985600000

for i in range(10):
        print(i)
        hitApi(date,cursor)
        date += 86400000

conn.commit() # <- We MUST commit to reflect the inserted data
cursor.close()
conn.close()
def convertDate():
    orig = datetime.datetime.fromtimestamp(1425917335)
    new = orig + datetime.timedelta(days=1)
    print(new.timestamp())



#result = json.loads(resp)
#
#print result['events']
#last_links = soup.find(class_='AlphaNav')
#last_links.decompose()

#artist_name_list = soup.find(class_='BodyText')
#artist_name_list_items = artist_name_list.find_all('a')
#print(len(mydivs))
#for div in mydivs:
#    names = div.contents[0]
#    print(names)