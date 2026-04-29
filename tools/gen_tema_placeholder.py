#!/usr/bin/env python3
"""Genera placeholders HTML para temas pendientes en gorka-quimica."""
import os

TEMAS = {
    1: ("Conceptos generales", "Materia · Mol · Composición · Estequiometría",
        ["1.1 Materia y sus propiedades","1.2 Mezclas y sustancias puras","1.3 El mol","1.4 Fórmulas químicas","1.5 Reacciones y estequiometría"]),
    2: ("Estructura atómica", "Átomo · Configuración electrónica · Tabla periódica",
        ["2.1 Modelos atómicos","2.2 Números cuánticos","2.3 Configuración electrónica","2.4 Tabla periódica","2.5 Propiedades periódicas"]),
    3: ("Enlace químico", "Iónico · Covalente · Metálico · Intermoleculares",
        ["3.1 Enlace iónico","3.2 Enlace covalente","3.3 Enlace metálico","3.4 Fuerzas intermoleculares"]),
    4: ("Estados de la materia", "Sólido · Líquido · Gaseoso · Cambios de estado",
        ["4.1.1 Estado sólido","4.1.2 Estado gaseoso","4.1.3 Estado líquido","4.2 Cambios de estado y curva de calentamiento"]),
    6: ("Termoquímica", "Entalpía · Hess · Combustión · Disolución · Variación con T",
        ["6.1 Entalpía","6.2 Cálculo de la entalpía estándar de reacción","6.3 Entalpía de combustión","6.4 Entalpía de disolución","6.5 Variación de la entalpía con la temperatura","6.6 Entalpía de cambio de estado"]),
    7: ("Espontaneidad y energía libre", "Entropía · 2ª/3ª ley · Gibbs",
        ["7.1 Procesos espontáneos","7.2 Entropía","7.3 Segunda ley","7.4 Tercera ley","7.5 Variación de entropía en reacciones","7.6 Energía libre de Gibbs"]),
    8: ("Cinética y equilibrio químico", "Velocidad · Kp/Kc · Le Châtelier",
        ["8.1 Cinética química","8.2 Equilibrio químico","8.3 El principio de Le Châtelier"]),
    9: ("Equilibrio ácido-base", "pH · Sales · Tampones · Valoraciones",
        ["9.1 Introducción","9.2 Ácidos y bases fuertes","9.3 Ácidos y bases débiles","9.4 Sales","9.5 Disoluciones reguladoras","9.6 Valoraciones"]),
}

NAV_PREV = {1:None, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8}
NAV_NEXT = {1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:None}

TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0a0e1a">
<title>T{N} · {TITULO} · Química</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="initKatex && initKatex()"></script>
<link rel="stylesheet" href="../shared/quimica.css">
<style>
body{{padding-top:52px;min-height:100vh;overflow-x:hidden;font-size:15px;line-height:1.65}}
.layout{{display:flex;min-height:calc(100vh - 52px)}}
.sidebar{{width:260px;flex-shrink:0;position:fixed;top:52px;left:0;bottom:0;background:rgba(255,255,255,.025);border-right:1px solid var(--line);overflow-y:auto;padding:12px 8px}}
.sb-head{{padding:8px 12px 12px;border-bottom:1px solid var(--line);margin-bottom:8px}}
.sb-subtitle{{font-family:var(--mono);font-size:.62em;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--txt3);margin-bottom:4px}}
.sb-current{{font-size:.78em;font-weight:600;color:var(--violet)}}
.sb-section{{padding:6px 10px;font-family:var(--mono);font-size:.62em;font-weight:700;color:var(--txt3);letter-spacing:.12em;text-transform:uppercase;margin-top:8px}}
.sb-link{{display:block;padding:7px 10px;font-size:.82em;color:var(--txt2);border-radius:6px;text-decoration:none;margin-bottom:1px;border-left:2px solid transparent;transition:.15s}}
.sb-link:hover{{background:rgba(255,255,255,.04);color:var(--txt);text-decoration:none}}
.sb-link.active{{background:rgba(var(--vr),.12);color:var(--violet);border-left-color:var(--violet);font-weight:600}}
.content{{flex:1;margin-left:260px;padding:32px 48px 60px;max-width:1100px}}
@media(max-width:900px){{.sidebar{{display:none}}.content{{margin-left:0;padding:20px 16px 40px}}}}
.t-head{{margin-bottom:28px;padding:18px 22px;background:linear-gradient(135deg,rgba(var(--vr),.08) 0%,transparent 60%);border:1px solid var(--line-v);border-left:3px solid var(--violet);border-radius:0 12px 12px 0}}
.t-tag{{font-family:var(--mono);font-size:.66em;font-weight:700;color:var(--violet);letter-spacing:.18em;text-transform:uppercase;margin-bottom:4px}}
.t-title{{font-family:var(--ui);font-size:1.6em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em}}
.t-meta{{font-family:var(--mono);font-size:.78em;color:var(--txt3);margin-top:6px}}
.placeholder{{padding:40px 30px;text-align:center;background:var(--s1);border:1px dashed var(--line-v);border-radius:12px;color:var(--txt2)}}
.placeholder h2{{font-family:var(--ui);color:var(--violet);font-size:1.2em;margin-bottom:10px}}
.placeholder ul{{display:inline-block;text-align:left;margin-top:14px;color:#cbd5e1;font-size:.92em}}
.placeholder li{{margin:5px 0;list-style:square}}
</style>
</head>
<body>

<nav class="topbar">
  <a class="topbar-back" href="../index.html">
    <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
      <path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    Inicio
  </a>
  <span class="topbar-title">Química · T{N} <em>· {TITULO}</em></span>
</nav>

<div class="layout">

  <aside class="sidebar">
    <div class="sb-head">
      <div class="sb-subtitle">Tema actual</div>
      <div class="sb-current">T{N} · {TITULO_CORTO}</div>
    </div>
    <div class="sb-section">Secciones</div>
{LINKS_SECCIONES}
    <div class="sb-section">Otros temas</div>
{NAV_TEMAS}
    <div class="sb-section">Recursos</div>
    <a class="sb-link" href="../formulario.html">📐 Formulario</a>
    <a class="sb-link" href="../ejercicios/tema{N}.html">📝 Ejercicios T{N}</a>
  </aside>

  <main class="content">

    <div class="t-head">
      <div class="t-tag">Tema 0{N}</div>
      <h1 class="t-title">{TITULO}</h1>
      <div class="t-meta">{META}</div>
    </div>

    <div class="placeholder">
      <h2>📚 Contenido en preparación</h2>
      <p>Este tema cubrirá los siguientes apartados según el material del profesor:</p>
      <ul>
{LISTA_SECCIONES}
      </ul>
      <p style="margin-top:18px;font-size:.86em;color:var(--txt3)">
        Mientras tanto puedes consultar el <a href="../formulario.html" style="color:var(--violet);font-weight:600">formulario</a>
        o los <a href="../ejercicios/index.html" style="color:var(--violet);font-weight:600">ejercicios</a>.
      </p>
    </div>

  </main>

</div>

<footer class="qg-footer">
  Química · 1º Grado · 2025-26 &nbsp;·&nbsp; <a href="../index.html">Inicio</a>
</footer>

<script>
function initKatex(){{
  if(typeof renderMathInElement === 'undefined') return;
  renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'$',right:'$',display:false}},{{left:'\\\\(',right:'\\\\)',display:false}}],throwOnError:false}});
}}
document.addEventListener('DOMContentLoaded',initKatex);
</script>
</body>
</html>
"""

OUT = os.path.join(os.path.dirname(__file__), '..', 'teoria')

for n, (titulo, meta, secciones) in TEMAS.items():
    titulo_corto = titulo if len(titulo) <= 22 else titulo[:22]
    links = '\n'.join([f'    <a class="sb-link" href="#sec-{i+1}">{s}</a>' for i,s in enumerate(secciones)])
    lista = '\n'.join([f'        <li>{s}</li>' for s in secciones])
    nav_lines = []
    if NAV_PREV[n]: nav_lines.append(f'    <a class="sb-link" href="tema{NAV_PREV[n]}.html">← T{NAV_PREV[n]}</a>')
    if NAV_NEXT[n]: nav_lines.append(f'    <a class="sb-link" href="tema{NAV_NEXT[n]}.html">→ T{NAV_NEXT[n]}</a>')
    nav = '\n'.join(nav_lines) if nav_lines else '    <span style="color:var(--txt3);padding:7px 10px;font-size:.78em">—</span>'

    html = (TEMPLATE
        .replace('{N}', str(n))
        .replace('{TITULO_CORTO}', titulo_corto)
        .replace('{TITULO}', titulo)
        .replace('{META}', meta)
        .replace('{LINKS_SECCIONES}', links)
        .replace('{LISTA_SECCIONES}', lista)
        .replace('{NAV_TEMAS}', nav)
    )
    path = os.path.join(OUT, f'tema{n}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generado tema{n}.html — {titulo}")
