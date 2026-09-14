#!/usr/bin/env python3
"""Exact reversal and orthogonal-normal audit on the C2 2-Segal baseline."""
import json
from pathlib import Path
import check_two_directional_path_spaces as base

def rev(x): return tuple(reversed(x))  # inversion is trivial in C2
def sx(x,i): return x[:i]+(0,)+x[i:]

def matvec(A,v): return tuple(sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A)))
def dot(u,v): return sum(a*b for a,b in zip(u,v))

def main():
    face_checks=0;degeneracy_checks=0
    for n in range(1,7):
      for x in base.X(n):
       for i in range(n+1):
        assert rev(base.dx(x,i)) == base.dx(rev(x),n-i)
        face_checks+=1
       for i in range(n+1):
        assert rev(sx(x,i)) == sx(rev(x),n-i)
        degeneracy_checks+=1
    # On decalage path spaces, reversal exchanges initial and final faces.
    exchange_checks=0
    for n in range(1,6):
      for x in base.Y(n):
       for i in range(n+1):
        assert rev(base.dy(x,i)) == base.dz(rev(x),n-i)
        exchange_checks+=1
    nu_left=(1,0);nu_right=(0,1);J=((0,-1),(-1,0))
    assert dot(nu_left,nu_right)==0
    assert matvec(J,nu_left)==(0,-1) and matvec(J,nu_right)==(-1,0)
    assert matvec(J,matvec(J,nu_left))==nu_left and matvec(J,matvec(J,nu_right))==nu_right
    assert dot(matvec(J,nu_left),matvec(J,nu_right))==0
    result={'schema':'marici.voevodsky.reversal-orthogonal-two-segal.v1','underlying_two_segal':'C2 nerve','reversal':'reverse simplex order; C2 inversion is trivial','simplicial_face_reversal_checks':face_checks,'simplicial_degeneracy_reversal_checks':degeneracy_checks,'initial_final_path_exchange_checks':exchange_checks,'normal_pairing_matrix':[[1,0],[0,1]],'normal_directions_orthogonal':True,'reversal_normal_action':[[0,-1],[-1,0]],'reversal_is_involutive':True,'reversal_changes_channel_sign':True,'claim_boundary':'Constructed algebraic reversal and orthogonal normal representation; no metric embedding as literal planes and no source-derived identification.'}
    out=Path(__file__).parents[1]/'results'/'reversal_orthogonal_two_segal.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
