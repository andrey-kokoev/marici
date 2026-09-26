# Concrete one-step diagrams require explicit pure compression

A new closed-port reifier reconstructs an abstract pending term from actual wires, records the contextual path of EACH F agent, and represents pure subtrees as keep(history). It checks complete traversal and preserves rule witnesses, seed evidence, premise order and layered histories. It does not evaluate reference flatten.

Important discovery: literal equality with one abstract rewrite is too strong for this canonical representation. When the last pending child finishes, reification compresses its pure ancestors into keep nodes. This administrative change is not an additional net rewrite. It must be accounted for explicitly, not hidden behind endpoint equality.

The checked executable diagram is now:

reify(actual_wire_step(net)) = compact(one_contextual_abstract_step(reify(net))).

`check_port_refinement.py` checks32 actual steps across38 states, including26 contextual steps and16 cases requiring pure compression. All three root schemas occur. A deliberately altered rule witness passes ordinary package/port admission but FAILS this refinement diagram, demonstrating that the check is stronger than endpoint typing or final-package agreement.

New Agda module ResolutionNetCompression.agda specifies the administrative relation with pack-one, pack-two and context/composition constructors. It proves compact-sound and compact-work: compression preserves full interpretation and pending work. A RepresentedStep consists explicitly of one abstract rewrite followed by compression; represented-sound and represented-work establish history preservation and exact one-unit decrease for such a step. Fresh --ignore-interfaces safe Cubical checking passes; log: results/agda-compression.log.

What remains: the Python-produced contextual path and compression equality are executable witnesses, NOT automatically inhabitants of Agda RepresentedStep. No universal graph-to-term refinement theorem has been established. The next focused obligation is a certificate export/check path for concrete traces, or an intrinsic typed port-tree representation whose rewrites construct RepresentedStep witnesses. Both must retain the original source/target port evidence rather than certify only an independently reconstructed abstract trace.

Reproduce the bounded wire check with python research/voevodsky/resolution-net-v1/check_port_refinement.py. Its source hashes and counts are in results/port-refinement.json. General admission, open-arrival and resource-commit boundaries remain as previously stated.
