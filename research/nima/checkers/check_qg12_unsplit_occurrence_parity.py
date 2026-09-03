"""Mod-two parity of the two unsplit q_G12 occurrence labels across sign chambers."""
import itertools,json
rows=[]
for s31,s23 in itertools.product((1,-1),repeat=2):
 signed_current=s31+s23
 boundary_mod2=(s31%2,s23%2)
 total_parity=sum(boundary_mod2)%2
 rows.append({'signs':[s31,s23],'signed_current':signed_current,'boundary_mod2':list(boundary_mod2),'total_branch_parity':total_parity})
assert sorted(set(r['signed_current'] for r in rows))==[-2,0,2]
assert all(r['boundary_mod2']==[1,1] for r in rows)
assert all(r['total_branch_parity']==0 for r in rows)
print(json.dumps({'schema':'marici.nima.qg12-unsplit-occurrence-parity.v1','status':'passed','bold_conjecture':'regulator sign chambers can change the mod-two branch parity of the unsplit two-occurrence object','chambers':rows,'signed_chamber_currents':[-2,0,2],'unsplit_boundary_mod2':[1,1],'unsplit_total_parity':0,'conjecture_disposition':'falsified at occurrence-label level','surviving_result':'retaining q_g31 and q_g23 once each forces even total parity independently of chamber signs','residual_conjecture':'the two occurrence labels map respectively to the two split nearby-cycle branch points; this label-to-branch correspondence must be derived'},sort_keys=True))
