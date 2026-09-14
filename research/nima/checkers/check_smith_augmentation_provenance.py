"""Audit what augmentation the integral Smith checker actually presents."""
import argparse,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 text=Path(a.source).read_text()
 checks={'forms_a2_products':"pos[(a+2,b)]" in text,
         'augments_with_products':"smith_summary(image+products)" in text,
         'contains_labelled_s11':"s11" in text,
         'contains_L2_formula':"l2_transition" in text or "L2 transition" in text}
 assert checks['forms_a2_products'] and checks['augments_with_products']
 assert not checks['contains_labelled_s11'] and not checks['contains_L2_formula']
 out={'schema':'marici.nima.smith-augmentation-provenance.v1','status':'correction-required','checks':checks,
  'actual_presentation':'integral Smith form of plus exact image augmented by a^2 times eligible image columns',
  'not_established':'identification of that a^2-product augmentation with the labelled L2 Bockstein transition',
  'conclusion':'Smith results 142-149 support the a^2 Cartier-product completion only; references to L2 require a separate integral presentation'}
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
