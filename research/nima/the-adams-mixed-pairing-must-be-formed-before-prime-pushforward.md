# The Adams mixed pairing must be formed before prime pushforward

## Source extraction

The adjacent valuation cell is

\[
\alpha_{p,1}(q)=W_{2\log p}(q)-W_{\log p}(q).
\]

The source records now determine where its missing pairing can live. It cannot first be pushed to the ordinary scale line and then paired as one Hilbert vector.

Prime-weighted pushforward reconstructs two inequivalent boundary grades:

\[
\sum_p p^{-1/2}\alpha_{p,1}(q)
\asymp-\frac{e^{q/2}}q,
\]

while

\[
\sum_p p^{-1}\alpha_{p,1}(q)\longrightarrow-\log 2.
\]

Thus primitive and square weights produce, respectively, an exponentially growing wall and a constant plateau. A post-pushforward scalar pairing would conflate different current spaces.

## Correct carrier

The cell has two comoving charts,

\[
u_-=q-\log p,
\qquad
u_+=q-2\log p,
\]

with limiting front profiles

\[
h_-(u)=H(u)-1,
\qquad
h_+(u)=-H(u).
\]

Their overlap satisfies

\[
h_-(u)+h_+(u)=-1.
\]

Therefore the first Adams edge must be constructed on the two-chart scale-observation correspondence before integration over the prime scale. Its coefficient object retains:

- the inner front;
- the outer front;
- the constant overlap wall;
- the prime-scale measure;
- the valuation orientation.

Only after these data are paired may one push forward to the analytic scale coordinate.

## Why the canonical transpose is insufficient

The source forcing does supply a canonical rigged transpose

\[
B_f^\times(\lambda)=\lambda(f).
\]

Applied after aggregation, however, the Euler-to-Green map factors as

\[
\nu\longmapsto \nu(f)G_s
\]

and has rank at most one. It cannot distinguish a primitive/square packet in the evaluation kernel.

Consequently the desired mixed form cannot be defined merely by evaluating both weighted cells on the same source test vector. Such a construction has the form

\[
b_{\mathrm{scalar}}(x,y)
=
\overline{\mu_1(x)(f)}\,\mu_2(y)(f),
\]

so it is rank one and discards the ordered two-front incidence. It may be a scalar shadow of the eventual pairing, but it cannot authorize the Adams type edge.

## Relative pairing signature

Let \(\mathscr C_p\) denote the two-chart cell and let \(J_1,J_2\) be primitive and square boundary currents on its two faces. The missing source operation must have the signature

\[
\mathcal G_{\mathrm{rel}}
:
J_1^\vee\times\mathscr C_p\times J_2
\longrightarrow\mathbb C,
\]

and define

\[
b_{\alpha,p}(x,y)
=
\mathcal G_{\mathrm{rel}}
\bigl(J_1x,\mathscr C_p,J_2y\bigr).
\]

The pairing must be relative: the bulk contribution and constant-wall contribution are retained separately. Scalar finite-part extraction cannot define it because the canonical heat finite part is not positivity preserving.

## Four exact identities

Before any norm estimate, the source pairing must prove four algebraic identities.

### Front balance

The oriented boundary of the interval cell is the difference of its two fronts. With source-fixed sign convention,

\[
\partial\mathscr C_p=F_{\mathrm{out}}-F_{\mathrm{in}}.
\]

This determines whether the induced relation points primitive-to-square or through its mate.

### Overlap conservation

The constant overlap is not an extra free channel. The two chart restrictions must reproduce

\[
h_-+h_+=-1.
\]

A pairing that counts the plateau twice or deletes it cannot satisfy the graph boundary identity.

### Rigged transpose covariance

For every admissible source test packet, the face pairings must agree with the canonical test-dual transpose before choosing a Hilbert metric. This prevents metric-dependent fitted adjoints.

### Reciprocal covariance

Reflection exchanges entrance and exit, while Fourier transport exchanges the constant overlap with delta incidence. The mixed pairing must intertwine these operations before scalar readout.

## Factorization after the relative pairing

Only after \(\mathcal G_{\mathrm{rel}}\) is defined do the previous defect-space tests become meaningful:

\[
|b_{\alpha,p}(x,y)|^2\le c_1[x]c_2[y],
\]

together with annihilation of both radicals. Then Riesz factorization yields a contraction between gauge-reduced defect spaces.

This orders the construction correctly:

\[
\text{two-chart relative cell}
\longrightarrow
\text{relative Green pairing}
\longrightarrow
\text{mixed defect form}
\longrightarrow
\text{contractive factor}
\longrightarrow
\text{closable graph relation}.
\]

## Minimal falsifiers

1. **Pushforward first.** The primitive traveling wall and square plateau are collapsed before pairing.
2. **One common test vector.** The proposed edge factors through the rank-one scalar evaluator.
3. **Plateau mishandling.** The constant overlap is omitted or counted twice.
4. **Metric invention.** The pairing changes when only the intermediate Hilbert realization changes.
5. **Wrong front sign.** The scalar cross term is correct but the oriented graph boundary is reversed.

## Immediate finite packet

For one prime \(p\), the next executable object is not yet a matrix between primitive and square fibers. It is a two-chart relative Gram packet with rows and columns indexed by

\[
(F_{\mathrm{in}},F_{\mathrm{out}},W_{\mathrm{const}}).
\]

The source must supply its relative Green matrix \(G_{\mathscr C_p}\). One then contracts it with the primitive and square face-incidence vectors to obtain

\[
K_{\alpha,p}
=
J_1^*G_{\mathscr C_p}J_2.
\]

The first numerical audit checks the overlap relation, orientation, radical inclusions, and normalized contraction norm.

## Current frontier

The carrier and typing of the missing pairing are now fixed: it is a relative Green pairing on the two-chart comoving correspondence before prime pushforward. The remaining undefined datum is the relative Green matrix of one adjacent cell.

That matrix, rather than another abstract coherence condition, is the next source extraction target.
