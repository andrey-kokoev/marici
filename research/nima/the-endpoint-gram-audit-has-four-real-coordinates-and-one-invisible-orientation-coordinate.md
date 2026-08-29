# The endpoint Gram audit has four real coordinates and one invisible orientation coordinate

## General polarized form

Write

[
u=[W_L],
qquad
v=[W_{2L}],
qquad
G_p=
egin{pmatrix}
a&z\
overline z&b
end{pmatrix},
]

where (a,binmathbb R) and (z=c+ih).

A Hermitian positive-semidefinite cell form requires

[
age0,
qquad
bge0,
qquad
abge c^2+h^2.
]

The entire two-endpoint polarization therefore has four real coordinates:

[
a,quad b,quad c=operatorname{Re}z,quad
h=operatorname{Im}z.
]

## Oriented difference energy

For

[
d=(-1,1),
]

the boundary energy is

[
d^*G_pd
=
a+b-2c.
]

Thus endpoint norms (a,b) and the oriented difference energy determine only
(c):

[
c=rac12left(a+b-d^*G_pdight).
]

They do not determine (h). The imaginary polarization is invisible to every
quadratic test on the real vector (d).

## Reciprocal orientation port

The missing coordinate is the antisymmetric current

[
rac{g(u,v)-g(v,u)}{2i}
=
h.
]

Endpoint reversal exchanges (u) and (v), hence

[
hlongmapsto-h.
]

This is the finite reciprocal seam character. A scalar difference-energy audit
can pass while the seam orientation is reversed or erased.

Therefore the minimal complete observer of the two-endpoint Hermitian form is

[
(a,b,E_d,h),
qquad
E_d=d^*G_pd.
]

From it one reconstructs (G_p) exactly.

## Radical tests

For a positive-semidefinite Hermitian form,

[
dinker G_p
]

if and only if

[
E_d=0.
]

Hence nonvanishing of the oriented direction is exactly

[
E_d>0.
]

The wall/common vector

[
s=(1,1)
]

has energy

[
E_s=s^*G_ps=a+b+2c.
]

Keeping the wall separately typed does not require (s) to be orthogonal to
(d). Their mixed polarization is

[
s^*G_pd
=
(b-a)+2ih.
]

Thus a demand that common and difference modes be orthogonal would force both
(a=b) and (h=0), accidentally deleting the reciprocal odd coordinate.
Wall separation should be a typed direct-sum statement, not an unjustified
orthogonality assumption.

## Source coefficients

The arithmetic endpoint coefficients form an external vector

[
w_p=
egin{pmatrix}
p^{-1/2-sigma-it}\
rac12p^{-1-2it}
end{pmatrix}.
]

The weighted scalar energy is (w_p^*G_pw_p), but (G_p) must be constructed
before inserting (w_p). Absorbing these coefficients into the Gram entries
prevents comparison across cutoffs and confuses source arithmetic with cell
geometry.

## Quadratic representation packet

Let

[
pi(u)=M_{W_L},
qquad
pi(v)=M_{W_{2L}}.
]

The quadratic lift sends matrix units to

[
Gamma_pi(|e_ianglelangle e_j|)
=
pi(e_i)^*pi(e_j).
]

The required representation theorem must identify the analytic polarized block

[
egin{pmatrix}
M_{W_L}^*M_{W_L}&M_{W_L}^*M_{W_{2L}}\
M_{W_{2L}}^*M_{W_L}&M_{W_{2L}}^*M_{W_{2L}}
end{pmatrix}
]

with the represented coefficient polarization on a common core, including any
relative derivative or boundary corrections prescribed by the Green identity.

Because the raw windows are real multiplication operators, this naive analytic
block has (h=0). Therefore any nonzero reciprocal odd polarization must come
from an additional source-authorized oriented Green/seam cell, not from plain
multiplication products alone.

## Decisive contraction

The finite source problem now splits cleanly:

1. derive (a,b,c) from the symmetric Green energy;
2. derive (h) from the oriented odd seam current;
3. verify (abge c^2+h^2) or use the correct indefinite/sectorial geometry;
4. prove the quadratic representation theorem.

The smallest failure is now one missing real number: the source-derived
imaginary polarization (h). Without it, the symmetric energy may be complete
as a norm but incomplete as a reciprocal oriented constructor.
