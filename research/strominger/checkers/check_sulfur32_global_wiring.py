from pathlib import Path
import json
import subprocess
import sys

if __name__ == '__main__':
    root=Path(__file__).resolve().parents[3]
    report=json.loads(subprocess.check_output(['node','research/strominger/checkers/check_sulfur32_global_wiring.mjs'],cwd=root,text=True))
    out=root/'research/strominger/results/sulfur-32-global-wiring'
    categorical=json.loads(subprocess.check_output([sys.executable,str(root/'research/aspect/scc/scc.py'),'categorical',str(out/'route-diagram.json')],cwd=root,text=True))
    assert categorical['passed'] and len(categorical['cells'])==2
    (out/'categorical-verification.json').write_text(json.dumps(categorical,indent=2)+'\n')
    report['categoricalCellsPassed']=2
    print(json.dumps(report,indent=2))
