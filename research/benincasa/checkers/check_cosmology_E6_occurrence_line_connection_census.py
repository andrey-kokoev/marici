#!/usr/bin/env python3
"""Deutsch-Popperian census for E6 occurrence-line connection data."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
conn=json.loads((B/'bivariate_soft_gram_connection.json').read_text());cyc=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());corner=json.loads((R/'cosmology_qtop_e6_scalar_connection_promotion.json').read_text());prior=json.loads((R/'cosmology_E6_cycle_scale_horizontal_gauges.json').read_text());assert prior['passed']
basis=conn['basis_order'];assert basis==[f'e{i}' for i in range(1,10)] and basis.count('e6')==1
# Falsify the tempting identification of three chart occurrences with e6,e7,e8.
conjectured_indices=[basis.index(x) for x in ('e6','e7','e8')]
chart_map_fields=[k for k in conn if 'chart' in k.lower() or 'occurrence' in k.lower()]
assert chart_map_fields==[] and cyc['target']=='A2 occurrence-difference submodule of the three e6 chart lines'
out={'schema':'marici.benincasa.cosmology-E6-occurrence-line-connection-census.v1','conjecture':'the bivariate basis entries e6,e7,e8 are the three cyclic e6 chart occurrences','falsifier':'a source-declared occurrence-to-basis map and compatible chart coordinate pullbacks must identify those entries','test':{'bivariate_basis':basis,'literal_e6_count':basis.count('e6'),'conjectured_indices_zero_based':conjectured_indices,'chart_or_occurrence_mapping_fields':chart_map_fields,'cyclic_target':cyc['target']},'disposition':'falsified as a source identification','reason':'the connection artifact has one literal e6 coordinate and no occurrence or chart map; e7 and e8 cannot be relabelled as e6 occurrences','available_restrictions':1,'available_restriction_evidence':corner['proved_equality'],'required_restrictions':3,'connection_forms_with_typed_chart_identifiers':0,'horizontal_comparison_testable':False,'next_conjecture':'separate chart-specific artifacts may carry three e6 line restrictions and coordinate pullbacks','next_falsifier':'exhaustive source-envelope search must find three artifacts with explicit chart ids, e6 basis lines, and maps to a common base','passed':True};(R/'cosmology_E6_occurrence_line_connection_census.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
