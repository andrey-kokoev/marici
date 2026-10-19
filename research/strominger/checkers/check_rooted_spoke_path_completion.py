#!/usr/bin/env python3
"""Fresh safe Cubical check plus a directed-arrow rejection control."""
import hashlib
import json
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
AGDA=Path('C:/Users/andrey/tools/cubical-agda/agda-2.8.0/agda.exe')
CUBICAL=Path('C:/Users/andrey/tools/cubical-agda/cubical-0.9')

def main():
    flags=['--transliterate','--cubical','--safe','--guardedness','--no-import-sorts','-WnoUnsupportedIndexedMatch','--no-libraries','--ignore-interfaces','-i','research/strominger/agda','-i','research/nima/agda','-i',str(CUBICAL)]
    logs={};checks={}
    for module,expected in [('RootedSpokePathCompletion',True),('SpokeBadDirectedCompletion',False)]:
        command=[str(AGDA)]+flags+[f'research/strominger/agda/{module}.agda']
        process=subprocess.run(command,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=240)
        text=process.stdout.decode('utf-8',errors='replace')
        dest=ROOT/f'research/strominger/results/{module}.log'
        dest.write_text(text,encoding='utf-8')
        checks[module]=(process.returncode==0) if expected else (process.returncode!=0 and ('A != B' in text or 'Arrow A B' in text))
        logs[module]={'returncode':process.returncode,'expected_success':expected,'log':str(dest.relative_to(ROOT)).replace('\\','/'),'command':command}
    deps=[Path(__file__),AGDA,CUBICAL/'cubical.agda-lib']+[ROOT/f'research/strominger/agda/{name}.agda' for name in ('RootedSpokePathCompletion','SpokeBadDirectedCompletion')]+[ROOT/f'research/nima/agda/{name}.agda' for name in ('MarkedTetrahedronCoherence','MarkedTriangleCoherence','RelativeCoherentCompletion','GradedBoundaryCoherence')]
    out={'schema':'marici.strominger.rooted-spoke-path-completion.v1','status':'passed' if all(checks.values()) else 'failed','fresh_execution':True,'ignore_interfaces':True,'checks':checks,'executions':logs,'constructor':{'input':['AB:A=B','AC:A=C','AD:A=D'],'derived_edges':{'BC':'sym AB . AC','BD':'sym AB . AD','CD':'sym AC . AD'},'faces':['ABC','ABD','ACD','BCD'],'tetrahedral_filler':'existing MarkedTetrahedronCoherence.unique123','original_spokes_preserved':True},'scope':'Path-specialized current completion machinery. Primitive directed occurrences alone are not equality paths and the negative control rejects their automatic branch completion. No metric is supplied or inferred.','source_hashes':{str(p.relative_to(ROOT)).replace('\\','/') if p.is_relative_to(ROOT) else str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}}
    (ROOT/'research/strominger/results/rooted_spoke_path_completion.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'fresh_execution':True,'checks':checks,'constructor':out['constructor']},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
