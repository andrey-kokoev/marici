# Thirty-Two Full Responses Form Five Smith Packets and Three Two-Adic Profiles

## Exact observation tower

The signed-presentation census has three distinct observation levels:

\[
32\text{ full response matrices}
\longrightarrow
5\text{ exact integral Smith packets}
\longrightarrow
3\text{ two-adic depth profiles}.
\]

The first number is exact faithfulness: every legal signed presentation has a
different \(4\times4\) response matrix.

The second number classifies the full and relational response deltas by their
exact integral Smith factors. Those five packets distribute across the three
depth-profile components as two, one, and two.

They have a source-side classifier

\[
A_+,\quad A_-,\quad B,\quad C_+,\quad C_-.
\]

On the endpoint stratum \(A\), multiply the orientation of the repeated
endpoint by the common tail sign. On the opposite-polarity through stratum
\(C\), multiply the orientation of the ordered tail labels by the sign of the
first tail. These two characters split \(A\) and \(C\). Equal-polarity through
states form the unsplit packet \(B\).

This \(2+1+2\) structural classifier is bijective with the five exact Smith
packets. Its class sizes are eight, eight, eight, four, and four.

The third number forgets every odd factor and retains only the 2-adic
valuations. These are the framing states of sizes sixteen, eight, and eight.

## Stratum-dependent visibility

Atomic simultaneous inversion of both nonrepeated generators behaves
differently on the three strata:

- endpoint: it changes the exact Smith packet but preserves its 2-adic depth;
- through with equal polarity: it preserves the exact Smith packet;
- through with opposite polarity: it changes the exact Smith packet but
  preserves its 2-adic depth.

Across the complete directed census it has eight exact-Smith equalities, all
on the equal-polarity through stratum, and zero exact-response equalities.

## Meaning

Constructor visibility is typed by the observation functor:

\[
\begin{array}{c|c}
\text{observation}&\text{visibility of coupled inversion}\\
\hline
\text{full matrix}&\text{always visible}\\
\text{exact integral Smith packet}&\text{invisible only on }T_+\\
\text{two-adic Smith depth}&\text{always invisible}.
\end{array}
\]

This is the smallest exact example in the census where a single source
constructor changes visibility across successive observation quotients.

## Replay

Run:

    python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py

The checker verifies seventy exact gates.
