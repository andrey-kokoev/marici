# The odd theta forcing is an ordered symplectic port

## Result

The remaining doubled-tail forcing has an exact operator type that is lost in the scalar autocorrelation presentation. It is the pairing of the two reciprocal source sheets through the antisymmetric order kernel.

Extend the positive half-line source \(f\) by zero to the real line and define

\[
a_z(q)=f(q)e^{-zq},
\qquad
b_z(v)=f(v)e^{zv}.
\]

Let \(S\) be the order operator

\[
(Sb)(q)
=
\int_{\mathbb R}\operatorname{sgn}(v-q)b(v)\,dv.
\]

Then the odd forcing function is exactly

\[
C_f(z)
=
\int_{\mathbb R^2}
\operatorname{sgn}(v-q)
f(q)f(v)e^{z(v-q)}
\,dq\,dv
=
\langle a_z,Sb_z\rangle.
\]

Indeed, splitting the plane into \(v>q\) and \(q>v\), and exchanging the variables in the second triangle, gives

\[
C_f(z)
=
2\int_{v>q}
f(q)f(v)\sinh\bigl(z(v-q)\bigr)
\,dq\,dv.
\]

This is the previous positive-autocorrelation formula after setting \(d=v-q\).

## Metric and ordered ports

The unordered two-copy pairing is

\[
E_f(z)
=
\int_{\mathbb R^2}
f(q)f(v)e^{z(v-q)}
\,dq\,dv
=
F(-z)F(z),
\]

where

\[
F(z)=\int_0^\infty f(v)e^{zv}\,dv.
\]

Thus the same reciprocal pair source has two inequivalent readouts:

\[
E_f(z)=\langle a_z,b_z\rangle_{\mathrm{all\ pairs}},
\]

and

\[
C_f(z)=\langle a_z,Sb_z\rangle_{\mathrm{ordered\ pairs}}.
\]

The first forgets order. The second records the orientation of each pair relative to the diagonal \(q=v\).

The kernel of \(S\) is antisymmetric:

\[
\operatorname{sgn}(v-q)
=
-\operatorname{sgn}(q-v).
\]

Consequently \(S^*=-S\) on a suitable source core. It is a symplectic or commutator-type port, not a positive energy observable.

## Fourier type

Distributionally, the sign kernel has Fourier multiplier proportional to

\[
\frac{1}{i\xi}.
\]

Equivalently, \(S\) is an inverse-derivative boundary operator, up to the constant-mode convention. This explains why the forcing persists after the positive bulk has closed:

- the Gram bulk is metric and local in the retained features;
- the forcing is an oriented, nonlocal boundary pairing;
- scalar completion can preserve the metric readout while erasing the ordered port.

The primitive and square boundary currents are therefore plausible incidence data for this port, but they do not acquire that role merely because their scalar cumulants match.

## Why the scalar zero does not control it

The completed scalar section is

\[
X(z)=F(z)+F(-z).
\]

At a zero,

\[
F(-z)=-F(z).
\]

This constrains two one-body scalar integrals. It does not determine the two-body ordered pairing

\[
\langle a_z,Sb_z\rangle.
\]

The earlier two-shell witness is now structurally transparent: it preserves the antidiagonal scalar condition while retaining a nonzero ordered-pair moment.

Therefore no algebraic manipulation of \(X(z)=0\), \(F(z)F(-z)\), or the positive autocorrelation alone can reconstruct the missing orientation.

## Required source bridge

Any explanatory theorem must now provide an authorized map from the labelled reciprocal pair source to the ordered boundary port.

It must specify:

1. the occurrence order or valuation orientation before scalar trace;
2. the domain and constant-mode convention of \(S\);
3. its transformation under Fourier–Poisson sewing;
4. its incidence with the primitive, square, seam, and archimedean boundary grades;
5. why the zero-state antidiagonal condition is incompatible with the forbidden sign of the ordered pairing.

The third item is the sharpest next calculation. Fourier conjugation turns the order kernel into an inverse-frequency singularity, so the \(k=1\), \(k=2\), and archimedean currents should appear as typed renormalization data if this route is genuine.

## Operational-order consequence

Benincasa's finite Hadamard result has the same variance pattern. The selected-sheet pairing retains the odd occurrence direction; the deck trace kills it. The analytic statement above shows what that odd direction must represent if the two constructions are eventually joined: an ordered-pair boundary port.

No join is currently authorized. The geometric occurrence labels have not yet been derived from the marked denominator and residue charts.

## Falsifier

Given any proposed Fourier–Tate lift \(\mathcal P\), compute on a finite labelled source core

\[
R_{\mathcal P}(z)
=
\langle a_z,Sb_z\rangle
-
J_{\mathcal P}(z),
\]

where \(J_{\mathcal P}\) is the boundary current produced by the proposed lift.

A nonzero residual on one two-shell or three-shell source disproves the claimed incidence. A construction that works for all unlabelled positive sources is also insufficient: it does not distinguish theta arithmetic from the hostile class.

## Disposition

The universal sign route is closed, but the forcing is no longer an opaque oscillatory remainder. It is the source pair's antisymmetric ordered port. The RH-bearing gate is whether Fourier–Tate completion carries this port, with its order and boundary anomaly intact, into the completed scalar zero-state system.
