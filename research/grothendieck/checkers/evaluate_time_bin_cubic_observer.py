"""Finite-time hat-integral receiver for the certified cubic observer.

CLI input is 449 joint_filter_values, total_joint_l1_error, optional precision_bits
and conjugate. Python feature/joint_filter APIs consume bounded hat integrals,
not point samples. All final values are per physical w_seam^2.
"""
from pathlib import Path
import importlib.util,json,hashlib,sys
from flint import arb,acb,ctx

spec=importlib.util.spec_from_file_location('base_receiver',Path(__file__).with_name('evaluate_finite_cubic_observer.py'))
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)

class TimeBinObserver(base.Observer):
    def __init__(self,manifest_path=base.RESULTS/'time-bin-cubic-observer.json',precision_bits=2048):
        if not isinstance(precision_bits,int) or not 64<=precision_bits<=16384:
            raise ValueError('precision_bits must be an integer in [64,16384]')
        self.precision_bits=precision_bits;ctx.prec=precision_bits
        path=Path(manifest_path);raw=path.read_bytes()
        certificate=json.loads(path.with_name('time-bin-cubic-observer-certificate.json').read_text(encoding='utf-8'))
        if hashlib.sha256(raw).hexdigest()!=certificate['manifest_sha256']:
            raise ValueError('Manifest does not match its certificate')
        self.manifest=json.loads(raw);self.filters=self.manifest['filters'];self.bins=self.manifest['bins']
        assert len(self.filters['nodes'])==self.bins+1
        self.coefficients={k:base.rational(v) for k,v in self.manifest['coefficients_per_w_squared'].items()}
        self.norm_bound=abs(self.coefficients['crossed'])
        assert self.norm_bound>abs(self.coefficients['positive'])
        weights=[]
        for f in self.filters['bulk']+[self.filters['weak'],self.filters['weak']]:
            assert len(f['nodal_numerators'])==self.bins+1 and f['nodal_numerators'][-1]==0
            weights.extend(arb(n)/self.filters['nodal_denominator']/base.rational(f['normalizer'])
                           for n in f['nodal_numerators'][:-1])
        weights.extend(base.rational(c)/base.rational(self.filters['endpoint_normalizer'])
                       for c in self.filters['endpoint_direction'])
        self.weights=weights

    def hat(self,index,u):
        """Value of the actual finite continuous nodal measurement weight."""
        ctx.prec=self.precision_bits
        if not isinstance(index,int) or not 0<=index<self.bins:raise ValueError('Invalid hat index')
        u=arb(u);nodes=[base.rational(n) for n in self.filters['nodes']]
        if not u.is_finite():raise ValueError('Nonfinite time')
        if u<0 or u>nodes[-1]:return arb(0)
        if index and u<=nodes[index] and u>=nodes[index-1]:
            return (u-nodes[index-1])/(nodes[index]-nodes[index-1])
        if u>=nodes[index] and u<=nodes[index+1]:
            return (nodes[index+1]-u)/(nodes[index+1]-nodes[index])
        if (index and u<nodes[index-1]) or u>nodes[index+1]:return arb(0)
        # An interval crossing a break is bounded, rather than tested at its midpoint.
        return arb(0).union(arb(1))

    def feature(self,fields,endpoint):
        """fields: bulk+, reflected bulk-, weak residual, weak even (76 hats each).

        Entry j is integral_0^64 hat_j(u)*exp(-u)*f(u)du. Endpoints are
        the two existing response coordinates. No measurement at t=64 is needed.
        """
        ctx.prec=self.precision_bits
        if len(fields)!=4 or any(len(f)!=self.bins for f in fields) or len(endpoint)!=2:
            raise ValueError('Expected four complete hat-integral arrays and two endpoints')
        data=[v for f in fields for v in f]+list(endpoint)
        return sum((w*base.complex_value(z) for w,z in zip(self.weights,data)),acb(0))

    def feature_error_bound(self,absolute_errors):
        """Independent complex-modulus error bounds in flattened measurement order."""
        ctx.prec=self.precision_bits
        if len(absolute_errors)!=len(self.weights):raise ValueError('Wrong error-vector length')
        total=arb(0)
        for w,e in zip(self.weights,absolute_errors):
            e=arb(e)
            if not e.is_finite() or not e>=0:raise ValueError('Nonnegative finite error required')
            total+=abs(w)*e
        return arb(total.upper())

    def joint_filter(self,matrix,absolute_entry_error='0'):
        """Full ordered joint-integral matrix, NOT a product of marginals.

        Flattened order in each slot is the four hat arrays followed by the two
        endpoints. Error bounds refer to each matrix entry's complex modulus.
        """
        ctx.prec=self.precision_bits
        n=len(self.weights)
        if len(matrix)!=n or any(len(row)!=n for row in matrix):raise ValueError('Wrong joint matrix dimensions')
        error=arb(absolute_entry_error)
        if not error.is_finite() or not error>=0:raise ValueError('Nonnegative finite entry error required')
        value=acb(0)
        for wi,row in zip(self.weights,matrix):
            for wj,z in zip(self.weights,row):
                value+=wi*wj*base.complex_value(z)
        bound=error*sum((abs(w) for w in self.weights),arb(0))**2
        return {'value':value,'error':arb(bound.upper())}

    def evaluate_acquired(self,blocks,additional_joint_error='0',conjugate=True):
        ctx.prec=self.precision_bits
        error=arb(additional_joint_error)
        if not error.is_finite() or not error>=0:raise ValueError('Nonnegative joint error required')
        for b in blocks:
            e=arb(b['error'])
            if not e.is_finite() or not e>=0:raise ValueError('Invalid block error')
            error+=e
        result=self.evaluate([b['value'] for b in blocks],arb(error.upper()),conjugate)
        rounding=arb(result['arithmetic_radius_upper_per_w_squared'].replace('[','').replace(']',''))
        total=error+rounding/arb(self.norm_bound.lower())
        result['total_error_in_joint_norm_units']=str(total)
        result['meets_1e_minus540_budget']=bool(total<=arb('1e-540'))
        return result

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit(__doc__)
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    o=TimeBinObserver(precision_bits=data.get('precision_bits',2048))
    print(json.dumps(o.evaluate(data['joint_filter_values'],data.get('total_joint_l1_error','0'),
                               data.get('conjugate',True)),indent=2))
