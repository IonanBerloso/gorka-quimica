"""
Generador de contenido teoría + ejercicios para gorka-quimica.

Una sola fuente de verdad para los 8 temas pendientes (T1-4, T6-9).
Genera HTML con el mismo skin que tema5 (referencia).

Uso: python tools/gen_content.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEORIA = ROOT / "teoria"
EJ = ROOT / "ejercicios"

sys.path.insert(0, str(Path(__file__).parent))
try:
    from ejercicios_extra import EJERCICIOS_EXTRA
except ImportError:
    EJERCICIOS_EXTRA = {}

# ─────────────────────────────────────────────────────────────────────
# CONTENIDO POR TEMA — Un dict gigante con todo
# ─────────────────────────────────────────────────────────────────────

TEMAS = {
    1: {
        "titulo": "Conceptos generales",
        "subtitulo": "Materia · Mol · Composición · Estequiometría",
        "secciones": [
            {
                "id": "sec-1",
                "h": "1.1. Materia: clasificación",
                "html": r"""
<p>La <strong>materia</strong> es todo aquello que tiene masa y ocupa un volumen. Se clasifica según su composición en:</p>
<ul>
  <li><strong>Sustancia pura</strong>: composición fija y propiedades constantes.
    <ul>
      <li><em>Elemento</em>: no se puede descomponer químicamente (Cu, O$_2$, He).</li>
      <li><em>Compuesto</em>: dos o más elementos combinados en proporción fija (H$_2$O, NaCl).</li>
    </ul>
  </li>
  <li><strong>Mezcla</strong>: dos o más sustancias en proporción variable.
    <ul>
      <li><em>Homogénea</em> (disolución): una sola fase visible (agua salada).</li>
      <li><em>Heterogénea</em>: distintas fases visibles (agua + aceite).</li>
    </ul>
  </li>
</ul>
<div class="concept">
  <div class="concept-label">Propiedades</div>
  <p><b>Intensivas</b>: no dependen de la cantidad de materia (densidad, $T$ de fusión, color). Son las que identifican la sustancia.</p>
  <p><b>Extensivas</b>: dependen de la cantidad (masa, volumen, energía).</p>
</div>
"""
            },
            {
                "id": "sec-2",
                "h": "1.2. El mol y el número de Avogadro",
                "html": r"""
<p>El <strong>mol</strong> es la unidad de cantidad de sustancia del SI. Un mol contiene exactamente:</p>
<div class="formula">
  <div class="formula-label">Número de Avogadro</div>
  $$N_A = 6{,}022\cdot 10^{23}\ \text{partículas/mol}$$
</div>
<p>Esto vale para átomos, moléculas, iones o electrones. La <strong>masa molar</strong> $M$ (g/mol) coincide numéricamente con la masa atómica/molecular relativa en unidades de masa atómica.</p>
<div class="formula">
  <div class="formula-label">Conversión clave</div>
  $$n = \dfrac{m}{M} \qquad N = n\cdot N_A$$
</div>
<p>$n$ = moles, $m$ = masa (g), $M$ = masa molar (g/mol), $N$ = número de partículas.</p>
"""
            },
            {
                "id": "sec-3",
                "h": "1.3. Composición porcentual y fórmulas",
                "html": r"""
<p>La <strong>composición porcentual</strong> indica el % en masa de cada elemento dentro de un compuesto:</p>
$$\%\,\text{elemento} = \dfrac{\text{masa del elemento}}{\text{masa total}}\cdot 100$$
<h3>Fórmula empírica vs. molecular</h3>
<ul>
  <li><strong>Empírica</strong>: relación entera más simple entre átomos (ej: CH$_2$O para la glucosa).</li>
  <li><strong>Molecular</strong>: número real de átomos por molécula (ej: C$_6$H$_{12}$O$_6$).</li>
</ul>
<p>Si conoces la masa molar real $M$ y la masa de la fórmula empírica $M_e$:</p>
<div class="formula">
  $$n = \dfrac{M}{M_e}\;\Rightarrow\;\text{Fórmula molecular}=(\text{empírica})_n$$
</div>
"""
            },
            {
                "id": "sec-4",
                "h": "1.4. Reacciones químicas y estequiometría",
                "html": r"""
<p>Una <strong>reacción química</strong> reordena los átomos de los reactivos para formar productos. La masa <em>se conserva</em> (Lavoisier): hay que <em>ajustar</em> la ecuación de modo que cada elemento tenga el mismo número de átomos en ambos lados.</p>
<div class="concept">
  <div class="concept-label">Procedimiento de ajuste</div>
  <ol>
    <li>Empezar por elementos que aparezcan una sola vez en cada lado.</li>
    <li>Dejar para el final O e H si solo aparecen en compuestos.</li>
    <li>Multiplicar por un denominador común si quedan fracciones.</li>
  </ol>
</div>
<h3>Cálculos estequiométricos</h3>
<p>Una vez ajustada, los <em>coeficientes</em> indican proporciones <em>en moles</em>. Para ir de gramos a moles se usa $n=m/M$, y los productos se calculan multiplicando por la relación molar.</p>
<div class="formula">
  <div class="formula-label">Esquema típico</div>
  $$g_A \xrightarrow{/M_A} \text{mol}_A \xrightarrow{\,\text{relación estequiométrica}\,} \text{mol}_B \xrightarrow{\times M_B} g_B$$
</div>
"""
            },
            {
                "id": "sec-5",
                "h": "1.5. Reactivo limitante y rendimiento",
                "html": r"""
<p>Cuando se mezclan reactivos en proporciones <em>no</em> estequiométricas, uno se agota antes que los otros: es el <strong>reactivo limitante</strong>. El que sobra es el <strong>reactivo en exceso</strong>.</p>
<div class="concept">
  <div class="concept-label">Cómo identificarlo</div>
  Para cada reactivo, calcula los moles disponibles y divídelos por su coeficiente estequiométrico. El que dé el menor valor es el limitante.
</div>
<p>El <strong>rendimiento</strong> de una reacción real raramente alcanza el 100%:</p>
<div class="formula">
  $$\eta\,(\%) = \dfrac{\text{cantidad real obtenida}}{\text{cantidad teórica}}\cdot 100$$
</div>
<div class="note"><strong>Pureza:</strong> si un reactivo no es puro (p. ej. mineral con 80% de NaCl), antes de calcular moles hay que aplicar el % de pureza a la masa total.</div>
"""
            },
        ],
        "ej": [
            {
                "title": "Cálculo del número de moléculas y átomos",
                "enunciado": r"Calcular cuántas moléculas y cuántos átomos de cada elemento hay en <b>50 g de glucosa</b> (C$_6$H$_{12}$O$_6$). Datos: $M_C=12$, $M_H=1$, $M_O=16$ g/mol.",
                "esperado": r"$1{,}67\cdot 10^{23}$ moléculas; $1{,}00\cdot 10^{24}$ átomos C; $2{,}01\cdot 10^{24}$ átomos H; $1{,}00\cdot 10^{24}$ átomos O.",
                "datos": [
                    ("Masa de glucosa", "$m=50\\ \\text{g}$"),
                    ("Fórmula molecular", "$\\text{C}_6\\text{H}_{12}\\text{O}_6$"),
                    ("Masas atómicas", "$M_C=12$, $M_H=1$, $M_O=16$ g/mol"),
                ],
                "demo": {
                    "title": "De dónde sale $N = n\\cdot N_A$",
                    "body": r"""
<p>Por <b>definición de mol</b>, una cantidad de sustancia $n$ contiene $n\cdot N_A$ partículas, donde $N_A=6{,}022\cdot 10^{23}$ es el número de Avogadro.</p>
<p>Para los átomos de cada elemento dentro de una molécula, multiplicamos por el subíndice del elemento en la fórmula:</p>
$$N_{\text{átomos elem.}} = N_{\text{moléculas}}\cdot (\text{subíndice})$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Masa molar de la glucosa",
                     "p": "Sumamos las masas atómicas pesadas por subíndices.",
                     "b": r"$$M = 6\cdot 12 + 12\cdot 1 + 6\cdot 16 = 72 + 12 + 96 = 180\ \text{g/mol}$$"},
                    {"t": "Paso 2 — Moles de glucosa",
                     "p": "$n = m/M$ es la relación fundamental.",
                     "b": r"$$n = \dfrac{50}{180} = 0{,}2778\ \text{mol}$$"},
                    {"t": "Paso 3 — Moléculas de glucosa",
                     "p": "Multiplico moles por $N_A$.",
                     "b": r"$$N = 0{,}2778\cdot 6{,}022\cdot 10^{23} = 1{,}673\cdot 10^{23}\ \text{moléculas}$$"},
                    {"t": "Paso 4 — Átomos de cada elemento",
                     "p": "Cada molécula tiene 6 C, 12 H y 6 O.",
                     "b": r"""$$N_C = 6N = 1{,}004\cdot 10^{24}$$
$$N_H = 12N = 2{,}008\cdot 10^{24}$$
$$N_O = 6N = 1{,}004\cdot 10^{24}$$"""},
                ],
                "resultado": r"$1{,}67\cdot 10^{23}$ moléculas · $\sum$ átomos $= N_C+N_H+N_O = 4{,}016\cdot 10^{24}$.",
                "verificacion": r"Los moles de C = 6·0,2778 = 1,667 mol → $1{,}667\cdot 6{,}022\cdot 10^{23}=1{,}004\cdot 10^{24}$ átomos C. ✓ Coincide con el cálculo anterior."
            },
            {
                "title": "Composición porcentual y fórmula empírica",
                "enunciado": r"Un compuesto contiene <b>40,0% C, 6,7% H y 53,3% O</b> en masa, y su masa molar es $180\ \text{g/mol}$. Determinar la fórmula empírica y la fórmula molecular.",
                "esperado": r"Empírica: CH$_2$O · Molecular: C$_6$H$_{12}$O$_6$.",
                "datos": [
                    ("% en masa", "40,0% C; 6,7% H; 53,3% O"),
                    ("Masa molar", "$M = 180\\ \\text{g/mol}$"),
                ],
                "demo": {
                    "title": "Procedimiento empírica → molecular",
                    "body": r"""
<p>Tomamos como base <b>100 g</b> de compuesto. Así los porcentajes se convierten directamente en gramos. Dividiendo por la masa atómica, obtenemos moles de cada elemento.</p>
<p>La <b>fórmula empírica</b> es la relación entera más simple entre esos moles. Para encontrarla, dividimos todos por el menor.</p>
<p>La <b>fórmula molecular</b> es múltiplo entero de la empírica:</p>
$$n = \dfrac{M_{\text{molecular}}}{M_{\text{empírica}}} \implies \text{Molecular}=(\text{empírica})_n$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Moles de cada elemento (base 100 g)",
                     "p": "Cada % se convierte directo a gramos sobre 100 g.",
                     "b": r"""$$n_C=\dfrac{40{,}0}{12}=3{,}33\quad n_H=\dfrac{6{,}7}{1}=6{,}7\quad n_O=\dfrac{53{,}3}{16}=3{,}33$$"""},
                    {"t": "Paso 2 — Relación entera (dividir por el menor)",
                     "p": "Divido todo entre 3,33.",
                     "b": r"""$$C:1\qquad H:2{,}01\approx 2\qquad O:1$$
<p>Fórmula empírica: <b>CH$_2$O</b> con $M_e = 12+2+16 = 30$ g/mol.</p>"""},
                    {"t": "Paso 3 — Fórmula molecular",
                     "p": "$n = M/M_e$.",
                     "b": r"""$$n = \dfrac{180}{30} = 6 \implies \text{Molecular} = (\text{CH}_2\text{O})_6 = \text{C}_6\text{H}_{12}\text{O}_6$$"""},
                ],
                "resultado": r"Empírica: <b>CH$_2$O</b> · Molecular: <b>C$_6$H$_{12}$O$_6$</b> (glucosa, fructosa…).",
                "verificacion": r"Comprobación: $M(\text{C}_6\text{H}_{12}\text{O}_6)=72+12+96=180$ g/mol. ✓ Coincide con el dato."
            },
            {
                "title": "Reactivo limitante y rendimiento",
                "enunciado": r"Se hacen reaccionar <b>10 g de Al</b> con <b>40 g de Cl$_2$</b> para formar AlCl$_3$. Calcular: (a) el reactivo limitante, (b) la masa teórica de AlCl$_3$, (c) el rendimiento si se obtienen experimentalmente 45 g del producto. Datos: $M_{Al}=27$, $M_{Cl}=35{,}5$ g/mol.",
                "esperado": r"(a) Al es el limitante; (b) $m_{\text{teórica}}=49{,}4$ g; (c) $\eta=91{,}1\%$.",
                "datos": [
                    ("Reacción", "$2\\,\\text{Al} + 3\\,\\text{Cl}_2 \\to 2\\,\\text{AlCl}_3$"),
                    ("Masas", "$m_{Al}=10$ g; $m_{Cl_2}=40$ g"),
                    ("Masa molar Cl$_2$", "$71$ g/mol"),
                    ("Masa molar AlCl$_3$", "$27+3\\cdot 35{,}5=133{,}5$ g/mol"),
                    ("Producto experimental", "$45$ g"),
                ],
                "demo": {
                    "title": "Identificación del limitante",
                    "body": r"""
<p>Para cada reactivo, calculamos $n/\nu$ (moles dividido entre coeficiente estequiométrico). Ese cociente representa cuántas <em>"unidades de reacción"</em> aporta cada reactivo. <b>El menor</b> es el limitante porque se acaba primero.</p>
$$\xi_i = \dfrac{n_i}{\nu_i}\;\;,\;\;\text{limitante} \Leftrightarrow \min(\xi_i)$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Moles de cada reactivo",
                     "p": "$n=m/M$.",
                     "b": r"""$$n_{Al}=\dfrac{10}{27}=0{,}370\ \text{mol}\qquad n_{Cl_2}=\dfrac{40}{71}=0{,}563\ \text{mol}$$"""},
                    {"t": "Paso 2 — Cociente estequiométrico $\\xi$",
                     "p": "Coeficientes: $\\nu_{Al}=2$, $\\nu_{Cl_2}=3$.",
                     "b": r"""$$\xi_{Al}=\dfrac{0{,}370}{2}=0{,}185\qquad \xi_{Cl_2}=\dfrac{0{,}563}{3}=0{,}188$$
<p>$\xi_{Al}<\xi_{Cl_2}$ ⟹ <b>el aluminio es el limitante</b>.</p>"""},
                    {"t": "Paso 3 — Masa teórica de AlCl$_3$",
                     "p": "Por estequiometría: 2 mol Al → 2 mol AlCl$_3$, así que $n_{AlCl_3}=n_{Al}=0{,}370$ mol.",
                     "b": r"""$$m_{\text{teórica}} = 0{,}370\cdot 133{,}5 = 49{,}4\ \text{g}$$"""},
                    {"t": "Paso 4 — Rendimiento",
                     "p": "Comparo experimental con teórico.",
                     "b": r"""$$\eta = \dfrac{45}{49{,}4}\cdot 100 = 91{,}1\%$$"""},
                ],
                "resultado": r"Limitante: <b>Al</b> · Teórico: <b>49,4 g</b> · Rendimiento: <b>91,1%</b>.",
                "verificacion": r"Cl$_2$ consumido = $1{,}5\cdot n_{Al}=0{,}555$ mol → $0{,}555\cdot 71 = 39{,}4$ g. Sobran $40-39{,}4=0{,}6$ g de Cl$_2$ ✓ (consistente con que Al es el limitante)."
            },
        ],
    },

    2: {
        "titulo": "Estructura atómica",
        "subtitulo": "Modelos · Cuántica · Orbitales · Configuración electrónica · Tabla periódica",
        "secciones": [
            {
                "id": "sec-1",
                "h": "2.1. Modelos atómicos: del clásico al cuántico",
                "html": r"""
<p>La descripción del átomo evolucionó en menos de un siglo desde un modelo clásico mecánico al modelo cuántico actual:</p>
<table class="tabla">
  <tr><th>Modelo</th><th>Año</th><th>Idea clave</th><th>Limitación</th></tr>
  <tr><td>Dalton</td><td>1808</td><td>Átomo indivisible</td><td>No explica electricidad</td></tr>
  <tr><td>Thomson</td><td>1897</td><td>"Pudín de pasas" — electrones en una matriz +</td><td>No explica dispersión $\alpha$</td></tr>
  <tr><td>Rutherford</td><td>1911</td><td>Núcleo + denso, electrones orbitando</td><td>Inestabilidad clásica</td></tr>
  <tr><td>Bohr</td><td>1913</td><td>Órbitas con energía cuantizada</td><td>Solo H</td></tr>
  <tr><td>Schrödinger</td><td>1926</td><td>Orbitales (probabilidad)</td><td>—</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Postulado de Bohr</div>
  Las órbitas estables tienen momento angular $L=n\hbar$. Cuando un electrón salta entre niveles emite/absorbe un fotón de energía:
  $$\Delta E = h\nu = E_f - E_i$$
</div>
"""
            },
            {
                "id": "sec-2",
                "h": "2.2. Dualidad onda-partícula. Heisenberg",
                "html": r"""
<p>La luz exhibe comportamiento de onda (interferencia) y de partícula (efecto fotoeléctrico). De Broglie postuló que <em>toda</em> partícula con masa lleva asociada una onda:</p>
<div class="formula">
  <div class="formula-label">Longitud de onda de De Broglie</div>
  $$\lambda = \dfrac{h}{p} = \dfrac{h}{m\,v}$$
</div>
<p>Heisenberg estableció que existe un límite fundamental al conocer simultáneamente posición y momento:</p>
<div class="formula">
  <div class="formula-label">Principio de incertidumbre</div>
  $$\Delta x\,\Delta p \ge \dfrac{\hbar}{2}$$
</div>
<div class="note"><strong>Consecuencia:</strong> ya no se habla de "trayectoria" del electrón sino de <em>orbital</em>: una región del espacio donde la probabilidad de encontrarlo es alta.</div>
"""
            },
            {
                "id": "sec-3",
                "h": "2.3. Números cuánticos y orbitales",
                "html": r"""
<p>La ecuación de Schrödinger para el átomo de H da soluciones caracterizadas por <strong>4 números cuánticos</strong>:</p>
<table class="tabla">
  <tr><th>Símbolo</th><th>Nombre</th><th>Valores</th><th>Información</th></tr>
  <tr><td>$n$</td><td>Principal</td><td>$1, 2, 3,\ldots$</td><td>Tamaño / energía</td></tr>
  <tr><td>$\ell$</td><td>Azimutal</td><td>$0,\ldots,n-1$</td><td>Forma (s,p,d,f)</td></tr>
  <tr><td>$m_\ell$</td><td>Magnético</td><td>$-\ell,\ldots,+\ell$</td><td>Orientación</td></tr>
  <tr><td>$m_s$</td><td>Espín</td><td>$\pm 1/2$</td><td>Giro intrínseco</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Notación</div>
  $\ell=0\to s$, $\ell=1\to p$, $\ell=2\to d$, $\ell=3\to f$. Cada orbital admite <b>2 electrones</b> (uno con cada espín).
</div>
<p>En cada nivel $n$ caben $2n^2$ electrones: $n=1\to 2$; $n=2\to 8$; $n=3\to 18$…</p>
"""
            },
            {
                "id": "sec-4",
                "h": "2.4. Configuración electrónica",
                "html": r"""
<p>La distribución de electrones en orbitales obedece tres reglas:</p>
<div class="concept">
  <div class="concept-label">Reglas de llenado</div>
  <ul>
    <li><b>Aufbau</b>: se llenan primero los orbitales de menor energía.</li>
    <li><b>Pauli</b>: en un orbital no puede haber dos electrones con los 4 números cuánticos iguales.</li>
    <li><b>Hund</b>: dentro de un subnivel degenerado, los electrones se colocan primero desapareados con espines paralelos.</li>
  </ul>
</div>
<p><b>Orden energético</b> (regla de Madelung — diagonal):</p>
$$1s\to 2s\to 2p\to 3s\to 3p\to 4s\to 3d\to 4p\to 5s\to 4d\to 5p\to 6s\to 4f\to 5d\to 6p\ldots$$
<div class="formula">
  <div class="formula-label">Ejemplos</div>
  <p>Fe ($Z=26$): $\ [Ar]\,4s^2\,3d^6$</p>
  <p>Cu ($Z=29$): $\ [Ar]\,4s^1\,3d^{10}$ (excepción: subnivel d semiocupado/lleno gana estabilidad).</p>
</div>
"""
            },
            {
                "id": "sec-5",
                "h": "2.5. Propiedades periódicas",
                "html": r"""
<p>La posición en la <strong>tabla periódica</strong> determina las tendencias de las propiedades atómicas:</p>
<table class="tabla">
  <tr><th>Propiedad</th><th>↑ en período</th><th>↓ en grupo</th></tr>
  <tr><td>Radio atómico</td><td>↓ disminuye</td><td>↑ aumenta</td></tr>
  <tr><td>Energía de ionización (EI)</td><td>↑ aumenta</td><td>↓ disminuye</td></tr>
  <tr><td>Afinidad electrónica (AE)</td><td>↑ aumenta (más –)</td><td>↓ disminuye</td></tr>
  <tr><td>Electronegatividad (EN)</td><td>↑ aumenta</td><td>↓ disminuye</td></tr>
  <tr><td>Carácter metálico</td><td>↓ disminuye</td><td>↑ aumenta</td></tr>
</table>
<div class="note"><strong>Por qué:</strong> al avanzar en período, sube $Z_{efectivo}$ con el mismo $n$ → núcleo atrae más → menor radio, mayor EI/EN. Al bajar de grupo aumenta $n$ → radio mayor → electrón más alejado → menor EI/EN.</div>
"""
            },
        ],
        "ej": [
            {
                "title": "Configuración electrónica del Fe y del Cu",
                "enunciado": r"Escribir la configuración electrónica completa del <b>Fe ($Z=26$)</b> y del <b>Cu ($Z=29$)</b>. Indicar los electrones desapareados en el estado fundamental.",
                "esperado": r"Fe: $[Ar]\,4s^2\,3d^6$ → 4 desapareados. Cu: $[Ar]\,4s^1\,3d^{10}$ → 1 desapareado.",
                "datos": [
                    ("$Z$ Fe", "26"),
                    ("$Z$ Cu", "29"),
                    ("Capacidad de cada subnivel", "$s$:2, $p$:6, $d$:10, $f$:14"),
                ],
                "demo": {
                    "title": "Aufbau, Hund y Pauli",
                    "body": r"""
<p>El llenado sigue la regla de Madelung. Para los metales de transición de la primera serie, el subnivel $4s$ se llena <em>antes</em> que $3d$, pero una vez ocupado, los electrones de $3d$ pueden estabilizar configuraciones especialmente estables ($d^5$, $d^{10}$). Eso explica las excepciones del Cr y del Cu.</p>
<p>Hund: en un mismo subnivel ($p$, $d$, $f$) los electrones se distribuyen primero <em>desapareados</em> con espines paralelos antes de aparearse.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Hierro: aplico orden Madelung",
                     "p": "26 e<sup>−</sup> repartidos siguiendo el orden estándar.",
                     "b": r"""$$1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6 = [Ar]\,4s^2\,3d^6$$
<p>El subnivel 3d tiene 6 electrones en 5 orbitales. Por Hund: <b>5 desapareados + 1 emparejado</b>:</p>
<p style="font-family:monospace">↑↓ ↑ ↑ ↑ ↑ → 4 electrones desapareados.</p>"""},
                    {"t": "Paso 2 — Cobre: excepción a Aufbau",
                     "p": "29 e<sup>−</sup>. La configuración Aufbau predice $[Ar]4s^2 3d^9$, pero la real es $[Ar]4s^1 3d^{10}$ porque $d^{10}$ es más estable.",
                     "b": r"""$$\text{Cu}: [Ar]\,4s^1\,3d^{10}$$
<p>El 4s queda con 1 electrón solo, el 3d completamente lleno:</p>
<p style="font-family:monospace">4s: ↑   3d: ↑↓ ↑↓ ↑↓ ↑↓ ↑↓ → <b>1 electrón desapareado</b> (en 4s).</p>"""},
                ],
                "resultado": r"Fe: $[Ar]\,4s^2\,3d^6$ con 4 e<sup>−</sup> desapareados (paramagnético, ferromagnético). Cu: $[Ar]\,4s^1\,3d^{10}$ con 1 e<sup>−</sup> desapareado.",
                "verificacion": r"Suma de e<sup>−</sup> Fe: $2+2+6+2+6+2+6=26$ ✓. Cu: $2+2+6+2+6+1+10=29$ ✓."
            },
            {
                "title": "Longitud de onda de De Broglie de un electrón",
                "enunciado": r"Calcular la longitud de onda asociada a un electrón acelerado a través de una diferencia de potencial de <b>100 V</b>. Datos: $m_e=9{,}11\cdot 10^{-31}$ kg, $h=6{,}626\cdot 10^{-34}$ J·s, $e=1{,}602\cdot 10^{-19}$ C.",
                "esperado": r"$\lambda \approx 1{,}23\cdot 10^{-10}$ m $=1{,}23$ Å.",
                "datos": [
                    ("Diferencia de potencial", "$V=100\\ \\text{V}$"),
                    ("Masa del electrón", "$m_e=9{,}11\\cdot 10^{-31}\\ \\text{kg}$"),
                    ("Constante de Planck", "$h=6{,}626\\cdot 10^{-34}\\ \\text{J·s}$"),
                    ("Carga del electrón", "$e=1{,}602\\cdot 10^{-19}\\ \\text{C}$"),
                ],
                "demo": {
                    "title": "Encadenando energía cinética y De Broglie",
                    "body": r"""
<p>El electrón acelerado por una diferencia de potencial $V$ adquiere una energía cinética igual al trabajo eléctrico:</p>
$$E_c = \tfrac{1}{2}m\,v^2 = e\,V \implies v = \sqrt{\dfrac{2eV}{m}}$$
<p>La longitud de onda de De Broglie depende del momento $p=mv$:</p>
$$\lambda = \dfrac{h}{p} = \dfrac{h}{m\,v} = \dfrac{h}{\sqrt{2\,m\,e\,V}}$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Velocidad del electrón",
                     "p": "Igualando trabajo eléctrico y energía cinética.",
                     "b": r"""$$v=\sqrt{\dfrac{2\cdot 1{,}602\cdot 10^{-19}\cdot 100}{9{,}11\cdot 10^{-31}}}=5{,}93\cdot 10^{6}\ \text{m/s}$$"""},
                    {"t": "Paso 2 — Longitud de onda",
                     "p": "$\\lambda = h/(mv)$.",
                     "b": r"""$$\lambda = \dfrac{6{,}626\cdot 10^{-34}}{9{,}11\cdot 10^{-31}\cdot 5{,}93\cdot 10^{6}} = 1{,}228\cdot 10^{-10}\ \text{m}$$"""},
                ],
                "resultado": r"$\lambda \approx 1{,}23\ \text{Å}$ — del orden de las distancias interatómicas (por eso el electrón es útil en difracción de cristales).",
                "verificacion": r"Comprobación con la fórmula directa: $\lambda=h/\sqrt{2meV}=6{,}626\cdot 10^{-34}/\sqrt{2\cdot 9{,}11\cdot 10^{-31}\cdot 1{,}602\cdot 10^{-19}\cdot 100}=1{,}23\cdot 10^{-10}$ m ✓."
            },
            {
                "title": "Energía del fotón emitido en un salto en el átomo de H",
                "enunciado": r"Calcular la longitud de onda del fotón emitido cuando un electrón del átomo de hidrógeno salta del nivel <b>$n=3$</b> al <b>$n=2$</b> (línea $H_\alpha$ de la serie de Balmer). Constante de Rydberg $R_H=1{,}097\cdot 10^{7}\ \text{m}^{-1}$.",
                "esperado": r"$\lambda \approx 656\ \text{nm}$ (rojo visible).",
                "datos": [
                    ("Salto", "$n_i=3 \\to n_f=2$"),
                    ("Constante de Rydberg", "$R_H=1{,}097\\cdot 10^{7}\\ \\text{m}^{-1}$"),
                ],
                "demo": {
                    "title": "Fórmula de Rydberg",
                    "body": r"""
<p>La energía de un nivel $n$ del H es $E_n = -R_H\,hc/n^2$. Al saltar de $n_i$ a $n_f$ con $n_f<n_i$, se emite un fotón:</p>
$$\Delta E = E_{n_i} - E_{n_f} = R_H\,hc\!\left(\dfrac{1}{n_f^2}-\dfrac{1}{n_i^2}\right)$$
<p>Como $E_{fotón}=hc/\lambda$, obtenemos la <b>fórmula de Rydberg</b>:</p>
$$\dfrac{1}{\lambda} = R_H\!\left(\dfrac{1}{n_f^2}-\dfrac{1}{n_i^2}\right)$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Sustitución",
                     "p": "Aplico la fórmula con $n_f=2$, $n_i=3$.",
                     "b": r"""$$\dfrac{1}{\lambda}=1{,}097\cdot 10^{7}\!\left(\dfrac{1}{4}-\dfrac{1}{9}\right)=1{,}097\cdot 10^{7}\cdot\dfrac{5}{36}$$"""},
                    {"t": "Paso 2 — Cálculo",
                     "p": "Desarrollo numérico.",
                     "b": r"""$$\dfrac{1}{\lambda}=1{,}524\cdot 10^{6}\ \text{m}^{-1}\implies\lambda=6{,}56\cdot 10^{-7}\ \text{m}=656\ \text{nm}$$"""},
                ],
                "resultado": r"$\lambda = 656$ nm — luz <b>roja</b> visible. Es la línea $H_\alpha$ de la serie de Balmer.",
                "verificacion": r"656 nm cae en el rojo del espectro visible (620–750 nm). Coincide con el dato experimental tabulado para la línea $H_\alpha$ ✓."
            },
        ],
    },

    3: {
        "titulo": "Enlace químico",
        "subtitulo": "Iónico · Covalente (Lewis, VSEPR, hibridación) · Metálico · Fuerzas intermoleculares",
        "secciones": [
            {
                "id": "sec-1",
                "h": "3.1. Enlace iónico",
                "html": r"""
<p>El <strong>enlace iónico</strong> se forma entre un metal (cede e<sup>−</sup>) y un no metal (gana e<sup>−</sup>): se transfieren electrones formando cationes y aniones que se mantienen unidos por <b>atracción electrostática</b> en una red cristalina.</p>
<div class="formula">
  <div class="formula-label">Energía de red (entalpía reticular)</div>
  $$U \propto -\dfrac{|q_+\cdot q_-|}{r_++r_-}$$
</div>
<p>$U$ es la energía liberada cuando se forma 1 mol de red iónica a partir de iones gaseosos. Mayor carga y menor distancia ⟹ red más estable.</p>
<div class="concept">
  <div class="concept-label">Ciclo de Born-Haber</div>
  Permite calcular $U$ aplicando la ley de Hess al proceso global:
  $$\text{M(s)} + \tfrac{1}{2}\text{X}_2(g) \to \text{MX(s)}$$
  descompuesto en sublimación, ionización, disociación, afinidad electrónica y formación de la red.
</div>
"""
            },
            {
                "id": "sec-2",
                "h": "3.2. Enlace covalente. Estructuras de Lewis",
                "html": r"""
<p>El <strong>enlace covalente</strong> se forma entre no metales: comparten pares de electrones para alcanzar configuración de gas noble (regla del <strong>octeto</strong>, dueto para H).</p>
<div class="concept">
  <div class="concept-label">Estructuras de Lewis: pasos</div>
  <ol>
    <li>Contar electrones de valencia totales (sumar grupos; restar/sumar carga si es ion).</li>
    <li>Esqueleto: el menos electronegativo en el centro (excepto H, que va siempre periférico).</li>
    <li>Distribuir pares para completar octetos (empezar por átomos terminales).</li>
    <li>Si faltan, formar enlaces múltiples desplazando pares no enlazantes.</li>
    <li>Verificar carga formal: $CF=N_v - N_{\text{libres}} - \tfrac{1}{2}N_{\text{enlazantes}}$.</li>
  </ol>
</div>
<div class="note"><strong>Excepciones al octeto:</strong> octeto incompleto (BF$_3$, BeCl$_2$), octeto expandido (PCl$_5$, SF$_6$), número impar de e<sup>−</sup> (NO, NO$_2$).</div>
"""
            },
            {
                "id": "sec-3",
                "h": "3.3. Geometría molecular: VSEPR",
                "html": r"""
<p>La <strong>teoría de repulsión de pares de e<sup>−</sup> de la capa de valencia (VSEPR)</strong> predice la geometría: los pares (enlazantes y libres) se separan al máximo alrededor del átomo central.</p>
<table class="tabla">
  <tr><th>Pares totales</th><th>Geom. electrónica</th><th>Ángulo</th><th>Ejemplo</th></tr>
  <tr><td>2</td><td>Lineal</td><td>180°</td><td>BeCl$_2$, CO$_2$</td></tr>
  <tr><td>3</td><td>Trigonal plana</td><td>120°</td><td>BF$_3$, SO$_3$</td></tr>
  <tr><td>4</td><td>Tetraédrica</td><td>109,5°</td><td>CH$_4$, NH$_3$, H$_2$O</td></tr>
  <tr><td>5</td><td>Bipirámide trig.</td><td>90°/120°</td><td>PCl$_5$</td></tr>
  <tr><td>6</td><td>Octaédrica</td><td>90°</td><td>SF$_6$</td></tr>
</table>
<div class="note"><strong>Pares libres:</strong> repelen más que los enlazantes y comprimen los ángulos. CH$_4$ tetraédrico (109,5°), NH$_3$ piramidal (107°), H$_2$O angular (104,5°).</div>
"""
            },
            {
                "id": "sec-4",
                "h": "3.4. Polaridad y momento dipolar",
                "html": r"""
<p>Un enlace es <strong>polar</strong> si los átomos enlazados tienen <em>distinta</em> electronegatividad. La diferencia $\Delta\chi$ marca la naturaleza del enlace:</p>
<table class="tabla">
  <tr><th>$\Delta\chi$</th><th>Tipo de enlace</th></tr>
  <tr><td>$<0{,}4$</td><td>Covalente apolar</td></tr>
  <tr><td>$0{,}4$ a $1{,}7$</td><td>Covalente polar</td></tr>
  <tr><td>$>1{,}7$</td><td>Iónico</td></tr>
</table>
<div class="formula">
  <div class="formula-label">Momento dipolar</div>
  $$\vec\mu = q\,\vec d \qquad [\mu]=\text{Debye}$$
</div>
<p>Una molécula es polar si la <em>suma vectorial</em> de los momentos dipolares de sus enlaces no se cancela. Por ejemplo CO$_2$ es apolar (lineal, dipolos opuestos), pero H$_2$O es polar (angular).</p>
"""
            },
            {
                "id": "sec-5",
                "h": "3.5. Fuerzas intermoleculares",
                "html": r"""
<p>Son las <em>atracciones</em> entre moléculas. Mucho más débiles que el enlace pero responsables del estado de agregación, $T_{eb}$, $T_{fus}$, etc.</p>
<table class="tabla">
  <tr><th>Tipo</th><th>Origen</th><th>Energía (kJ/mol)</th></tr>
  <tr><td>London (dispersión)</td><td>Dipolos instantáneos</td><td>0,05–40</td></tr>
  <tr><td>Dipolo-dipolo</td><td>Moléculas polares</td><td>5–25</td></tr>
  <tr><td>Puente de H</td><td>H unido a N, O, F + par libre cercano</td><td>10–40</td></tr>
  <tr><td>Ion-dipolo</td><td>Ion + molécula polar (en disolución)</td><td>40–600</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Puentes de hidrógeno</div>
  Solo entre N, O, F (átomos pequeños y muy electronegativos). Explican el alto $T_{eb}$ del agua (100 °C frente a –60 °C esperado), la solubilidad del NH$_3$ y la estructura de proteínas y ADN.
</div>
"""
            },
        ],
        "ej": [
            {
                "title": "Estructura de Lewis y geometría VSEPR del NH$_3$",
                "enunciado": r"Determinar la estructura de Lewis del <b>amoniaco NH$_3$</b>, su geometría electrónica y molecular, el ángulo de enlace H–N–H y si la molécula es polar.",
                "esperado": r"Geom. electrónica tetraédrica, geom. molecular piramidal trigonal, ángulo $\approx 107°$, molécula polar.",
                "datos": [
                    ("Electrones de valencia N", "5"),
                    ("Electrones de valencia H", "1"),
                    ("Electronegatividades (Pauling)", "$\\chi_N=3{,}04$; $\\chi_H=2{,}20$"),
                ],
                "demo": {
                    "title": "Conteo de pares y aplicación de VSEPR",
                    "body": r"""
<p>Total de electrones de valencia: $5 + 3\cdot 1 = 8$ electrones (= 4 pares).</p>
<p>Tres pares se usan para los enlaces N–H. El cuarto queda como <b>par libre</b> sobre el N.</p>
<p>VSEPR cuenta <em>todos</em> los pares para definir la geometría electrónica → tetraédrica. Pero la geometría <em>molecular</em> describe la posición de los <b>átomos</b>, así que ignora el par libre y el resultado es <b>piramidal trigonal</b>.</p>
<p>El par libre repele más que los enlazantes ⟹ comprime los ángulos H–N–H respecto del valor ideal 109,5°.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Estructura de Lewis",
                     "p": "N central; tres H periféricos.",
                     "b": r"""<p style="font-family:monospace;font-size:1.1em">H–N–H con un H abajo y un par no enlazante :↑↓ sobre N</p>
<p>Verificación octeto: N tiene 3 enlaces + 1 par = 8 e<sup>−</sup>. ✓ H tiene 2 e<sup>−</sup> (dueto). ✓</p>"""},
                    {"t": "Paso 2 — Geometría VSEPR",
                     "p": "4 pares totales sobre N.",
                     "b": r"""<p>Geometría <b>electrónica</b>: tetraédrica.<br>Geometría <b>molecular</b>: piramidal trigonal (3 H + 1 par libre).</p>"""},
                    {"t": "Paso 3 — Ángulo y polaridad",
                     "p": "El par libre comprime el ángulo, y los dipolos N–H apuntan al N (más electronegativo).",
                     "b": r"""<p>Ángulo H–N–H ≈ <b>107°</b> (menor que el ideal tetraédrico).</p>
<p>$\Delta\chi=3{,}04-2{,}20=0{,}84$ ⟹ enlace polar. Los tres dipolos $+$ el par libre suman → momento dipolar neto ≠ 0 ⟹ <b>molécula polar</b> ($\mu \approx 1{,}47$ D).</p>"""},
                ],
                "resultado": r"NH$_3$: 4 pares VSEPR → tetraédrica electrónica, <b>piramidal molecular</b>, ángulo $\approx 107°$, <b>polar</b>.",
                "verificacion": r"Coherencia: el NH$_3$ disuelve bien en agua (forma puentes de H con ella) y tiene $T_{eb}=-33$ °C, alto para su masa molar (17 g/mol) — confirma la polaridad. ✓"
            },
            {
                "title": "Energía de red por la fórmula de Born-Landé",
                "enunciado": r"Estimar la energía de red del <b>NaCl</b> usando la aproximación de Coulomb a partir de las cargas y distancia interiónica $r_0=2{,}82$ Å. Compararla con el valor experimental $U_{exp}=-787$ kJ/mol. Datos: $k_e=8{,}988\cdot 10^{9}\ \text{N·m}^2/\text{C}^2$, $e=1{,}602\cdot 10^{-19}$ C, $N_A=6{,}022\cdot 10^{23}$, constante de Madelung $A=1{,}748$ (NaCl), $n=8$ (factor de Born).",
                "esperado": r"$U \approx -757$ kJ/mol (excelente coincidencia con el experimental).",
                "datos": [
                    ("Cargas", "Na$^+$: $+e$; Cl$^-$: $-e$"),
                    ("Distancia interiónica", "$r_0=2{,}82\\cdot 10^{-10}\\ \\text{m}$"),
                    ("Constante de Madelung", "$A=1{,}748$"),
                    ("Exponente de Born", "$n=8$"),
                    ("$k_e$", "$8{,}988\\cdot 10^{9}\\ \\text{N·m}^2/\\text{C}^2$"),
                ],
                "demo": {
                    "title": "Born-Landé desde el potencial coulombiano",
                    "body": r"""
<p>La energía potencial entre dos cargas es $E=k_e q_1 q_2/r$. Sumando sobre todos los iones de la red (atractivos y repulsivos) aparece la <b>constante de Madelung</b> $A$ (depende solo del tipo de red).</p>
<p>Born añadió un término repulsivo a corta distancia $\propto 1/r^n$ que estabiliza la red:</p>
$$U = -\dfrac{N_A\,A\,|q_+ q_-|\,k_e}{r_0}\!\left(1-\dfrac{1}{n}\right)$$
<p>El factor $(1-1/n)$ representa la fracción del potencial coulombiano que <em>queda</em> tras compensar la repulsión de Born.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Energía coulombiana de un par",
                     "p": "Calcular $k_e e^2 / r_0$.",
                     "b": r"""$$\dfrac{k_e e^2}{r_0}=\dfrac{8{,}988\cdot 10^{9}\cdot(1{,}602\cdot 10^{-19})^2}{2{,}82\cdot 10^{-10}}=8{,}18\cdot 10^{-19}\ \text{J}$$"""},
                    {"t": "Paso 2 — Multiplicar por $N_A\\cdot A\\cdot(1-1/n)$",
                     "p": "Suma sobre toda la red de 1 mol; signo negativo (atractivo neto).",
                     "b": r"""$$U = -6{,}022\cdot 10^{23}\cdot 1{,}748\cdot 8{,}18\cdot 10^{-19}\cdot\!\left(1-\dfrac{1}{8}\right)$$
$$U = -6{,}022\cdot 10^{23}\cdot 1{,}748\cdot 8{,}18\cdot 10^{-19}\cdot 0{,}875$$
$$U \approx -7{,}53\cdot 10^{5}\ \text{J/mol} = -753\ \text{kJ/mol}$$"""},
                ],
                "resultado": r"$U_{calc}\approx -753$ kJ/mol vs $U_{exp}=-787$ kJ/mol → diferencia $\sim 4\%$.",
                "verificacion": r"La pequeña discrepancia se debe a que la fórmula no incluye dispersión de London ni efectos de polarización. ✓ La aproximación es excelente para enlaces puramente iónicos."
            },
            {
                "title": "Identificar fuerzas intermoleculares dominantes",
                "enunciado": r"Ordenar de menor a mayor punto de ebullición las siguientes sustancias e indicar qué fuerza intermolecular domina en cada una: <b>CH$_4$, CH$_3$OH, H$_2$O, He, HF</b>.",
                "esperado": r"He < CH$_4$ < HF < CH$_3$OH < H$_2$O.",
                "datos": [
                    ("Sustancias", "He · CH$_4$ · HF · CH$_3$OH · H$_2$O"),
                    ("Recordatorio", "Puentes H entre N–H, O–H, F–H y un par libre electronegativo"),
                ],
                "demo": {
                    "title": "Jerarquía de fuerzas intermoleculares",
                    "body": r"""
<p>El punto de ebullición depende de cuánta energía hace falta para separar las moléculas en estado líquido. Las fuerzas relevantes son (de menor a mayor):</p>
<ol>
  <li><b>Dispersión de London</b> (apolares; aumentan con la masa molar).</li>
  <li><b>Dipolo-dipolo</b> (moléculas polares).</li>
  <li><b>Puente de H</b> (H unido a N/O/F + par libre cercano).</li>
</ol>
<p>Más fuerte la fuerza ⟹ más energía para evaporar ⟹ mayor $T_{eb}$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Clasificar cada sustancia",
                     "p": "Examino enlaces y polaridad de cada una.",
                     "b": r"""<table class="tdatos">
<tr><th>Sustancia</th><th>Enlace dominante</th><th>$T_{eb}$ aprox.</th></tr>
<tr><td>He</td><td>London (apolar, masa muy baja)</td><td>$-269$ °C</td></tr>
<tr><td>CH$_4$</td><td>London (apolar)</td><td>$-161$ °C</td></tr>
<tr><td>HF</td><td>Puente de H (1 H disponible)</td><td>$+20$ °C</td></tr>
<tr><td>CH$_3$OH</td><td>Puente de H (1 H, 2 pares libres)</td><td>$+65$ °C</td></tr>
<tr><td>H$_2$O</td><td>Puente de H (2 H, 2 pares libres)</td><td>$+100$ °C</td></tr>
</table>"""},
                    {"t": "Paso 2 — Ordenar",
                     "p": "Apolares con London < polar con dipolo < con puente H, y entre los puentes H, gana el que pueda formar más por molécula (H$_2$O > CH$_3$OH > HF).",
                     "b": r"""$$\boxed{\;\text{He} < \text{CH}_4 < \text{HF} < \text{CH}_3\text{OH} < \text{H}_2\text{O}\;}$$"""},
                ],
                "resultado": r"$T_{eb}$: <b>He < CH$_4$ < HF < CH$_3$OH < H$_2$O</b>.",
                "verificacion": r"El H$_2$O puede formar 2 puentes de H por molécula (los dos H y los dos pares libres del O) → red 3D extensa → mayor $T_{eb}$. ✓ El HF solo aporta 1 H, por eso queda por debajo del metanol pese a tener mayor diferencia de electronegatividad."
            },
        ],
    },

    4: {
        "titulo": "Estados de la materia",
        "subtitulo": "Sólidos · Líquidos · Gases · Cambios de estado · Diagramas de fases",
        "secciones": [
            {
                "id": "sec-1",
                "h": "4.1. Estados de agregación: visión general",
                "html": r"""
<p>La materia se presenta principalmente en tres estados: <strong>sólido</strong>, <strong>líquido</strong> y <strong>gas</strong>, que se diferencian por la magnitud de las fuerzas intermoleculares relativa a la energía cinética de las partículas:</p>
<table class="tabla">
  <tr><th>Estado</th><th>Forma</th><th>Volumen</th><th>$T_{IM}/E_c$</th></tr>
  <tr><td>Sólido</td><td>Propia</td><td>Propio</td><td>Muy alta</td></tr>
  <tr><td>Líquido</td><td>Adopta</td><td>Propio</td><td>Intermedia</td></tr>
  <tr><td>Gas</td><td>Adopta</td><td>Adopta</td><td>Muy baja</td></tr>
</table>
<p>Subiendo $T$ aumentamos $E_c$ y vencemos las fuerzas intermoleculares: pasamos sólido → líquido → gas. Bajando $T$ ocurre lo contrario.</p>
"""
            },
            {
                "id": "sec-2",
                "h": "4.2. Gases ideales",
                "html": r"""
<p>Un <strong>gas ideal</strong> cumple dos hipótesis: las moléculas no interactúan entre sí y su volumen propio es despreciable frente al recipiente. Lo describe la ecuación de estado:</p>
<div class="formula">
  <div class="formula-label">Ecuación de los gases ideales</div>
  $$\boxed{\;pV = nRT\;}$$
</div>
<p>Casos particulares (manteniendo $n$ constante):</p>
<table class="tabla">
  <tr><th>Ley</th><th>Fija</th><th>Expresión</th></tr>
  <tr><td>Boyle</td><td>$T$, $n$</td><td>$pV=$ cte</td></tr>
  <tr><td>Charles</td><td>$p$, $n$</td><td>$V/T=$ cte</td></tr>
  <tr><td>Gay-Lussac</td><td>$V$, $n$</td><td>$p/T=$ cte</td></tr>
  <tr><td>Avogadro</td><td>$p$, $T$</td><td>$V/n=$ cte</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Ley de Dalton (mezclas)</div>
  La presión total de una mezcla de gases que no reaccionan es la suma de sus presiones parciales:
  $$p_T = \sum_i p_i \qquad p_i = x_i\,p_T \;,\; x_i=\dfrac{n_i}{n_T}$$
</div>
"""
            },
            {
                "id": "sec-3",
                "h": "4.3. Gases reales: Van der Waals",
                "html": r"""
<p>A altas presiones o bajas temperaturas, los gases reales se desvían del modelo ideal. Van der Waals corrigió la ecuación introduciendo dos términos:</p>
<div class="formula">
  $$\!\left(p+\dfrac{a\,n^2}{V^2}\right)\!(V-nb)=nRT$$
</div>
<ul>
  <li>$a$: corrige por <em>atracciones</em> intermoleculares (la presión real es menor).</li>
  <li>$b$: corrige por el <em>volumen propio</em> de las moléculas (el espacio libre es menor).</li>
</ul>
<div class="note"><strong>Factor de compresibilidad</strong>: $Z=pV/(nRT)$. Para un gas ideal $Z=1$. Si $Z<1$ dominan atracciones; si $Z>1$, dominan repulsiones.</div>
"""
            },
            {
                "id": "sec-4",
                "h": "4.4. Líquidos y sólidos",
                "html": r"""
<h3>Líquidos</h3>
<ul>
  <li><b>Tensión superficial</b> $\sigma$: energía por unidad de área (N/m). Las moléculas de la superficie tienen menos vecinas → mayor energía → tienden a minimizar el área.</li>
  <li><b>Viscosidad</b> $\eta$: resistencia al flujo. Aumenta con fuerzas intermoleculares y disminuye con $T$.</li>
  <li><b>Presión de vapor</b> $p_v$: presión del vapor en equilibrio con su líquido. Crece con $T$ (Clausius-Clapeyron).</li>
  <li><b>Punto de ebullición</b>: $T$ a la que $p_v$ iguala la presión externa.</li>
</ul>
<h3>Sólidos</h3>
<table class="tabla">
  <tr><th>Tipo</th><th>Partículas</th><th>Fuerza</th><th>Ejemplo</th><th>$T_{fus}$</th></tr>
  <tr><td>Iónico</td><td>iones</td><td>electrostática</td><td>NaCl</td><td>alto</td></tr>
  <tr><td>Covalente</td><td>átomos</td><td>enlace covalente</td><td>diamante, SiO$_2$</td><td>muy alto</td></tr>
  <tr><td>Metálico</td><td>cationes + e<sup>−</sup>$_{deslocalizados}$</td><td>enlace metálico</td><td>Fe, Cu</td><td>variable</td></tr>
  <tr><td>Molecular</td><td>moléculas</td><td>IM (London, dipolo, H)</td><td>hielo, I$_2$</td><td>bajo</td></tr>
</table>
"""
            },
            {
                "id": "sec-5",
                "h": "4.5. Cambios de estado y diagrama de fases",
                "html": r"""
<p>Un <strong>cambio de fase</strong> ocurre a $p$ y $T$ fijas: durante el proceso, todo el calor aportado se invierte en romper o formar enlaces, no en subir la temperatura.</p>
<div class="formula">
  <div class="formula-label">Calor de cambio de fase</div>
  $$Q = m\,L_{f/v}$$
</div>
<p>$L_f$ = calor latente de fusión (J/g); $L_v$ = calor latente de vaporización.</p>
<div class="concept">
  <div class="concept-label">Diagrama p-T</div>
  En un diagrama presión-temperatura aparecen tres curvas (sublimación, fusión, vaporización) que delimitan las fases sólida, líquida y gas. Se cortan en el <b>punto triple</b> (las tres coexisten) y la curva líquido-gas termina en el <b>punto crítico</b> (más allá no se distingue líquido de gas: fluido supercrítico).
</div>
<div class="formula">
  <div class="formula-label">Clausius-Clapeyron</div>
  $$\ln\!\dfrac{p_2}{p_1} = -\dfrac{\Delta H_{vap}}{R}\!\left(\dfrac{1}{T_2}-\dfrac{1}{T_1}\right)$$
</div>
<p>Predice cómo cambia la presión de vapor con la temperatura.</p>
"""
            },
        ],
        "ej": [
            {
                "title": "Ley de los gases ideales: hallar volumen",
                "enunciado": r"Calcular el volumen que ocupan <b>2,5 mol de N$_2$</b> a <b>27 °C</b> y <b>2 atm</b> de presión, suponiendo comportamiento ideal. ¿Cuál sería ese volumen en condiciones normales (0 °C, 1 atm)?",
                "esperado": r"$V_1=30{,}77$ L; $V_{CN}=56{,}0$ L.",
                "datos": [
                    ("Moles", "$n=2{,}5\\ \\text{mol}$"),
                    ("Temperatura", "$T_1=300\\ \\text{K}$ (27 °C)"),
                    ("Presión", "$p_1=2\\ \\text{atm}$"),
                    ("$R$", "$0{,}082\\ \\text{atm·L/(mol·K)}$"),
                ],
                "demo": {
                    "title": "De $pV=nRT$ a las condiciones normales",
                    "body": r"""
<p>La ecuación $pV=nRT$ permite encontrar cualquier variable conocidas las otras tres. Para un proceso entre dos estados con $n$ constante:</p>
$$\dfrac{p_1V_1}{T_1}=\dfrac{p_2V_2}{T_2}$$
<p>En <b>condiciones normales (CN)</b>: $T=273{,}15$ K, $p=1$ atm. 1 mol de gas ideal ocupa <b>22,4 L</b>.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Volumen a 27 °C, 2 atm",
                     "p": "Despejo $V$ de $pV=nRT$.",
                     "b": r"""$$V_1 = \dfrac{nRT_1}{p_1} = \dfrac{2{,}5\cdot 0{,}082\cdot 300}{2} = 30{,}75\ \text{L}$$"""},
                    {"t": "Paso 2 — Volumen en CN",
                     "p": "En CN, 1 mol = 22,4 L.",
                     "b": r"""$$V_{CN} = 2{,}5\cdot 22{,}4 = 56{,}0\ \text{L}$$"""},
                ],
                "resultado": r"$V_1 = 30{,}75$ L · $V_{CN}=56{,}0$ L.",
                "verificacion": r"Comprobación con $pV=nRT$ en CN: $V=2{,}5\cdot 0{,}082\cdot 273{,}15/1 = 56{,}0$ L. ✓"
            },
            {
                "title": "Mezcla de gases: ley de Dalton",
                "enunciado": r"En un recipiente de <b>10 L</b> a <b>27 °C</b> se mezclan <b>4 g de He</b>, <b>14 g de N$_2$</b> y <b>32 g de O$_2$</b>. Calcular: (a) la presión parcial de cada gas; (b) la presión total. Datos: $M_{He}=4$, $M_{N_2}=28$, $M_{O_2}=32$ g/mol.",
                "esperado": r"$p_{He}=2{,}46$ atm; $p_{N_2}=1{,}23$ atm; $p_{O_2}=2{,}46$ atm; $p_T=6{,}15$ atm.",
                "datos": [
                    ("Volumen", "$V=10\\ \\text{L}$"),
                    ("Temperatura", "$T=300\\ \\text{K}$"),
                    ("Masas", "He: 4 g · N$_2$: 14 g · O$_2$: 32 g"),
                ],
                "demo": {
                    "title": "Ley de Dalton de presiones parciales",
                    "body": r"""
<p>En una mezcla de gases ideales que no reaccionan, cada gas se comporta como si ocupara solo el recipiente. Su <b>presión parcial</b> es la que ejercería en solitario:</p>
$$p_i = \dfrac{n_i RT}{V}$$
<p>La <b>presión total</b> es la suma de las parciales:</p>
$$p_T = \sum_i p_i = \dfrac{(\sum_i n_i)RT}{V} = \dfrac{n_T RT}{V}$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Moles de cada gas",
                     "p": "$n=m/M$.",
                     "b": r"""$$n_{He}=\dfrac{4}{4}=1\ \text{mol}\quad n_{N_2}=\dfrac{14}{28}=0{,}5\ \text{mol}\quad n_{O_2}=\dfrac{32}{32}=1\ \text{mol}$$"""},
                    {"t": "Paso 2 — Presiones parciales",
                     "p": "Aplico $p_i=n_i RT/V$ con $RT/V=0{,}082\\cdot 300/10=2{,}46$.",
                     "b": r"""$$p_{He}=1\cdot 2{,}46=2{,}46\ \text{atm}$$
$$p_{N_2}=0{,}5\cdot 2{,}46=1{,}23\ \text{atm}$$
$$p_{O_2}=1\cdot 2{,}46=2{,}46\ \text{atm}$$"""},
                    {"t": "Paso 3 — Presión total",
                     "p": "Suma de parciales (= Dalton).",
                     "b": r"""$$p_T = 2{,}46 + 1{,}23 + 2{,}46 = 6{,}15\ \text{atm}$$"""},
                ],
                "resultado": r"$p_{He}=2{,}46$ atm · $p_{N_2}=1{,}23$ atm · $p_{O_2}=2{,}46$ atm · $p_T=6{,}15$ atm.",
                "verificacion": r"$n_T=2{,}5$ mol → $p_T=n_T RT/V = 2{,}5\cdot 0{,}082\cdot 300/10=6{,}15$ atm ✓."
            },
            {
                "title": "Calor para fundir y calentar hielo",
                "enunciado": r"Calcular el calor necesario para transformar <b>50 g de hielo a –10 °C</b> en <b>agua líquida a 25 °C</b>. Datos: $c_{hielo}=2{,}09$ J/(g·K), $c_{agua}=4{,}18$ J/(g·K), $L_f=334$ J/g.",
                "esperado": r"$Q\approx 22{,}0$ kJ.",
                "datos": [
                    ("Masa", "$m=50\\ \\text{g}$"),
                    ("Temperatura inicial", "$T_1=-10$ °C"),
                    ("Temperatura final", "$T_2=25$ °C"),
                    ("Calor específico hielo", "$c_h=2{,}09$ J/(g·K)"),
                    ("Calor específico agua", "$c_a=4{,}18$ J/(g·K)"),
                    ("Calor latente de fusión", "$L_f=334$ J/g"),
                ],
                "demo": {
                    "title": "Tres etapas: calor sensible + cambio de fase + calor sensible",
                    "body": r"""
<p>El proceso <b>−10 °C hielo → 0 °C hielo → 0 °C agua → 25 °C agua</b> consta de tres etapas en las que el calor se invierte de forma distinta:</p>
<ol>
  <li>Calentar el hielo de −10 a 0 °C: $Q_1=m\,c_h\,\Delta T$ (calor sensible).</li>
  <li>Fundir el hielo a 0 °C: $Q_2=m\,L_f$ (calor latente, $T$ fija).</li>
  <li>Calentar el agua de 0 a 25 °C: $Q_3=m\,c_a\,\Delta T$.</li>
</ol>
<p>El calor total es $Q=Q_1+Q_2+Q_3$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Calentar hielo",
                     "p": "$\\Delta T = 0-(-10)=10$ K.",
                     "b": r"""$$Q_1 = 50\cdot 2{,}09\cdot 10 = 1\,045\ \text{J}$$"""},
                    {"t": "Paso 2 — Fundir el hielo",
                     "p": "$T$ se mantiene en 0 °C durante la fusión.",
                     "b": r"""$$Q_2 = 50\cdot 334 = 16\,700\ \text{J}$$"""},
                    {"t": "Paso 3 — Calentar el agua líquida",
                     "p": "$\\Delta T = 25-0=25$ K.",
                     "b": r"""$$Q_3 = 50\cdot 4{,}18\cdot 25 = 5\,225\ \text{J}$$"""},
                    {"t": "Paso 4 — Calor total",
                     "p": "Suma de las tres etapas.",
                     "b": r"""$$Q = 1\,045 + 16\,700 + 5\,225 = 22\,970\ \text{J}\approx \boxed{23{,}0\ \text{kJ}}$$"""},
                ],
                "resultado": r"$Q \approx 23{,}0$ kJ — la mayor parte del calor (16,7 kJ ≈ 73%) se gasta en <em>fundir</em> el hielo, no en calentarlo.",
                "verificacion": r"Comprobación de proporción: con la misma masa, fundir hielo (16,7 kJ) equivale a calentar agua líquida 80 K, mucho más que los 35 K reales del proceso. Esto refleja el alto $L_f$ del agua. ✓"
            },
        ],
    },

    6: {
        "titulo": "Termoquímica",
        "subtitulo": "Calores de reacción · Ley de Hess · Energías de enlace · Calorimetría",
        "secciones": [
            {
                "id": "sec-1",
                "h": "6.1. Calor de reacción y entalpía estándar",
                "html": r"""
<p>El <strong>calor de reacción</strong> es el calor intercambiado durante una reacción química. Si el proceso ocurre a presión constante, coincide con la variación de entalpía:</p>
$$\Delta H = Q_p$$
<ul>
  <li><b>Exotérmica</b>: $\Delta H<0$ (libera calor).</li>
  <li><b>Endotérmica</b>: $\Delta H>0$ (absorbe calor).</li>
</ul>
<div class="concept">
  <div class="concept-label">Estado estándar (°)</div>
  Convención termodinámica: $p=1$ bar (≈ 1 atm) y la sustancia en su forma más estable a la $T$ considerada (normalmente 298 K). Las entalpías estándar se denotan con un superíndice °: $\Delta H°$.
</div>
"""
            },
            {
                "id": "sec-2",
                "h": "6.2. Tipos de entalpías estándar",
                "html": r"""
<table class="tabla">
  <tr><th>Símbolo</th><th>Proceso</th><th>Convención</th></tr>
  <tr><td>$\Delta H°_f$</td><td>Formación: 1 mol del compuesto a partir de los elementos</td><td>$\Delta H°_f$(elemento estable) = 0</td></tr>
  <tr><td>$\Delta H°_c$</td><td>Combustión: 1 mol con O$_2$ → CO$_2$ + H$_2$O</td><td>Siempre $<0$</td></tr>
  <tr><td>$\Delta H°_{at}$</td><td>Atomización: 1 mol en átomos gaseosos</td><td>$>0$</td></tr>
  <tr><td>$\Delta H°_{disol}$</td><td>Disolución: 1 mol en exceso de disolvente</td><td>+/–</td></tr>
  <tr><td>$\Delta H°_{neut}$</td><td>Neutralización ácido + base → 1 mol H$_2$O</td><td>$\approx -57{,}3$ kJ/mol (fuertes)</td></tr>
</table>
<div class="formula">
  <div class="formula-label">$\Delta H°$ a partir de las entalpías de formación</div>
  $$\Delta H°_{rxn} = \sum \nu_i\,\Delta H°_f(\text{productos}) - \sum \nu_i\,\Delta H°_f(\text{reactivos})$$
</div>
"""
            },
            {
                "id": "sec-3",
                "h": "6.3. Ley de Hess",
                "html": r"""
<p>Como $H$ es función de estado, la entalpía de una reacción global es <b>independiente del camino</b>. Si una reacción se puede escribir como suma de etapas, su $\Delta H$ es la suma de los $\Delta H$ de las etapas (con sus coeficientes y signos).</p>
<div class="concept">
  <div class="concept-label">Reglas de manipulación</div>
  <ul>
    <li>Invertir una reacción cambia el signo de $\Delta H$.</li>
    <li>Multiplicar una reacción por $k$ multiplica su $\Delta H$ por $k$.</li>
    <li>Sumar reacciones suma sus $\Delta H$.</li>
  </ul>
</div>
<div class="note">La ley de Hess permite calcular calores de reacción <em>imposibles de medir directamente</em> a partir de otros conocidos.</div>
"""
            },
            {
                "id": "sec-4",
                "h": "6.4. Energías de enlace",
                "html": r"""
<p>La <strong>energía de enlace</strong> $E(A-B)$ es la energía promedio necesaria para romper 1 mol de enlaces $A-B$ en estado gaseoso. Es siempre <b>positiva</b> (se necesita energía para romper).</p>
<div class="formula">
  <div class="formula-label">$\Delta H$ por energías de enlace</div>
  $$\Delta H_{rxn} \approx \sum E(\text{enlaces rotos}) - \sum E(\text{enlaces formados})$$
</div>
<p>Romper enlaces consume energía (entra al sistema), formar enlaces libera energía (sale del sistema). De ahí la diferencia.</p>
<div class="note"><strong>Aproximación:</strong> los valores son <em>promedios</em>. Cada molécula concreta puede desviarse algo, especialmente si los enlaces están en entornos químicos distintos.</div>
"""
            },
            {
                "id": "sec-5",
                "h": "6.5. Calorimetría",
                "html": r"""
<p>Un <strong>calorímetro</strong> mide el calor de una reacción a partir del cambio de temperatura del sistema (la disolución, el agua del calorímetro, las paredes, etc.).</p>
<div class="formula">
  $$Q_{rxn} = -(m\,c\,\Delta T + C_{cal}\,\Delta T)$$
</div>
<p>$C_{cal}$ es la capacidad calorífica del calorímetro (J/K) y se mide con una reacción de calor conocido.</p>
<div class="concept">
  <div class="concept-label">Bomba calorimétrica vs. taza</div>
  <ul>
    <li><b>Bomba</b> (volumen constante): mide $Q_V = \Delta U$.</li>
    <li><b>Taza/coffee-cup</b> (presión constante): mide $Q_p = \Delta H$.</li>
  </ul>
  Para pasar entre ambos: $\Delta H = \Delta U + \Delta n_{gas}\,RT$.
</div>
"""
            },
        ],
        "ej": [
            {
                "title": "Entalpía de combustión del metano por entalpías de formación",
                "enunciado": r"Calcular $\Delta H°_{rxn}$ de la combustión del metano: $\text{CH}_4(g)+2\text{O}_2(g)\to\text{CO}_2(g)+2\text{H}_2\text{O}(l)$. Datos $\Delta H°_f$ (kJ/mol): CH$_4$(g) = −74,8; CO$_2$(g) = −393,5; H$_2$O(l) = −285,8.",
                "esperado": r"$\Delta H°_{rxn} = -890{,}3$ kJ/mol.",
                "datos": [
                    ("Reacción", "$\\text{CH}_4 + 2\\,\\text{O}_2 \\to \\text{CO}_2 + 2\\,\\text{H}_2\\text{O}(l)$"),
                    ("$\\Delta H°_f$ CH$_4$(g)", "$-74{,}8$ kJ/mol"),
                    ("$\\Delta H°_f$ CO$_2$(g)", "$-393{,}5$ kJ/mol"),
                    ("$\\Delta H°_f$ H$_2$O(l)", "$-285{,}8$ kJ/mol"),
                    ("$\\Delta H°_f$ O$_2$(g)", "$0$ (elemento)"),
                ],
                "demo": {
                    "title": "Por qué $\\Delta H_{rxn}=\\sum H_f^{prod}-\\sum H_f^{reac}$",
                    "body": r"""
<p>Para cualquier reacción, podemos imaginar dos caminos termodinámicamente equivalentes:</p>
<ol>
  <li><b>Directo</b>: reactivos → productos con $\Delta H_{rxn}$.</li>
  <li><b>Indirecto</b>: reactivos → elementos puros → productos.</li>
</ol>
<p>La etapa "elementos → productos" libera $+\sum H_f^{prod}$. La etapa "reactivos → elementos" libera $-\sum H_f^{reac}$ (es la inversa de la formación). Como $H$ es función de estado, los dos caminos dan lo mismo:</p>
$$\Delta H_{rxn} = \sum\nu_i\Delta H_f^{prod} - \sum\nu_i\Delta H_f^{reac}$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Identificar coeficientes y aplicar la fórmula",
                     "p": "Coeficientes: 1 CH$_4$, 2 O$_2$, 1 CO$_2$, 2 H$_2$O.",
                     "b": r"""$$\Delta H°_{rxn} = [1\cdot\Delta H°_f(\text{CO}_2) + 2\cdot\Delta H°_f(\text{H}_2\text{O})] - [1\cdot\Delta H°_f(\text{CH}_4) + 2\cdot 0]$$"""},
                    {"t": "Paso 2 — Sustituir valores",
                     "p": "Cuidado con los signos negativos.",
                     "b": r"""$$\Delta H°_{rxn} = [(-393{,}5) + 2\cdot(-285{,}8)] - [(-74{,}8)] $$
$$= -393{,}5 - 571{,}6 + 74{,}8 = \boxed{-890{,}3\ \text{kJ/mol}}$$"""},
                ],
                "resultado": r"$\Delta H°_{rxn} = -890{,}3$ kJ/mol — fuertemente exotérmica (combustible).",
                "verificacion": r"Por mol de O$_2$ liberado: $-890{,}3/2 = -445$ kJ/mol O$_2$. Es del orden de los $-470$ kJ/mol O$_2$ típicos de combustiones de hidrocarburos. ✓"
            },
            {
                "title": "Ley de Hess: combustión de carbono → CO",
                "enunciado": r"Calcular $\Delta H°$ de $\text{C(s)} + \tfrac{1}{2}\text{O}_2(g) \to \text{CO}(g)$ a partir de: (1) $\text{C}+\text{O}_2\to\text{CO}_2$, $\Delta H_1=-393{,}5$ kJ. (2) $\text{CO}+\tfrac{1}{2}\text{O}_2\to\text{CO}_2$, $\Delta H_2=-283{,}0$ kJ.",
                "esperado": r"$\Delta H = -110{,}5$ kJ.",
                "datos": [
                    ("Reacción 1", "$\\text{C}+\\text{O}_2\\to\\text{CO}_2$, $\\Delta H_1=-393{,}5$ kJ"),
                    ("Reacción 2", "$\\text{CO}+\\tfrac{1}{2}\\text{O}_2\\to\\text{CO}_2$, $\\Delta H_2=-283{,}0$ kJ"),
                    ("Objetivo", "$\\text{C}+\\tfrac{1}{2}\\text{O}_2\\to\\text{CO}$, $\\Delta H=?$"),
                ],
                "demo": {
                    "title": "Combinación lineal de las dos reacciones",
                    "body": r"""
<p>Buscamos una combinación de las reacciones (1) y (2) cuya suma sea exactamente la objetivo. Dado que la objetivo tiene CO como <em>producto</em>, debemos <b>invertir</b> la reacción (2) (que tiene CO como reactivo):</p>
<p>(1) C + O$_2$ → CO$_2$ &nbsp;&nbsp;($\Delta H_1$)<br>
(−2) CO$_2$ → CO + ½ O$_2$ &nbsp;&nbsp;($-\Delta H_2$)</p>
<p>Sumando: C + ½ O$_2$ → CO. Coincide con la objetivo. Por tanto $\Delta H=\Delta H_1-\Delta H_2$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Plantear la combinación",
                     "p": "(1) directa + (2) invertida.",
                     "b": r"""<table class="tdatos">
<tr><th>Reacción</th><th>$\Delta H$ (kJ)</th></tr>
<tr><td>C + O$_2$ → CO$_2$</td><td>$-393{,}5$</td></tr>
<tr><td>CO$_2$ → CO + ½ O$_2$</td><td>$+283{,}0$</td></tr>
<tr><td><b>C + ½ O$_2$ → CO</b></td><td><b>?</b></td></tr>
</table>"""},
                    {"t": "Paso 2 — Sumar",
                     "p": "Las CO$_2$ se cancelan; queda la objetivo.",
                     "b": r"""$$\Delta H = -393{,}5 + 283{,}0 = \boxed{-110{,}5\ \text{kJ}}$$"""},
                ],
                "resultado": r"$\Delta H = -110{,}5$ kJ/mol — exotérmica (combustión incompleta).",
                "verificacion": r"$\Delta H_f$(CO,g) tabulado = $-110{,}5$ kJ/mol. ✓ Coincide exactamente."
            },
            {
                "title": "Calorimetría a presión constante",
                "enunciado": r"Al añadir <b>50 mL de NaOH 1,0 M</b> a <b>50 mL de HCl 1,0 M</b> en un calorímetro de taza, la temperatura sube de <b>20,5 °C a 27,3 °C</b>. Calcular el calor de neutralización por mol de agua formada. Suponer que la disolución tiene la densidad y el calor específico del agua, y despreciar la capacidad calorífica del calorímetro.",
                "esperado": r"$\Delta H_{neut} \approx -56{,}9$ kJ/mol — coincide con el valor estándar para ácido y base fuertes ($-57{,}3$ kJ/mol).",
                "datos": [
                    ("Volumen total", "$V = 100\\ \\text{mL}$"),
                    ("Densidad", "$\\rho = 1\\ \\text{g/mL}$"),
                    ("Calor específico", "$c=4{,}18\\ \\text{J/(g·K)}$"),
                    ("$\\Delta T$", "$27{,}3-20{,}5=6{,}8$ K"),
                    ("Moles", "$n_{HCl}=n_{NaOH}=0{,}050\\cdot 1{,}0=0{,}050$ mol"),
                ],
                "demo": {
                    "title": "Balance de calor en el calorímetro",
                    "body": r"""
<p>El calor liberado por la reacción se invierte en calentar la disolución:</p>
$$Q_{rxn} = -Q_{disol} = -m\,c\,\Delta T$$
<p>El signo negativo refleja que la reacción libera calor (exotérmica). Para obtener la entalpía molar dividimos por los moles de agua formada (= moles del limitante):</p>
$$\Delta H = \dfrac{Q_{rxn}}{n_{H_2O}}$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Calor absorbido por la disolución",
                     "p": "Masa = 100 g (densidad 1 g/mL).",
                     "b": r"""$$Q_{disol} = m\,c\,\Delta T = 100\cdot 4{,}18\cdot 6{,}8 = 2\,842\ \text{J}$$"""},
                    {"t": "Paso 2 — Calor de la reacción",
                     "p": "$Q_{rxn}=-Q_{disol}$ (lo que pierde la reacción lo gana la disolución).",
                     "b": r"""$$Q_{rxn} = -2\,842\ \text{J}$$"""},
                    {"t": "Paso 3 — Entalpía molar",
                     "p": "Dividir entre los 0,050 mol de H$_2$O formados.",
                     "b": r"""$$\Delta H_{neut} = \dfrac{-2\,842}{0{,}050} = -56\,840\ \text{J/mol} \approx \boxed{-56{,}8\ \text{kJ/mol}}$$"""},
                ],
                "resultado": r"$\Delta H_{neut} \approx -56{,}8$ kJ/mol.",
                "verificacion": r"Valor de bibliografía para HCl + NaOH: $-57{,}3$ kJ/mol. La pequeña diferencia (≈ 1 %) se debe a despreciar la capacidad calorífica del calorímetro y suponer densidad/calor específico del agua para la disolución 0,5 M. ✓"
            },
        ],
    },

    7: {
        "titulo": "Espontaneidad y energía libre",
        "subtitulo": "2ª Ley · Entropía · Energía libre de Gibbs · Equilibrio",
        "secciones": [
            {
                "id": "sec-1",
                "h": "7.1. Procesos espontáneos y reversibilidad",
                "html": r"""
<p>Un <strong>proceso espontáneo</strong> es el que ocurre sin necesidad de aporte externo: agua que cae, hielo que se funde a 25 °C, expansión de un gas en el vacío. La 1ª ley no basta para predecir la espontaneidad — necesitamos la 2ª ley.</p>
<div class="concept">
  <div class="concept-label">Reversible vs. irreversible</div>
  <ul>
    <li><b>Reversible</b>: cuasi-estático, en equilibrio en cada instante; se puede invertir sin pérdidas.</li>
    <li><b>Irreversible</b>: real; pasa por estados de no-equilibrio; no se puede invertir sin gastar energía adicional.</li>
  </ul>
</div>
<p>Todos los procesos espontáneos son irreversibles.</p>
"""
            },
            {
                "id": "sec-2",
                "h": "7.2. Entropía y 2ª ley",
                "html": r"""
<p>La <strong>entropía</strong> $S$ mide el grado de <em>desorden</em> o de <em>distribución microscópica de la energía</em>. Boltzmann la definió como:</p>
<div class="formula">
  $$S = k_B\,\ln W$$
</div>
<p>donde $W$ es el número de microestados compatibles con el estado macroscópico, y $k_B = 1{,}38\cdot 10^{-23}$ J/K. Más microestados accesibles ⟹ más entropía.</p>
<div class="formula">
  <div class="formula-label">2ª Ley de la termodinámica</div>
  $$\Delta S_{universo} = \Delta S_{sistema} + \Delta S_{entorno} \ge 0$$
</div>
<ul>
  <li>$=0$: proceso reversible.</li>
  <li>$>0$: proceso irreversible (espontáneo).</li>
  <li>$<0$: imposible.</li>
</ul>
<div class="concept">
  <div class="concept-label">Variación de entropía: cálculo</div>
  Para un proceso reversible: $\Delta S = \int \delta Q_{rev}/T$. Para uno isotermo: $\Delta S = Q_{rev}/T$.
</div>
"""
            },
            {
                "id": "sec-3",
                "h": "7.3. 3ª Ley y entropías estándar",
                "html": r"""
<div class="formula">
  <div class="formula-label">3ª Ley de la termodinámica</div>
  $$\lim_{T\to 0}S(T)=0\;\;\text{(cristal puro)}$$
</div>
<p>Esta ley fija un cero absoluto para la entropía: a 0 K un cristal perfecto solo tiene un microestado posible. Permite tabular <b>entropías absolutas</b> $S°$ a 298 K.</p>
<div class="formula">
  $$\Delta S°_{rxn} = \sum\nu_i\,S°(\text{productos}) - \sum\nu_i\,S°(\text{reactivos})$$
</div>
<table class="tabla">
  <tr><th>Cambio</th><th>$\Delta S$ típico</th></tr>
  <tr><td>Sólido → líquido</td><td>$+$</td></tr>
  <tr><td>Líquido → gas</td><td>$++$ (mucho mayor)</td></tr>
  <tr><td>Aumento de moles gaseosos</td><td>$+$</td></tr>
  <tr><td>$T$ aumenta</td><td>$+$</td></tr>
  <tr><td>Volumen aumenta (gas)</td><td>$+$</td></tr>
</table>
"""
            },
            {
                "id": "sec-4",
                "h": "7.4. Energía libre de Gibbs",
                "html": r"""
<p>La <strong>energía libre de Gibbs</strong> es el criterio de espontaneidad <em>cuando se trabaja a $p$ y $T$ constantes</em> (lo habitual en química):</p>
<div class="formula">
  $$\boxed{\;G = H - TS \;}$$
</div>
<div class="formula">
  $$\Delta G = \Delta H - T\Delta S$$
</div>
<table class="tabla">
  <tr><th>Signo $\Delta G$</th><th>Significado</th></tr>
  <tr><td>$\Delta G < 0$</td><td>Espontáneo</td></tr>
  <tr><td>$\Delta G = 0$</td><td>Equilibrio</td></tr>
  <tr><td>$\Delta G > 0$</td><td>No espontáneo (sí lo es la inversa)</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Análisis cualitativo según signos</div>
  <table class="tabla">
    <tr><th>$\Delta H$</th><th>$\Delta S$</th><th>$\Delta G$ (espontaneidad)</th></tr>
    <tr><td>$<0$</td><td>$>0$</td><td>Siempre espontáneo</td></tr>
    <tr><td>$<0$</td><td>$<0$</td><td>Espontáneo a $T$ baja</td></tr>
    <tr><td>$>0$</td><td>$>0$</td><td>Espontáneo a $T$ alta</td></tr>
    <tr><td>$>0$</td><td>$<0$</td><td>Nunca espontáneo</td></tr>
  </table>
</div>
"""
            },
            {
                "id": "sec-5",
                "h": r"7.5. $\Delta G$ y constante de equilibrio",
                "html": r"""
<p>En condiciones cualesquiera, la energía libre de una reacción es:</p>
<div class="formula">
  $$\Delta G = \Delta G° + RT\ln Q$$
</div>
<p>donde $Q$ es el cociente de reacción. En el <em>equilibrio</em>, $\Delta G=0$ y $Q=K$:</p>
<div class="formula">
  <div class="formula-label">Relación clave $\Delta G°$–$K$</div>
  $$\boxed{\;\Delta G° = -RT\ln K\;}$$
</div>
<ul>
  <li>$\Delta G° < 0 \Rightarrow K > 1$: equilibrio desplazado hacia productos.</li>
  <li>$\Delta G° > 0 \Rightarrow K < 1$: hacia reactivos.</li>
  <li>$\Delta G° = 0 \Rightarrow K = 1$.</li>
</ul>
<div class="note"><strong>Temperatura de inversión:</strong> el signo de $\Delta G$ puede cambiar con $T$ si $\Delta H$ y $\Delta S$ tienen el mismo signo. La temperatura crítica es $T^* = \Delta H/\Delta S$.</div>
"""
            },
        ],
        "ej": [
            {
                "title": "$\\Delta G°$ a partir de $\\Delta H°$ y $\\Delta S°$",
                "enunciado": r"Para la reacción $2\text{NO}(g)+\text{O}_2(g)\to 2\text{NO}_2(g)$ se conocen $\Delta H°=-114{,}1$ kJ/mol y $\Delta S°=-146{,}5$ J/(mol·K). Calcular $\Delta G°$ a 298 K y discutir su espontaneidad. ¿A qué temperatura deja de ser espontánea?",
                "esperado": r"$\Delta G°=-70{,}45$ kJ/mol a 298 K (espontánea). Deja de serlo a $T>779$ K.",
                "datos": [
                    ("$\\Delta H°$", "$-114{,}1$ kJ/mol"),
                    ("$\\Delta S°$", "$-146{,}5$ J/(mol·K) $=-0{,}1465$ kJ/(mol·K)"),
                    ("Temperatura", "$T=298$ K"),
                ],
                "demo": {
                    "title": "Criterio $\\Delta G = \\Delta H - T\\Delta S$ y temperatura de cambio",
                    "body": r"""
<p>La espontaneidad a $p$,$T$ constantes la decide el signo de $\Delta G = \Delta H - T\Delta S$. Cuando $\Delta H$ y $\Delta S$ son del <em>mismo signo</em>, hay una <b>temperatura de inversión</b> $T^*$ en la que $\Delta G=0$:</p>
$$T^* = \dfrac{\Delta H}{\Delta S}$$
<p>Por encima/debajo de $T^*$ el signo de $\Delta G$ se invierte. En este caso $\Delta H<0$ y $\Delta S<0$, así que el proceso es espontáneo a baja $T$ (cuando domina $\Delta H$) y deja de serlo cuando $T$ es alta (domina $-T\Delta S$).</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Calcular $\\Delta G°$ a 298 K",
                     "p": "Cuidado: $\\Delta S$ pasa a kJ/(mol·K) para que las unidades cuadren.",
                     "b": r"""$$\Delta G° = -114{,}1 - 298\cdot(-0{,}1465) = -114{,}1 + 43{,}66 = \boxed{-70{,}44\ \text{kJ/mol}}$$"""},
                    {"t": "Paso 2 — Espontaneidad",
                     "p": "$\\Delta G°<0$ ⟹ espontánea a 298 K. Predominio del término entálpico.",
                     "b": r"""<p>El proceso es <b>exotérmico</b> y ordena el sistema (menos moles gaseosos): $\Delta H$ favorece, $\Delta S$ desfavorece. A 298 K $\Delta H$ gana.</p>"""},
                    {"t": "Paso 3 — Temperatura de inversión",
                     "p": "$T^* = \\Delta H/\\Delta S$.",
                     "b": r"""$$T^* = \dfrac{-114{,}1}{-0{,}1465} = 779\ \text{K}$$
<p>Para $T>779$ K, $\Delta G > 0$ y la reacción <b>deja de ser espontánea</b>: el equilibrio se desplaza hacia NO + O$_2$.</p>"""},
                ],
                "resultado": r"$\Delta G°(298\,\text{K})=-70{,}44$ kJ/mol (espontánea). $T^*=779$ K (≈ 506 °C).",
                "verificacion": r"Comprobación a $T=779$ K: $\Delta G = -114{,}1 - 779\cdot(-0{,}1465) = -114{,}1 + 114{,}1 = 0$. ✓ Coherente con $T^*$."
            },
            {
                "title": "Constante de equilibrio a partir de $\\Delta G°$",
                "enunciado": r"Para la reacción $\text{N}_2(g)+3\text{H}_2(g)\rightleftharpoons 2\text{NH}_3(g)$ se sabe que $\Delta G°(298\,\text{K})=-32{,}9$ kJ/mol. Calcular la constante de equilibrio $K_p$.",
                "esperado": r"$K_p\approx 5{,}73\cdot 10^{5}$.",
                "datos": [
                    ("$\\Delta G°$", "$-32{,}9$ kJ/mol $=-32\\,900$ J/mol"),
                    ("$T$", "298 K"),
                    ("$R$", "$8{,}314$ J/(mol·K)"),
                ],
                "demo": {
                    "title": "Relación $\\Delta G° = -RT\\ln K$",
                    "body": r"""
<p>En el equilibrio, $\Delta G=0$ y $Q=K$. Sustituyendo en $\Delta G=\Delta G°+RT\ln Q$:</p>
$$0 = \Delta G° + RT\ln K \implies \boxed{\;K = e^{-\Delta G°/(RT)}\;}$$
<p>Si $\Delta G°<0$ entonces $K>1$ (equilibrio favorable a productos). Si $\Delta G°>0$, $K<1$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Despejar $K$",
                     "p": "$K = e^{-\\Delta G°/(RT)}$.",
                     "b": r"""$$K = \exp\!\left(-\dfrac{-32\,900}{8{,}314\cdot 298}\right) = \exp\!\left(\dfrac{32\,900}{2\,477{,}6}\right)=e^{13{,}28}$$"""},
                    {"t": "Paso 2 — Calcular el valor",
                     "p": "Cálculo del exponencial.",
                     "b": r"""$$K_p = e^{13{,}28} \approx \boxed{5{,}79\cdot 10^{5}}$$"""},
                ],
                "resultado": r"$K_p \approx 5{,}8\cdot 10^{5}$ — el equilibrio está fuertemente desplazado hacia el NH$_3$ a 298 K.",
                "verificacion": r"Sin embargo, la cinética a temperatura ambiente es muy lenta (proceso Haber-Bosch usa 400 °C y catalizador). El alto $K_p$ <em>termodinámico</em> no implica una reacción rápida. ✓"
            },
            {
                "title": "$\\Delta S$ de un cambio de fase",
                "enunciado": r"Calcular la entropía de vaporización del agua a 100 °C, sabiendo que $\Delta H_{vap}=40{,}66$ kJ/mol y que el proceso es reversible a $T_{eb}$.",
                "esperado": r"$\Delta S_{vap} = +109{,}0$ J/(mol·K).",
                "datos": [
                    ("$\\Delta H_{vap}$", "$40\\,660$ J/mol"),
                    ("$T_{eb}$", "$373{,}15$ K"),
                ],
                "demo": {
                    "title": "Cambio de fase reversible",
                    "body": r"""
<p>Un cambio de fase ocurre a $p$ y $T$ constantes. Como las dos fases coexisten en equilibrio, el proceso es <em>reversible</em>. Para un proceso reversible isotermo:</p>
$$\Delta S = \dfrac{Q_{rev}}{T} = \dfrac{\Delta H_{vap}}{T_{eb}}$$
<p>$\Delta H>0$ y $T>0$ ⟹ $\Delta S>0$: la fase gas tiene mucha más entropía que la líquida (más microestados accesibles, mayor desorden).</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Aplicar la fórmula",
                     "p": "Sustituyendo los valores.",
                     "b": r"""$$\Delta S_{vap} = \dfrac{40\,660}{373{,}15} = 108{,}96\ \text{J/(mol·K)}$$"""},
                ],
                "resultado": r"$\Delta S_{vap} \approx +109$ J/(mol·K) — coherente con la <b>regla de Trouton</b> ($\sim 88$ J/(mol·K) para líquidos no asociados; el agua queda por encima por sus puentes de H).",
                "verificacion": r"En el equilibrio líquido-gas a 100 °C: $\Delta G = \Delta H - T\Delta S = 40\,660 - 373{,}15\cdot 109 = 0$ ✓. Coherente con el equilibrio."
            },
        ],
    },

    8: {
        "titulo": "Cinética y equilibrio",
        "subtitulo": "Velocidad · Ley de Arrhenius · Equilibrio · $K_c$ y $K_p$ · Le Châtelier",
        "secciones": [
            {
                "id": "sec-1",
                "h": "8.1. Velocidad de reacción",
                "html": r"""
<p>La <strong>velocidad de una reacción</strong> mide cómo cambian las concentraciones con el tiempo. Para $aA+bB\to cC+dD$:</p>
<div class="formula">
  $$v=-\dfrac{1}{a}\dfrac{d[A]}{dt}=-\dfrac{1}{b}\dfrac{d[B]}{dt}=\dfrac{1}{c}\dfrac{d[C]}{dt}=\dfrac{1}{d}\dfrac{d[D]}{dt}$$
</div>
<div class="concept">
  <div class="concept-label">Ecuación de velocidad</div>
  Determinada experimentalmente, suele tener la forma $v = k\,[A]^m\,[B]^n$, donde $m,n$ son los <b>órdenes parciales</b> y $m+n$ el <b>orden total</b>. La constante $k$ depende de $T$ y del catalizador.
</div>
<p>Los exponentes $m,n$ <em>NO</em> coinciden en general con los coeficientes estequiométricos.</p>
"""
            },
            {
                "id": "sec-2",
                "h": "8.2. Órdenes de reacción",
                "html": r"""
<table class="tabla">
  <tr><th>Orden</th><th>Ecuación integrada</th><th>$t_{1/2}$</th></tr>
  <tr><td>0</td><td>$[A]=[A]_0-kt$</td><td>$[A]_0/(2k)$</td></tr>
  <tr><td>1</td><td>$\ln[A]=\ln[A]_0-kt$</td><td>$\ln 2/k$ (independiente de $[A]_0$)</td></tr>
  <tr><td>2</td><td>$\dfrac{1}{[A]}=\dfrac{1}{[A]_0}+kt$</td><td>$\dfrac{1}{k\,[A]_0}$</td></tr>
</table>
<div class="note"><strong>Test gráfico:</strong> orden 0 (lineal $[A]$ vs $t$); orden 1 (lineal $\ln[A]$ vs $t$); orden 2 (lineal $1/[A]$ vs $t$). El que dé recta es el orden correcto.</div>
"""
            },
            {
                "id": "sec-3",
                "h": "8.3. Ley de Arrhenius. Energía de activación",
                "html": r"""
<p>La constante $k$ depende de la temperatura según la <strong>ley de Arrhenius</strong>:</p>
<div class="formula">
  $$k = A\,e^{-E_a/(RT)}$$
</div>
<ul>
  <li>$A$ = factor preexponencial (frecuencia de colisiones efectivas).</li>
  <li>$E_a$ = energía de activación (barrera energética para la reacción).</li>
</ul>
<p>Forma logarítmica:</p>
<div class="formula">
  $$\ln k = \ln A - \dfrac{E_a}{R}\cdot\dfrac{1}{T}\qquad\Longrightarrow\qquad \ln\dfrac{k_2}{k_1}=-\dfrac{E_a}{R}\!\left(\dfrac{1}{T_2}-\dfrac{1}{T_1}\right)$$
</div>
<div class="concept">
  <div class="concept-label">Catalizador</div>
  Reduce $E_a$ proporcionando un camino alternativo. Acelera la reacción <em>directa e inversa</em> por igual: <b>no</b> cambia el equilibrio, solo el tiempo en alcanzarlo.
</div>
"""
            },
            {
                "id": "sec-4",
                "h": "8.4. Equilibrio químico",
                "html": r"""
<p>Una reacción es reversible cuando productos y reactivos coexisten. En el <strong>equilibrio</strong>, $v_{directa}=v_{inversa}$ y las concentraciones permanecen constantes (aunque la reacción no se detiene microscópicamente).</p>
<div class="formula">
  <div class="formula-label">Constante de equilibrio</div>
  $$K_c = \dfrac{[C]^c[D]^d}{[A]^a[B]^b}$$
</div>
<p>$K_c$ depende solo de $T$. No depende de las concentraciones iniciales ni de la presencia de catalizador.</p>
<div class="formula">
  <div class="formula-label">Relación con la presión (gases)</div>
  $$K_p = K_c\,(RT)^{\Delta n_{gas}}$$
</div>
<p>$\Delta n_{gas}=$ (moles gas productos) − (moles gas reactivos).</p>
<div class="note"><strong>Sólidos puros y líquidos puros</strong> NO aparecen en $K_c$ ni en $K_p$ (su "concentración" es esencialmente constante).</div>
"""
            },
            {
                "id": "sec-5",
                "h": "8.5. Cociente $Q$ y principio de Le Châtelier",
                "html": r"""
<p>El <strong>cociente de reacción</strong> $Q$ tiene la misma forma que $K$ pero se calcula con concentraciones en cualquier instante (no necesariamente equilibrio):</p>
<table class="tabla">
  <tr><th>Comparación</th><th>Sentido del desplazamiento</th></tr>
  <tr><td>$Q < K$</td><td>→ productos</td></tr>
  <tr><td>$Q = K$</td><td>Equilibrio</td></tr>
  <tr><td>$Q > K$</td><td>← reactivos</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Principio de Le Châtelier</div>
  Si un sistema en equilibrio se perturba, evoluciona en el sentido que <em>contrarresta</em> la perturbación.
  <ul>
    <li><b>Concentración</b>: añadir reactivo → equilibrio se desplaza hacia productos.</li>
    <li><b>Presión</b> (gases): aumentar $p$ → desplaza hacia el lado con menos moles gaseosos.</li>
    <li><b>Temperatura</b>: aumentar $T$ → desplaza en el sentido endotérmico.</li>
    <li><b>Catalizador</b>: NO desplaza el equilibrio.</li>
  </ul>
</div>
"""
            },
        ],
        "ej": [
            {
                "title": "Cinética de primer orden: tiempo de vida media",
                "enunciado": r"La descomposición de N$_2$O$_5$ a 65 °C sigue cinética de primer orden con $k=5{,}2\cdot 10^{-3}\ \text{s}^{-1}$. Calcular: (a) el tiempo de vida media $t_{1/2}$; (b) el tiempo necesario para que se descomponga el 75% de la muestra inicial.",
                "esperado": r"(a) $t_{1/2}=133$ s; (b) $t=267$ s.",
                "datos": [
                    ("Orden", "Primer orden"),
                    ("$k$", "$5{,}2\\cdot 10^{-3}\\ \\text{s}^{-1}$"),
                    ("$\\%$ descompuesto", "75% (queda 25%)"),
                ],
                "demo": {
                    "title": "Ecuación integrada y vida media",
                    "body": r"""
<p>En cinética de primer orden, $-d[A]/dt=k[A]$. Integrando entre $[A]_0$ y $[A]$:</p>
$$\ln\!\dfrac{[A]_0}{[A]}=k\,t \implies [A]=[A]_0\,e^{-kt}$$
<p>El <b>tiempo de vida media</b> es el tiempo en que se descompone la mitad de la muestra:</p>
$$\dfrac{[A]_0}{[A]_0/2}=2 \implies \ln 2 = k\,t_{1/2} \implies \boxed{\;t_{1/2}=\dfrac{\ln 2}{k}\;}$$
<p>Notable: $t_{1/2}$ es <b>independiente de la concentración inicial</b> en cinética de primer orden.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Vida media",
                     "p": "Aplico la fórmula directa.",
                     "b": r"""$$t_{1/2} = \dfrac{\ln 2}{k} = \dfrac{0{,}693}{5{,}2\cdot 10^{-3}} = 133{,}3\ \text{s}$$"""},
                    {"t": "Paso 2 — Tiempo para descomponer el 75%",
                     "p": "Si se descompone el 75%, queda el 25%, es decir $[A]/[A]_0=0{,}25$.",
                     "b": r"""$$\ln\!\dfrac{1}{0{,}25}=k\,t \implies t = \dfrac{\ln 4}{k} = \dfrac{1{,}386}{5{,}2\cdot 10^{-3}}=266{,}5\ \text{s}$$"""},
                ],
                "resultado": r"$t_{1/2}=133$ s · $t_{75\%}=267$ s.",
                "verificacion": r"75% desaparecido = 2 vidas medias (½·½=¼ queda). Por tanto $t_{75\%} = 2\,t_{1/2} = 266$ s ✓."
            },
            {
                "title": "Energía de activación con la ecuación de Arrhenius",
                "enunciado": r"Una reacción duplica su velocidad al pasar de 25 °C a 35 °C. Calcular su energía de activación $E_a$.",
                "esperado": r"$E_a \approx 52{,}9$ kJ/mol.",
                "datos": [
                    ("$T_1$", "298 K"),
                    ("$T_2$", "308 K"),
                    ("$k_2/k_1$", "2"),
                    ("$R$", "$8{,}314$ J/(mol·K)"),
                ],
                "demo": {
                    "title": "Forma diferencial de Arrhenius (dos puntos)",
                    "body": r"""
<p>Tomando logaritmos en $k=A e^{-E_a/RT}$ y restando para dos temperaturas distintas:</p>
$$\ln\!\dfrac{k_2}{k_1} = -\dfrac{E_a}{R}\!\left(\dfrac{1}{T_2}-\dfrac{1}{T_1}\right) = \dfrac{E_a}{R}\cdot\dfrac{T_2-T_1}{T_1 T_2}$$
<p>Despejando $E_a$:</p>
$$E_a = \dfrac{R\,T_1\,T_2}{T_2-T_1}\,\ln\!\dfrac{k_2}{k_1}$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Sustituir valores",
                     "p": "Con $\\ln 2=0{,}693$.",
                     "b": r"""$$E_a = \dfrac{8{,}314\cdot 298\cdot 308}{308-298}\cdot 0{,}693$$
$$E_a = \dfrac{8{,}314\cdot 91\,784}{10}\cdot 0{,}693$$"""},
                    {"t": "Paso 2 — Cálculo final",
                     "p": "Multiplicación y división.",
                     "b": r"""$$E_a = 76\,309{,}9\cdot 0{,}693 = 52\,900\ \text{J/mol}\approx \boxed{52{,}9\ \text{kJ/mol}}$$"""},
                ],
                "resultado": r"$E_a \approx 52{,}9$ kJ/mol — un valor típico para reacciones que doblan velocidad cada $\sim 10$ °C.",
                "verificacion": r"Regla práctica empírica: si $E_a\approx 50$ kJ/mol, una subida de 10 K duplica $k$ alrededor de la temperatura ambiente. ✓"
            },
            {
                "title": "Equilibrio: cálculo de concentraciones a partir de $K_c$",
                "enunciado": r"Para la reacción $\text{H}_2(g)+\text{I}_2(g)\rightleftharpoons 2\text{HI}(g)$, $K_c=54{,}3$ a 425 °C. Si se introducen <b>0,500 mol</b> de H$_2$ y <b>0,500 mol</b> de I$_2$ en un recipiente de <b>1,00 L</b>, calcular las concentraciones en el equilibrio.",
                "esperado": r"$[\text{H}_2]=[\text{I}_2]=0{,}107$ M; $[\text{HI}]=0{,}786$ M.",
                "datos": [
                    ("$K_c$", "54,3 a 425 °C"),
                    ("Iniciales", "$[\\text{H}_2]_0=[\\text{I}_2]_0=0{,}500$ M"),
                    ("Inicial HI", "$[\\text{HI}]_0=0$"),
                ],
                "demo": {
                    "title": "Tabla ICE y resolución",
                    "body": r"""
<p>Llamemos $x$ a los moles/L de H$_2$ que reaccionan. Por estequiometría reaccionan también $x$ de I$_2$ y se forman $2x$ de HI:</p>
<table class="tdatos">
<tr><th></th><th>H$_2$</th><th>I$_2$</th><th>HI</th></tr>
<tr><td>Inicial</td><td>0,500</td><td>0,500</td><td>0</td></tr>
<tr><td>Cambio</td><td>$-x$</td><td>$-x$</td><td>$+2x$</td></tr>
<tr><td>Equilibrio</td><td>$0{,}5-x$</td><td>$0{,}5-x$</td><td>$2x$</td></tr>
</table>
<p>Sustituyendo en $K_c$:</p>
$$K_c = \dfrac{(2x)^2}{(0{,}5-x)^2} = 54{,}3$$
<p>Como tanto numerador como denominador son cuadrados perfectos, podemos sacar raíz cuadrada:</p>
$$\dfrac{2x}{0{,}5-x}=\sqrt{54{,}3}=7{,}37$$
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Resolver para $x$",
                     "p": "Despejo de $2x = 7{,}37(0{,}5-x)$.",
                     "b": r"""$$2x = 3{,}685 - 7{,}37x$$
$$9{,}37x = 3{,}685 \implies x = 0{,}393\ \text{M}$$"""},
                    {"t": "Paso 2 — Concentraciones de equilibrio",
                     "p": "Sustituyo $x$ en la tabla ICE.",
                     "b": r"""$$[\text{H}_2]=[\text{I}_2]=0{,}500-0{,}393=0{,}107\ \text{M}$$
$$[\text{HI}]=2\cdot 0{,}393=0{,}786\ \text{M}$$"""},
                    {"t": "Paso 3 — Verificar $K_c$",
                     "p": "Comprobación numérica.",
                     "b": r"""$$K_c = \dfrac{(0{,}786)^2}{(0{,}107)^2}=\dfrac{0{,}618}{0{,}01145}=54{,}0\;\;✓$$
<p>Coincide con el dato ($\approx 54{,}3$, diferencia por redondeos).</p>"""},
                ],
                "resultado": r"$[\text{H}_2]=[\text{I}_2]=0{,}107$ M, $[\text{HI}]=0{,}786$ M.",
                "verificacion": r"En el equilibrio: 78,6% del HI formado. Como $K_c$ es alto y la mezcla inicial es estequiométrica, hay un alto rendimiento hacia productos. ✓"
            },
        ],
    },

    9: {
        "titulo": "Equilibrio ácido-base",
        "subtitulo": "Definiciones · pH · $K_a/K_b$ · Hidrólisis · Tampones · Valoraciones",
        "secciones": [
            {
                "id": "sec-1",
                "h": "9.1. Definiciones de ácido y base",
                "html": r"""
<table class="tabla">
  <tr><th>Teoría</th><th>Ácido</th><th>Base</th></tr>
  <tr><td>Arrhenius</td><td>Cede H$^+$ en agua</td><td>Cede OH$^-$ en agua</td></tr>
  <tr><td>Brønsted-Lowry</td><td>Dador de H$^+$ (protón)</td><td>Aceptor de H$^+$</td></tr>
  <tr><td>Lewis</td><td>Aceptor de par electrónico</td><td>Dador de par electrónico</td></tr>
</table>
<div class="concept">
  <div class="concept-label">Pares conjugados</div>
  Brønsted introduce el concepto de <em>par ácido-base conjugado</em>:
  $$\text{HA} + \text{H}_2\text{O}\rightleftharpoons \text{A}^- + \text{H}_3\text{O}^+$$
  HA y A$^-$ forman un par conjugado; H$_3$O$^+$ y H$_2$O, otro. Cuanto más fuerte es un ácido, más débil es su base conjugada (y viceversa).
</div>
"""
            },
            {
                "id": "sec-2",
                "h": "9.2. Autoionización del agua. pH y pOH",
                "html": r"""
<p>El agua se autoioniza en pequeñísima medida:</p>
$$2\text{H}_2\text{O}\rightleftharpoons \text{H}_3\text{O}^+ + \text{OH}^-$$
<div class="formula">
  <div class="formula-label">Producto iónico del agua (25 °C)</div>
  $$K_w = [\text{H}_3\text{O}^+][\text{OH}^-] = 1{,}0\cdot 10^{-14}$$
</div>
<div class="formula">
  $$\text{pH} = -\log[\text{H}_3\text{O}^+] \quad \text{pOH} = -\log[\text{OH}^-] \quad \text{pH}+\text{pOH}=14$$
</div>
<table class="tabla">
  <tr><th>pH</th><th>Carácter</th></tr>
  <tr><td>$<7$</td><td>Ácido</td></tr>
  <tr><td>$=7$</td><td>Neutro</td></tr>
  <tr><td>$>7$</td><td>Básico</td></tr>
</table>
<div class="note"><strong>A 25 °C</strong>. Si la temperatura cambia, $K_w$ cambia y el "pH neutro" se desplaza.</div>
"""
            },
            {
                "id": "sec-3",
                "h": "9.3. Ácidos y bases fuertes vs débiles",
                "html": r"""
<p>Un ácido es <strong>fuerte</strong> si se disocia totalmente en agua. Para un monoprótico fuerte $[\text{H}_3\text{O}^+]\approx C_a$ (concentración inicial).</p>
<p>Un ácido <strong>débil</strong> se disocia parcialmente. La constante de equilibrio es:</p>
<div class="formula">
  $$K_a=\dfrac{[\text{A}^-][\text{H}_3\text{O}^+]}{[\text{HA}]}\quad\text{p}K_a=-\log K_a$$
</div>
<p>Para una base débil, análogamente:</p>
<div class="formula">
  $$K_b=\dfrac{[\text{HB}^+][\text{OH}^-]}{[\text{B}]}\quad K_a\cdot K_b = K_w$$
</div>
<div class="concept">
  <div class="concept-label">Cálculo de pH de ácido débil</div>
  Si $C_a\gg K_a$ (aproximación habitual): $[\text{H}_3\text{O}^+]\approx\sqrt{K_a\cdot C_a}$, y por tanto:
  $$\text{pH}\approx\tfrac{1}{2}(\text{p}K_a-\log C_a)$$
</div>
"""
            },
            {
                "id": "sec-4",
                "h": "9.4. Hidrólisis de sales",
                "html": r"""
<p>Las sales pueden alterar el pH al disolverse según el carácter de los iones:</p>
<table class="tabla">
  <tr><th>Sal de</th><th>Catión</th><th>Anión</th><th>pH disolución</th></tr>
  <tr><td>Ácido fuerte + base fuerte</td><td>Inerte</td><td>Inerte</td><td>≈ 7 (neutro)</td></tr>
  <tr><td>Ácido fuerte + base débil</td><td>Hidroliza</td><td>Inerte</td><td>$<7$ (ácido)</td></tr>
  <tr><td>Ácido débil + base fuerte</td><td>Inerte</td><td>Hidroliza</td><td>$>7$ (básico)</td></tr>
  <tr><td>Ácido débil + base débil</td><td>Hidroliza</td><td>Hidroliza</td><td>Depende de $K_a$ vs $K_b$</td></tr>
</table>
<div class="formula">
  <div class="formula-label">Para anión de ácido débil</div>
  $$K_h = \dfrac{K_w}{K_a}$$
</div>
"""
            },
            {
                "id": "sec-5",
                "h": "9.5. Disoluciones reguladoras (tampones)",
                "html": r"""
<p>Un <strong>tampón</strong> es una mezcla de un ácido débil y su base conjugada (o viceversa) en concentraciones similares. Resiste cambios de pH al añadir pequeñas cantidades de ácido o base.</p>
<div class="formula">
  <div class="formula-label">Henderson-Hasselbalch</div>
  $$\text{pH} = \text{p}K_a + \log\!\dfrac{[\text{base}]}{[\text{ácido}]}$$
</div>
<div class="concept">
  <div class="concept-label">Capacidad reguladora máxima</div>
  Cuando $[\text{base}]=[\text{ácido}]$, la pH = p$K_a$ y el tampón resiste mejor las perturbaciones. El rango útil del tampón es típicamente p$K_a\pm 1$.
</div>
<h3>Valoraciones ácido-base</h3>
<p>El <strong>punto de equivalencia</strong> es donde se han añadido moles estequiométricamente equivalentes de valorante. El <em>indicador</em> debe cambiar de color cerca de ese pH.</p>
<table class="tabla">
  <tr><th>Tipo</th><th>pH equivalencia</th><th>Indicador</th></tr>
  <tr><td>HF + BF</td><td>$\approx 7$</td><td>Fenolftaleína (8,2-10) o naranja metilo (3,2-4,4)</td></tr>
  <tr><td>HF + BD</td><td>$<7$</td><td>Naranja metilo</td></tr>
  <tr><td>HD + BF</td><td>$>7$</td><td>Fenolftaleína</td></tr>
</table>
"""
            },
        ],
        "ej": [
            {
                "title": "pH de un ácido débil: ácido acético",
                "enunciado": r"Calcular el pH y el grado de disociación $\alpha$ de una disolución <b>0,100 M</b> de ácido acético (CH$_3$COOH). $K_a = 1{,}8\cdot 10^{-5}$.",
                "esperado": r"pH = 2,87; $\alpha=1{,}34\%$.",
                "datos": [
                    ("$C_a$", "0,100 M"),
                    ("$K_a$", "$1{,}8\\cdot 10^{-5}$"),
                ],
                "demo": {
                    "title": "Tabla ICE y aproximación $C\\gg K_a$",
                    "body": r"""
<p>El equilibrio de disociación es:</p>
$$\text{CH}_3\text{COOH}+\text{H}_2\text{O}\rightleftharpoons\text{CH}_3\text{COO}^- + \text{H}_3\text{O}^+$$
<p>Tabla ICE con $x = [\text{H}_3\text{O}^+]_{eq}$:</p>
<table class="tdatos">
<tr><th></th><th>HA</th><th>A$^-$</th><th>H$_3$O$^+$</th></tr>
<tr><td>Inicial</td><td>0,100</td><td>0</td><td>~0</td></tr>
<tr><td>Cambio</td><td>$-x$</td><td>$+x$</td><td>$+x$</td></tr>
<tr><td>Equilibrio</td><td>$0{,}1-x$</td><td>$x$</td><td>$x$</td></tr>
</table>
<p>$K_a = x^2/(0{,}1-x)$. Si $x\ll 0{,}1$ (válido si $C_a/K_a > 100$): $K_a\approx x^2/0{,}1$, así que $x\approx \sqrt{K_a\cdot C_a}$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Comprobar la aproximación",
                     "p": "$C_a/K_a = 0{,}1/1{,}8\\cdot 10^{-5}=5\\,556 > 100$ ⟹ se puede aproximar.",
                     "b": r"""$$x \approx \sqrt{K_a\cdot C_a}=\sqrt{1{,}8\cdot 10^{-5}\cdot 0{,}1}=\sqrt{1{,}8\cdot 10^{-6}}=1{,}342\cdot 10^{-3}$$"""},
                    {"t": "Paso 2 — Calcular el pH",
                     "p": "$\\text{pH}=-\\log[\\text{H}_3\\text{O}^+]$.",
                     "b": r"""$$\text{pH} = -\log(1{,}342\cdot 10^{-3}) = \boxed{2{,}87}$$"""},
                    {"t": "Paso 3 — Grado de disociación",
                     "p": "$\\alpha = x/C_a$.",
                     "b": r"""$$\alpha = \dfrac{1{,}342\cdot 10^{-3}}{0{,}100}=0{,}0134=\boxed{1{,}34\%}$$"""},
                ],
                "resultado": r"pH = 2,87 · $\alpha = 1{,}34\%$ — solo un 1,3% del ácido se disocia (ácido débil).",
                "verificacion": r"Verificación de la aproximación: $x=1{,}3\cdot 10^{-3}\ll 0{,}1$. Sustituyendo sin aproximar: $K_a=(1{,}34\cdot 10^{-3})^2/(0{,}0987)=1{,}82\cdot 10^{-5}$ ✓ (vs 1,8·10⁻⁵)."
            },
            {
                "title": "Tampón acético/acetato (Henderson-Hasselbalch)",
                "enunciado": r"Calcular el pH de una disolución que contiene <b>0,20 mol</b> de ácido acético y <b>0,30 mol</b> de acetato sódico en <b>1,0 L</b>. ¿Cómo cambia el pH al añadir <b>0,01 mol</b> de HCl (suponiendo $V$ constante)? $K_a = 1{,}8\cdot 10^{-5}$, p$K_a=4{,}74$.",
                "esperado": r"pH inicial = 4,92; pH tras HCl = 4,89 (apenas cambia).",
                "datos": [
                    ("[HA]", "0,20 M"),
                    ("[A$^-$]", "0,30 M"),
                    ("p$K_a$", "4,74"),
                    ("HCl añadido", "0,01 mol"),
                ],
                "demo": {
                    "title": "Henderson-Hasselbalch y respuesta a la perturbación",
                    "body": r"""
<p>En un tampón, partiendo del equilibrio $K_a=[\text{A}^-][\text{H}^+]/[\text{HA}]$ y tomando logaritmos:</p>
$$-\log K_a = -\log\dfrac{[\text{A}^-]}{[\text{HA}]} - \log[\text{H}^+]\implies \text{pH}=\text{p}K_a + \log\dfrac{[\text{A}^-]}{[\text{HA}]}$$
<p>Cuando añadimos un ácido fuerte (HCl), parte del A$^-$ se convierte en HA según:</p>
$$\text{A}^- + \text{H}^+ \to \text{HA}$$
<p>Las nuevas concentraciones se sustituyen en Henderson-Hasselbalch. Como ambos cambios son pequeños frente a las cantidades del tampón, el pH apenas se altera.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — pH inicial",
                     "p": "Aplicar Henderson-Hasselbalch directamente.",
                     "b": r"""$$\text{pH} = 4{,}74 + \log\!\dfrac{0{,}30}{0{,}20} = 4{,}74 + 0{,}176 = \boxed{4{,}92}$$"""},
                    {"t": "Paso 2 — Cantidades tras añadir HCl",
                     "p": "0,01 mol H$^+$ consume 0,01 mol A$^-$ y produce 0,01 mol HA.",
                     "b": r"""$$[\text{HA}]_{nuevo} = 0{,}20+0{,}01 = 0{,}21\ \text{M}$$
$$[\text{A}^-]_{nuevo} = 0{,}30-0{,}01 = 0{,}29\ \text{M}$$"""},
                    {"t": "Paso 3 — pH tras la perturbación",
                     "p": "Misma fórmula, nuevas concentraciones.",
                     "b": r"""$$\text{pH} = 4{,}74 + \log\!\dfrac{0{,}29}{0{,}21} = 4{,}74 + 0{,}140 = \boxed{4{,}88}$$"""},
                ],
                "resultado": r"pH inicial = 4,92 → pH final = 4,88. Cambio de solo 0,04 unidades.",
                "verificacion": r"Comparación: añadir 0,01 mol HCl a <b>agua pura</b> (1 L) daría pH = 2 → cambio de 5 unidades. El tampón reduce el cambio en un factor de $\sim 100$. ✓"
            },
            {
                "title": "Hidrólisis de una sal",
                "enunciado": r"Calcular el pH de una disolución <b>0,10 M</b> de acetato sódico (NaCH$_3$COO). $K_a$ del ácido acético = $1{,}8\cdot 10^{-5}$.",
                "esperado": r"pH = 8,87 (carácter básico).",
                "datos": [
                    ("$C_{sal}$", "0,10 M"),
                    ("$K_a$ acético", "$1{,}8\\cdot 10^{-5}$"),
                    ("$K_w$", "$1{,}0\\cdot 10^{-14}$"),
                ],
                "demo": {
                    "title": "Hidrólisis del anión",
                    "body": r"""
<p>El acetato es la base conjugada de un ácido débil, así que <em>hidroliza</em> en agua:</p>
$$\text{A}^- + \text{H}_2\text{O}\rightleftharpoons \text{HA}+\text{OH}^-$$
<p>La constante de hidrólisis (= $K_b$ del anión) se relaciona con $K_a$ del ácido conjugado:</p>
$$K_b = K_h = \dfrac{K_w}{K_a}$$
<p>El catión Na$^+$ es inerte (no hidroliza). El pH lo determina la hidrólisis del A$^-$.</p>
"""
                },
                "pasos": [
                    {"t": "Paso 1 — Calcular $K_b$",
                     "p": "Aplicando la relación.",
                     "b": r"""$$K_b = \dfrac{K_w}{K_a}=\dfrac{1{,}0\cdot 10^{-14}}{1{,}8\cdot 10^{-5}}=5{,}56\cdot 10^{-10}$$"""},
                    {"t": "Paso 2 — Calcular [OH$^-$]",
                     "p": "Como $C_{sal}/K_b\\gg 100$, aproximación: $[\\text{OH}^-]\\approx\\sqrt{K_b C_{sal}}$.",
                     "b": r"""$$[\text{OH}^-]=\sqrt{5{,}56\cdot 10^{-10}\cdot 0{,}10}=\sqrt{5{,}56\cdot 10^{-11}}=7{,}45\cdot 10^{-6}$$"""},
                    {"t": "Paso 3 — pH a partir de pOH",
                     "p": "$\\text{pH}=14-\\text{pOH}$.",
                     "b": r"""$$\text{pOH}=-\log(7{,}45\cdot 10^{-6})=5{,}13\implies \text{pH}=14-5{,}13=\boxed{8{,}87}$$"""},
                ],
                "resultado": r"pH = 8,87 — disolución <b>básica</b>, como corresponde a una sal de ácido débil + base fuerte.",
                "verificacion": r"Coherencia: el acetato es la base conjugada del ácido acético; al ser su $K_a$ pequeño, $K_b$ es relativamente grande (en su escala) y la hidrólisis genera un pH netamente básico. ✓"
            },
        ],
    },
}


# ─────────────────────────────────────────────────────────────────────
# TEMPLATES HTML
# ─────────────────────────────────────────────────────────────────────

TEORIA_TPL = r"""<!DOCTYPE html>
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
body{padding-top:52px;min-height:100vh;overflow-x:hidden;font-size:15px;line-height:1.65}
.layout{display:flex;min-height:calc(100vh - 52px)}
.sidebar{width:260px;flex-shrink:0;position:fixed;top:52px;left:0;bottom:0;background:rgba(255,255,255,.025);border-right:1px solid var(--line);overflow-y:auto;padding:12px 8px}
.sb-head{padding:8px 12px 12px;border-bottom:1px solid var(--line);margin-bottom:8px}
.sb-subtitle{font-family:var(--mono);font-size:.62em;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:var(--txt3);margin-bottom:4px}
.sb-current{font-size:.78em;font-weight:600;color:var(--violet)}
.sb-section{padding:6px 10px;font-family:var(--mono);font-size:.62em;font-weight:700;color:var(--txt3);letter-spacing:.12em;text-transform:uppercase;margin-top:8px}
.sb-link{display:block;padding:7px 10px;font-size:.82em;color:var(--txt2);border-radius:6px;text-decoration:none;margin-bottom:1px;border-left:2px solid transparent;transition:.15s}
.sb-link:hover{background:rgba(255,255,255,.04);color:var(--txt);text-decoration:none}
.sb-link.active{background:rgba(var(--vr),.12);color:var(--violet);border-left-color:var(--violet);font-weight:600}
.content{flex:1;margin-left:260px;padding:32px 48px 60px;max-width:1100px}
@media(max-width:900px){.sidebar{display:none}.content{margin-left:0;padding:20px 16px 40px}}
.t-head{margin-bottom:28px;padding:18px 22px;background:linear-gradient(135deg,rgba(var(--vr),.08) 0%,transparent 60%);border:1px solid var(--line-v);border-left:3px solid var(--violet);border-radius:0 12px 12px 0}
.t-tag{font-family:var(--mono);font-size:.66em;font-weight:700;color:var(--violet);letter-spacing:.18em;text-transform:uppercase;margin-bottom:4px}
.t-title{font-family:var(--ui);font-size:1.6em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em}
.t-meta{font-family:var(--mono);font-size:.78em;color:var(--txt3);margin-top:6px}
section.sec{margin-bottom:28px;background:var(--s1);border:1px solid var(--line);border-radius:10px;padding:18px 22px}
section.sec h2{font-family:var(--ui);font-size:1.15em;font-weight:700;color:#f1f5f9;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:10px}
section.sec h2::before{content:'';display:inline-block;width:4px;height:18px;background:linear-gradient(180deg,var(--blue),var(--violet));border-radius:2px}
section.sec h3{font-family:var(--ui);font-size:1em;font-weight:600;color:var(--violet);margin:14px 0 8px}
section.sec p{margin:8px 0;color:#cbd5e1}
section.sec ul,section.sec ol{margin:8px 0 8px 20px;color:#cbd5e1}
section.sec li{margin:4px 0}
section.sec b,section.sec strong{color:#f1f5f9;font-weight:600}
.concept{background:rgba(var(--br),.08);border-left:3px solid var(--blue);border-radius:6px;padding:12px 16px;margin:12px 0}
.concept-label{font-family:var(--mono);font-size:.66em;color:var(--blue);font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:4px}
.formula{background:rgba(var(--vr),.06);border-left:3px solid var(--violet);border-radius:6px;padding:10px 16px;margin:10px 0}
.formula-label{font-family:var(--mono);font-size:.66em;color:var(--violet);font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
.note{background:rgba(var(--ar),.08);border:1px solid rgba(var(--ar),.22);border-left:3px solid var(--amber);border-radius:6px;padding:10px 14px;margin:10px 0;font-size:.92em;color:#fed7aa;font-style:italic}
.note strong{color:#fcd34d;font-style:normal}
.tabla{width:100%;border-collapse:collapse;margin:12px 0;font-size:.92em}
.tabla th{background:rgba(var(--vr),.12);color:var(--violet);padding:8px 10px;text-align:left;border:1px solid var(--line-v);font-weight:600}
.tabla td{padding:8px 10px;border:1px solid var(--line);color:#cbd5e1}
.tabla tr:nth-child(even) td{background:rgba(255,255,255,.02)}
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
      <div class="sb-current">T{N} · {TITULO}</div>
    </div>
    <div class="sb-section">Secciones</div>
{SIDEBAR_LINKS}
    <div class="sb-section">Otros temas</div>
{SIDEBAR_OTHER}
    <div class="sb-section">Recursos</div>
    <a class="sb-link" href="../formulario.html">📐 Formulario</a>
    <a class="sb-link" href="../ejercicios/tema{N}.html">📝 Ejercicios T{N}</a>
  </aside>

  <main class="content">

    <div class="t-head">
      <div class="t-tag">Tema {NN}</div>
      <h1 class="t-title">{TITULO}</h1>
      <div class="t-meta">{SUBTITULO}</div>
    </div>

{SECCIONES}

  </main>

</div>

<footer class="qg-footer">
  Química · 1º Grado · 2025-26 &nbsp;·&nbsp; <a href="../index.html">Inicio</a>
</footer>

<script>
function initKatex(){
  if(typeof renderMathInElement === 'undefined') return;
  renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false});
}
document.addEventListener('DOMContentLoaded',initKatex);
const links=document.querySelectorAll('.sb-link[href^="#"]');
const sections=document.querySelectorAll('section.sec');
window.addEventListener('scroll',()=>{
  let current='';
  sections.forEach(s=>{const top=s.offsetTop-80;if(window.scrollY>=top)current=s.id});
  links.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+current));
});
</script>
</body>
</html>
"""


EJ_TPL = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#131313">
<title>T{N} · Ejercicios · Química · {TITULO}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="initKatex && initKatex()"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#131313;
  --surface:rgba(255,255,255,.04);
  --surface2:rgba(255,255,255,.07);
  --border:rgba(255,255,255,.08);
  --border2:rgba(255,255,255,.12);
  --text:#e2e8f0;
  --text2:#94a3b8;
  --text3:#64748b;
  --accent:#c084fc;
  --accent-dim:rgba(192,132,252,.12);
  --accent-border:rgba(192,132,252,.28);
  --gold:#f59e0b;
  --gold-dim:rgba(245,158,11,.1);
  --gold-border:rgba(245,158,11,.28);
  --green:#10b981;
  --blue:#38bdf8;
  --orange:#fb923c;
  --yellow:#ffd93d;
  --ff:'Space Grotesk',system-ui,sans-serif;
  --ff-mono:'JetBrains Mono',monospace;
  --radius:10px;
  --radius-sm:6px;
  --topbar-h:52px;
  --sidebar-w:280px;
  --transition:.22s cubic-bezier(.4,0,.2,1);
}
html{scroll-behavior:smooth}
body{font-family:var(--ff);background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6;font-size:15px;overflow-x:hidden}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
b,strong{color:#f1f5f9;font-weight:600}

.topbar{position:fixed;top:0;left:0;right:0;z-index:300;background:rgba(19,19,19,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);display:flex;align-items:center;height:52px}
.topbar-back{display:flex;align-items:center;gap:8px;padding:0 18px;height:100%;color:var(--text2);font-size:.82em;font-weight:500;border-right:1px solid var(--border);transition:color var(--transition);white-space:nowrap;text-decoration:none}
.topbar-back:hover{color:var(--accent);text-decoration:none}
.topbar-back svg{transition:transform var(--transition)}
.topbar-back:hover svg{transform:translateX(-3px)}
.topbar-title{padding:0 16px;flex:1;font-size:.88em;font-weight:600;color:#f1f5f9;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}

.tema-picker{position:relative;margin-right:16px}
.tema-picker-btn{background:var(--accent-dim);border:1px solid var(--accent-border);border-radius:20px;padding:4px 13px;font-size:.72em;font-weight:700;color:var(--accent);cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;transition:.15s;font-family:var(--ff)}
.tema-picker-btn:hover{background:rgba(192,132,252,.2)}
.tema-dropdown{display:none;position:absolute;right:0;top:calc(100% + 8px);background:rgba(19,19,19,.98);border:1px solid var(--accent-border);border-radius:10px;padding:6px;min-width:240px;z-index:300;box-shadow:0 8px 32px rgba(0,0,0,.85)}
.tema-picker.open .tema-dropdown{display:block}
.td-item{display:block;padding:7px 11px;border-radius:6px;font-size:.79em;text-decoration:none;transition:.15s;white-space:nowrap;font-weight:500;color:#e2e8f0}
.td-item:hover{background:var(--accent-dim);color:var(--accent)}
.td-item.td-active{color:var(--accent);background:var(--accent-dim);font-weight:700;pointer-events:none}
.td-num{display:inline-block;width:28px;font-weight:700;color:var(--accent)}

.layout{display:flex;padding-top:52px;min-height:calc(100vh - 52px)}

.sidebar{width:var(--sidebar-w);flex-shrink:0;position:fixed;top:52px;left:0;bottom:0;background:rgba(255,255,255,.025);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
.sb-head{padding:12px 12px 8px;border-bottom:1px solid var(--border);flex-shrink:0}
.sb-subtitle{font-size:.68em;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--text3);margin-bottom:3px}
.sb-current{font-size:.74em;font-weight:600;color:var(--accent);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-height:1.1em}
.sb-list{flex:1;overflow-y:auto;padding:5px 5px 16px}
.sb-item{width:100%;display:flex;align-items:center;gap:8px;padding:6px 9px;border-radius:var(--radius-sm);background:none;border:1px solid transparent;color:var(--text2);font-family:var(--ff);font-size:.78em;cursor:pointer;text-align:left;transition:all var(--transition);margin-bottom:1px}
.sb-item:hover{background:var(--surface);color:var(--text)}
.sb-item.active{background:var(--accent-dim);color:var(--accent);border-color:var(--accent-border)}
.sb-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;min-width:30px;color:inherit;opacity:.75;flex-shrink:0}
.sb-name{flex:1;font-weight:500;line-height:1.3;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sb-footer{padding:7px 10px;border-top:1px solid var(--border);flex-shrink:0;display:flex;flex-direction:column;gap:5px}
.sb-link{display:flex;align-items:center;gap:6px;padding:5px 8px;border-radius:var(--radius-sm);font-size:.76em;font-weight:600;text-decoration:none;transition:background var(--transition)}
.sb-link-purple{background:var(--accent-dim);border:1px solid var(--accent-border);color:var(--accent)}
.sb-link-purple:hover{background:rgba(192,132,252,.2)}
.sb-link-gold{background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);color:var(--gold)}
.sb-link-gold:hover{background:rgba(245,158,11,.15)}

.content{flex:1;margin-left:var(--sidebar-w);padding:28px 40px 60px;min-width:0}

.topic-panel{display:none;max-width:860px}
.topic-panel.active{display:block;animation:tpFadeIn .18s ease forwards}
@keyframes tpFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

.panel-header{margin-bottom:24px;padding:14px 18px 16px;background:linear-gradient(135deg,rgba(192,132,252,.06) 0%,transparent 60%);border:1px solid rgba(192,132,252,.18);border-left:3px solid var(--accent);border-radius:0 var(--radius) var(--radius) 0}
.panel-tag{font-family:var(--ff-mono);font-size:.68em;font-weight:700;color:var(--accent);opacity:.8;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px}
.panel-title{font-size:1.3em;font-weight:700;color:#f1f5f9;letter-spacing:-.02em;line-height:1.3}
.panel-meta{font-size:.78em;color:var(--text3);margin-top:5px}

.read-progress{position:fixed;top:52px;left:var(--sidebar-w);right:0;height:2px;z-index:200;background:linear-gradient(90deg,var(--accent),var(--blue));transform-origin:left;transform:scaleX(0);transition:transform .08s linear}

::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:rgba(192,132,252,.18);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(192,132,252,.35)}

@media(max-width:768px){
  body{font-size:17px}
  .sidebar{position:static;width:100%;height:auto;border-right:none;border-bottom:1px solid var(--border)}
  .layout{flex-direction:column}
  .content{margin-left:0;padding:20px 16px 40px}
  .sb-list{max-height:200px}
  .read-progress{left:0}
  .katex{font-size:1.05em}
}

.section-wrap{margin-bottom:14px;border-radius:var(--radius-sm);overflow:hidden}
.sec-btn{width:100%;text-align:left;padding:10px 13px;border:none;border-radius:var(--radius-sm);cursor:pointer;font-size:.86em;font-weight:600;letter-spacing:.3px;transition:var(--transition);display:flex;justify-content:space-between;align-items:center;font-family:var(--ff)}
.sec-btn .sarr{transition:.2s;flex-shrink:0}
.sec-open .sec-btn .sarr{transform:rotate(180deg)}
.sec-body{display:none;border-radius:0 0 var(--radius-sm) var(--radius-sm);padding:13px 15px;font-size:.86em;line-height:1.75}
.sec-open .sec-body{display:block}

.s-datos .sec-btn{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}
.s-datos .sec-body{background:rgba(192,132,252,.04);border:1px solid var(--accent-border);border-top:none}
.s-teoria .sec-btn{background:rgba(251,146,60,.1);color:var(--orange);border:1px solid rgba(251,146,60,.25)}
.s-teoria .sec-body{background:rgba(251,146,60,.05);border:1px solid rgba(251,146,60,.2);border-top:none}
.s-resolucion .sec-btn{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.25)}
.s-resolucion .sec-body{background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-top:none}

.enunciado{background:var(--surface2);border-radius:var(--radius-sm);padding:13px 15px;font-size:.87em;line-height:1.75;margin-bottom:14px;border-left:3px solid var(--accent-border)}

.t-datos{width:100%;border-collapse:collapse;font-size:.84em}
.t-datos th{background:var(--accent-dim);color:var(--accent);padding:7px 10px;text-align:left;border:1px solid var(--accent-border)}
.t-datos td{padding:7px 10px;border:1px solid var(--border);color:var(--text2)}
.t-datos tr:nth-child(even) td{background:rgba(192,132,252,.04)}

.paso{margin-bottom:13px;padding:10px 13px;background:rgba(16,185,129,.06);border-radius:var(--radius-sm);border-left:3px solid rgba(16,185,129,.4)}
.paso-titulo{color:var(--green);font-size:.78em;font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px}
.porque{font-size:.83em;color:#94a3b8;font-style:italic;margin-bottom:6px}
.porque b{color:var(--orange);font-style:normal}

.resultado-final{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.3);border-radius:var(--radius-sm);padding:11px 15px;margin-top:12px}
.rf-label{font-size:.7em;color:var(--green);text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px;font-weight:700}
.rf-val{color:#d1fae5;font-size:.9em;line-height:1.9}

.verificacion{background:rgba(56,189,248,.06);border:1px solid rgba(56,189,248,.25);border-left:3px solid #38bdf8;border-radius:var(--radius-sm);padding:10px 14px;margin-top:10px;font-size:.82em;color:#bae6fd}
.verificacion .vlabel{font-family:var(--ff-mono);font-size:.7em;color:#38bdf8;text-transform:uppercase;letter-spacing:.5px;font-weight:700;margin-bottom:4px;display:block}

.katex{font-size:1.04em}
.katex-display{overflow-x:auto;overflow-y:hidden}
.footer{text-align:center;padding:40px 20px;color:var(--text3);font-size:.78em}

.empty-state{text-align:center;padding:80px 20px;color:var(--text3)}
</style>
</head>
<body>

<nav class="topbar">
  <a class="topbar-back" href="index.html">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
    Ejercicios
  </a>
  <span class="topbar-title">Química · T{N} <span style="color:var(--accent)">· {TITULO}</span></span>
  <div class="tema-picker" id="temaPicker">
    <button class="tema-picker-btn" onclick="this.closest('.tema-picker').classList.toggle('open')">T{N} ▾</button>
    <div class="tema-dropdown">
{TEMA_DROPDOWN}
    </div>
  </div>
</nav>

<div class="read-progress" id="readProgress"></div>

<div class="layout">
  <aside class="sidebar">
    <div class="sb-head">
      <div class="sb-subtitle">T{N} · {TITULO}</div>
      <div class="sb-current" id="sbCurrent"></div>
    </div>
    <div class="sb-list">
{SIDEBAR_ITEMS}
    </div>
    <div class="sb-footer">
      <a class="sb-link sb-link-purple" href="../teoria/tema{N}.html">
        <svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Teoría
      </a>
      <a class="sb-link sb-link-gold" href="../formulario.html">📐 Formulario</a>
    </div>
  </aside>

  <main class="content">
{PANELES}
  </main>
</div>

<div class="footer">Química · 1.º Grado · 2025-26 &nbsp;·&nbsp; <a href="../index.html">Inicio</a></div>

<script>
function initKatex(){
  if(typeof renderMathInElement==='undefined') return;
  renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false});
}

document.addEventListener('DOMContentLoaded', function(){
  initKatex();
  var panels = document.querySelectorAll('.topic-panel');
  if(panels.length>0) showEx(panels[0].id);
});

function showEx(id){
  document.querySelectorAll('.topic-panel').forEach(function(p){p.classList.remove('active')});
  document.querySelectorAll('.sb-item').forEach(function(b){b.classList.remove('active')});
  var panel = document.getElementById(id);
  if(panel) panel.classList.add('active');
  var btn = document.querySelector('[data-id="'+id+'"]');
  if(btn){
    btn.classList.add('active');
    var name = btn.querySelector('.sb-name');
    var curr = document.getElementById('sbCurrent');
    if(curr && name) curr.textContent = name.textContent;
  }
  window.scrollTo({top:0,behavior:'instant'});
  updateProgress();
}

function toggleSec(btn){
  var wrap = btn.closest('.section-wrap');
  wrap.classList.toggle('sec-open');
  if(wrap.classList.contains('sec-open') && typeof renderMathInElement!=='undefined'){
    renderMathInElement(wrap,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false});
  }
}

function updateProgress(){
  var bar = document.getElementById('readProgress');
  if(!bar) return;
  var scrolled = window.scrollY;
  var total = document.body.scrollHeight - window.innerHeight;
  bar.style.transform = 'scaleX('+(total>0?Math.min(scrolled/total,1):0)+')';
}
window.addEventListener('scroll', updateProgress, {passive:true});

document.addEventListener('click', function(e){
  var picker = document.getElementById('temaPicker');
  if(picker && !picker.contains(e.target)) picker.classList.remove('open');
});
</script>
</body>
</html>
"""



# ─────────────────────────────────────────────────────────────────────
# GENERACIÓN
# ─────────────────────────────────────────────────────────────────────

def render_teoria(n, data):
    nn = f"{n:02d}"
    sidebar_links = "\n".join(
        f'    <a class="sb-link" href="#{s["id"]}">{s["h"]}</a>'
        for s in data["secciones"]
    )

    sidebar_other = []
    for k in [n - 1, n + 1]:
        if 1 <= k <= 9:
            arrow = "←" if k < n else "→"
            t = TEMAS.get(k)
            label = t["titulo"] if t else (
                {5: "Termodinámica química"}.get(k, f"Tema {k}")
            )
            sidebar_other.append(f'    <a class="sb-link" href="tema{k}.html">{arrow} T{k} {label}</a>')
    sidebar_other_str = "\n".join(sidebar_other)

    secciones_html = []
    for s in data["secciones"]:
        secciones_html.append(f'    <section class="sec" id="{s["id"]}">\n      <h2>{s["h"]}</h2>\n{s["html"]}\n    </section>')
    secciones_str = "\n\n".join(secciones_html)

    return (TEORIA_TPL
            .replace("{N}", str(n))
            .replace("{NN}", nn)
            .replace("{TITULO}", data["titulo"])
            .replace("{SUBTITULO}", data["subtitulo"])
            .replace("{SIDEBAR_LINKS}", sidebar_links)
            .replace("{SIDEBAR_OTHER}", sidebar_other_str)
            .replace("{SECCIONES}", secciones_str))


_TEMA_TITULOS = {
    1: "Conceptos generales",
    2: "Estructura atómica",
    3: "Enlace químico",
    4: "Estados de la materia",
    5: "Termodinámica química",
    6: "Termoquímica",
    7: "Espontaneidad y energía libre",
    8: "Cinética y equilibrio",
    9: "Equilibrio ácido-base",
}


def _short_title(title, max_chars=44):
    """Devuelve título corto para sidebar, sin LaTeX visible."""
    import re
    t = re.sub(r'\$[^$]*\$', '', title)
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    t = re.sub(r'[{}_^\\]', '', t).strip()
    if len(t) > max_chars:
        t = t[:max_chars - 1].rstrip() + "…"
    return t or title


def render_ejercicios(n, data):
    extra = EJERCICIOS_EXTRA.get(n, [])
    todos_ej = list(data["ej"]) + list(extra)
    nn = f"{n:02d}"

    # Tema dropdown (todos los temas con el actual marcado)
    tema_drop_lines = []
    for k in range(1, 10):
        cls = "td-active" if k == n else ""
        tema_drop_lines.append(
            f'    <a class="td-item {cls}" href="tema{k}.html"><span class="td-num">T{k}</span> {_TEMA_TITULOS[k]}</a>'
        )
    tema_dropdown = "\n".join(tema_drop_lines)

    # Sidebar items
    sidebar_lines = []
    for i, ej in enumerate(todos_ej):
        idx = i + 1
        ex_id = f"ex{n}-{idx}"
        sb_name = _short_title(ej["title"], max_chars=42)
        sidebar_lines.append(
            f'      <button class="sb-item" onclick="showEx(\'{ex_id}\')" data-id="{ex_id}">\n'
            f'        <span class="sb-tag">{n}.{idx}</span>\n'
            f'        <span class="sb-name">{sb_name}</span>\n'
            f'      </button>'
        )
    sidebar_items = "\n".join(sidebar_lines)

    # Topic panels
    paneles = []
    for i, ej in enumerate(todos_ej):
        idx = i + 1
        ex_id = f"ex{n}-{idx}"
        datos_rows = "\n".join(
            f"            <tr><td>{lbl}</td><td>{val}</td></tr>"
            for lbl, val in ej["datos"]
        )
        pasos_html = "\n".join(
            f"""          <div class="paso">
            <div class="paso-titulo">{p["t"]}</div>
            <p class="porque"><b>¿Por qué?</b> {p["p"]}</p>
            {p["b"]}
          </div>"""
            for p in ej["pasos"]
        )

        teoria_section = ""
        if ej.get("demo"):
            teoria_section = f"""
    <div class="section-wrap s-teoria sec-open">
      <button class="sec-btn" onclick="toggleSec(this)">📐 Fundamento teórico — {ej["demo"]["title"]} <span class="sarr">▾</span></button>
      <div class="sec-body">
{ej["demo"]["body"]}
      </div>
    </div>
"""

        verif_html = ""
        if ej.get("verificacion"):
            verif_html = f"""
    <div class="verificacion">
      <span class="vlabel">✓ Verificación</span>
      {ej["verificacion"]}
    </div>"""

        meta_html = ""
        if ej.get("esperado"):
            meta_html = f'<div class="panel-meta">Resultado: {ej["esperado"]}</div>'

        paneles.append(f"""  <div class="topic-panel" id="{ex_id}">
    <div class="panel-header">
      <div class="panel-tag">Ejercicio {n}.{idx}</div>
      <h1 class="panel-title">{ej["title"]}</h1>
      {meta_html}
    </div>

    <div class="enunciado">
      {ej["enunciado"]}
    </div>

    <div class="section-wrap s-datos sec-open">
      <button class="sec-btn" onclick="toggleSec(this)">📋 Datos <span class="sarr">▼</span></button>
      <div class="sec-body">
        <table class="t-datos">
          <tr><th>Magnitud</th><th>Valor</th></tr>
{datos_rows}
        </table>
      </div>
    </div>
{teoria_section}
    <div class="section-wrap s-resolucion sec-open">
      <button class="sec-btn" onclick="toggleSec(this)">🔢 Resolución paso a paso <span class="sarr">▾</span></button>
      <div class="sec-body">
{pasos_html}

        <div class="resultado-final">
          <div class="rf-label">Resultado</div>
          <div class="rf-val">{ej["resultado"]}</div>
        </div>
      </div>
    </div>{verif_html}
  </div>""")

    paneles_html = "\n".join(paneles)

    return (EJ_TPL
            .replace("{N}", str(n))
            .replace("{NN}", nn)
            .replace("{TITULO}", data["titulo"])
            .replace("{TEMA_DROPDOWN}", tema_dropdown)
            .replace("{SIDEBAR_ITEMS}", sidebar_items)
            .replace("{PANELES}", paneles_html))


def main():
    TEORIA.mkdir(exist_ok=True)
    EJ.mkdir(exist_ok=True)
    for n, data in TEMAS.items():
        teoria_path = TEORIA / f"tema{n}.html"
        teoria_path.write_text(render_teoria(n, data), encoding="utf-8")
        print(f"  · {teoria_path.relative_to(ROOT)}")

        ej_path = EJ / f"tema{n}.html"
        ej_path.write_text(render_ejercicios(n, data), encoding="utf-8")
        print(f"  · {ej_path.relative_to(ROOT)}")
    print(f"OK — generados {len(TEMAS)*2} ficheros.")


if __name__ == "__main__":
    main()
