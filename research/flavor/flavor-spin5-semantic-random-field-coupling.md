# Spin(5) semantic random-field coupling (WP904)

## Question

Can WP903's sequential-randomness defect be removed by an executable source
constructor whose coupling survives width-dependent control flow?

## Constructor

Define a frozen random field

\[
R(K,e,s,a,i)\in\{0,\ldots,2^{64}-1\},
\]

where (K) is a preregistered seed-family key, (e) is the pair identifier,
(s) is a stage, (a) is a semantic physical address, and (i) is a local
draw index. The checker instantiates (R) as the first 64 bits of SHA-256 over
a length-delimited canonical encoding of these fields.

The two width arms consume the same immutable field. Width is an argument to
the registered source transform, not to (R). For example, both arms obtain
the parent-lineshape uniform from
`source/parent_virtuality/0`; shower, pile-up, detector, and reconstruction
draws occupy disjoint namespaces. A rejected proposal may request further
draws below its own address without shifting any other address.

This is stronger than using the same sequential seed. Inserting an extra draw
at `source/width_branch/0` leaves every previously named draw unchanged. The
complete trial key remains available even when selection fails, so the output
can be one of WP902's seven null-completed symbols.

## Executed hostile checks

The checker executes 256 event pairs and verifies:

- bit-identical replay under the same manifest;
- independence of all registered addresses from width-arm labels;
- invariance of registered downstream draws after insertion of a
  width-dependent branch draw;
- separation of distinct event identifiers and seed-family keys;
- explicit retention of pair identifiers for null outputs;
- rejection of ambiguous, unregistered, or duplicate semantic addresses.

The smallest exact falsifier of the semantic-address guarantee is one
registered address whose 64-bit value changes after an unrelated branch draw
is inserted. WP905 corrects the authority boundary: such a failure need not
kill an otherwise reproducible shared-seed coupling with correct marginals;
it kills this stronger coordinate-alignment and variance-reduction claim.

## Authority boundary

WP904 supplies an executable reference constructor for a source-level common
random field and a prospective variance-reduction adapter. It is sufficient
but not necessary for WP902's coupling inequality. It does not establish that
Pythia, Geant4, CMSSW modules, or the
2015 CMS analysis can consume this field by semantic address. An adapter that
merely reseeds their sequential engines would reintroduce WP903's defect.

The next physical-instrument gate is a module-by-module adapter or typed
base-event record proving that every stochastic operation used by both arms
is either addressed in this field or replayed from an immutable upstream
product. Software hashes, transform versions, nuisance support, null records,
and the independently calibrated acceptance floor remain mandatory.

This construction is neither a flavor selector nor a presentation
rigidifier. It is a prospective simulation instrument that makes the WP902
coupling premise executable at the reference level.

Run:

~~~text
uv run python research/flavor/checkers/wp904_spin5_semantic_random_field_coupling.py
~~~
