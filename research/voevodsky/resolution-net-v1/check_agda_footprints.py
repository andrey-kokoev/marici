"""Fresh headless check of pointwise resource accounting and footprint separation."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent;repo=root.parents[2]
cubical=Path(sys.argv[1]) if len(sys.argv)>1 else Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')
source=root/'agda/ResolutionNetFootprints.agda';reference=repo/'research/nima/agda/CoherenceResolutionClosure.agda'
args=['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(reference.parent),'-i',str(cubical),str(source)]
version=subprocess.run(['agda','--version'],capture_output=True,text=True,check=True).stdout.strip()
completed=subprocess.run(args,capture_output=True,text=True)
(root/'results/agda-footprints.log').write_text(completed.stdout+'\n'+completed.stderr)
report={'passed':completed.returncode==0,'agda_version':version,'cubical_library':str(cubical),'fresh_interfaces':True,'command':args,'source_sha256':{str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,reference,Path(__file__))},'checked_laws':['use-accounting','origin-accounting','no-double-spend','no-duplicate-origin','no-overlap','TwoTokenExample.combined','TwoTokenExample.reject-revival'],'scope':'Generic per-token use/origin conservation for unary changes and binary footprint-separated joins. Includes nonvacuous two-token derivation and spent/free overlap rejection. Not global commit authority, resource creation/splitting, Python refinement or finite total-cardinality accounting.'}
(root/'results/agda-footprints.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));sys.exit(completed.returncode)
