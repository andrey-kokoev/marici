import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

export const sourcePath='research/kitaev/isotope-electron-shells.html';
export const targetPath='research/matter/isotope-reference.resource.json';
const root=fileURLToPath(new URL('../',import.meta.url));

// Parse only the two simple string dictionaries, without executing the page.
function dictionary(html,name){
 const body=html.match(new RegExp(`const ${name} = \\{([\\s\\S]*?)\\};`))?.[1];
 if(body===undefined)throw new Error(`Missing ${name}`);
 const pattern=/'([^']+)'\s*:\s*'([^']*)'/g,entries=[...body.matchAll(pattern)].map(m=>m.slice(1));
 if(body.replace(pattern,'').replace(/[\s,]/g,''))throw new Error(`Unsupported syntax in ${name}`);
 if(new Set(entries.map(e=>e[0])).size!==entries.length)throw new Error(`Duplicate key in ${name}`);
 return Object.fromEntries(entries);
}
export function extractIsotopeReference(html){
 const abundances=dictionary(html,'abundancePercent'),exceptions=dictionary(html,'stabilityExceptions');
 const body=html.match(/<tbody id="isotope-body">([\s\S]*?)<\/tbody>/)?.[1];
 if(!body)throw new Error('Missing isotope table');
 const integer=text=>{if(!/^\d+$/.test(text))throw new Error(`Invalid integer: ${text}`);return Number(text);};
 const rows=[...body.matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(([,row])=>{
  const cells=[...row.matchAll(/<(?:th|td)\b[^>]*>([^<]*)<\/(?:th|td)>/g)].map(m=>m[1].trim());
  if(cells.length!==9)throw new Error(`Expected nine source cells: ${row}`);
  const [name,z,n,...shells]=cells;
  if(!/^[A-Za-z]+-\d+$/.test(name))throw new Error(`Unsupported isotope name: ${name}`);
  const abundance=abundances[name];
  if(abundance!==undefined&&!/^\d+(?:\.\d+)?$/.test(abundance))throw new Error(`Invalid abundance for ${name}`);
  return [name,integer(z),integer(n),...shells.map(v=>v==='—'?null:integer(v)),abundance===undefined?null:Number(abundance),abundance===undefined?'Not assessed':exceptions[name]??'Stable'];
 }).sort((a,b)=>a[1]-b[1]||a[2]-b[2]);
 const names=new Set(rows.map(row=>row[0]));
 if(!rows.length||names.size!==rows.length)throw new Error('Empty table or duplicate isotope');
 for(const name of [...Object.keys(abundances),...Object.keys(exceptions)])if(!names.has(name))throw new Error(`Orphan metadata: ${name}`);
 for(const row of rows){if(row[1]+row[2]!==Number(row[0].split('-')[1]))throw new Error(`Mass-number mismatch: ${row[0]}`);if(row.slice(3,9).reduce((sum,v)=>sum+(v??0),0)!==row[1])throw new Error(`Electron-count mismatch: ${row[0]}`);if(row[9]!==null&&(row[9]<0||row[9]>100))throw new Error(`Abundance outside [0,100]: ${row[0]}`);}
 return {
  profile:'tabular-data-resource',name:'isotope-reference',title:'Isotope and electron-shell reference',
  description:'Extraction of the repository HTML reference, independent of proposed geometric models. Selected isotopes only; not a complete nuclide evaluation.',
  dialect:{header:false},
  sources:[
   {title:'Repository isotope reference (extraction source)',path:'../kitaev/isotope-electron-shells.html'},
   {title:'NIST representative isotopic compositions (cited by the HTML)',path:'https://physics.nist.gov/PhysRefData/Compositions/index.html'},
   {title:'IAEA LiveChart / ENSDF stability (cited by the HTML)',path:'https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html'}
  ],
  provenance:{sourceFile:sourcePath,sourceSha256:createHash('sha256').update(html).digest('hex'),generator:'scripts/extract-isotope-reference.mjs',verification:'Repository extraction only. Upstream sources were not fetched or independently revalidated by this extraction.'},
  notes:[
   'Natural abundance is percent of an element’s atoms, not percent of all matter. Uncertainties were omitted in the HTML; none are invented here.',
   'Natural compositions vary between samples, particularly hydrogen, helium, lithium, boron and lead. Selected isotope rows need not sum to 100 percent.',
   'Stable means no radioactive decay observed, not a proven infinite lifetime. Lead-204 retains the reported half-life lower limit, not a measured decay lifetime.',
   'An em dash in an electron-shell column is exported as null; zero occupancy is not imputed.',
   'unit and sourceRef on schema fields, and provenance and notes on this resource, are extension metadata. Other fields use Frictionless vocabulary.',
   'Spin/parity, binding energies, radii and moments are absent from the source HTML and are not added by this extraction.'
  ],
  schema:{fields:[
   {name:'isotope',title:'Nucleus',type:'string',constraints:{required:true,pattern:'^[A-Za-z]+-[0-9]+$'},description:'Full element name and mass number as recorded in the HTML; not the editor shorthand ID.'},
   {name:'protons',title:'Protons',type:'integer',constraints:{required:true,minimum:1}},
   {name:'neutrons',title:'Neutrons',type:'integer',constraints:{required:true,minimum:0}},
   ...[2,8,18,32,50,72].map((maximum,i)=>({name:`electron_shell_${i+1}`,title:`Shell ${i+1} ≤${maximum}`,type:'integer',constraints:{minimum:0,maximum},description:'Neutral-atom electron population; null preserves a source em dash.'})),
   {name:'natural_abundance_percent',title:'Natural abundance (%)',type:'number',unit:'%',constraints:{minimum:0,maximum:100},sourceRef:'https://physics.nist.gov/PhysRefData/Compositions/index.html',description:'Representative composition; source uncertainties omitted. Null means unavailable.'},
   {name:'nuclear_stability',title:'Nuclear stability',type:'string',constraints:{required:true},sourceRef:'https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html',description:'Exact display wording, including the Pb-204 half-life lower-limit qualifier.'}
  ],primaryKey:'isotope',missingValues:['']},
  data:rows
 };
}
export function serializeResource({data,...descriptor}){
 return JSON.stringify(descriptor,null,2).slice(0,-2)+',\n  "data": [\n'+data.map(row=>'    '+JSON.stringify(row)).join(',\n')+'\n  ]\n}\n';
}
export async function prepare({check=false}={}){
 const html=await readFile(path.join(root,sourcePath),'utf8'),resource=extractIsotopeReference(html),expected=serializeResource(resource),target=path.join(root,targetPath);
 if(check){if(await readFile(target,'utf8')!==expected)throw new Error(`Stale ${targetPath}; run node scripts/extract-isotope-reference.mjs`);}else await writeFile(target,expected);
 return {path:targetPath,rows:resource.data.length,elements:new Set(resource.data.map(r=>r[1])).size,check};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(await prepare({check:process.argv.includes('--check')}));
