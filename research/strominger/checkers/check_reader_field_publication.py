"""Validate the built closeout page, archive entry, navigation and evidence."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib
ROOT=Path(__file__).resolve().parents[3];DIST=ROOT/'website/.vitepress/dist';OUT=ROOT/'research/strominger/results/reader-field-closeout'
page='/research/results/tessellated-reader-fields';ledger='/research/ledger/20261018-4326-tessellated-reader-fields-and-bounded-framed-coherence/'
def resolve(url):
    path=unquote(urlsplit(url).path).lstrip('/');p=DIST/path
    for candidate in [p,p/'index.html',Path(str(p)+'.html')]:
        if candidate.is_file():return candidate
    raise AssertionError('Missing public route: '+url)
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a:self.links.append(a)
built=resolve(page).read_text(encoding='utf8');archive=resolve(ledger).read_text(encoding='utf8');home=resolve('/').read_text(encoding='utf8');results=resolve('/research/results/').read_text(encoding='utf8')
assert '250,040' in built and '458,912' in built and 'bounded' in built.lower();assert 'marici.Strominger' in archive;assert '4326' in archive;assert 'ev-000000016183-00d9231f-dce3-4554-b610-d1d70bea1f1f' in archive
assert 'katex-error' not in built and 'katex-error' not in archive
for document in [home,results,built]:assert page in document
parser=Links();parser.feed(built);local=[a['href'] for a in parser.links if a['href'].startswith('/') and not a['href'].startswith('//')]
for href in local:resolve(href)
assert any(a['href']==ledger and a.get('target')=='_self' for a in parser.links)
manifest=resolve('/research/tessellated-reader-fields/verification.json');assert manifest.read_bytes()==(OUT/'verification.json').read_bytes()
records=json.loads(resolve('/research/ledger/index.json').read_text(encoding='utf8'));entry=[r for r in records if r['entry']==4326];assert len(entry)==1 and entry[0]['authors']==['marici.Strominger']
report={'status':'built-publication-links-and-evidence-passed','resultRoute':page,'ledgerRoute':ledger,'ledgerEntry':4326,'author':'marici.Strominger','navigationAndLandingLinksPresent':True,'checkedLocalLinks':len(local),'publicManifestMatchesResearchReceipt':True,'buildLogSha256':hashlib.sha256((OUT/'site-build.log').read_bytes()).hexdigest(),'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Local static build only. No commit, push or deployment performed; graph admission is provenance, not scientific certification.'}
(OUT/'publication-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
