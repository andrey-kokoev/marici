# Tate reflection needs a support-changing comparison cell

Date: 2026-08-23

The full-log source sectors carry reflection

\[
s_{\rm src}(i)=1-i\pmod 6,
\]

whereas Entry 324's literal completed vertex stars carry

\[
s_{\rm lit}(i)=5-i\pmod 6.
\]

Both commute with rotation \(i\mapsto i+2\).  Exact enumeration shows that
translations by \(2\) and \(5\) conjugate the two reflections abstractly.
However, the complementary-road sequence is

\[
(2,1,0,2,1,0),
\]

and both conjugacies rotate every road label by \(+1\).  There is no
road-preserving conjugacy.

Therefore the mismatch cannot be repaired by a sign, polarity line,
suspension, Tor character, or occurrence-line scalar: these can correct
degree and coefficient parity but cannot change support.  The missing strict
reflection comparison must be a genuinely support-changing 2-cell whose
boundary includes the adjacent-road transition.  This is precisely the sort
of mixed-variance Beck--Chevalley datum excluded from the finite packets.

This no-go does not contradict Entry 324's reflection closure inside the
literal vertex-star system.  It concerns comparison between that frozen
target action and the independently frozen full-log source action.

Evidence:

- `research/nima/checkers/check_tate_reflection_road_conjugacy_gate.py`.
- Entries 210, 225, 249, 252, and 324.
