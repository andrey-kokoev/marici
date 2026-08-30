# The magnetic response is controlled by a source-fixed isotropic flag

## Exact source identities

Let

[
iota=
egin{pmatrix}1\1\1\1end{pmatrix},
qquad
omega=
egin{pmatrix}1&-1&1&-1end{pmatrix}.
]

Every atomic labelled constructor and its inverse,

[
C^{pm1}, X^{pm1}, Z^{pm1}, Y^{pm1},
]

satisfies

[
Miota=iota,
qquad
omega M=omega.
]

These identities were checked exactly for all eight atomic matrices. They are
multiplicative, so they hold for every source word and therefore for every
nested commutator response (R_n).

Put

[
Delta_n=R_n-I.
]

Then, for every integral grade (n),

[
Delta_niota=0,
qquad
omegaDelta_n=0.
]

Thus the response has a source-fixed kernel line and source-fixed image
hyperplane:

[
G=mathbf ZiotasubseteqkerDelta_n,
qquad
operatorname{im}Delta_nsubseteq H=keromega.
]

Because

[
omegaiota=0,
]

the line lies inside the hyperplane:

[
Gsubset Hsubset V.
]

This flag, rather than a chosen matrix chart, is the invariant geometric
object.

## Natural automorphism

The non-scalar centralizer generator is

[
N=iotaomega.
]

Since (omegaiota=0),

[
N^2=0.
]

Moreover,

[
NDelta_n=iotaomegaDelta_n=0,
qquad
Delta_nN=Delta_niotaomega=0.
]

Consequently every integral shear (I+aN) fixes the response, and the selected
full readout is already horizontal. This proves the bounded gauge-invariance
observations for every grade and every integral shear.

The exact integral stabilizer inside the two-dimensional rational centralizer
is

[
{epsilon I+aN:epsilonin{1,-1}, ainmathbf Z}.
]

Indeed, the integral centralizer lattice is
(mathbf ZIoplusmathbf ZN), while

[
det(bI+aN)=b^4.
]

Unimodularity forces (b=pm1).

## Rank consequences

The full response has rank at most three because it kills (G). The relational
projection

[
P(v_1,v_2,v_3,v_4)
=
(v_1-v_4,v_2-v_4,v_3-v_4)
]

also has kernel (G). Since the response image lies in (H) and (Gsubset H),
projecting the codomain removes a direction already contained in the image
hyperplane. This forces the persistent relational rank defect.

The full and relational Smith data therefore measure different parts of one
source-fixed flag:

- the full readout measures the map into (H);
- the relational readout measures its further image modulo (G);
- their valuation mismatch measures the integral extension between these
  layers.

This supplies an unbounded explanation for the common gauge line, the
rank-three ceiling, the relational rank defect, and the square-zero stabilizer.
