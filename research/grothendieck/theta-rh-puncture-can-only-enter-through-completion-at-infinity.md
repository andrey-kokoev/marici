# An RH puncture can only enter through completion at infinity

## Bounded correction

Packet 139 retyped a zero as cohomology of a source-derived complex and
proposed contractions on the two open half-planes. Nima identified the next
limit trap: finite-cutoff acyclicity does not imply acyclicity after analytic
or restricted-product completion when the contractions escape every bounded
class.

The scalar hostile model is

\[
 \mathbb C\xrightarrow{\varepsilon_X}\mathbb C,
 \qquad \varepsilon_X\to0.
\]

Every finite map is invertible, with contraction

\[
 h_X=\varepsilon_X^{-1},
\]

but the contraction diverges and the limiting differential is zero.

## Geometric interpretation

At every finite cutoff, all Clifford/Koszul states may be paired. Completion
can nevertheless move one partner to infinite norm, leaving an unpaired state
in the completed complex.  Thus an off-seam puncture need not originate at a
finite prime. It can enter through the boundary at infinity of the Euler
system.

The sharpened conjecture is therefore

\[
 \boxed{
 \text{no source state becomes unpaired under restricted-product completion
 inside either open reciprocal sector}.}
\]

The critical seam remains the permitted locus where the two sector
contractions meet and may change type.

## Correct categorical target

The desired property is not merely algebraic exactness at every finite stage.
It is **strict exactness preserved by completion**.  For a compatible family
of source complexes `C_(s,X)`, seek homotopies satisfying

\[
 d_{s,X}h_{s,X}+h_{s,X}d_{s,X}=1
\]

and cutoff compatibility

\[
 h_{s,Y}\iota_{X,Y}simeq\iota_{X,Y}h_{s,X}.
\]

One must then prove either a uniform bound in the completed topology,

\[
 \sup_X\lVert h_{s,X}\rVert_{\mathrm{comp}}<\infty,
\]

or construct an explicit relative homotopy whose boundary fields retain the
divergent components. Without one of these two statements, completion may
create cohomology.

This should not be mislabeled as an automatic derived-limit theorem. The
relevant completion, transition maps, topology, and strictness structure must
first be specified. Failure of closed range, failure of bounded inverse, and
a genuine derived-limit obstruction are distinct possibilities until those
data are fixed.

## Role of the three Tate strata

The exact connected filtration predicts how a completed contraction must be
typed:

\[
 \begin{array}{c|c}
 k\ge3 & \text{ordinary trace-class limiting homotopy}\\
 k=2 & \text{relative Hilbert/determinant boundary channel}\\
 k=1 & \text{rigged-space distributional boundary channel}.
 \end{array}
\]

The first two connected currents cannot be subtracted and forgotten. They
must provide the missing partners that would otherwise escape at infinity.
This gives them a potential RH-bearing role: they are candidate completion
data preventing an off-seam state from becoming unpaired.

## Three theorem gates

The puncture programme now has a forced order:

1. **Canonical-complex rigidity.** A hostile divisor multiplier cannot be
   lifted to the labelled source complex.
2. **Cohomology--section bridge.** The determinant section vanishes exactly
   when the source complex has cohomology.
3. **Completion-stable open-sector acyclicity.** Compatible source
   contractions survive the infinite Euler completion, with the primitive
   and square currents retained as typed boundary channels.

Only their conjunction excludes off-seam punctures.

## Immediate falsifier

For any proposed finite complex, compute the least norm of a contracting
homotopy in the source-completed topology as the prime cutoff grows.  The
construction fails if that norm diverges and no independently derived
boundary channel has the exact divergent principal part.

The test must be made on the full labelled complex, not solely on its scalar
determinant. A bounded determinant value does not control the norm of a
contracting homotopy.

## Present boundary

This packet does not construct the finite source complex. It identifies the
only place an off-seam puncture could survive the proposed finite geometric-
algebra cancellation: loss of a pairing partner at infinite completion.

