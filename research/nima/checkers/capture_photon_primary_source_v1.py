"""Freeze attributed primary-source excerpts; never execute downloaded TeX.

Inputs were retrieved under operator-authorized fallback after curl was refused
by structured-command. Ordinary verification uses the frozen excerpts offline.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

HOME=Path(__file__).resolve().parents[1]
SOURCES=HOME/'sources'
PINNED={
    'pdf':'886acd1357146f94cde8e503e919d5a36d4b6d7cab2bf519eb08e51472d535eb',
    'archive':'a46a0e0c1622208b8b4dd56832b852d93bd2804bbb96f0dbdd60a77bec9548f3',
    'tex':'63d21a309c371b93b383a5af756e449302e00b9efe7c41504b1f94d37a398430',
    'pdf_text':'c3ef0c9c4b7b375bc2c7294d73957cf4885ae03985ea83c2a70a56679c5646d3',
}
RANGES=[(235,274),(419,471),(1611,1664),(1706,1722),(1846,1874),(3118,3140)]
CREDIT=('Kelian Haring, Aditya Hebbar, Denis Karateev, Marco Meineri, Joao Penedones; '
        'Bounds on photon scattering; JHEP10(2024)103; DOI:10.1007/JHEP10(2024)103; CC-BY-4.0')


def sha(data):return hashlib.sha256(data).hexdigest()

def create_exact(path,data):
    if path.exists():
        assert path.read_bytes()==data,'refusing to replace a different source snapshot: '+str(path)
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in PINNED:p.add_argument('--'+name.replace('_','-'),type=Path,required=True)
    a=p.parse_args();data={k:getattr(a,k).read_bytes() for k in PINNED}
    assert {k:sha(v) for k,v in data.items()}==PINNED,'primary source bytes differ from inspected retrieval'
    lines=data['tex'].decode('utf-8').splitlines(keepends=True)
    chunks=[];ranges=[]
    for first,last in RANGES:
        body=''.join(lines[first-1:last]);ranges.append({'first_line':first,'last_line':last,'sha256':sha(body.encode('utf-8'))})
        chunks.append(f'% main.tex lines {first}-{last}; unmodified quotation follows.\n'+body+'\n')
    tex=('% '+CREDIT+'\n% Source: https://arxiv.org/src/2211.05795\n% Attribution/header comments added; quotations unmodified.\n\n'+''.join(chunks)).encode('utf-8')
    equation=re.compile(r'\((?:1\.8|1\.21|1\.22|A\.3|A\.5|A\.7|A\.26|A\.32|C\.4)\)\s*$',re.M)
    pages=data['pdf_text'].decode('utf-8').split('\f')
    selected=[(i,text) for i,text in enumerate(pages,1) if equation.search(text)]
    assert len(selected)>=5,'primary PDF equation pages not found'
    pdf_text=(CREDIT+'\nSource: https://doi.org/10.1007/JHEP10(2024)103\n'
              'Selected pdftotext -enc UTF-8 -layout pages; no formula repair.\n\n'+
              '\n'.join(f'=== PDF page {i} ===\n{text}' for i,text in selected)).encode('utf-8')
    filenames={'tex_excerpt':'photon-scattering-2024-excerpts.tex','pdf_text_excerpt':'photon-scattering-2024-pdf-excerpts.txt'}
    for key,body in (('tex_excerpt',tex),('pdf_text_excerpt',pdf_text)):create_exact(SOURCES/filenames[key],body)
    record={'schema':'marici.primary-source-snapshot.v1','citation':CREDIT,
        'published_pdf_url':'https://link.springer.com/content/pdf/10.1007/JHEP10%282024%29103.pdf',
        'author_tex_url':'https://arxiv.org/src/2211.05795',
        'retrieved_at_utc':datetime.now(timezone.utc).isoformat(),
        'retrieval':'curl authorized by operator after command-policy refusal; TeX extracted as data; pdftotext -enc UTF-8 -layout',
        'operator_authorization':'proceed to do that, following explicit request to supply PDF or authorize retrieval',
        'input_sha256':PINNED,'main_tex_ranges':ranges,'pdf_page_numbers':[i for i,_ in selected],
        'snapshot_files':filenames,'snapshot_sha256':{'tex_excerpt':sha(tex),'pdf_text_excerpt':sha(pdf_text)},
        'scope':'Primary amplitude conventions and one-loop coefficients only; not a review of all paper claims'}
    path=SOURCES/'photon-scattering-2024-provenance.json'
    if path.exists():record['retrieved_at_utc']=json.loads(path.read_text(encoding='utf-8'))['retrieved_at_utc']
    create_exact(path,(json.dumps(record,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({'status':'captured','provenance':path.relative_to(HOME).as_posix(),
                      'snapshot_sha256':record['snapshot_sha256'],'pdf_page_numbers':record['pdf_page_numbers']}))

if __name__=='__main__':main()
