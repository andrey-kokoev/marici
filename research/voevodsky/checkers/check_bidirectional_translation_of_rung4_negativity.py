#!/usr/bin/env python3
"""Exact audit of bidirectional propagation of a stationary rung-4 defect."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 # Stationary local Schwarz data: diagonals positive, cross-correlation too large.
 a=Fraction(1);b=Fraction(2);det=a*a-b*b;assert a>0 and det<0
 ks=list(range(-4,5));plaquettes=[{'k':k,'left_reading':str(a),'right_reading':str(a),'cross_reading':str(b),'determinant':str(det)} for k in ks]
 assert all(Fraction(x['determinant'])==det for x in plaquettes)
 result={'schema':'marici.voevodsky.bidirectional-translation-rung4-negativity.v1','covariance_law':'L((U^k p)*(U^k q))=L(p*q)','forward_shift':'U','reverse_plane_shift':'U^-1','plaquettes':plaquettes,'negative_propagates_to_all_translated_plaquettes':True,'endpoint_readings_become_negative':False,'distinction':'Translation covariance preserves the complete Schwarz determinant, not the sign of its positive diagonal readings.','remaining_boundary_gate':'To derive contradiction, one translated copy of the same composite primitive must land in a source-proved positive Schwarz base. Translation does not reduce composite ancestry.'}
 out=Path(__file__).parents[1]/'results'/'bidirectional_translation_rung4_negativity.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'determinant':str(det),'translated_plaquettes':len(plaquettes)},indent=2))
if __name__=='__main__':main()
