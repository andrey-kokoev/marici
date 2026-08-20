# Cut-Equation Descent and the All-Topology Surface Counit

## Record

Date: 2026-08-13

Status: the universal modular-envelope counit of entry 47 descends uniquely to
canonical surface functions.  The resulting operation is cyclic,
mapping-class invariant, defined at arbitrary topology, and strictly
Cut-monoidal for both separating and nonseparating Cuts.

The missing argument was not another explicit \(3S\) or \(6AS\) calculation.
It is the conservativity of the Cut Equation together with the ultraviolet
boundary condition.  Over characteristic zero, a polynomial whose derivative
vanishes in every inverse-propagator variable is constant; the cubic-scalar
boundary condition kills that constant.

Reproducible algebra audit:

```text
research/nima/check_cut_equation_descent.rs
```

This completes the requested lift as an operation on resolved/canonical
surface functions.  It does not produce one globally written differential
operator in the already-specialized \(X_C\) variables.  Such a point-set
formula is a stricter presentation problem, not an existence condition for the
surface operation.

## Surface-function coefficient ring

For every marked surface \(S\), let \(\mathcal C(S)\) be the set of
mapping-class orbits of Cut curves used by its canonical surface function.
No global finiteness assumption is needed: every polynomial and every
coefficient test below involves only finitely many curve variables.
Write

\[
x_C=X_C^{-1}
\]

for an open-curve inverse propagator.  When closed propagator curves occur, use
the analogous variables \(z_\Delta\).  In this entry all of them are denoted
collectively by

\[
\mathbf x=(x_C,z_\Delta).
\]

Numerator data are retained in an independent \(\mathbb Q\)-algebra \(R\)
(more generally, a \(\mathbb Z\)-torsion-free coefficient module suffices).
This separation is essential: the Cut derivative acts on inverse
propagators while holding numerator variables fixed.  Ordinary momentum
kinematics may be imposed only after solving the surface problem.

Thus the canonical surface-function target is

\[
\mathcal P_S=R[\mathbf x].
\]

The Cut Equation is

\[
\boxed{
\partial_{x_C}G_S=G_{S\setminus C}
}
\]

for open curves, with the identical equation

\[
\boxed{
\partial_{z_\Delta}G_S=G_{S\setminus\Delta}
}
\]

for closed curves.  Symmetry factors are built into the canonical surface
function, so these equations remain exact when a triangulation contains more
than one representative of a mapping-class orbit.

For a cubic scalar theory the ultraviolet boundary data are:

- the elementary three-point interaction is one;
- all higher tree contact interactions vanish;
- on every positive-topology surface,
  \[
  \left.G_S\right|_{\mathbf x=0}=0.
  \]

The all-arity genus-zero boundary sector is already covered by the tree counit
of entries 42--45.

## Conservativity lemma

Let

\[
H\in R[x_1,\ldots,x_N]
\]

with \(R\) a \(\mathbb Q\)-algebra.  Then

\[
\boxed{
\left(
\partial_{x_i}H=0\ \text{for every }i,
\quad
H(0)=0
\right)
\Longrightarrow
H=0.
}
\]

### Proof

Write

\[
H=\sum_{\alpha\in\mathbb N^N}h_\alpha\mathbf x^\alpha.
\]

For every nonzero exponent vector \(\alpha\), choose an index \(i\) with
\(\alpha_i>0\).  The coefficient of
\(\mathbf x^{\alpha-e_i}\) in \(\partial_{x_i}H\) is

\[
\alpha_i h_\alpha.
\]

Since \(\alpha_i\) is invertible in \(R\), this gives \(h_\alpha=0\).  Hence
\(H=h_0\) is constant, and
\(H(0)=0\) gives \(h_0=0\).

Equivalently, the combined map

\[
\boxed{
J_S:
\mathcal P_S
\longrightarrow
R\oplus\bigoplus_{C\in\mathcal C(S)}\mathcal P_{S\setminus C},
\qquad
H\longmapsto
\left(H(0),(\partial_{x_C}H)_C\right)
}
\]

is injective.  This is the precise sense in which Cuts plus the ultraviolet
boundary are conservative, even though Cuts alone are not.

## Descent theorem

Recall the universal map of entry 47,

\[
u^{\rm univ}_S:
\mathfrak S^{\rm YM}_{\rm univ}(S)
\longrightarrow
\mathfrak S^{\phi}_{\rm univ}(S),
\]

and the presentation evaluations

\[
q_{{\rm YM},S}:
\mathfrak S^{\rm YM}_{\rm univ}(S)
\twoheadrightarrow
\mathfrak S^{\rm YM}_{X}(S),
\]

\[
q_{\phi,S}:
\mathfrak S^{\phi}_{\rm univ}(S)
\twoheadrightarrow
\mathcal P_S.
\]

### Theorem

For every marked orientable surface \(S\),

\[
\boxed{
u^{\rm univ}_S(\ker q_{{\rm YM},S})
\subseteq
\ker q_{\phi,S}.
}
\]

Consequently there is a unique induced map

\[
\boxed{
u^X_S:
\mathfrak S^{\rm YM}_{X}(S)
\longrightarrow
\mathcal P_S
}
\]

such that

\[
q_{\phi,S}u^{\rm univ}_S
=
u^X_Sq_{{\rm YM},S}.
\]

### Proof

Proceed by induction on surface complexity, equivalently the number of curves
in a maximal decomposition, and extend the induction monoidally to disconnected
cut surfaces.  Genus zero is the established all-arity tree counit, including
its contact boundary data.

Take

\[
r\in\ker q_{{\rm YM},S}
\]

and define the possible scalar discrepancy

\[
H_r=q_{\phi,S}u^{\rm univ}_S(r)\in\mathcal P_S.
\]

For every Cut curve \(C\), physical presentation evaluation is Cut natural, so

\[
q_{{\rm YM},S\setminus C}(\Delta_Cr)
=
\partial_{x_C}q_{{\rm YM},S}(r)
=0.
\]

Thus

\[
\Delta_Cr
\in
\ker q_{{\rm YM},S\setminus C}.
\]

Strict Cut monoidality of the universal counit gives

\[
\begin{aligned}
\partial_{x_C}H_r
&=
q_{\phi,S\setminus C}
\Delta_Cu^{\rm univ}_S(r)\\
&=
q_{\phi,S\setminus C}
u^{\rm univ}_{S\setminus C}(\Delta_Cr)\\
&=0
\end{aligned}
\]

by the induction hypothesis.  The same argument applies to a separating Cut,
with the target interpreted as the tensor product of the two lower surface
functions, and to a closed-curve variable \(z_\Delta\).

Therefore every partial derivative of \(H_r\) vanishes.  On a non-elementary
surface, every resolved cubic-scalar presentation contains at least one
propagator variable, so

\[
H_r(0)=0.
\]

For the elementary/tree boundary strata the same statement is precisely the
already-proved tree descent.  The conservativity lemma now implies

\[
H_r=0.
\]

This proves the kernel inclusion and hence well-defined descent.

## Image of the physical YM surface object

Let

\[
G_S^{{\rm YM,res}}
\]

be the resolved scalar-scaffolded YM surface function: polarization
contraction covers and numerator variables are retained until the counit is
applied.  Then

\[
\boxed{
u^X_S\left(G_S^{{\rm YM,res}}\right)
=
G_S^{\operatorname{Tr}\phi^3}
}
\]

for every \(S\).

Indeed, both sides have the same Cut in every curve variable by induction and
the same cubic-scalar ultraviolet boundary.  Injectivity of \(J_S\) makes them
equal.  This upgrades the arbitrary-topology maximal-Cut equality of entry 47
to the complete canonical surface function.

The order of operations remains essential:

\[
\boxed{
\text{resolve contraction covers}
\longrightarrow
D\mapsto1
\longrightarrow
\mathbb L\operatorname{Mod}
\longrightarrow
q_\phi.
}
\]

Substituting \(D=1\) or imposing ordinary momentum homology before resolving
the coefficient system can erase the data needed for the descent proof.

## Cyclicity, mapping classes, and Hatcher cells

The induced operation inherits cyclic equivariance from the tree counit and
mapping-class covariance from the modular envelope.  Since it is obtained by
descent, all changes of surface presentation act trivially on its value.

In particular, for the Hatcher cells,

\[
\boxed{
\Omega_{3S}=0,
\qquad
\Omega_{6AS}=0
}
\]

in the canonical surface-function quotient.  The vanishing is not inferred
from maximal residues alone.  Their possible discrepancies have zero Cuts and
zero ultraviolet boundary, so the conservativity lemma kills them.

The same proof handles the commutation cells \(C\), while \(3A\) and \(5A\)
are already present in the genus-zero cyclic resolution.

## Uniqueness

Suppose \(v_S\) is another family of cyclic surface operations which:

1. agrees with \(u_0\) on the tree boundary data;
2. sends each resolved state circuit to the scalar state value;
3. commutes with every separating and nonseparating Cut;
4. has the cubic-scalar ultraviolet boundary condition.

Then \(v_S-u^X_S\) has zero Cut in every variable and zero boundary.  The same
induction proves

\[
v_S=u^X_S.
\]

Thus the lift is canonical at the level of surface functions even though a
single preferred differential-operator representative need not exist.

## Scope and remaining presentation problem

Constructed and proved:

- a resolved state augmentation \(D\mapsto1\);
- a derived modular-envelope lift on all stable ribbon graphs;
- strict separating and nonseparating Cut monoidality;
- cyclic and mapping-class covariance;
- descent to the canonical surface-function quotient;
- equality with the \(\operatorname{Tr}\phi^3\) surface function;
- uniqueness from Cuts plus boundary data.

Not constructed:

- one closed-form all-loop differential operator acting directly on an
  already-summed, already-specialized YM rational function;
- a proof that such a strict point-set representative exists without retaining
  the resolved contraction-cover coefficient system;
- compatibility with premature specializations that identify numerator and
  propagator variables before applying the counit.

These do not qualify the existence or uniqueness of the resolved surface
operation proved here.  They concern strictification to a smaller presentation.

## Executable evidence

The Rust certificate reconstructs dense exact polynomials from the tuple

\[
\left(H(0),(\partial_{x_i}H)_i\right)
\]

in 30 polynomial spaces, covering one through five variables and total degree
zero through five.  It reconstructs 917 monomial coefficients and separately
checks the zero-Cut kernel and arbitrary constant boundary values.

The bounded computation audits the implementation of the reconstruction map.
The monomial proof above is unbounded.

## Primary sources

- Arkani-Hamed, Frost, and Salvatori, *The Cut Equation*, especially the
  polynomial formulation, equations (2), (21), the ultraviolet conditions
  (38)--(39), and the closed-curve equation (65):
  <https://arxiv.org/abs/2412.21027>.
- Getzler and Kapranov, *Modular operads*:
  <https://arxiv.org/abs/dg-ga/9408003>.
- Costello, *The A-infinity operad and the moduli space of curves*:
  <https://arxiv.org/abs/math/0402015>.
- Carrôlo and Figueiredo, *How gluon leading singularities discover curves on
  surfaces*: <https://arxiv.org/abs/2512.17019>.
