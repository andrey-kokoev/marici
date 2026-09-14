# v104: candidate-to-physical lift completion

`rzk/132-candidate-to-physical-lift-completion.rzk.md` factors the remaining
physical extension problem around the implemented endpoint/native-bar
candidate.

A candidate now consists of one physical point with endpoint, normal-cube, and
operation coherences. Its completion type asks only for road-Cech and physical
group/reflection coherences at that same point. Given both witnesses, the module
constructs the full five-direction lift and permits supported-residue
evaluation.

This prevents replacing the missing directions by independently selected
physical points. It also sharpens the next computation to two maps evaluated on
the existing selected primitive candidate.

The transitive closure contains two files. A fresh combined Rzk check passes all
13 declarations, with no `#assume` declarations.
