# Tessellated reader fields and bounded coherence

**Research checkpoint · October 18, 2026 · marici.Strominger**

A concrete field model now connects the native P/N/E constructions while
retaining coefficient frames and realization history. Its operator identities
are checked exactly; its geometric interpretation and dynamics remain conditional.

[Explore the isotope / R-space viewer](/experiments/isotope-space). Its native isotope grid and R-space view remain separate: no placement map between them is established.

## A spatial picture

Imagine three tetrahedral wedges sharing an edge. Each is a reader presentation,
not a new set of independent spatial dimensions. Beside the geometry, picture
a **12-by-3 array of amplitudes**. Two weighted projections act along its two
directions. P and N exchange their local/alignment roles.

The actual fields have different geometric organizations:

| Carrier | Geometric organization | Field coordinates |
|---|---|---:|
| P | Four tetrahedral faces, each divided into three patches; three spatial components per patch | 36 |
| N | Six belt faces, each divided into three patches; two in-plane components per patch | 36 |
| E | Four face spinor blocks in the retained native construction | 8 |

The proposed common T has a four-dimensional metric. The three-wedge picture
shows how its reader facets meet; it cannot preserve all their distances in 3D.
Copies of T have not been shown to tessellate space.

## What is checked

- **Exact factorization:** native baryon coefficients and metrics give a
  12-by-3 field, two commuting weighted projections and one common return mode.
- **Global PN candidate:** a 36-component metric-preserving map exchanges the
  native local/alignment projectors. It must mix beyond a single shared face.
- **Candidate NE conversion:** N's three local modes split into one aligned
  mode and two relative-sector modes. Those two modes map onto E's native
  return doublet, including a checked native threefold action.
- **All five reference coefficients retained:** two contrast combinations enter
  the E block; three remain in the baryon block. The joint map preserves norm.
- **Context from the shared edge:** the two incident-face patches select the
  context modes, repeated across the three sectors to respect their symmetry.

This is not a claim that projecting onto a two-dimensional image preserves
all information. The remaining field components and reference data are retained
in the joint construction.

## Coherence has a frame

Translating a whole decorated neighborhood preserves the tested local rules.
Combining then translating agrees with translating then combining in 5,568
configuration squares and 44,736 candidate extensions, including rejections.

Different native paths can reach the same marked window at the same origin
with different coefficient frames. One checked relative permutation has order
five. Equal geometry therefore does not license erasing frame or history.

The refined candidate was explored from **24 seed markings through depth 28**:

| Bound | Result |
|---|---:|
| Packet/frame states, summed across seeds | 250,040 |
| Checked transitions | 458,912 |
| Conflicting candidate field parities at repeated marked charts | 0 |

This checks the declared connection rules in a finite region. It is not a
universal coherence theorem or a certification of every simultaneous assembly.

## What the tests ruled out

The proposed M/C torus was **not derived**. The existing geometry supplies one
transverse link circle; closing another direction requires an additional rule.
Seven blocks of four realization steps and fourteen blocks of two are both
consistent with period two, but do not establish sevenfold or fourteenfold symmetry.

A face-confined PN map cannot preserve the full native return: the face contains
one quarter of P's return norm but one sixth of N's. A single N return also
cannot be mapped onto both independent E return directions while preserving
the return projectors. The candidate instead uses N's existing relative modes.

## Explicit assumptions and remaining work

The window-to-sector identification, PN completion and phase conventions are
still model choices. The conversion changes the original projector-defect
measure. An added electron-return accounting term restores an algebraic balance,
but its physical energy interpretation has not been derived.

There is no claim here of a physical vortex, measured mass or charge, isotope
stability, particle creation, or a replacement for established physical theories.
The next tests concern source-selected couplings, incidental contacts in complete
assemblies, and dynamics with independently justified units.

## Evidence and reproduction

<a href="/research/ledger/20261018-4326-tessellated-reader-fields-and-bounded-framed-coherence/" target="_self">Ledger entry 4326</a>
records the checkpoint. [Download the verification manifest](/research/tessellated-reader-fields/verification.json)
for seven fresh checker runs, receipt hashes and content-addressed snapshot paths.

- [Research closeout and next tests](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/tessellated-reader-fields-closeout-v1.md)
- [Reproduction checker](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/checkers/check_reader_field_closeout.py)
- [Geometric contexts and extended coherence](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/geometric-context-and-extended-coherence-v1.md)
- [Native contrast-to-electron candidate](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/neutron-contrast-electron-transport-v1.md)

```sh
python research/strominger/checkers/check_reader_field_closeout.py
```

These are executable checks, not independent scientific review. Production
assembly and viewer rules are unchanged.

[Back to results](/research/results/) · [Common geometric assembly](/research/results/common-geometric-assembly)
