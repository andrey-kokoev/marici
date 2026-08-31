# G4 is equivalent to an acyclic mapping cone between the theta-section complex and the Green boundary pencil

> **Constructor-order correction.** The successor packet
> `the-theta-poisson-determinant-line-is-not-yet-a-theta-complex.md` shows that
> the present source constructs the theta--Poisson determinant line but not yet
> a completed complex \(T_\theta\). The mapping-cone theorem below is a final
> sufficient comparison criterion; it cannot be instantiated until that
> differential, its domains, and its determinant-line identification exist.

## Two completed objects

Let \(T_\theta(s)\) denote the completed three-stratum theta--Poisson complex
whose determinant-line section is trivialized as \(\xi(s)\).  Let
\(C_{\rm FP}(s)\) denote the closed maximal-isotropic boundary pencil whose
kernel states satisfy the Green flux identity.

Scalar equality of determinant sections does not compare their cohomology.
The missing datum must be a morphism before applying the determinant functor.

## Chain comparison

The required constructor is a holomorphic chain map

\[
F(s):T_\theta(s)\longrightarrow C_{\rm FP}(s)
\]

on the common reduced three-stratum carrier, preserving:

- primitive distributional ports;
- square Hilbert ports;
- connected determinant-class ports;
- reciprocal Fourier--Poisson sewing;
- endpoint traces and their contragredient responses;
- cutoff inclusions and grade labels.

Form its mapping cone

\[
\operatorname{Cone}F(s).
\]

## Acyclicity criterion

If there is a bounded holomorphic contraction \(h(s)\) satisfying

\[
d_{\rm cone}(s)h(s)+h(s)d_{\rm cone}(s)=I,
\]

then \(\operatorname{Cone}F(s)\) is acyclic.  Consequently \(F(s)\) is a
quasi-isomorphism and induces

\[
H^\bullet(T_\theta(s))
\cong
H^\bullet(C_{\rm FP}(s)).
\]

This gives the desired zero-to-kernel arrow without defining either complex
from the other's scalar determinant.

## Determinant-line consequence

The determinant functor applied to the exact triangle

\[
T_\theta
\xrightarrow{F}
C_{\rm FP}
\longrightarrow
\operatorname{Cone}F
\longrightarrow
T_\theta[1]
\]

supplies

\[
\operatorname{Det}(C_{\rm FP})
\cong
\operatorname{Det}(T_\theta)
\otimes
\operatorname{Det}(\operatorname{Cone}F).
\]

A chosen contraction canonically trivializes the acyclic cone determinant
line by a nowhere-zero section \(E(s)\).  In source trivializations,

\[
\det C_{\rm FP}(s)=E(s)\xi(s).
\]

Thus the comparison factor is a unit because it is the torsion of an acyclic
source cone, not because a scalar quotient was assumed nonzero.

## Algebraic multiplicity

For a holomorphic Fredholm complex, local algebraic multiplicity is the length
of the parameter-local cohomology module.  A holomorphic quasi-isomorphism
preserves that module.  Therefore

\[
\operatorname{ord}_{s_0}\det C_{\rm FP}
=
\operatorname{ord}_{s_0}\xi
\]

including generalized root chains, provided the contraction is holomorphic
through \(s_0\).

A pointwise vector-space isomorphism is insufficient; it can lose the local
nilpotent parameter action and hence algebraic multiplicity.

## Reciprocal compatibility

Let \(\mathscr R_\theta\) and \(\mathscr R_C\) be the reciprocal transports.
The comparison must satisfy

\[
F(1-s)\mathscr R_\theta
=
\mathscr R_C F(s)
\]

and the contraction must obey the induced cone relation.  This makes the
determinant torsion unit reciprocal and prevents an orientation reversal in
the chart overlap.

## Finite-cutoff construction test

At cutoff \(X\), an admissible candidate \(F_X\) must pass four tests:

1. its primitive, square, and connected components are the existing source
   incidence maps, not scalar fitted rows;
2. the mapping-cone contraction uses only typed bounded eliminations;
3. contraction bounds are uniform in \(X\) on compact parameter sets;
4. the determinant torsion agrees with the Euler-domain normalization.

Failure of the second test identifies the first boundary map that blocks
completion.  Failure of the third permits spectral pollution.

## Relation to existing results

The current packets provide the endpoints of this comparison:

- theta Mellin--Poisson trivialization constructs \(T_\theta\) and its Xi
  section;
- retained G1--G2 incidence and reciprocal maps provide candidate components
  of \(F\);
- the closed-loop Schur theorem and maximal-isotropic domain construct
  \(C_{\rm FP}\);
- G3 supplies coercive estimates that may bound a cone contraction off the
  critical seam.

They do not yet assemble a differential-commuting \(F\) or a contraction of
its mapping cone.

## G4 frontier

The remaining G4 constructor is now one exact object:

\[
(F,h),
\qquad
dF=Fd,
\qquad
d_{\rm cone}h+hd_{\rm cone}=I.
\]

Constructing it with uniform completed bounds proves determinant
factorization, zero-to-kernel equivalence, and multiplicity preservation in
one step.  Without it, the theta divisor and Green kernel remain adjacent but
unidentified.  No RH conclusion is authorized.
