#!/usr/bin/env python3
"""Rigorous-formula trace bound for low Fourier leakage of a Legendre tail."""
import json,math
from pathlib import Path
L=.55;R=10.;N=160;z=L*R
# |j_n(z)| <= sqrt(pi) z^n exp(z^2/4)/(2^(n+1) Gamma(n+3/2)).
def log_j_bound(n):return .5*math.log(math.pi)+n*math.log(z)+z*z/4-(n+1)*math.log(2)-math.lgamma(n+1.5)
# Fourier normalization gives integral <= 2R*L(2n+1)/pi * bound^2.
logs=[]
for n in range(N,1000):logs.append(math.log(2*R*L*(2*n+1)/math.pi)+2*log_j_bound(n))
m=max(logs);tail_ratio=math.exp(logs[-1]-logs[-2]);scaled=sum(math.exp(v-m) for v in logs)+math.exp(logs[-1]-m)*tail_ratio/(1-tail_ratio);logtrace=m+math.log(scaled)
out={'schema':'marici.voevodsky.legendre-low-frequency-concentration-bound.v1','L':L,'frequency_band':[-R,R],'first_legendre_tail_degree':N,'log_trace_upper_including_geometric_tail':logtrace,'log10_trace_upper':logtrace/math.log(10),'last_term_ratio':tail_ratio,'tail_beyond_999_included_geometrically':True,'bound_used':'|j_n(z)| <= sqrt(pi) z^n exp(z^2/4)/(2^(n+1) Gamma(n+3/2))','passed':logtrace<-800 and tail_ratio<1e-3,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'legendre_low_frequency_concentration_bound.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']
