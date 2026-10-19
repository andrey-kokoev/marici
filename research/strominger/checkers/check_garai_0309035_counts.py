"""Audit explicit counting in Garai0309035v2, not its physical interpretation."""
from collections import Counter,defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
PDF=ROOT/'references/0309035v2.pdf'
INDEX=ROOT/'references/extractions/pdf-search-all/0309035v2'
OUT=ROOT/'research/strominger/results/garai-0309035v2/count-audit.json'

def main():
    rows=[]
    pattern=re.compile(r'(?<![\d.])(\d+)\s+([1-6])\s+([spdf])\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)')
    paths=[INDEX/f'pdf-page-{p:04}.txt' for p in range(12,16)]
    for page,path in zip(range(12,16),paths):
        for match in pattern.finditer(path.read_text(encoding='utf-8')):
            n,period,subshell,x,y,z=match.groups()
            rows.append({'id':int(n),'period':int(period),'subshell':subshell,'coordinate':[float(x),float(y),float(z)],'pdf_page':page})
    assert len(rows)==172 and [r['id'] for r in rows]==list(range(1,173))
    byperiod=Counter(r['period'] for r in rows)
    expected=[4,16,16,36,36,64]
    assert [byperiod[p] for p in range(1,7)]==expected
    bysub=defaultdict(Counter)
    for row in rows:bysub[row['period']][row['subshell']]+=1
    ell=dict(s=0,p=1,d=2,f=3)
    assert all(count==4*(2*ell[sub]+1) for counts in bysub.values() for sub,count in counts.items())
    triangle=lambda k:k*(k+1)//2
    paired=[triangle(2*n-1)+triangle(2*n) for n in range(1,5)]
    assert paired==[4,16,36,64]
    z=sorted({r['coordinate'][2] for r in rows})
    report={'status':'counting_identities_verified_not_physical_validation','pdf_title':'The double tetrahedron structure of the nucleus','author':'Jozsef Garai','pages':15,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),PDF,*paths]},
      'paired_triangular_layers':{'formula':'T_(2n-1)+T_(2n)=4n^2','all_nucleon_counts':paired,'protons_if_P_equals_N':[x//2 for x in paired]},
      'supplementary_rows':len(rows),'nucleons_by_period':dict(byperiod),'protons_by_period_if_P_equals_N':[byperiod[p]//2 for p in range(1,7)],
      'nucleons_by_period_and_subshell':dict(bysub),'subshell_rule':'4 corners times(2ell+1) nucleons; assuming half protons gives2(2ell+1)',
      'table_z_layers':z,'successive_table_z_gaps_rounded':[round(b-a,3) for a,b in zip(z,z[1:])],
      'source_discrepancies':['Page2 and Fig1B give54 for28+36; correct64 is printed in Fig1C.','FigS1 caption gives gap d*sqrt(2/3), while table coordinate z levels differ by approximately d/sqrt(2) with stated sphere diameter d=1. Layer directions/conventions require reconciliation.'],
      'physical_scope':['Table172 sites represents86P+86N under equal species counts; this does not represent common radon222 with86P+136N.','Sites are spherical nucleons in an FCC aggregate, not individual tetrahedral nucleons in diamond.','The spatial labels/counts do not supply an angular momentum representation, conserved charge or electronic-state readout.'],
      'rows':rows}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','paired_triangular_layers','supplementary_rows','protons_by_period_if_P_equals_N','source_discrepancies']}))

if __name__=='__main__':main()
