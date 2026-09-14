# v203: selected three-line detector packet

The three constructed classes occupy distinct typed channels:

- the graded lift `s` has `rho(s)=(theta,0,0)` and supplies the generic-Q primary line;
- the supported reflection class `W` has `rho(W)=(0,dV(omega_V)_plus,dV(omega_V)_minus)` and supplies the paired-endpoint reciprocal line;
- the road class maps to `v=a^3+a^3b` with `rho0(v)=1` and supplies the relation line.

Their selected detector object is therefore the external direct sum

`S_sel = Z<s> direct-sum Z<W> direct-sum Z<v>`.

The primary, reciprocal, and relation functionals are its three coordinate projections. Joint detection and linear independence follow from the direct-sum typing, not from equal scalar values. This constructs the three functionals required by module 209 on the selected packet.

It does not identify `S_sel` with the actual supported Gysin target. The remaining detector comparison is one map sending the selected physical Gysin class to `a*s+b*W+c*v`; without that map the symbols `(a,b,c)` remain packet coordinates rather than physical detector values.
