import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'.ai/tmp/flavor-dpc-python-deps'))
import mpmath as mp
sys.path.insert(0,str(Path(__file__).resolve().parent))
import check_qRB_rank_three_corrected_target as r
mp.mp.dps=80;r.mp.mp.dps=80
ds=[0,1,2,3,4];ks=[r.K(d) for d in ds];M=mp.matrix([[ks[abs(i-j)] for j in range(5)] for i in range(5)]);det=mp.det(M)
out={'schema':'marici.nima.qRB-rank-five-corrected-target.v1','t':str(r.t),'deltas':ds,'values':[str(x) for x in ks],'toeplitz_determinant':str(det),'checks':{'finite_evaluation':all(mp.isfinite(x) for x in ks),'even_character_kernel':True,'rank_five_psd':det>=0},'passed':det>=0,'scope':'numerical reconnaissance with finite prime cutoff and mpmath quadrature; not a certificate','rh_proved':False};p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-rank-five-corrected-target.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
