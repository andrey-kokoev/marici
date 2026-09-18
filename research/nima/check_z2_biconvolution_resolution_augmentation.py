#!/usr/bin/env python3
"""Toy model for [(I,I),(*,*)] convolutional resolution and augmentation."""
import json,itertools
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
G=list(itertools.product((0,1),repeat=2));idx={x:i for i,x in enumerate(G)}
def add(x,y):return (x[0]^y[0],x[1]^y[1])
def conv_matrix(f):return [[f[add(x,y)] for y in G] for x in G]
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(4)) for i in range(4)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def augment(v):return sum(v)
def fourier(f,chi):return sum(((-1)**(chi[0]*x[0]+chi[1]*x[1]))*f[x] for x in G)
e=[Fraction(1),Fraction(0),Fraction(0),Fraction(0)]
f={(0,0):Fraction(2),(0,1):Fraction(1),(1,0):Fraction(3),(1,1):Fraction(-2)}
f_alt={(0,0):Fraction(5),(0,1):Fraction(-1),(1,0):Fraction(1),(1,1):Fraction(-1)}
g={(0,0):Fraction(1),(0,1):Fraction(2),(1,0):Fraction(-1),(1,1):Fraction(3)}
Cf,Ca,Cg=map(conv_matrix,(f,f_alt,g));rf,ra=mv(Cf,e),mv(Ca,e);full_two=mv(mm(Cg,Cf),e);alt_two=mv(mm(Cg,Ca),e)
chars={str(c):{'f':str(fourier(f,c)),'f_alt':str(fourier(f_alt,c)),'g':str(fourier(g,c))} for c in G}
out={'schema':'marici.nima.z2-biconvolution-resolution-augmentation.v1','coordinates':['(0,0)','(0,1)','(1,0)','(1,1)'],'identity_state':[str(v) for v in e],'resolved_f':[str(v) for v in rf],'resolved_f_alt':[str(v) for v in ra],'augmentation_f':str(augment(rf)),'augmentation_f_alt':str(augment(ra)),'two_phase_resolved_f_then_g':[str(v) for v in full_two],'two_phase_resolved_f_alt_then_g':[str(v) for v in alt_two],'two_phase_augmentation_f_then_g':str(augment(full_two)),'two_phase_augmentation_f_alt_then_g':str(augment(alt_two)),'fourier_channels':chars,'checks':{'two_convolution_coordinates':len(G)==4,'different_resolved_states':rf!=ra,'same_identity_readout':augment(rf)==augment(ra),'nontrivial_fourier_information_differs':any(fourier(f,c)!=fourier(f_alt,c) for c in G if c!=(0,0)),'repeated_augmentation_retains_only_trivial_channel':augment(full_two)==augment(alt_two)==fourier(g,(0,0))*fourier(f,(0,0)),'resolved_two_phase_states_remain_distinct':full_two!=alt_two}}
out['passed']=all(out['checks'].values());out['interpretation']='Double augmentation projects H tensor H onto the trivial Fourier character; repeated scalar phases cannot recover the other three channels.'
p=ROOT/'research/nima/results/z2-biconvolution-resolution-augmentation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
