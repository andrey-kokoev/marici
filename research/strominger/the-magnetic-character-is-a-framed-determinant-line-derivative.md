# The magnetic character is a framed determinant-line derivative

## Result

The normalized Pluecker character is not an invariant of an unframed
determinantal jet. It becomes invariant after retaining the source framing, or
equivalently after equipping the determinant line with the connection induced
by that framing.

Let

[
B:Flongrightarrow E,qquad
p(B)=Lambda^3BinLambda^3Eotimes(Lambda^3F)^ee.
]

At every strict magnetic contact tested previously, the source-derived response
(H) satisfies

[
d p_B(H)=chi p(B).
]

This derivative is radial. Its image in the tangent space of the projective
Pluecker variety is zero. Hence (chi) is not carried by the Grassmannian
point; it is carried by the chosen determinant-line scale.

## Gauge law

For a fixed change of presentation (B'=UBV),

[
p(B')=det(V)Lambda^3(U)p(B),
]

and the same fixed factor acts on (d p_B(H)). Therefore (chi) is invariant
under fixed row and column gauges.

For a moving presentation (U(arepsilon),V(arepsilon)), ordinary
differentiation also differentiates the gauge. In the domain-only scalar
example

[
V(arepsilon)=operatorname{diag}(1+alphaarepsilon,1,1),
]

the naive coefficient changes by (alpha). A moving row gauge can additionally
create transverse Pluecker coordinates. Thus neither the scalar coefficient nor
even radiality is invariant under naive differentiation in a moving frame.

Let (G=det(V)Lambda^3(U)) be the induced determinant-line presentation.
Subtracting the infinitesimal gauge term defines the covariant derivative

[

abla p'=d p'-dG,G^{-1}p'.
]

It obeys

[

abla p'=G
abla p.
]

Consequently the covariant coefficient in

[

abla_Hp=chi_{mathrm{src}}p
]

is invariant.

## Exact hostile fixture

The checker works over (mathbf F_3[arepsilon]/(arepsilon^2)). It verifies:

- a radial baseline derivative with (chi=2);
- a moving domain gauge that changes the naive character from (2) to (0);
- a moving row gauge that creates a transverse Pluecker coordinate;
- restoration of the full jet after subtracting the induced connection terms;
- invariance under a fixed unimodular row-and-column gauge;
- vanishing of the projective tangent.

All seven gates pass.

## Interpretation

The closest established object is not an ordinary jet of a determinantal
variety. It is a determinantal jet together with a trivialized determinant line,
or equivalently a connection on that line.

In the magnetic construction the candidate trivialization is supplied by the
source packet: the Laurent-monomial basis, the reflected observation basis, the
integral lattice, and the grade recurrence. Calling a presentation change
authorized must therefore include its induced connection cell. Transporting
only the matrices discards structure needed to define (chi).

The remaining theorem obligation is source-specific: prove that those four
pieces determine one connection independently of all authorized constructor
factorizations. Until that is proved, (chi) is invariant relative to the
declared source frame, not absolutely.

## Artifacts

- `research/strominger/checkers/framed_determinantal_jet_checks.py`
- `research/strominger/results/framed_determinantal_jet_checks.json`
