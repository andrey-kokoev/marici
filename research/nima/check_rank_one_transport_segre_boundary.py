#!/usr/bin/env python3
"""Segre P1xP1 boundary coordinates of rank-one NNMHV transports."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-projective-transport-correspondences.json').read_text());rows=[];mats=[]
for h in src['histories']:
 r=h['xi_transport']
 if r['rank']!=1:continue
 M=s.Matrix([[s.sympify(v) for v in row] for row in r['matrix']]);u=M.columnspace()[0];v=(u.T*u).inv()[0]*(u.T*M);ker=M.nullspace()[0];recon=s.simplify(u*v);mats.append(M);rows.append({'history_index':h['history_index'],'image_P1':[str(s.factor(x)) for x in u],'covector_P1':[str(s.factor(x)) for x in v],'kernel_P1':[str(s.factor(x)) for x in ker],'segre_reconstruction':recon==M,'incidence_v_dot_kernel':str(s.factor((v*ker)[0]))})
# Rank-one composition law MN=(v.s)u t^T, tested on all pairs; zero is allowed on incidence.
composition=[]
for i,M in enumerate(mats):
 for j,N in enumerate(mats):
  P=M*N;composition.append({'left':rows[i]['history_index'],'right':rows[j]['history_index'],'rank':P.rank(),'det_zero':s.factor(P.det())==0})
checks={'four_rank_one_histories':len(rows)==4,'all_factor_through_segre':all(r['segre_reconstruction'] for r in rows),'kernel_is_annihilated':all(r['incidence_v_dot_kernel']=='0' for r in rows),'rank_one_boundary_closed_under_nonzero_composition':all(c['rank'] in (0,1) and c['det_zero'] for c in composition)}
out={'schema':'marici.nima.rank-one-transport-segre-boundary.v1','ambient':'P(Mat_2)=P^3','boundary':'det=0 = Segre(P^1 x P^1)','coordinates':rows,'pairwise_compositions':composition,'checks':checks,'passed':all(checks.values()),'meaning':'A singular transport is an ordered pair (image line, kernel line). Rank-two boundary updates act separately on these two polarities; rank-one composition is controlled by their incidence pairing.'};p=ROOT/'research/nima/results/rank-one-transport-segre-boundary.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
