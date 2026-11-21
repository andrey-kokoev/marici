"""Run compiled ramsey_forward_sparse26 on a 21-vertex input; no 26- or 35-target incidences are used for selection."""
import sys,subprocess
from ramsey_slack_ladder_replay import attach,verify
from ramsey_hall_anchor_ports import D,json,anchor_lift
if __name__=='__main__':
    H=json.loads((D/'ramsey_slack_ladder_certificates.json').read_text())[0]['graph'];p=subprocess.run([sys.argv[1],*map(str,H)],capture_output=True,text=True,check=True);print(p.stderr);rows=[]
    for line in p.stdout.splitlines():
        S=list(map(int,line.split()));A=attach(H,S);verify(A,8);r=anchor_lift(A,9);assert r is not None;rows.append({'first_supports':S,'anchor_lift':r});print(S,'regular 35?', 'graph' in r,'nodes',r['search_nodes'])
    (D/'ramsey_sparse26_forward_check.json').write_text(json.dumps(rows)+'\n')
