#!/usr/bin/env python3
"""Exact two-prime no-go for representing a terminal scalar square by a prime-diagonal norm."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 fixtures=[]
 for x,y in [(Fraction(1),Fraction(1)),(Fraction(1),Fraction(-1)),(Fraction(2),Fraction(3))]:
  retained=x*x+y*y;terminal=(x+y)*(x+y);cross=terminal-retained
  fixtures.append({'x':str(x),'y':str(y),'prime_diagonal_norm':str(retained),'terminal_scalar_square':str(terminal),'missing_cross_term':str(cross)})
 assert any(f['missing_cross_term']!='0' for f in fixtures)
 result={'schema':'marici.voevodsky.prime-diagonal-carrier-terminal-square-no-go.v1','retained_carrier':'H_p direct-sum H_q with orthogonal prime idempotents','terminal_evaluator':'epsilon(x,y)=x+y','identity_required':'||x||^2+||y||^2 = |x+y|^2','fixtures':fixtures,'identity_holds_for_all_inputs':False,'obstruction':'The terminal square contains 2 Re(conj(x)y), while the retained G1 Green form has exactly zero cross-prime block.','consequence':'The local positive G1 carrier cannot by itself realize the globally scalar-polarized Weil observer. A new source-authorized cross-prime coupling or a different target notion is required.'}
 out=Path(__file__).parents[1]/'results'/'prime_diagonal_carrier_terminal_square_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
