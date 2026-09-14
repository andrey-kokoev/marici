# Noncanonical attachment homology scan

## Question

Do noncanonical grades supply the first relative attachments with genuine homology, in contrast with the completely matched canonical cube packages?

## Claim boundary

This is a bounded scan of the distinct-shell filtration through grade 20000. Relative homology at one grade measures the cells entering at that grade; it does not by itself establish persistent absolute homology or a physical class.

## Bold conjecture

Canonical prime-exponent grades are specially coherent: their cells arrive in complete acyclic packages. Away from those grades, divisibility collisions can omit cofaces and leave nonzero relative homology.

## Rivals

1. Every exact-grade attachment is acyclic, so canonicality is irrelevant.
2. Nonzero results arise only from an incorrect degree-zero birth rule.
3. Nonzero relative classes occur but are immediately removed and carry no persistent information.

## Test

Enumerate every distinct-shell positive-dimensional cell with birth grade at most 20000 directly from

\[
\operatorname{birth}[D;I]
=
\frac{D}{\prod_{i\in I}p_i}
\left(p_{\max I}\prod_{i\in I}p_{i+1}\right).
\]

Generate degree-zero relative cells independently as vertices whose least incident-edge grade equals the tested grade. At each event grade, retain only boundary faces born at that same grade, verify the relative differential squares to zero, and compute Betti numbers over two prime fields.

Record the first noncanonical grade with nonzero relative homology, the earliest example in each detected degree, and whether the two fields agree. Recheck every canonical grade inside the bound against acyclicity.

## Falsifier

The conjecture fails on this bounded domain if every noncanonical attachment is acyclic. A field-rank disagreement or broken boundary composition is an implementation defect, not supporting evidence.

## Computed result

Among 4922 event grades through 20000, 2085 have nonzero relative homology. Grade 6 is the first: one edge introduces two new vertices, leaving one relative connected-component class. The first positive-degree exception occurs at grade 70, where one edge has both endpoints already present and therefore gives

\[
H_1(X_{\leq70},X_{<70};\mathbb Z)\cong\mathbb Z.
\]

The two tested fields agree at every event grade, every relative differential squares to zero, and the canonical grades 525 and 8085 remain acyclic.

## Disposition

The prediction survives strongly on the bounded domain: noncanonical grades frequently carry relative homology, while both canonical grades in range carry none. This establishes attachment-level exceptions, not persistence in the absolute filtration. The next test must determine the lifetime of the grade-70 class and distinguish immediate filling from a persistent arithmetic feature.
