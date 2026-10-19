"""Exact joint-sector test of a common two-projector field model for T."""
from pathlib import Path
import json, hashlib
from fractions import Fraction
from assemble_metric_coefficient_protocol import read_operator, product, plus, scaled, integer_trace, sharp, A, ONE, ZERO
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/strominger/results';hashes={};rows={}
for species in ['proton','neutron','electron']:
    file=BASE/'common-three-carrier-protocol'/f'{species}.json';raw=file.read_bytes();hashes[str(file.relative_to(ROOT))]=hashlib.sha256(raw).hexdigest();d=json.loads(raw);metric=list(map(Fraction,d['source']['metric']));n=len(metric)
    L=read_operator(d['source']['local'],n);G=read_operator(d['source']['alignment'],n);N=read_operator(d['operators']['N'],n);I={(i,i):ONE for i in range(n)}
    assert product(L,G)==product(G,L)==N
    for X in [L,G]:assert product(X,X)==X and sharp(X,metric)==X
    sectors={'both':N,'local_only':plus(L,scaled(A(-1),N)),'alignment_only':plus(G,scaled(A(-1),N)),'neither':plus(I,scaled(A(-1),L),scaled(A(-1),G),N)}
    # Commuting orthogonal projectors imply these are orthogonal projectors;
    # their exact traces count joint eigenspace dimensions.
    dims={k:integer_trace(v) for k,v in sectors.items()};assert min(dims.values())>=0;assert sum(dims.values())==n
    H=plus(scaled(A(2),I),scaled(A(-1),L),scaled(A(-1),G));assert H==read_operator(d['operators']['H_in_pi_over_four_units'],n)
    spectrum={'0':dims['both'],'1':dims['local_only']+dims['alignment_only'],'2':dims['neither']}
    assert product(H,N)=={}
    rows[species]={'rawDimension':n,'rankL':integer_trace(L),'rankG':integer_trace(G),'rankReturn':integer_trace(N),'jointSectorDimensions':dims,'defectSpectrum':spectrum}
p=rows['proton']['jointSectorDimensions'];n=rows['neutron']['jointSectorDimensions'];e=rows['electron']['jointSectorDimensions']
assert p=={'both':n['both'],'local_only':n['alignment_only'],'alignment_only':n['local_only'],'neither':n['neither']}
assert e['alignment_only']==0;assert e['both']>p['both']
# Restriction preserving both projectors can only reduce joint multiplicities.
# Hence electron cannot be such a restriction of a single native baryon field.
minimumCopies=max((e[k]+p[k]-1)//p[k] for k in p if e[k]);assert minimumCopies==2
capacity={k:minimumCopies*p[k] for k in p};assert all(e[k]<=capacity[k] for k in p)
# Canonical under all within-sector unitary changes means selecting entire
# joint sectors. A smaller proper subspace requires additional structure.
noncanonical=[k for k in p if 0<e[k]<capacity[k]];assert noncanonical
out=BASE/'T-projector-field';out.mkdir(exist_ok=True)
result={'status':'common-projector-law-and-multiplicity-tested','carriers':rows,'universalLaw':{'return':'N=G L=L G','defect':'H=2I-L-G'},'protonNeutronExchange':{'jointSpectraExchangeExactly':True,'meaning':'Finite-dimensional metric-unitary equivalence exists after exchanging L/G, by the joint spectral theorem; no geometrically natural intertwiner constructed.'},'electron':{'singleBaryonRestrictionPossible':False,'obstruction':'common-image dimension 2 exceeds baryon common-image dimension 1','minimumBaryonCopiesForMultiplicityEmbedding':minimumCopies,'twoCopyCapacity':capacity,'electronTarget':e,'properSectorSelectionsNeedingAdditionalStructure':noncanonical,'meaning':'Dimension-level possibility of a reducing-subspace embedding, not a canonical physical doublet or a derived T field.'},'sourceHashes':hashes,'checkerSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact recomputation from native saved L/G source matrices and metrics. Universal projector law is prior established work. Tests common-field restriction/exchange hypotheses; does not derive native L/G, carrier geometry, metric or isotope contraction from T.'}
(out/'verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
