# The four kinematic chambers supply distinct Bunch–Davies braid words

## Question

How does the lower-half-plane path through the four energy punctures change when one of the triangle inequalities fails, and can that chamber dependence provide the asymmetry needed by the second detector?

## Claim boundary

This packet determines which real punctures the physical path passes in each positive kinematic chamber. It does not identify the resulting braid factors with conductor wall swaps or prove a physical \(v_{\rm alg}\) period.

## Exact chamber words

Let

\[
E_{\rm phys}=x+y+z
\]

for positive \(x,y,z\). The punctures are

\[
0,
\quad2x,
\quad2y,
\quad2(x+y).
\]

Travel from \(E_{\rm phys}\) toward zero through the lower half-plane. The punctures encountered are exactly those strictly between zero and the basepoint, in decreasing real order.

### Triangle chamber

If all triangle inequalities hold, then

\[
\max(2x,2y)<E_{\rm phys}<2(x+y).
\]

The path passes both middle punctures, larger first, and does not pass \(2(x+y)\).

### \(x\)-dominant chamber

If \(x>y+z\), then

\[
2y<E_{\rm phys}<2x<2(x+y).
\]

The path passes only \(2y\).

### \(y\)-dominant chamber

If \(y>x+z\), then

\[
2x<E_{\rm phys}<2y<2(x+y).
\]

The path passes only \(2x\).

### \(z\)-dominant chamber

If \(z>x+y\), then

\[
2(x+y)<E_{\rm phys}.
\]

The path passes all three nonzero punctures in decreasing order:

\[
2(x+y),
\quad\max(2x,2y),
\quad\min(2x,2y).
\]

## Role of the missing lift

The chamber itself supplies a non-arbitrary asymmetry. In the \(x\)- and \(y\)-dominant chambers, the Bunch–Davies path contains exactly one middle-puncture braid factor. These two chambers are exchanged by \(x\leftrightarrow y\).

Therefore a braid-to-integral-Picard lift could send the single-middle words to exchanged primitive detector classes without choosing one wall externally. The triangle chamber instead carries the ordered product of both middle factors; the \(z\)-dominant chamber also includes the top factor.

This gives the missing thing a precise role: it must turn chamber-dependent braid words into integral lattice actions while respecting exchange and path composition. If both single-middle words map to the same diagonal action, no second detector results. If they map to exchanged wall actions, their relative class supplies the antisymmetric channel.

## Disposition

The information path is chamber-dependent, not universal. The highest-value test of the missing integral lift is now localized to the two dominant chambers:

\[
\beta_x=(\text{lower detour around }2y),
\qquad
\beta_y=(\text{lower detour around }2x).
\]

Compute their integral Picard–Lefschetz matrices and test whether exchange conjugates them and whether their relative action on the canonical mixed state reaches the primitive \(v_{\rm alg}\) line.

Verification:

- `research/voevodsky/checkers/check_four_kinematic_chamber_braid_words.py`
- `research/voevodsky/results/four_kinematic_chamber_braid_words.json`
