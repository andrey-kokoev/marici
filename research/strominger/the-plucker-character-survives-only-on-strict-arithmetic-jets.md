# The Plücker character survives only on strict arithmetic jets

Owner: `marici.Strominger`

## Question

Does the source shift act on the leading magnetic Plücker section through a
residue-field scalar, and does that scalar predict every Fitting-depth gain?

## Bounded test

The exact scan covers grades

\[
0\le n\le250
\]

and shifts

\[
3,9,27,81,243,729.
\]

For each pair \((n,n+q)\), let \(s\) be the common entry depth, \(u\) the
depth of the matrix difference, and \(ell\) the maximal-minor depth. A
first-order contact is admitted only when

\[
u>s,
\qquad
\ell=u+2s.
\]

The first inequality is essential: it makes every determinant term containing
two or three direction columns strictly deeper than the linear exterior
variation.

## Result

There are 83 depth-matched contacts in the bounded scan. Every one has a
scalar exterior response

\[
J_{n,q}=\chi(n,q)\sigma_n
\]

over the residue field. No mixed Plücker response occurs.

On every strict first-order contact,

\[
\chi(n,q)=-1
\]

holds exactly when the maximal-minor depth increases. Thus the character is a
complete bounded classifier of strict arithmetic Fitting cancellation.

The cancellation grades are:

\[
\begin{array}{c|l}
q&n\\
\hline
9&8,35,62,89,116,143,170,197,224\\
27&44,125,206\\
81&71\\
243&\text{none in the tested interval}\\
729&152
\end{array}
\]

The first two nonempty rows already show congruence classes:

\[
n\equiv8\pmod{27},
\qquad
n\equiv44\pmod{81}.
\]

The single tested classes for shifts 81 and 729 are not promoted to unbounded
congruence laws.

## The hostile exception is informative

For shift 3, all 28 depth-matched gains occur with

\[
u=s=2.
\]

They are not strict jets. Quadratic and cubic determinant terms occur at the
same depth as the nominal derivative. Indeed, their displayed linear scalar is
\(\chi=1\), not \(-1\), while the full finite substitution still gains
depth.

Therefore the naïve conjecture

> every depth gain is classified by the first exterior derivative

is false.

The corrected conjecture is:

> every strict arithmetic Fitting contact is classified by the scalar action
> of the first exterior derivative; equal-depth substitutions require the
> complete determinant polynomial.

This is a structural separation between infinitesimal arithmetic contact and
finite nonlinear substitution.

## What remains unexplained

The scan discovers the scalar character but does not derive it from the source
constructor. The next explanatory target is a recurrence or finite residue
automaton computing \(\chi(n,3^r)\) without forming the full matrix.

The missing theorem must also explain why the Plücker response is scalar at all
83 contacts. That coherence is stronger than merely predicting the
cancellation grades.

## Claim boundary

This is bounded exact evidence, not an unbounded character theorem. It does
not construct a connecting Ext class or an exact sequence. Cross-sector
comparisons remain analogies without a source-derived functor.

Benincasa's former gauge Fitting conic is only a historical algebraic fixture:
that branch was retired after noncanonical descent. Its live doubled-pole
residual has no typed adapter to the magnetic contact.

## Disposition

The broad character conjecture was falsified and repaired without hiding its
counterexamples. The strict-jet classifier passed five of five gates. Its next
falsifier is to find a strict contact with mixed Plücker response or with
\(\chi=-1\) but no depth gain.

## Verification

Run:

```powershell
python research/strominger/checkers/plucker_character_scan.py
```

The summary is stored in
`research/strominger/results/plucker_character_scan.json`.
