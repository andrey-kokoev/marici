"""Try robust witnesses first; use a stored calibration refinement only if needed.

Usage: uv run python <this-file> task.json [refined-calibration.json]
This workflow enables auto_witness without changing observations or the prior.
It does not silently launch expensive calibration computations. If no refined
bundle exists, run refine_three_channel_source_task.py and replay the same input.
"""
from pathlib import Path
import importlib.util,json,hashlib,copy,sys

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('source_task',HERE/'three_channel_source_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
DEFAULT_REFINEMENT=t.RESULTS/'three-channel-source-task-calibration-refined.json'

def certify(data,refinement_path=DEFAULT_REFINEMENT):
    original=copy.deepcopy(data)
    request=copy.deepcopy(data);request['auto_witness']=True
    baseline=t.SourceTask();first=baseline.certify(request)
    attempts=[{'calibration':'baseline',
               'calibration_sha256':hashlib.sha256((t.RESULTS/'three-channel-source-task-calibration.json').read_bytes()).hexdigest(),
               'result':first}]
    answer={'automatic_witness_search_enabled':True,'attempts':attempts,'status':first['status']}
    if first['status']=='UNRESOLVED':
        path=Path(refinement_path)
        if path.exists():
            refined=t.SourceTask(path)
            if not refined.refinements or refined.cal['protocol_sha256']!=baseline.cal['protocol_sha256']:
                raise ValueError('Expected a refinement of the same deployed protocol')
            ancestor=refined
            while hasattr(ancestor,'parent') and ancestor.cal!=baseline.cal:ancestor=ancestor.parent
            if ancestor.cal!=baseline.cal:raise ValueError('Refinement does not descend from the current baseline')
            second=refined.certify(request)
            attempts.append({'calibration_file':str(path),'calibration_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                             'result':second})
            answer['status']=second['status']
        else:
            answer['refinement_pending']='Run refine_three_channel_source_task.py, then replay this unchanged input.'
    assert original==data
    answer['scope']='At most one stored refinement; UNRESOLVED is not infeasibility or source ambiguity.'
    return answer

if __name__=='__main__':
    if len(sys.argv) not in (2,3):raise SystemExit(__doc__)
    path=Path(sys.argv[1]);raw=path.read_bytes()
    data=json.loads(raw)
    answer=certify(data,Path(sys.argv[2]) if len(sys.argv)==3 else DEFAULT_REFINEMENT)
    assert path.read_bytes()==raw, 'Input changed during certification'
    answer['input_sha256']=hashlib.sha256(raw).hexdigest()
    print(json.dumps(answer,indent=2))
