"""Recover the third inclusion-minimal predecessor route with the unchanged forward rule. Separately classify which families permit a blocked initial addition."""
from ramsey_contact_blind_neighbors import build,CAT,D,decode,gzip,Path,tempfile,subprocess,json
from itertools import islice
from ramsey_cube_retention_floor import induced,G,iso

def audit():
    x=json.loads((D.parent/'ramsey_centered_family_envelope.json').read_text());new,=set(x['minimum_records'])-{236272,262402};ref=lambda t:x['types'][t]['record'];path={}
    for r in x['signatures']:
        for m in r['models']:
            if sum(m['extra_paths']):path.setdefault(ref(m['type']),set()).update(ref(t) for t in m['min_ancestors'])
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,new,None)).strip())
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'frozen.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True);st,ws=build(exe,a)
    target=induced(G,[u for u in range(34) if not G[34]>>u&1]);
    for w in ws:w['cube']=iso(induced(w.pop('core'),[u for u in range(27) if u!=w['z']]),target) is not None
    out=dict(record=new,counts=st,witnesses=ws,blocked_families={k:sorted(v) for k,v in path.items()});print(out);(D.parent/'ramsey_centered_third_root.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
