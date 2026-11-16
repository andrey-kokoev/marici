"""Search arXiv for missing corpus works and download verified title/DOI matches.
Queries are serialized, with >=3 seconds between requests per arXiv guidance.
"""
import datetime
import difflib
import hashlib
import json
import re
import runpy
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'references/braiding'
NS={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
last_request=0
queries=[]

def normalize(text):
    return ' '.join(re.findall(r'\w+',text.lower()))

def search(query):
    global last_request
    time.sleep(max(0,3.1-(time.monotonic()-last_request)))
    address='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':query,'start':0,'max_results':100})
    observation={'query':query,'url':address,'results':[]}
    queries.append(observation)
    try:
        last_request=time.monotonic()
        request=urllib.request.Request(address,headers={'User-Agent':'MariciBibliography/1.0'})
        with urllib.request.urlopen(request,timeout=35) as response:
            tree=ET.fromstring(response.read())
        observation['total']=int(tree.findtext('o:totalResults','0',NS))
        for entry in tree.findall('a:entry',NS):
            identifier=entry.findtext('a:id','',NS)
            if 'api/errors' in identifier: raise RuntimeError(entry.findtext('a:summary','arXiv API error',NS))
            paper={'id':identifier,'title':' '.join(entry.findtext('a:title','',NS).split()),
                   'doi':entry.findtext('x:doi','',NS),'published':entry.findtext('a:published','',NS),
                   'authors':[a.findtext('a:name','',NS) for a in entry.findall('a:author',NS)],
                   'pdf':next((l.attrib['href'] for l in entry.findall('a:link',NS) if l.attrib.get('title')=='pdf'),None)}
            observation['results'].append(paper)
        print('arXiv',observation['total'],query[:100],flush=True)
    except Exception as error:
        observation['error']=str(error)
        print('arXiv error',query[:60],str(error),flush=True)
    return observation['results']

if __name__=='__main__':
    rows=json.loads((OUT/'download-manifest.json').read_text(encoding='utf-8'))
    missing=[r for r in rows if r['status']!='downloaded']
    candidates={}
    for row in missing:
        title=row.get('verified_title') or row['title']
        # Strip punctuation without changing the title's words.
        query='ti:"'+normalize(title)+'"'
        for paper in search(query):candidates[paper['id']]=paper
    for query in [
        'ti:braiding AND (all:carrier OR all:maypole OR all:textile OR all:rotary OR all:horngear)',
        'au:Krauskopf AND (all:braiding OR all:maypole)',
        'ti:cliques AND (all:partite OR all:textile)',
        'au:Assi AND (all:braiding OR all:tresses)',
        'au:Kyosev AND all:braiding',
    ]:
        for paper in search(query):candidates[paper['id']]=paper
    results=[]
    downloader=runpy.run_path(str(ROOT/'scripts/download-braiding-corpus.py'))
    for row in missing:
        title=normalize(row.get('verified_title') or row['title'])
        ranked=[]
        for paper in candidates.values():
            score=difflib.SequenceMatcher(None,title,normalize(paper['title'])).ratio()
            doi_match=bool(row.get('doi') and row['doi'].lower()==paper['doi'].lower().strip())
            ranked.append((doi_match,score,paper))
        ranked.sort(key=lambda x:(x[0],x[1]),reverse=True)
        matches=[p for doi_match,score,p in ranked if doi_match or score>=.9]
        item={'number':row['number'],'title':row['title'],'matches':matches,
              'nearest_candidates':[{'title':p['title'],'id':p['id'],'title_similarity':round(score,3)} for _,score,p in ranked[:3]],
              'status':'matching preprint found' if matches else 'no matching preprint found in completed searches'}
        if matches:
            for paper in matches:
                if paper['pdf']:
                    pdf=paper['pdf'].replace('http://','https://')
                    if pdf not in row['candidates']:row['candidates'].insert(0,pdf)
            row['arxiv_matches']=matches
            replacement=downloader['download'](row)
            rows[rows.index(row)]=replacement
            item['download_status']=replacement['status']
        results.append(item)
    data={'searched_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope':'18 missing bibliography items; exact normalized titles plus broader topic/author searches. A failed query is not evidence of absence.',
          'queries':queries,'works':results}
    (OUT/'arxiv-search-results.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# arXiv search for missing braiding works','',f"Searched {len(missing)} missing works. Matching works: {sum(bool(r['matches']) for r in results)}. Query errors: {sum('error' in q for q in queries)}.",'',
           'Searched normalized titles and broader braiding/carrier, Krauskopf, clique/partite, Assi, and Kyosev queries. Only close title matches or exact DOI matches qualify for download; unrelated braid-theory papers are not substitutes. See `arxiv-search-results.json` for queries and candidates.','',
           '| # | Work | arXiv result |','|---|---|---|']
    for result in results:
        links='; '.join(p['id'] for p in result['matches']) or result['status']
        lines.append(f"| {result['number']} | {result['title']} | {links} |")
    (OUT/'arxiv-search-report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    downloader['report'](rows)
    print('Matching works:',sum(bool(r['matches']) for r in results),'Query errors:',sum('error' in q for q in queries),flush=True)
