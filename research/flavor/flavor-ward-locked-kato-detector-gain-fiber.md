# Ward-Locked Kato Detector and Its Gain Fiber

## Question

Can a conserved source current make WP869's co-moving detector physically
unavoidable, and does the same Ward principle fix the portal magnitude and RG
basin?

## Claim boundary

Let the microscopic action contain a detector source term

\[
S_{\rm src}=j\,g\,e_0\psi_0.
\]

Suppose the admitted threshold matching of the source field is

\[
\psi_t=U_t\psi_0,
\]

where \(U_t\) is the Kato unitary derived in WP869. Rewriting the same source
term in the matched field gives

\[
S_{\rm src}=j\,g\,e_0U_t^*\psi_t.
\]

Thus the matched detector vertex is necessarily

\[
e_t=e_0U_t^*.
\]

This is not a detector row chosen after seeing the kernel. It is the pullback
of one bare source vertex through the same field matching. If \(j\) couples to
an exactly conserved, anomaly-free current, the Ward identity forbids an
independent relative vertex rotation. The Kato detector co-transport then has
a legitimate shared-action constructor.

For the transported kernel \(k_t=U_tk_0\),

\[
g\,e_tk_t=g.
\]

The fixed laboratory row instead gives \(g\cos t\). The shared-action Ward
constructor therefore closes the frame-attachment part of the physical
instrument gate.

## Residual gain and RG fibers

The Ward identity does not select the common coupling \(g\). The theories
\(g=1\) and \(g=2\) have the same:

- conserved-current representation;
- Kato transport;
- normalized dark ray;
- conditional-expectation basin;
- threshold intertwining;
- normalized detector direction.

Their absolute source amplitudes are \(1\) and \(2\), and their intensities are
\(1\) and \(4\). A calibrated reference channel carrying the same \(g\) can
form a unit ratio, but that ratio removes rather than predicts the absolute
portal magnitude.

Nor does current conservation determine the beta function. A vanishing beta
function and a nonzero cubic beta function are both compatible with the exact
frame Ward law in this finite audit. Additional dynamics must fix the
coefficients, fixed point, physical RG normalization, and global basin of
\(g\). WP866 supplies a basin for the state-selection channel, not for this
continuous coupling coordinate.

The construction also assumes the current is anomaly-free on the admitted
domain. An anomalous divergence or a threshold that changes current support
breaks the Ward premise rather than producing a corrected co-transport
theorem.

## Gate classification

- Relative sign and normalized ray: inherited from the source boundary
  character and transported without relative vertex renormalization.
- State basin: fixed by WP866's conditional expectation.
- Threshold attachment: repaired by the common field/source pullback.
- Source-level readout: executable in principle as a current vertex, subject
  to an admitted current-coupled apparatus.
- Absolute magnitude: free common coupling \(g\).
- Coupling RG basin: not fixed by the Ward identity.
- Detector calibration: a detector-unit map for \(g\) remains experimental
  input.

## Smallest exact falsifier

At fixed Kato path, the pair \(g=1\) and \(g=2\) satisfies the same Ward
co-transport law and every normalized structural gate. The terminal
intensities are \(1\) and \(4\). This is the smallest exact proof that Ward
locking does not select portal magnitude.

## Disposition

Progressive interface theorem and negative magnitude result. A shared-action
Ward identity can make the Kato detector transport source-derived rather than
an added moving reference. It still leaves a one-dimensional common-gain fiber
and does not derive the coupling beta function. The remaining source principle
must quantize or dynamically select \(g\), fix its physical RG flow, and bind
that normalization to a calibrated detector standard without losing the
Ward-locked threshold attachment.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp870_ward_locked_kato_detector_gain_fiber.py
~~~
