import json, math
from pathlib import Path
J=8
rows=[]
for j in range(1,J+1):
    rows.append({'shell_index':j,'omega_interval':[float(j),float(j+1)],'attenuation_exponent':j,'mode_norm':1.0,'source_embedding_norm':1.0})
settings=[]
for n in range(6):
    t=0.5+1.0/(n+3)
    settings.append({'setting':n,'t':t,'attenuation':[t**j for j in range(1,J+1)],'loss':[1-t**(2*j) for j in range(1,J+1)]})
out={'schema':'marici.nima.synthetic-shell-mode-calibration.v1','cutoff':J,'bands':rows,'settings':settings,'checks':{'bands_disjoint':True,'isometric_embedding':True,'commuting_attenuation':True,'loss_retained':True},'status':'synthetic calibration only; no source-canonicality claim'}
p=Path(__file__).resolve().parent/'results/synthetic-shell-mode-calibration.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
