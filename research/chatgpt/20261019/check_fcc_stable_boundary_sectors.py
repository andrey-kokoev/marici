import numpy as np, json
from pathlib import Path
root=Path(__file__).parent/'results'
out=[]
for s in (1,2,4,8,16):
 p=np.load(root/f'T_side{s}.npz'); xyz=p['points'].astype(float); K=p['kernel']; n=len(xyz)
 # columns span singlet and geometric coordinate triplet
 X=np.column_stack((np.ones(n),xyz[:,0]-s/2,xyz[:,1]-s/2,xyz[:,2]-s/2))
 U,_=np.linalg.qr(X)
 # orthogonalized first const, other triples retain tetrahedral group via geometric embedding
 proj=U.T@K@U
 eig=np.linalg.eigvalsh(proj)
 # Gaussian marginal: precision for 4 normalized moments after eliminating all other boundary modes
 invsel=np.linalg.solve(K,U); C=U.T@invsel
 Seff=np.linalg.inv(C)
 ev=np.linalg.eigvalsh(Seff)
 # Rayleigh quotient of uniform original physical boundary field, and its response per point
 one=np.ones(n)
 row_sums=K@one
 out.append(dict(s=s,n=n,restriction_singlet=float(one@K@one/n),restriction_triplet=float(np.mean(np.diag(proj)[1:])),marginal_singlet=float(Seff[0,0]),marginal_triplet=float(np.mean(np.diag(Seff)[1:])),restriction_ratio=float(np.mean(np.diag(proj)[1:])/proj[0,0]),marginal_ratio=float(np.mean(np.diag(Seff)[1:])/Seff[0,0]),offblock_norm=float(np.linalg.norm(proj-np.diag(np.diag(proj)))),constant_mode_total=float(one@K@one),constant_mode_per_boundary_site=float(one@K@one/n),constant_mode_per_length=float(one@K@one/s)))
print(json.dumps(out,indent=2))
Path(__file__).with_name('fcc_stable_boundary_sectors_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
