# Source spin-lift splitting: neutron section, proton obstruction

## Question and disposition

Iteration 1 executes the registered `source-spin-lift-splitting` proposition using freshly read net and source state. The result is **constructed at the finite source-group scope**: the actual neutron pullback spin extension splits; the actual proton extension does not.

The mutable [proposition record](contracts/source-spin-lift-splitting.v1.json) now records the completed test. Its mathematical content is fixed independently by [the prospective test contract](contracts/source-spin-lift-splitting-test.v1.json): semantic digest `ce8709bb5aa011dfd9c6054557fcf700112a1333712b5b0fe17f07a68b209c0d`. Only execution-state fields are excluded from that digest. Updating them cannot change the proposition, source obligations, rivals or falsifiers.

This is global source-word/comparison compatibility, not physical spin selection. No new physical records arrived in the addressed inbox.

## Actual source identification and full extension

Reconstruct the proper Cartesian rotations from each actual source generator and the retained source-frame adapter. Check the transported spin matrices against the original Clifford lifts, and attach their actual 36-mode coefficient actions.

The proton rotations act faithfully on the retained tetrahedron as **all twelve even vertex permutations**, with every multiplication checked. This proves the actual source action is $A_4$, rather than inferring it from cardinality. The neutron generator has exactly three distinct powers, with multiplication checked modulo three, giving the actual $C_3$ action. Matching rotation words also have matching native coefficient actions.

For each actual source element, the checker constructs both spin lifts. They give full pullback sizes 24 and 6. Completeness is not an assumption that one chosen generator-lift subgroup is exhaustive: the ratio of any two lifts of the same rotation commutes with every quaternion-unit matrix. Commuting with the first two forces a scalar; determinant one forces that scalar to be $\pm1$. The two verified lifts therefore exhaust each fibre.

All pullback products are checked: 576 proton pairs and 36 neutron pairs. All source rotation/mode products are checked as well.

## Neutron: an explicit homomorphic section

Let $g$ be the actual neutron source generator and $U_+$ its transported positive-scalar lift. The source has $g^3=e$, while

\[
U_+^3=-I.
\]

Choose

\[
\sigma(e)=I,\qquad \sigma(g)=-U_+,\qquad
\sigma(g^2)=(-U_+)^2=U_+^2.
\]

Then $\sigma(g)^3=I$. All nine source-pair multiplication equations and the actual lift projections pass. Among all four normalized section-sign choices, exactly one is homomorphic; its bits relative to the retained reference section are $(0,1,0)$. Using the positive generator lift instead fails a source relation.

This uniqueness concerns the given finite source representation and fixed projection. It does not select a physical neutron spin preparation or justify erasing phase under the larger 24-operation packet language.

## Proton: a sign-invariant obstruction

Let $g_0,g_1$ be the actual two source generators. The source element

\[
h=g_0^2g_1
\]

is a nonidentity involution. Both its spin lifts satisfy

\[
\widetilde h^2=-I.
\]

Hence a homomorphic section cannot exist: it would require $\sigma(h)^2=\sigma(e)=I$, but neither available lift has that square.

The checker exports the concrete source identity word

\[
(g_0^2g_1)^2=e.
\]

Its original 36-mode action is also identity. Its lifted spin word is $-I$ for **all four** independent sign choices of the two generator lifts. Each generator occurs an even number of times in the word, so sign changes cannot alter this residual. In particular, choosing both opposite lifts makes each individual generator's cube equal $I$, but the mixed source relation still fails. Generator-order tests alone are insufficient.

## Exhaustive section and cocycle control

A normalized reference section $s$ gives bits $c(g,h)$ by

\[
s(g)s(h)=(-I)^{c(g,h)}s(gh).
\]

Normalization and the cocycle identity are checked on every pair/triple: 1,728 proton triples and 27 neutron triples. Changing section by normalized signs $b$ gives

\[
c'(g,h)=c(g,h)+b(g)+b(h)+b(gh)\pmod2.
\]

For the proton involution,

\[
c'(h,h)=1+b(h)+b(h)+b(e)=1.
\]

Thus the obstruction survives **every** normalized sign redefinition, not merely the four generator-sign choices. Independently, all $2^{11}=2048$ normalized proton section choices are tested; none is homomorphic. All $2^2=4$ neutron choices are tested; one is homomorphic.

## Source attachment and implementation correction

For every source group element the actual mode action is retained, and its doubled spin action is checked through the existing transported encoder and decoder. No mode identity is substituted except when the actual source word really returns to identity.

The first checker run failed a raw encoding square because it inserted a common-frame spin matrix directly into the old raw tensor coordinates. This was an implementation frame-type error. The corrected construction transports back explicitly:

\[
U_{\mathrm{raw}}=C^{-1}U_{\mathrm{common}}C.
\]

It is also checked against the product of the **original** source lift matrices along the same word. The unchanged encoding/decoding equations then pass. No source, normalization rule, conjecture or acceptance criterion was weakened. The initial freeze is retained; the corrected checker was frozen again before the passing challenge.

Hostiles reject the incorrect neutron section, a proton certificate claiming square $+I$, and a matrix whose abstract source label has the wrong actual projection.

## Verification and stop boundary

Sixteen exact check groups pass. The corrected prospective SCC freeze is `0e96175b417ff2338ffd562e6b121acade821aa50bd8ed14b4d850d67c5acc1d`; its frozen challenge passes. A fresh SCC check also verifies the completed execution-state metadata without changing the mathematical digest.

```text
python research/aspect/scc/scc.py check source-spin-lift-splitting-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

Artifacts:

- `research/strominger/checkers/check_source_spin_lift_splitting.py`.
- `research/strominger/results/source-spin-lift-splitting-v1.json`: actual rotations, tetrahedral permutation certificate, source words/mode actions, multiplication tables, reference lifts, cocycles, neutron section and invariant proton obstruction.
- `research/strominger/scc-models/source-spin-lift-splitting-v1.json`.
- `research/strominger/contracts/source-spin-lift-splitting-test.v1.json`: immutable scientific contract.

Arithmetic is exact over inherited source fields and Gaussian rationals. Native inputs and prerequisite receipts remain unchanged; no native producer or proof-assistant compiler is run.

The net proposition is resolved. The original physical coupling gate and root remain open: a finite-source splitting theorem neither selects the doublet/preparation nor supplies charge, magnetic, internal interaction or resource laws. With no new source records, the actionable frontier is empty. Do not repeat the same tests or create a waiting successor merely to fill further iterations.
