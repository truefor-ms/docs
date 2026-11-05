#!/usr/bin/env python3
"""Run from any directory with Python 3. Uses the standard library only."""
from pathlib import Path
import json, hashlib, re, struct, xml.etree.ElementTree as E
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1];NS='{http://www.w3.org/2000/svg}';checks=[]
def check(name,condition):
 if not condition:raise AssertionError(name)
 checks.append(name)
def geometry(r):
 return {'viewBox':r.get('viewBox'),'paths':[e.get('d') for e in r.iter(NS+'path')],'transforms':[e.get('transform') for e in r.iter() if e.get('transform')],'stroke':[e.get('stroke-width') for e in r.iter() if e.get('stroke-width')]}
for v in ['a','b']:
 src=ROOT/'source-reference'/f'approved-{v}.svg';ref=E.parse(src).getroot()
 alias=ROOT/'assets/svg'/('trueforms-logo.svg' if v=='b' else 'trueforms-logo-alt-a.svg')
 check(f'{v} alias bytes',src.read_bytes()==alias.read_bytes())
 for mode in ['color','dark','mono','black','white','currentcolor']:
  f=ROOT/'assets/svg'/f'trueforms-logo-{v}-{mode}.svg';r=E.parse(f).getroot();check(f'{v}/{mode} geometry',geometry(r)==geometry(ref))
  expected={'mono':'#183C32','black':'#000000','white':'#FFFFFF','currentcolor':'currentColor'}.get(mode)
  if expected:
   paints={el.get(a) for el in r.iter() for a in ['fill','stroke'] if el.get(a) not in [None,'none']};check(f'{v}/{mode} single color',paints=={expected})
 for mode in ['color','dark','mono','black','white']:
  for width in [1200,2400]:
   p=ROOT/'assets/png'/f'trueforms-logo-{v}-{mode}-{width}.png';b=p.read_bytes();w,h=struct.unpack('>II',b[16:24]);check(p.name+' dimensions',w==width and h==round(width*100.895/619.5523611111))
for p in (ROOT/'assets/svg').glob('*.svg'):
 r=E.parse(p).getroot();check(p.name+' vector only',not any(e.tag in [NS+'image',NS+'text',NS+'script',NS+'foreignObject'] for e in r.iter()))
for p in ROOT.rglob('*.json'):json.loads(p.read_text())
class Links(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.anchors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for name in ['href','src']:
   if name not in a:continue
   u=a[name]
   if u.startswith('#'):self.anchors.append(u[1:])
   elif u and not u.startswith(('data:','http:','https:','/','mailto:')):self.refs.append(u)
for p in [ROOT/'trueforms-logo-master-spec.html',*[ROOT/'examples'/f for f in ['index.html','light.html','dark.html','monochrome.html','email-header.html']]]:
 l=Links();l.feed(p.read_text());check(p.name+' references',all((p.parent/u).is_file() for u in l.refs));check(p.name+' ids',len(l.ids)==len(set(l.ids)));check(p.name+' anchors',all(a in l.ids for a in l.anchors))
css=(ROOT/'tokens/trueforms.css').read_text();check('font URLs',all((ROOT/'tokens'/u).is_file() for u in re.findall(r'url\("([^"]+)"\)',css)))
for x in json.loads((ROOT/'specs/source-provenance.json').read_text())['files']:check(x['path']+' source hash',hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'])
check('A/B font shapes match',[e.get('d') for e in E.parse(ROOT/'source-reference/approved-a.svg').getroot().find(NS+"g[@id='trueforms-wordmark']")]==[e.get('d') for e in E.parse(ROOT/'source-reference/approved-b.svg').getroot().find(NS+"g[@id='trueforms-wordmark']")])
manifest=ROOT/'MANIFEST.sha256'
if manifest.exists():
 for line in manifest.read_text().splitlines():
  digest,relative=line.split('  ',1);check('manifest '+relative,hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()==digest)
print(json.dumps({'status':'passed','checks':len(checks),'items':checks},ensure_ascii=False,indent=2))
