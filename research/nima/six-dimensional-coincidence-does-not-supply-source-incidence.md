# Six-dimensional coincidence does not supply source incidence

## Question

Does Grothendieck's six-channel source-natural carrier resolve the 720-fold
typing ambiguity in Aspect's finite cyclic sewing control?

## Three distinct six-dimensional objects

The current programme contains three objects of dimension six:

1. the regular cyclic control \(\mathbb C[\mathbb Z/6\mathbb Z]\), equipped
   with translation and discrete Fourier transform;
2. the source-natural boundary carrier \(V\oplus V^*\), equipped with the
   split evaluation form;
3. the conditional paired-sector carrier
   \(S\otimes\operatorname{Sym}^2 T\), equipped with a two-by-three tensor
   factorization and a quadratic relation on the three-dimensional factor.

Equal dimension does not identify these objects. Their admitted structure is
different: cyclic order, dual evaluation, and tensor factorization are
independent data.

## Exact reduction of the ambiguity

Forget all structure and label six coordinates. There are \(6!=720\)
assignments.

Suppose a source map constructs only the perfect dual pairing between three
carrier coordinates and three covector coordinates. The automorphism group of
that matching has size

\[
2^3 3! = 48.
\]

If the source also distinguishes the two summands \(V\) and \(V^*\), only a
common permutation of the three paired coordinates remains, giving \(3!=6\)
assignments. If it preserves the matching and the unordered two-by-three
factorization but permits global exchange of the two sectors, 12 assignments
remain.

Thus the full-dual theorem is a genuine gain: it can reduce the untyped cyclic
ambiguity from 720 to 6 once the primal and dual summands are source-labelled.
It does not select one of those six coordinate incidences.

## Why the remaining ambiguity matters

The three residual permutations exchange the directional components of the
source coflag. A Fourier matrix remains unitary after any of them, and the
split evaluation form is also preserved. Therefore neither optical matrix
quality nor dual-pairing naturality can decide which coordinate is primitive,
prime-square, seam, endpoint, connected tail, or archimedean.

The earlier six-name list is also not the same typing as \(V\oplus V^*\).
Grothendieck's finite boundary packet retains primitive, square, connected
tail, seam, and a five-component archimedean cell in different topological
grades. It explicitly warns against collapsing them into one Hilbert
Gramian. The six-dimensional full dual instead arises from a
three-dimensional carrier and its contragredient. Treating these as the same
six ports would erase precisely the source typing the construction was meant
to preserve.

## DPC verdict

Current gain: a source-natural candidate pairing architecture reduces the
finite assignment ambiguity.

Withheld claim: a source-derived identification between the cyclic residues,
the three carrier directions, their duals, and the arithmetic boundary
currents.

The next constructor must provide an ordered source basis
\((v_1,v_2,v_3)\), its contragredient basis, and the incidence of those basis
elements with the analytic boundary maps. Only then may the cyclic control be
conjugated into the source carrier. A convenient permutation is not a
constructor.

## Finite falsifier

Take any nontrivial common permutation of the three primal-dual pairs. It
preserves the summand distinction and the split evaluation form, yet changes
the typed coordinate incidence. Therefore dual naturality plus exact Fourier
unitarity is insufficient to fix the source map.

## Verification

The checker `check_six_dimensional_source_incidence.py` enumerates all 720
coordinate permutations and verifies the residual counts 48, 12, and 6.

Source packets audited:

- `research/grothendieck/source-naturality-requires-the-full-six-channel-dual.md`
- `research/grothendieck/the-six-channel-sewing-space-is-conditionally-a-segre-veronese-module.md`
- `research/grothendieck/the-finite-full-boundary-packet-closes-as-a-fourier-stable-pro-gram-extension.md`
- `research/grothendieck/theta-primitive-and-square-incidence-are-atomic-scale-currents.md`
- `research/aspect/completed-sewing-finite-cyclic-realization.md`

