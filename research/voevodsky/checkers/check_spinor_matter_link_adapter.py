"""Source spinor-line adapter to the existing weighted matter/link action.

Exact Q(sqrt(3),i) calculations retain the tetrahedral Berry link phases.
Signed electric charges are declared field assignments, not norm inference.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from check_electron_tetrahedral_spinor import D, ident, adj, sm, ma, trace, gmm, G0, G1, GI, gc, gm, ga, gs, gt, pos, encode

BASE = Path(__file__).resolve().parents[1]


def decode(z):
    return tuple(D(F(a), F(b)) for a, b in z)


def action(a, v):
    return tuple(gt(gm(x,y) for x,y in zip(row,v)) for row in a)


def evaluate(a, phases, norms, pairs, hops):
    gradient = [gs(n,z) for n,z in zip(norms,a)]
    energy = sum(n*gm(gc(z),z)[0] for n,z in zip(norms,a))
    currents = []
    for (i,j), hop, phase in zip(pairs,hops,phases):
        u = gm(hop,phase)
        cross = gm(gc(a[j]),gm(u,a[i]))
        energy -= 2*cross[0]
        gradient[i] = ga(gradient[i],gs(-1,gm(gc(u),a[j])))
        gradient[j] = ga(gradient[j],gs(-1,gm(u,a[i])))
        currents.append(2*cross[1])
        # d/d(q*A) of -2 Re(conj(a_j)*hop*exp(i*q*A)*a_i).
        derivative = -2*gm(GI,cross)[0]
        assert derivative==currents[-1]
    velocity = tuple(gs(D(-1)/n,gm(GI,z)) for n,z in zip(norms,gradient))
    density_rate = [2*n*gm(gc(z),dz)[0] for n,z,dz in zip(norms,a,velocity)]
    divergence = [D() for _ in a]
    for (i,j), current in zip(pairs,currents):
        divergence[i] -= current
        divergence[j] += current
    assert all(dr+dj==0 for dr,dj in zip(density_rate,divergence))
    return energy, currents, density_rate, divergence


def main():
    path = BASE/'results/electron_tetrahedral_spinor_store.json'
    raw = path.read_bytes()
    store = json.loads(raw)
    face = [tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors']]
    # A nonzero source column supplies each local line, without taking roots.
    local = [tuple(p[i][0] for i in range(2)) for p in face]
    norms = [gt(gm(gc(z),z) for z in v)[0] for v in local]
    assert all(pos(n) for n in norms)
    v = tuple(tuple(local[j][i%2] if i//2==j else G0 for j in range(4)) for i in range(8))
    decoder = tuple(tuple(gs(D(1)/n,gc(v[i][j])) for i in range(8)) for j,n in enumerate(norms))
    assert gmm(decoder,v)==ident(4)
    l = tuple(tuple(face[i//2][i%2][j%2] if i//2==j//2 else G0 for j in range(8)) for i in range(8))
    n = tuple(tuple(gs(F(1,2),gmm(face[i//2],face[j//2])[i%2][j%2]) for j in range(8)) for i in range(8))
    h = ma(ma(ident(8),sm(-1,l)),sm(2,ma(ident(8),sm(-1,n))))
    k = gmm(decoder,gmm(h,v))
    assert gmm(h,v)==gmm(v,k)
    assert gmm(k,k)==sm(2,k)
    assert trace(k)[0]==4 and trace(k)[1]==0
    assert all(gs(norms[i],k[i][j])==gc(gs(norms[j],k[j][i])) for i in range(4) for j in range(4))
    pairs = list(combinations(range(4),2))
    hops = []
    for i,j in pairs:
        assert k[i][i]==G1 and k[j][j]==G1
        hop = gs(-norms[j],k[j][i])
        assert gm(gc(hop),hop)[0]==norms[i]*norms[j]/3
        hops.append(hop)
    fluxes = []
    for i,j,kindex in combinations(range(4),3):
        triple = trace(gmm(gmm(face[i],face[j]),face[kindex]))
        normalized = gs(D(0,3),triple)  # magnitude 1/(3*sqrt(3))
        assert normalized in (GI,gs(-1,GI))
        fluxes.append({'faces':[i,j,kindex], 'projector_loop_phase':encode(normalized)})
    a = ((F(1,3),F(1,5)),(F(-2,7),F(1,4)),(F(3,8),F(-1,6)),(F(1,2),F(2,9)))
    phases = (G1,GI,gs(-1,G1),gs(-1,GI),G1,GI)
    e,current,dr,div = evaluate(a,phases,norms,pairs,hops)
    gauge = (G1,GI,gs(-1,G1),gs(-1,GI))
    charge_checks = {}
    for charge in (-1,1):
        local_gauge = gauge if charge==1 else tuple(gc(z) for z in gauge)
        transformed = tuple(gm(u,z) for u,z in zip(local_gauge,a))
        phase_new = tuple(gm(gm(local_gauge[j],phase),gc(local_gauge[i]))
                          for (i,j),phase in zip(pairs,phases))
        ee,jj,dd,bb = evaluate(transformed,phase_new,norms,pairs,hops)
        assert ee==e and jj==current and dd==dr and bb==div
        # E_dot=-charge*J, so B E_dot-charge*rho_dot vanishes.
        assert all(-charge*b-charge*d==0 for b,d in zip(div,dr))
        charge_checks[str(charge)] = {'weighted_continuity':True,
                                      'gauge_covariance':True,
                                      'signed_Gauss_derivative':True}
    # Extend the EXISTING common graph, retaining its inactive blocks.
    weighted_path = BASE/'results/weighted_matter_link_adapter.json'
    weighted_raw = weighted_path.read_bytes()
    weighted = json.loads(weighted_raw)['carriers']
    contact_path = BASE/'results/all_face_contact.json'
    contact_raw = contact_path.read_bytes()
    contacts = json.loads(contact_raw)['carriers']
    exterior = 34
    graph = []
    for species, offset in (('proton',0),('belt',12)):
        graph.extend((i+offset,j+offset) for i,j,_ in weighted[species]['edges'])
        graph.extend((exterior,i+offset) for i in contacts[species]['covered_triangles'])
    graph.extend((i+30,j+30) for i,j in pairs)
    graph.extend((exterior,i+30) for i in range(4))
    assert len(graph)==97
    def gauss(rp,re):
        # Belt has declared electric charge zero. It remains in the graph.
        phi = list(rp)+[D()]*18+[-(x+sum(re))/5 for x in re]+[D()]
        fields = [phi[j]-phi[i] for i,j in graph]
        divergence = [D() for _ in range(35)]
        for (i,j),field in zip(graph,fields):
            divergence[i] -= field
            divergence[j] += field
        assert divergence==list(rp)+[D()]*18+[-x for x in re]+[-sum(rp)+sum(re)]
        return sum(x*x for x in fields)/2
    assert gauss([D()]*12,[D()]*4)==0
    assert gauss([F(1,12)]*12,[D()]*4)==F(1,24)
    assert gauss([D()]*12,[F(1,4)]*4)==F(1,8)
    assert gauss([F(1,12)]*12,[F(1,4)]*4)==F(1,6)
    # The all-spin spinor has rho_i=(1-n_i dot s)/4 for unit Bloch s.
    normals = [[D(F(a),F(b)) for a,b in row] for row in store['normals']]
    for spin in ((1,0,0),(0,1,0),(0,0,1),(F(3,5),F(4,5),0)):
        assert sum(x*x for x in spin)==1
        density = [(1-sum(x*y for x,y in zip(normal,spin)))/4 for normal in normals]
        assert sum(density)==1 and sum(x*x for x in density)==F(1,3)
        # Complete four-vertex graph with a lead at every vertex:
        # L_boundary=5I-ones, inverse=(I+ones)/5.
        assert (sum(x*x for x in density)+1)/5==F(4,15)
        assert gauss([D()]*12,density)==F(2,15)
    beta,eta = F(3,5),F(1,5)
    root3 = D(0,1)
    onsite = 1-root3
    assert pos(-onsite)
    relaxed_electron = onsite+beta/8+eta/2
    coherent_electron = 2*beta/15+eta/2
    assert pos(coherent_electron-relaxed_electron)
    report = {
        'verification_passed':True,
        'source_sha256':{'electron_spinor':sha256(raw).hexdigest(),
                         'weighted_carriers':sha256(weighted_raw).hexdigest(),
                         'all_face_contacts':sha256(contact_raw).hexdigest()},
        'selected_spinor_lines':4,
        'raw_spinor_coordinates':8,
        'metric_norms':[[str(x.a),str(x.b)] for x in norms],
        'zero_field_intertwiner_exact':True,
        'reduced_spectrum':{'0':2,'2':2},
        'spectator_spectrum':{'3':4},
        'normalized_link_magnitudes':'1/sqrt(3), all six source face edges',
        'mandatory_onsite_term':'1-sqrt(3) per unit matter norm',
        'native_energy_identity':'K_e=sum_edges (1/sqrt(3))*|a_j-U_source,ij*a_i|^2 +(1-sqrt(3))*sum_i |a_i|^2 in normalized line coordinates',
        'source_face_fluxes':fluxes,
        'source_flux_is_flat':False,
        'signed_charge_checks':charge_checks,
        'common_graph_extension':{'vertices':35,'links':97,'charged_species':{'proton':1,'belt':0,'elementary_spinor':-1},'exterior_charge':'-(Q_proton-Q_elementary)', 'zero_background_Gauss_checked':True},
        'coherent_spinor_density_squared_sum':'1/3, independent of pure logical spin',
        'electron_coherent_field_energy':'2*beta/15+eta/2 at native link phases',
        'electric_only_relaxed_unit_sector':{
            'electron':'1-sqrt(3)+beta/8+eta/2',
            'proton':'beta/24+eta/2',
            'neutral_belt':'0',
            'reason':'Free electric-only link phases can cancel the source spinor holonomy; uniform density then attains both matter and field lower bounds.',
            'source_doublet_preserved_by_global_minimization':False},
        'fixture':{'beta':str(beta),'eta':str(eta),
                   'electron_correction':float(relaxed_electron.a)+float(relaxed_electron.b)*3**0.5,
                   'electron_with_one_unit_occupation':1+float(relaxed_electron.a)+float(relaxed_electron.b)*3**0.5,
                   'proton_correction':float(beta/24+eta/2),'neutral_belt_correction':0},
        'next_gate':'Retain or dynamically source the nonflat spinor face holonomy, using the actual face loops; an electric-only scalar adapter cannot preserve the elementary doublet. Signed electric loading alone does not generate a heavier neutral belt.',
        'scope':'Classical weighted matter/link adapter with declared signed charges, not charge quantization or nuclear binding.',
    }
    out = BASE/'results/spinor_matter_link_adapter.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
