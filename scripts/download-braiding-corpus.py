"""Retrieve publicly available PDFs listed in the braiding corpus; no paywall bypass.
Uses Crossref/OpenAlex for discovery and records retrieval failures explicitly.
Run: python scripts/download-braiding-corpus.py
"""
import concurrent.futures as futures
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse as url
import urllib.request as http
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'references/braiding'
SOURCE = OUT / '20261111 braiding corpus.md'
HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible; MariciBibliography/1.0)', 'Accept': '*/*'}

def get(address):
    req = http.Request(address, headers=HEADERS)
    with http.urlopen(req, timeout=18) as response:
        data = response.read(45_000_001)
        if len(data) > 45_000_000:
            raise ValueError('response exceeds 45 MB limit')
        return data, response.geturl(), response.headers.get('Content-Type', '')

def api(address):
    return json.loads(get(address)[0])

def entries():
    text = SOURCE.read_text(encoding='utf-8')
    rows = []
    for match in re.finditer(r'\[([^\]]+)\]\((https?://(?:\\.|[^)])+)\)', text):
        title, address = match.groups()
        if title == 'image':
            continue
        address = re.sub(r'\\([()&])', r'\1', address)
        parts = url.urlsplit(address)
        query = url.urlencode([(k,v) for k,v in url.parse_qsl(parts.query) if not k.startswith('utm_')])
        address = url.urlunsplit((parts.scheme,parts.netloc,parts.path,query,''))
        if 'publications.polymtl.ca/view/' in address:
            title = "Développement d'un procédé sans collision pour la fabrication de tresses 3D avec géométries variables"
        doi = address.split('doi.org/', 1)[1] if 'doi.org/' in address else None
        rows.append({'number': len(rows)+1, 'title': title, 'listed_url': address, 'doi': doi})
    return rows

def discover(row):
    row = dict(row, candidates=[], discovery_errors=[])
    def add(address):
        if address and address not in row['candidates']:
            row['candidates'].append(address)
    try:
        if row['doi']:
            work = api('https://api.crossref.org/works/' + url.quote(row['doi'], safe=''))['message']
        else:
            works = api('https://api.crossref.org/works?rows=1&query.title='+url.quote(row['title']))['message']['items']
            work = works[0] if works else {}
            from difflib import SequenceMatcher
            similarity = SequenceMatcher(None, row['title'].lower(), ' '.join(work.get('title', [])).lower()).ratio()
            if similarity < .8:
                work = {}
        if work:
            row['doi'] = work.get('DOI', row['doi'])
            row['verified_title'] = ' '.join(work.get('title', []))
            row['year'] = work.get('published', {}).get('date-parts', [[None]])[0][0]
            for link in work.get('link', []):
                if link.get('content-type') == 'application/pdf':
                    add(link.get('URL'))
            row['publisher_url'] = work.get('resource', {}).get('primary', {}).get('URL')
    except Exception as e:
        row['discovery_errors'].append('Crossref: '+str(e))
    if row['doi']:
        try:
            work = api('https://api.openalex.org/works/https://doi.org/'+url.quote(row['doi'], safe=''))
            row['open_access'] = work.get('open_access')
            locations = work.get('locations', [])
            for loc in locations:
                add(loc.get('pdf_url'))
            for loc in locations:
                if loc.get('is_oa'):
                    add(loc.get('landing_page_url'))
        except Exception as e:
            row['discovery_errors'].append('OpenAlex: '+str(e))
        doi = row['doi']
        if doi.startswith('10.1177/'):
            add('https://journals.sagepub.com/doi/pdf/'+doi)
        if doi.startswith('10.1007/'):
            add('https://link.springer.com/content/pdf/'+doi+'.pdf')
        if doi.startswith('10.1155/'):
            add('https://onlinelibrary.wiley.com/doi/pdf/'+doi)
        if doi.startswith('10.4188/'):
            add('https://www.jstage.jst.go.jp/article/jte1955/10/3/10_3_84/_pdf')
        add('https://doi.org/'+doi)
    for address in [row.get('publisher_url'), row['listed_url']]:
        if address:
            pii = re.search(r'(S[0-9]{16})', address)
            if pii:
                add('https://www.sciencedirect.com/science/article/pii/'+pii[1]+'/pdfft?isDTMRedir=true&download=true')
            add(address)
    print('Discovered', row['number'], row['doi'] or row['title'][:50], flush=True)
    return row

def pdf_links(data, base):
    text = data.decode('utf-8', errors='replace')
    links=[]
    # Publisher and repository citation metadata.
    for tag in re.findall(r'<meta\b[^>]+>', text, flags=re.I):
        if re.search(r'(citation_pdf_url|wkhealth_pdf_url|eprints.document_url)', tag, re.I):
            match=re.search(r'content\s*=\s*["\']([^"\']+)',tag,re.I)
            if match: links.append(url.urljoin(base,html.unescape(match[1])))
    for address in re.findall(r'(?:href|src)\s*=\s*["\']([^"\']+)',text,re.I):
        address=html.unescape(address)
        if re.search(r'\.pdf(?:$|[?#])|/pdf(?:/|$|\?)|/_pdf|/pdfft',address,re.I):
            links.append(url.urljoin(base,address))
    # PolyPublie author listings link to the dissertation record, not its PDF.
    if '/view/person/' in base:
        for address in re.findall(r'href\s*=\s*["\']([^"\']+)',text,re.I):
            if re.search(r'publications.polymtl.ca/\d+/?$',address): links.append(address)
    return list(dict.fromkeys(links))

def download(row):
    if row.get('status') == 'downloaded' and (OUT/row['file']).exists():
        return row
    row=dict(row, attempts=list(row.get('attempts', [])), status='unavailable')
    title=re.sub(r'[^\w .-]+','',row.get('verified_title') or row['title'],flags=re.UNICODE)
    filename=f"{row['number']:02d} - {row.get('year') or 'undated'} - {title[:155].strip()}.pdf"
    destination=OUT/filename
    if destination.exists() and destination.read_bytes().startswith(b'%PDF-'):
        row.update(status='downloaded',file=filename,bytes=destination.stat().st_size)
        return row
    queue=[(u,0) for u in row['candidates']]
    visited={a['url'] for a in row['attempts']}
    fresh_attempts=0
    while queue and fresh_attempts<18:
        address,depth=queue.pop(0)
        if address in visited or not address.startswith(('http://','https://')):continue
        visited.add(address)
        fresh_attempts+=1
        try:
            data,final,kind=get(address)
            if data.lstrip().startswith(b'%PDF-'):
                destination.write_bytes(data)
                row.update(status='downloaded',file=filename,bytes=len(data),download_url=final,sha256=hashlib.sha256(data).hexdigest())
                print('Downloaded',row['number'],filename,flush=True)
                return row
            row['attempts'].append({'url':address,'result':'non-PDF','final_url':final,'content_type':kind})
            if depth<2:
                queue[0:0]=[(u,depth+1) for u in pdf_links(data,final) if u not in visited][:8]
        except Exception as e:
            row['attempts'].append({'url':address,'result':str(e)})
    print('Unavailable',row['number'],row['title'][:65],flush=True)
    return row

def report(rows):
    (OUT/'download-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# Braiding corpus download report','',f"Downloaded {sum(r['status']=='downloaded' for r in rows)} of {len(rows)} listed works (including the dissertation).",'',
           'Only PDF responses were saved as papers. Unavailable means retrieval failed, not necessarily that the work is paywalled. See `download-manifest.json` for source URLs and HTTP errors.','',
           '| # | Work | Status | Local PDF |','|---|---|---|---|']
    for r in rows:
        local='['+r['file']+']('+url.quote(r['file'])+')' if r.get('file') else '—'
        lines.append(f"| {r['number']} | {r['title']} | {r['status']} | {local} |")
    (OUT/'download-report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def supplement(row):
    from difflib import SequenceMatcher
    row = dict(row)
    row['listed_url'] = entries()[row['number']-1]['listed_url']
    def add(address):
        if address and address not in row['candidates']: row['candidates'].append(address)
    add(row['listed_url'])
    try:
        if row.get('doi'):
            work = api('https://api.openalex.org/works/https://doi.org/'+url.quote(row['doi'],safe=''))
        else:
            results = api('https://api.openalex.org/works?per-page=3&search='+url.quote(row['title']))['results']
            matches = [w for w in results if SequenceMatcher(None,row['title'].lower(),w['display_name'].lower()).ratio()>.75]
            work = matches[0] if matches else None
        if work:
            row['verified_title'] = work['display_name']
            row['year'] = work.get('publication_year')
            row['doi'] = (work.get('doi') or '').replace('https://doi.org/','') or row.get('doi')
            row['open_access'] = work.get('open_access')
            for loc in work.get('locations',[]):
                add(loc.get('pdf_url')); add(loc.get('landing_page_url'))
    except Exception as e:
        row.setdefault('discovery_errors',[]).append('Supplement: '+str(e))
    for address in list(row['candidates']):
        match = re.search(r'10\.5281/zenodo\.(\d+)',address)
        if match:
            try:
                record=api('https://zenodo.org/api/records/'+match[1])
                row['zenodo_title']=record.get('metadata',{}).get('title')
                for file in record.get('files',[]):
                    if file['key'].lower().endswith('.pdf'): add(file['links']['self'])
            except Exception as e:
                row.setdefault('discovery_errors',[]).append('Zenodo: '+str(e))
    print('Supplemented',row['number'],flush=True)
    return row

if __name__=='__main__':
    import sys
    if '--retry' in sys.argv:
        rows=json.loads((OUT/'download-manifest.json').read_text(encoding='utf-8'))
        with futures.ThreadPoolExecutor(max_workers=2) as pool:
            rows=list(pool.map(supplement,rows))
    else:
        with futures.ThreadPoolExecutor(max_workers=2) as pool:
            rows=list(pool.map(discover,entries()))
    (OUT/'download-discovery.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    with futures.ThreadPoolExecutor(max_workers=2) as pool:
        rows=list(pool.map(download,rows))
    report(rows)
    print(f"Saved {sum(r['status']=='downloaded' for r in rows)}/{len(rows)} PDFs",flush=True)
