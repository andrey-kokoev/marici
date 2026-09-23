"""Saturation analysis of a source-admitted binary section of the tail family.

S consists of x=0 and y in {0,1/2} on the ten even probe coordinates, zero
elsewhere. It is a finite section of the owning tail carrier, not its entirety.
Every zero-frame set J restricts S by vanishing at J. L retains eight probes.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import subprocess
import json
import sys
import hashlib
ROOT=Path(__file__).resolve().parents[3];N=ROOT/'research/nima';OUT=ROOT/'research/voevodsky/results'
p=N/'results/certified-forgetting-storage-obstruction-packet.json'
c=N/'results/certified-forgetting-storage-obstruction-contract.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
owner=json.loads(c.read_text());coords=owner['finite_test']['probe_coordinates'];H=len(coords);h=8
cp=OUT/'storage-obstruction-fiber-saturation-contract.json'
save(cp,{'packet_sha256':sha(p),'owner_sha256':sha(c),
 'source_section':'x=0; y_n is 0 or 1/2 on owning ten even probe coordinates and zero elsewhere.',
 'evidence':'C_J consists of section points with zero mass at every coordinate in J.',
 'observation':'First eight probe mass coordinates.',
 'reconstruction':'Sat(C)=S intersect L^-1(L(C)), using the known complete section S.',
 'prediction':'Exact model-based reconstruction iff hidden zero-frame restrictions are absent; a hidden frame supplies a source-admitted reopened point and a separating query.',
 'scope':'Finite section of owning infinite carrier. Query-collision witnesses are genuine admitted tails; no claim that the section equals every admitted tail.'})
subprocess.run([sys.executable,str(N/'checkers/verify_certified_forgetting_storage_obstruction.py')],check=True,capture_output=True,text=True)
S=set(range(1<<H));visible=(1<<h)-1;hidden=((1<<H)-1)^visible
# Independently verify every point of the section against all adjacent-capacity
# intervals through the last probe. Zero extension and monotone capacities
# handle later endpoints. x=0 satisfies its even-support constraints.
checks=0
for mask in S:
 for a in range(max(coords)):
  for b in range(a+1,max(coords)+1):
   mass=sum(Q(1,2) for i,n in enumerate(coords) if mask&(1<<i) and a<n<=b)
   assert mass<=Q(1,2)*((b-a+1)//2)
   checks+=1

def carrier(J):return {s for s in S if s&J==0}
def image(C):return {s&visible for s in C}
def reopen(V):return {s for s in S if s&visible in V}
def saturation(C):return reopen(image(C))
safe=unsafe=0;counterexamples=[]
for J in S:
 C=carrier(J);sat=saturation(C)
 assert sat==carrier(J&visible)
 assert C<=sat and saturation(sat)==sat
 if C==sat:
  safe+=1;assert J&hidden==0
 else:
  unsafe+=1;assert J&hidden
  bit=(J&hidden)&-(J&hidden)
  # A single source-admitted mass in an excluded hidden coordinate is restored.
  assert bit in sat-C
  assert any(s&bit for s in sat) and not any(s&bit for s in C)
  if len(counterexamples)<2:
   i=bit.bit_length()-1
   counterexamples.append({'zero_frame_coordinates':[coords[j] for j in range(H) if J&(1<<j)],
      'reopened_tail':{'x':'identically zero','y':{str(coords[i]):'1/2'},'other_y':'zero'},
      'separating_query':f'y_{coords[i]} >= 1/2',
      'actual_carrier_answer':'INFEASIBLE','reconstructed_answer':'FEASIBLE'})
assert safe==2**h and unsafe==2**H-2**h
# Four different hidden restrictions share each visible zero-frame image.
image_groups={}
for J in S:image_groups.setdefault(J&visible,[]).append(J)
assert len(image_groups)==256 and all(len(g)==4 for g in image_groups.values())
# Visible-coordinate refinement cannot eliminate independent hidden freedom
# in this source section: any nonempty visible image retains the hidden cube.
for code in range(1<<h):
 fiber=reopen({code});assert len(fiber)==4
 for i in range(h,H):
  assert {bool(s&(1<<i)) for s in fiber}=={False,True}
assert sha(p)==json.loads(cp.read_text())['packet_sha256']
report={'passed':True,'contract_sha256':sha(cp),'admitted_source_section_points':len(S),
 'independent_interval_checks':checks,'retained_zero_frame_carriers':1<<H,
 'fiber_saturated_carriers':safe,'unsaturated_carriers':unsafe,
 'identical_visible_image_groups':len(image_groups),'carriers_per_image':4,
 'counterexamples':counterexamples,
 'structural_result':'Known source model reconstructs the entire visible fiber. It cannot determine which hidden restriction had been admitted. Saturation supplies exactly the premise for safe reconstruction.',
 'sharpening':'In this independent-coordinate section, no nonempty visible refinement makes a hidden zero constraint redundant. Coupled analytical constraints can behave differently, as in the owning upgrade example.',
 'scope':'Exact finite-section test with genuine infinite zero-extended tail witnesses. It preserves the owning storage obstruction and does not conflate a possible source point with a retained possibility carrier.'}
save(OUT/'storage-obstruction-fiber-saturation.json',report)
print(json.dumps(report,indent=2))
