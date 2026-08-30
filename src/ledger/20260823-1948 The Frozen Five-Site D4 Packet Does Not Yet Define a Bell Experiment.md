# 1948 — The Frozen Five-Site (D_4) Packet Does Not Yet Define a Bell Experiment

## Question

Entries 1945--1946 exhibit five labelled coefficient channels, a
four-dimensional augmentation sector, and one physical scalar port.  Do these
objects already satisfy Entry 1567's admission contract for a Bell test?

## Frozen packet

Audit only:

- the 180-term five-cycle OFPT source packet;
- the five-occurrence (D_4) monodromy packet;
- the scalar readout decomposition.

No bipartition, analyzer, outcome effect, or probability is added for the
purpose of passing the test.

## Positive pre-Bell structure

The packet contains:

\[
5\text{ labelled occurrence channels},qquad
\dim I_{\rm aug}=4,
\]

one source-defined equal-weight scalar port, and a nonzero invariant
logarithm.

This is meaningful readout structure, but it is not by itself a bipartite
measurement protocol.

## Six-gate audit

Use the Bell admission order:

1. source-defined bipartite preparation and wing decomposition;
2. two independently selectable local settings per wing;
3. exclusive local outcome effects;
4. normalized positive joint readout;
5. no-signalling marginals;
6. CHSH and Tsirelson audit.

The result is

\[
\boxed{(0,0,0,0,0,0).}
\]

The first failure is gate one.  The five cyclic occurrences are alternative
labelled pinch locations, not two independently controlled local wings.  The
augmentation directions are coefficient differences, not detector settings
or exclusive outcomes.

Consequently no joint probability table or CHSH functional is currently
typed.

## Result

\[
\boxed{
\text{The frozen }D_4\text{ packet contains rich labelled readout data but
does not yet define a Bell experiment.}
}
\]

This is a bounded source-packet census, not a no-go theorem for cosmological
Bell tests.  It prevents a category error: hidden coefficient information is
not equivalent to Bell nonlocality.

## Cross-sector interpretation

The result matches Entry 1567's architecture.  Bell belongs at the physical
readout layer, after source-defined preparation, local instruments, positive
normalization, and marginals exist.  The QED lane supplied those missing
objects independently; the present cosmological lane has not.

## Next falsifier

Search for an independently defined cosmological observable with:

- two separated external subcollections or detector regions;
- two source-controlled settings on each;
- exclusive local effects and a positive normalized joint pairing.

Only such a packet licenses mapping the (D_4) augmentation sector into a
Bell test.  Do not reinterpret cyclic occurrence labels as settings.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_d4_bell_admission.rs`
- `research/benincasa/results/five-site-d4-bell-admission.json`
- Entries 1567, 1569, 1945, and 1946
- allocator claim: `seqclaim-0dd527722c10db1b15a27b46`

