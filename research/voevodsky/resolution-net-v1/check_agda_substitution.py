"""Fresh headless check of the generic substitution bridge, not the Python net."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent;repo=root.parents[2]
cubical=Path(sys.argv[1]) if len(sys.argv)>1 else Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')
source=root/'agda/ResolutionNetSubstitution.agda';reference=repo/'research/nima/agda/CoherenceResolutionClosure.agda'
args=['agda','--ignore-interfaces','--transliterate','-i',str(root/'agda'),'-i',str(reference.parent),'-i',str(cubical),str(source)]
version=subprocess.run(['agda','--version'],capture_output=True,text=True,check=True).stdout.strip()
completed=subprocess.run(args,capture_output=True,text=True)
(root/'results/agda-substitution.log').write_text(completed.stdout+'\n'+completed.stderr)
report={'passed':completed.returncode==0,'agda_version':version,'cubical_library':str(cubical),'fresh_interfaces':True,'command':args,'source_sha256':{str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,reference,Path(__file__))},'checked_laws':['plug-unit','plug-compose','plug-flatten','plug-cong'],'scope':'Generic typed witnessed-resolution substitution laws, importing the original closure under safe/cubical/guardedness. Does not verify Python graph rewrites, admission, receipts or linear ownership.'}
(root/'results/agda-substitution.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));sys.exit(completed.returncode)
