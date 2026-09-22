"""Conditional finite-time acquisition for the existing finite cubic filter.

Samples are of DAMPED fields g(u)=exp(-u)f(u). Field L2, sup and total
variation budgets are external hypotheses, not inferred from samples.
"""
from pathlib import Path
import importlib.util,json,math
from flint import arb,acb,ctx

spec=importlib.util.spec_from_file_location('finite_receiver',Path(__file__).with_name('evaluate_finite_cubic_observer.py'))
receiver=importlib.util.module_from_spec(spec);spec.loader.exec_module(receiver)

def nonnegative(x):
    x=arb(x)
    if not x.is_finite() or not x>=0:raise ValueError('Expected finite nonnegative bound')
    return x

def upper(x):return arb(x.upper())
def smaller_bound(a,b):return a if float(a.upper())<float(b.upper()) else b

class Acquisition:
    def __init__(self,observer=None):
        self.observer=observer or receiver.Observer()
        self.bounds=None

    def certify_kernel_bounds(self):
        ctx.prec=128
        o=self.observer;out=[]
        for channel in range(2):
            mass=arb(0);moment=arb(0);variation=arb(0);squared=arb(0);previous=None
            previous_end=arb(0)
            for row in o.cells:
                j,rate=row[:2];a=arb(j)/rate;b=arb(j+1)/rate
                assert a==previous_end and b>a
                previous_end=b
                r=acb(arb(row[2+2*channel])/o.den,arb(row[3+2*channel])/o.den)
                mass+=(b-a)*abs(r)
                moment+=(b*b-a*a)*abs(r)/2
                squared+=(b-a)*(r.real*r.real+r.imag*r.imag)
                if previous is None:variation+=abs(r.imag)
                else:variation+=abs(r-previous)
                previous=r
            variation+=abs(previous)
            nu=receiver.rational(o.manifest['bulk_normalizers'][channel])
            assert squared/(arb.pi()*nu*nu)<1
            values={'sup':mass/(arb.pi()*nu),'derivative_sup':moment/(arb.pi()*nu),
                    'tail_prefactor':variation/(arb.pi()*nu)}
            rounded={}
            for name,value in values.items():
                n=math.ceil(float(value.upper())*10**9)+2
                assert arb(n)/10**9>value
                rounded[name]=[str(n),str(10**9)]
            out.append(rounded)
        self.bounds=out
        return {'schema':'marici.grothendieck.sampled-filter-kernels.v1',
                'filter_sha256':o.manifest['cell_file_sha256'],
                'bulk_normalizers':o.manifest['bulk_normalizers'],'bulk':out,
                'meaning':'|k|<=sup, |k_prime|<=derivative_sup, L2(k on [H,infinity))<=tail_prefactor/sqrt(H)',
                'assumption':'original verified finite filter manifest and rational normalizers'}

    def load_kernel_bounds(self,path=None):
        path=path or receiver.RESULTS/'finite-cubic-acquisition-kernels.json'
        data=json.loads(Path(path).read_text(encoding='utf-8'))
        if (data['filter_sha256']!=self.observer.manifest['cell_file_sha256'] or
            data['bulk_normalizers']!=self.observer.manifest['bulk_normalizers']):
            raise ValueError('Stale kernel certificate')
        self.bounds=data['bulk']

    def kernel(self,channel,u):
        o=self.observer;u=nonnegative(u)
        if channel=='weak':return receiver.rational(o.manifest['weak_multiplier'])*(-4*u).exp()
        if channel not in (0,1):raise ValueError('Unknown channel')
        nu=receiver.rational(o.manifest['bulk_normalizers'][channel]);total=arb(0)
        for row in o.cells:
            j,rate=row[:2]
            r=acb(arb(row[2+2*channel])/o.den,arb(row[3+2*channel])/o.den)
            if u.is_zero():integral=acb(arb(1)/rate)
            else:
                z=acb(0,-u)
                integral=((z*(arb(j+1)/rate)).exp()-(z*(arb(j)/rate)).exp())/z
            total+=(r.conjugate()*integral).real
        return total/(arb.pi()*nu)

    def sample_field(self,channel,samples,start,step,l2_bound,sup_bound,
                     variation_bound,sample_error='0',tail_l2_bound=None,head_l2_bound=None):
        """Composite midpoint rule on [start,start+len(samples)*step].

        variation_bound is total variation of the actual chosen damped-field
        representative on that interval, including jumps. sample_error bounds
        EACH complex sample error. Optional head/tail budgets bound field L2
        mass outside the interval and require independent justification.
        """
        ctx.prec=self.observer.precision_bits
        a=nonnegative(start);d=nonnegative(step)
        if not samples or not d>0:raise ValueError('Nonempty samples and positive step required')
        H=a+len(samples)*d
        B=nonnegative(l2_bound);G=nonnegative(sup_bound);V=nonnegative(variation_bound)
        sigma=nonnegative(sample_error)
        if channel=='weak':
            m0=receiver.rational(self.observer.manifest['weak_multiplier']);m1=4*m0
            tail=m0*(-4*H).exp()/arb(8).sqrt()
        else:
            if channel not in (0,1) or self.bounds is None:raise ValueError('Certify/load bulk kernel bounds first')
            m0=receiver.rational(self.bounds[channel]['sup'])
            m1=receiver.rational(self.bounds[channel]['derivative_sup'])
            tail=receiver.rational(self.bounds[channel]['tail_prefactor'])/H.sqrt()
        head_error=m0*a.sqrt()*B
        tail_error=smaller_bound(tail*B,B)
        if head_l2_bound is not None:head_error=smaller_bound(head_error,nonnegative(head_l2_bound))
        if tail_l2_bound is not None:tail_error=smaller_bound(tail_error,nonnegative(tail_l2_bound))
        quadrature=d*(m0*V+m1*G*(H-a))
        sampled=(H-a)*m0*sigma
        value=acb(0)
        for j,z in enumerate(samples):
            value+=d*self.kernel(channel,a+(arb(j)+arb(1)/2)*d)*receiver.complex_value(z)
        error=upper(head_error+tail_error+quadrature+sampled)
        if not value.is_finite():raise ValueError('Nonfinite quadrature enclosure')
        return {'value':value,'error':error,'norm_bound':B,
                'error_terms':{'head':upper(head_error),'tail':upper(tail_error),
                               'quadrature':upper(quadrature),'samples':upper(sampled)},
                'conditional_on':'sup, variation, L2 and pointwise sample-error hypotheses for the actual damped field'}

    def feature(self,fields,endpoint,endpoint_error='0'):
        """fields: bulk+, bulk-, residual, even acquisitions, in that order."""
        if len(fields)!=4 or len(endpoint)!=2:raise ValueError('Four fields and two endpoints required')
        o=self.observer
        E=nonnegative(endpoint_error)
        ev=[receiver.complex_value(x) for x in endpoint]
        e_norm=(abs(ev[0])**2+abs(ev[1])**2).sqrt()+E
        value=sum((v['value'] for v in fields),acb(0))
        for direction,z in zip(o.manifest['endpoint_direction'],ev):
            value+=receiver.rational(direction)*z/receiver.rational(o.manifest['endpoint_normalizer'])
        return {'value':value,'error':upper(sum((v['error'] for v in fields),E)),
                'norm_bound':upper(sum((v['norm_bound'] for v in fields),e_norm))}

    @staticmethod
    def tensor(terms,projective_remainder='0'):
        """terms=(exact coefficient, left acquired feature, right acquired feature).

        Requires a genuine finite-rank decomposition/approximation; never
        substitutes products of marginal data for a joint tensor measurement.
        """
        value=acb(0);error=nonnegative(projective_remainder)
        for coefficient,left,right in terms:
            c=receiver.complex_value(coefficient)
            value+=c*left['value']*right['value']
            el,er=left['error'],right['error']
            error+=abs(c)*(left['norm_bound']*er+right['norm_bound']*el+el*er)
        return {'value':value,'error':upper(error)}

    def evaluate(self,blocks,additional_joint_error='0',conjugate=True):
        error=upper(sum((b['error'] for b in blocks),nonnegative(additional_joint_error)))
        result=self.observer.evaluate([b['value'] for b in blocks],error,conjugate)
        result['conditional_joint_acquisition_error']=str(error)
        rounding=arb(result['arithmetic_radius_upper_per_w_squared'].replace('[','').replace(']',''))
        total=upper(error+rounding/arb(self.observer.norm_bound.lower()))
        result['total_error_in_joint_norm_units']=str(total)
        result['meets_1e_minus540_budget']=bool(total<=arb('1e-540'))
        return result

if __name__=='__main__':
    a=Acquisition();result=a.certify_kernel_bounds()
    path=receiver.RESULTS/'finite-cubic-acquisition-kernels.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
