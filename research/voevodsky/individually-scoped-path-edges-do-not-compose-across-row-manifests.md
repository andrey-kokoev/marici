# Individually scoped path edges do not compose across row manifests

Fresh `check_mixed_manifest_path.py` models weakening start x<=1 -> middle x<=2 scoped to rows-A generation 1, then middle x<=2 -> end x<=3 scoped to rows-B generation 2. Each edge has consistent local target arithmetic, but composition fails `SOURCE_GENERATION_MISMATCH_NEEDS_TYPED_MIGRATION`; a same-source control passes. A changed middle target also fails even on the same manifest. A path-level consistency gate is therefore separate from per-edge commitments.

This fixture does NOT prove Farkas endpoint packets or provide an actual migration edge. A source migration would require an independently authorized source change, proof-catalogue revalidation, and explicit transition binding both generations. Source ownership and analytic S,A,R,C,G assignment remain unavailable.

Next test a proposed SOURCE-MIGRATION edge with a correct old/new row digest but no issuer: it may be mathematically well-scoped yet must be refused as authorized provenance, rather than laundered into the path via a convenient edge label.
