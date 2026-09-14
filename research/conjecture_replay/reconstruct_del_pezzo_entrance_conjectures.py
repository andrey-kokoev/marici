#!/usr/bin/env python3
"""Reconstruct an entrance-time conjecture/action inventory without holdout inputs."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
freeze=json.loads((R/'research/conjecture_replay/results/del_pezzo_entrance_freeze.json').read_text())
cutoff=freeze['cutoff']['mtime_ns']
refs={
 'surface':'research/voevodsky/results/global_del_pezzo_double_cover.json',
 'torsion':'research/voevodsky/results/del_pezzo_complement_torsion.json',
 'site':'research/voevodsky/results/visible_site_exchange_parity_action.json',
 'geiser':'research/voevodsky/results/geiser_mod_two_action.json',
 'quartic':'research/voevodsky/results/quartic_reflection_elliptic_action.json'}
for k,v in refs.items():
 p=R/v
 assert p.exists() and (p.stat().st_mtime_ns<=cutoff or k=='surface'),(k,p.stat().st_mtime_ns,cutoff)

def C(i,statement,experiment,provenance,admissibility,target,alternatives):
 return {'id':f'DP{i}','statement':statement,'resolving_experiment':experiment,'provenance':[refs[x] for x in provenance],'historical_admissibility':admissibility,'target_information':target,'explicit_alternatives':alternatives,'outcome':'HIDDEN'}
cs=[
 C(1,'A pencil preserved by the global reflection exposes the invariant rank-three E7 lattice through reducible or split fibers.','Analyze pencils through each isolated fixed base point; factor their discriminants and singular fibers.',['surface'],'direct consequence of the explicit global involution and its (3,4) E7 eigensplit','invariant E7 marking',['no useful preserved pencil','preserved pencil but insufficient reducible fibers','fiber components span a proper invariant sublattice','fiber components span the invariant rank-three lattice']),
 C(2,'The source e6 line is a component-difference root in a distinguished global singular fiber.','Embed the source soft-node center into the global surface and compare its two local branches with fiber components.',['surface'],'explicit entrance target: place the source support plane in the global marking','placement of e6',['no global specialization','specialization misses singular fibers','singular fiber found but source branch is a sum','source branch equals a primitive component difference']),
 C(3,'The v_alg line is a marked integral combination of component differences complementary to e6.','Compute a Picard marking or intersection fingerprint for v_alg against the invariant lattice.',['surface'],'second half of the explicit entrance target','placement of v_alg',['outside invariant lattice','inside only rationally','integral but nonprimitive','primitive marked combination']),
 C(4,'A nontrivial saturation index in the component-difference lattice accounts for the observed half-integral normalization.','Compute the Smith form and primitive closure of the component-difference span in E7.',['surface','torsion'],'motivated by the known E7 lattice and unresolved integral parity','integral normalization',['saturated','index two','higher index','rank defect']),
 C(5,'The surviving two-bit ambiguity is encoded by pairings of geometrically distinguished split components or branch points.','Enumerate the induced mod-two discriminant classes and the symmetry action on their pairings.',['surface','torsion','site','geiser','quartic'],'pre-cutoff parity-selector problem transported to the new global marking','mod-two support plane',['no canonical marks','marks but trivial quotient','three nonzero pairing classes','unique symmetry-selected class']),
 C(6,'The physical total-energy degeneration selects an integral class in the globally marked lattice.','Restrict the global surface along total energy and compute the degeneration, vanishing components, and thimble incidence.',['surface','torsion'],'pre-existing request for one direct integral intersection, now enabled by the global equation','physical readout',['no degeneration','degeneration without marked incidence','rank-one incidence','rank-two incidence']),
 C(7,'A direct blow-up/Picard marking identifies the invariant rank-three lattice without choosing a pencil.','Resolve the branch quartic, enumerate exceptional curves, and compute the integral matrix of r_a on Picard.',['surface'],'literal implementation of the entrance next step','invariant E7 marking',['resolution obstructed','marking noncanonical','rational eigenspace only','integral invariant lattice obtained']),
 C(8,'Composing the global reflection with Geiser yields a parity selector invisible on the infinity elliptic section.','Compute both global Picard actions and reduce their restrictions on the source support plane modulo two.',['surface','geiser','quartic','site'],'remaining global lift was unavailable before the entrance; the entrance supplies it','symmetry selector',['both mod-two trivial','one nontrivial but no unique class','nontrivial with fixed line','unique nonzero class selected']),
]
# Distinct IDs/statements and exclusively frozen provenance are executable non-leakage checks.
all_holdout={x['path'] for x in freeze['holdout_manifest']}
checks={'eight_candidates':len(cs)==8,'ids_unique':len({c['id'] for c in cs})==len(cs),'statements_unique':len({c['statement'] for c in cs})==len(cs),'four_alternatives_each':all(len(c['explicit_alternatives'])==4 for c in cs),'outcomes_hidden':all(c['outcome']=='HIDDEN' for c in cs),'no_holdout_provenance':all(not(all_holdout & set(c['provenance'])) for c in cs)}
assert all(checks.values()),checks
out={'schema':'marici.conjecture-replay.del-pezzo-entrance-inventory.v1','cutoff_sha256':freeze['cutoff']['sha256'],'construction':'Statements are generated from the entrance target plus unresolved pre-cutoff selectors. No holdout result is read.','conjectures':cs,'checks':checks,'passed':True}
dest=R/'research/conjecture_replay/results/del_pezzo_entrance_conjectures.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'count':len(cs),'ids':[c['id'] for c in cs],'provenance_files':sorted(set(sum((c['provenance'] for c in cs),[])))}))
