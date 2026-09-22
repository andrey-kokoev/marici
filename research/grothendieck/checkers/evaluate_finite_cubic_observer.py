"""Bounded-integral evaluator; outputs per physical w_seam^2.

CLI: uv run --with python-flint python <this-file> observations.json
Input: joint_filter_values (449 [real,imag] decimal-string pairs),
       total_joint_l1_error (nonnegative decimal string), conjugate (default true).
No point-sample acquisition is implied by this interface.
"""
from pathlib import Path
import json,gzip,hashlib,sys
from flint import arb,acb,ctx

ctx.prec=2048
RESULTS=Path(__file__).resolve().parents[1]/'results'
def rational(pair):return arb(pair[0])/arb(pair[1])
def complex_value(pair):
    if isinstance(pair,acb):
        if not pair.is_finite():raise ValueError('Nonfinite measurement')
        return pair
    if len(pair)!=2:raise ValueError('Expected [real, imaginary]')
    z=acb(arb(pair[0]),arb(pair[1]))
    if not z.is_finite():raise ValueError('Nonfinite measurement')
    return z

class Observer:
    def __init__(self,manifest_path=RESULTS/'finite-cubic-observer.json',precision_bits=2048):
        if not isinstance(precision_bits,int) or not 64<=precision_bits<=16384:
            raise ValueError('precision_bits must be an integer in [64,16384]')
        ctx.prec=precision_bits
        self.precision_bits=precision_bits
        manifest_path=Path(manifest_path)
        self.manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        raw=(manifest_path.parent/self.manifest['cell_file']).read_bytes()
        if hashlib.sha256(raw).hexdigest()!=self.manifest['cell_file_sha256']:
            raise ValueError('Filter checksum mismatch')
        payload=json.loads(gzip.decompress(raw))
        self.cells=payload['cells'];self.den=payload['dyadic_denominator']
        if len(self.cells)!=self.manifest['positive_frequency_cells']:
            raise ValueError('Cell count mismatch')
        self.coefficients={k:rational(v) for k,v in self.manifest['coefficients_per_w_squared'].items()}
        self.norm_bound=abs(self.coefficients['crossed'])
        assert self.norm_bound>abs(self.coefficients['positive'])

    def feature(self,bulk,endpoint,weak_residual,weak_even):
        """bulk[channel][cell]=[positive_cell_integral,negative_cell_integral].

        Each cell integral is [real,imag]. These are integrals, not averages.
        Complex data at opposite frequencies are independent inputs.
        """
        ctx.prec=self.precision_bits
        if len(bulk)!=2 or any(len(b)!=len(self.cells) for b in bulk):
            raise ValueError('Two complete bulk cell-integral arrays required')
        value=acb(0)
        for channel in range(2):
            total=acb(0)
            for row,measurements in zip(self.cells,bulk[channel]):
                if len(measurements)!=2:raise ValueError('Both frequency signs required')
                r=acb(arb(row[2+2*channel])/self.den,arb(row[3+2*channel])/self.den)
                total+=r.conjugate()*complex_value(measurements[0])+r*complex_value(measurements[1])
            value+=total/(2*arb.pi()*rational(self.manifest['bulk_normalizers'][channel]))
        if len(endpoint)!=2:raise ValueError('Two endpoint coordinates required')
        for c,v in zip(self.manifest['endpoint_direction'],endpoint):
            value+=rational(c)*complex_value(v)/rational(self.manifest['endpoint_normalizer'])
        value+=rational(self.manifest['weak_multiplier'])*(complex_value(weak_residual)+complex_value(weak_even))
        return value

    def finite_rank_tensor(self,terms):
        """terms=(complex coefficient, left-feature dict, right-feature dict).

        This evaluates a supplied finite-rank ordered tensor, NOT the product
        of its marginal readings. Any tensor approximation error is external.
        """
        ctx.prec=self.precision_bits
        return sum((complex_value(c)*self.feature(**left)*self.feature(**right)
                    for c,left,right in terms),acb(0))

    def evaluate(self,values,total_joint_l1_error='0',conjugate=True):
        ctx.prec=self.precision_bits
        if len(values)!=len(self.manifest['rows']):raise ValueError('Expected 449 joint filter readings')
        error=arb(total_joint_l1_error)
        if not error.is_finite() or not error>=0:raise ValueError('Nonnegative error budget required')
        value=acb(0)
        for row,z in zip(self.manifest['rows'],values):
            value+=row['sign']*self.coefficients[row['coefficient']]*complex_value(z)
        if conjugate:value=value.conjugate()
        radius=self.norm_bound*error
        box=arb(0).union(radius).union(-radius)
        return {'value_per_w_squared':str(value),
                'acquisition_error_bound_per_w_squared':str(radius),
                'arithmetic_radius_upper_per_w_squared':str(value.real.rad()+value.imag.rad()),
                'precision_bits':ctx.prec,
                'measurement_enclosure_per_w_squared':str(value+acb(box,box)),
                'scope':'Encloses the rational finite-filter observer on the true input if the supplied joint integral error budget holds. Source calibration defects are separate.'}

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit(__doc__)
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    print(json.dumps(Observer(precision_bits=data.get('precision_bits',2048)).evaluate(data['joint_filter_values'],
                                        data.get('total_joint_l1_error','0'),
                                        data.get('conjugate',True)),indent=2))
