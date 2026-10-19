"""SCC Python entrypoint; delegates to the two exact Node checkers."""
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    for name in ('check_isotope_obstruction_atlas.mjs','check_isotope_materialization_square.mjs'):
        result=subprocess.run(['node',f'research/strominger/checkers/{name}'],cwd=ROOT,capture_output=True,text=True,timeout=180)
        if result.returncode:
            print(result.stdout);print(result.stderr);raise SystemExit(result.returncode)
    base=ROOT/'research/strominger/results/isotope-obstruction-atlas'
    atlas=json.loads((base/'verification.json').read_text())
    square=json.loads((base/'materialization-square.json').read_text())
    assert atlas['status']==square['status']=='pass' and square['allFiveRoutesPlanned']
    print(json.dumps({'status':'pass','classification':'finite-fixed-support-obstruction-and-neon-materialization-square',
                      'cases':sum(r['cases'] for r in atlas['summaries'].values()),
                      'portBudgetCounterexamples':len(atlas['portBudgetCollisions']),
                      'routesReplayed':len(square['routes']),
                      'scope':'Exact declared experimental construction, not native adoption or physical isotope dynamics'}))
