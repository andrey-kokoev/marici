# Inequivalent D5 doublets remove mixed quartic angles

Work package: WP600  
Owner: marici.Figueiredo

## Scope correction

This packet proves a complete statement only for mixed quartics of bidegree
\((2,2)\). It does not define a complete renormalizable architecture. WP601
exhibits the allowed cubic \(\operatorname{Re}(z_\phi z_\psi^2)\), which
moves the candidate vacuum. The representation criterion below remains valid
at its stated quartic degree; the earlier progressive architectural reading is
withdrawn.

## Representation criterion

For irreducible real orthogonal source representations \(V\) and \(W\), each
with one invariant metric, mixed scalar quartics of bidegree \((2,2)\) form

\[
\left(\operatorname{Sym}^2V^*\otimes
\operatorname{Sym}^2W^*\right)^G.
\]

The radial product is always present through the unique trivial summand in
each symmetric square. Angle-moving mixed quartics are absent precisely when
\(\operatorname{Sym}^2V\) and \(\operatorname{Sym}^2W\) share no
nontrivial irreducible channel. This converts the WP599 obstruction into a
source-representation selection rule rather than a coefficient deletion.

## Smallest dihedral window

Let a common \(D_5\) act on two inequivalent faithful real doublets with
rotation weights one and two. Exact enumeration of all nine mixed quartic
monomials leaves a one-dimensional invariant space,

\[
(x^2+y^2)(u^2+v^2).
\]

It is purely radial. For comparison, two identical \(D_4\) doublets have a
three-dimensional mixed-quartic invariant space before the twisted exchange,
which is why the angle-moving operators of WP597 and WP599 occur.

The same \(D_5\) pair admits a generalized-CP-breaking orientation. For
\(\theta_\phi=0\), only the generalized CP with rotation power zero fixes
\(\phi\). For \(\theta_\psi=\pi/5\), only power three fixes \(\psi\).
Their stabilizer intersection is empty.

## Exact limitation

The first individual angular invariant of either faithful \(D_5\) doublet is
quintic,

\[
\operatorname{Re}(z_\phi^5),
\qquad
\operatorname{Re}(z_\psi^5).
\]

Therefore the renormalizable potential has accidental independent angular
freedom. The representation solves the mixed-quartic stability obstruction,
but it does not yet select the two orientations. Selecting the axis and
off-axis sectors requires degree-five operators with opposite relative signs.
That sign must follow from a microscopic source operation; choosing it because
it breaks CP would repeat the defect corrected in WP599.

A quintic scalar term is also not a globally stable standalone potential.
The claim is therefore an effective-theory window with an explicit cutoff.
A microscopic completion must generate stabilizing higher-degree terms and
show that they do not move the selected angular orbit inside the admitted
domain.

## Source and experiment programme

Any progressive successor would have to supply:

1. two inequivalent faithful \(D_5\) doublets;
2. a microscopic mediator grammar generating both quintic anisotropies with a
   forced opposite sign;
3. a complete invariant-ring and radiative-closure audit through the mediator
   threshold;
4. a portal descending the selected orbit to a CP-odd `physical16`
   coordinate;
5. calibrated threshold records that test the same mediators responsible for
   the quintic operators.

The last item supplies the prospective independent criticism. If the
mediators are absent, their relative sign is wrong, or threshold data reveal
an angle-moving mixed operator larger than the allowed stability margin, the
source architecture is refuted. None of those records is yet calibrated in
the current flavor packet.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp600_d5_mixed_quartic_radial_window.py

The generated result is
research/flavor/results/wp600_d5_mixed_quartic_radial_window.json.
