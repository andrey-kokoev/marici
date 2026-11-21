"""Direct four-column binding test. Use native endpoint incidence and its two directed cycles; distinguish arrow automorphism from reversal of endpoints. No Ramsey colors as input."""
from itertools import permutations
from collections import Counter
from ramsey_directed_flag_pole import sub,cross,dot,flip,D,json
V='ABCD';E={'AB','BC','CA','AD','DB','BA'};R={'AB','BC','CA'};B=E-R;corners=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]

def run():
    syms={False:[],True:[]};rows=[]
    for p in permutations(V):
        m=dict(zip(V,p));image=lambda e:m[e[1]]+m[e[0]] if rev else m[e[0]]+m[e[1]]
        for rev in (False,True):
            if {image(e) for e in E}==E:syms[rev].append((''.join(p),{image(e) for e in R}==B))
    for p in permutations(V):
        a,b,c,d=p;rho=dict(zip(p,(a,c,b,d)));im=lambda e:rho[e[1]]+rho[e[0]]
        if {im(e) for e in E}!=E or {im(e) for e in R}!=B:continue
        pos=dict(zip(p,corners));diag=sub(corners[0],flip(corners[0]));normal=lambda a,b,c:cross(sub(pos[b],pos[a]),sub(pos[c],pos[a]));proj=[dot(diag,normal(*s)) for s in ('ABC','ADB')];seam=dot(diag,sub(pos['B'],pos['A']));rows.append(dict(columns=''.join(p),projections=proj,seam_projections=[seam,-seam]));assert abs(seam)==2;assert proj[0]==proj[1]!=0
    return dict(symmetries=syms,anti_row_bindings=rows)
if __name__=='__main__':
    r=run();print(r);(D/'ramsey_native_seam_pole.json').write_text(json.dumps(r)+'\n')
