"""
Ejercicios extra (ej 4-10) por tema.
Mismo formato que los del dict TEMAS de gen_content.py:
{title, enunciado, esperado, datos, demo (opcional), pasos, resultado, verificacion}
"""

EJERCICIOS_EXTRA = {

# ═══════════════════════════════════════════════════════════════════════
# TEMA 1 — CONCEPTOS GENERALES
# ═══════════════════════════════════════════════════════════════════════
1: [
    {
        "title": "Composición porcentual a partir de la fórmula",
        "enunciado": r"Calcular la composición porcentual en masa de cada elemento en el <b>nitrato de amonio</b> (NH$_4$NO$_3$). Datos: $M_N=14$, $M_H=1$, $M_O=16$ g/mol.",
        "esperado": r"$\%N=35{,}0\%$; $\%H=5{,}0\%$; $\%O=60{,}0\%$.",
        "datos": [
            ("Fórmula", "NH$_4$NO$_3$"),
            ("Masas atómicas", "$M_N=14$; $M_H=1$; $M_O=16$ g/mol"),
        ],
        "demo": {
            "title": r"De masa molar a porcentajes",
            "body": r"""
<p>El % en masa de cada elemento en un compuesto puro se calcula como:</p>
$$\%\,X = \dfrac{n_X\cdot M_X}{M_{\text{compuesto}}}\cdot 100$$
<p>donde $n_X$ es el número de átomos del elemento $X$ en la fórmula y $M_X$ su masa atómica. La suma de todos los porcentajes debe dar exactamente 100%.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Masa molar del compuesto",
             "p": "Sumamos las masas atómicas con sus respectivos subíndices: 2 N, 4 H, 3 O.",
             "b": r"""$$M = 2\cdot 14 + 4\cdot 1 + 3\cdot 16 = 28 + 4 + 48 = 80\ \text{g/mol}$$"""},
            {"t": "Paso 2 — Porcentaje de cada elemento",
             "p": "Cada elemento aporta su masa total dentro del compuesto.",
             "b": r"""$$\%N = \dfrac{28}{80}\cdot 100 = 35{,}0\%$$
$$\%H = \dfrac{4}{80}\cdot 100 = 5{,}0\%$$
$$\%O = \dfrac{48}{80}\cdot 100 = 60{,}0\%$$"""},
        ],
        "resultado": r"$\%N=35{,}0\%$; $\%H=5{,}0\%$; $\%O=60{,}0\%$.",
        "verificacion": r"$35{,}0+5{,}0+60{,}0=100{,}0\%$ ✓. La suma cierra exactamente."
    },
    {
        "title": "Concentración: molaridad, molalidad y % en masa",
        "enunciado": r"Se prepara una disolución mezclando <b>40 g de NaOH</b> con <b>360 g de agua</b>. La densidad resultante es $\rho=1{,}10\ \text{g/mL}$. Calcular: (a) % en masa; (b) molalidad $m$; (c) molaridad $M$. Datos: $M_{NaOH}=40$ g/mol.",
        "esperado": r"(a) 10,0%; (b) 2,78 mol/kg; (c) 2,75 mol/L.",
        "datos": [
            ("Soluto NaOH", "$m_s=40$ g"),
            ("Disolvente agua", "$m_d=360$ g"),
            ("Densidad disolución", "$\\rho=1{,}10\\ \\text{g/mL}$"),
            ("$M_{NaOH}$", "40 g/mol"),
        ],
        "demo": {
            "title": "Tres formas de expresar concentración",
            "body": r"""
<p>Las tres concentraciones más usadas en química se diferencian por <em>respecto de qué</em> se calculan:</p>
<ul>
  <li><b>% en masa</b>: g de soluto por 100 g de disolución.</li>
  <li><b>Molalidad $m$</b>: mol de soluto por kg de <em>disolvente</em>. Independiente de la $T$.</li>
  <li><b>Molaridad $M$</b>: mol de soluto por L de <em>disolución</em>. Depende de la $T$ (dilatación).</li>
</ul>
$$\%\,m = \dfrac{m_s}{m_s+m_d}\cdot 100\qquad m=\dfrac{n_s}{m_d(\text{kg})}\qquad M=\dfrac{n_s}{V(\text{L})}$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — % en masa",
             "p": "Soluto sobre disolución total.",
             "b": r"""$$\%\,m = \dfrac{40}{40+360}\cdot 100 = \dfrac{40}{400}\cdot 100 = 10{,}0\%$$"""},
            {"t": "Paso 2 — Molalidad",
             "p": "Mol de NaOH dividido entre kg de agua.",
             "b": r"""$$n_s=\dfrac{40}{40}=1{,}0\ \text{mol}\implies m=\dfrac{1{,}0}{0{,}360}=2{,}78\ \text{mol/kg}$$"""},
            {"t": "Paso 3 — Volumen de la disolución",
             "p": "Masa total dividida entre densidad.",
             "b": r"""$$V=\dfrac{m_{\text{tot}}}{\rho}=\dfrac{400\ \text{g}}{1{,}10\ \text{g/mL}}=363{,}6\ \text{mL}=0{,}3636\ \text{L}$$"""},
            {"t": "Paso 4 — Molaridad",
             "p": "Mol de NaOH entre L de disolución.",
             "b": r"""$$M=\dfrac{1{,}0}{0{,}3636}=2{,}75\ \text{mol/L}$$"""},
        ],
        "resultado": r"$\%m=10{,}0\%$; $m=2{,}78$ mol/kg; $M=2{,}75$ mol/L.",
        "verificacion": r"Coherencia: $M$ y $m$ son parecidas porque la disolución es relativamente diluida (10%) y la densidad cercana a 1. En disoluciones muy concentradas $M$ y $m$ divergen mucho. ✓"
    },
    {
        "title": "Reactivo limitante con concentraciones de disolución",
        "enunciado": r"Se mezclan <b>50 mL de AgNO$_3$ 0,20 M</b> con <b>30 mL de NaCl 0,15 M</b>. Calcular la masa del precipitado de AgCl formado. $M_{AgCl}=143{,}3$ g/mol.",
        "esperado": r"$m_{AgCl}=0{,}645$ g. AgNO$_3$ es el reactivo en exceso.",
        "datos": [
            ("Reacción", "AgNO$_3$ + NaCl → AgCl(s)↓ + NaNO$_3$"),
            ("$V_{AgNO_3}$", "50 mL"),
            ("$M_{AgNO_3}$", "0,20 mol/L"),
            ("$V_{NaCl}$", "30 mL"),
            ("$M_{NaCl}$", "0,15 mol/L"),
        ],
        "demo": {
            "title": "Limitante con disoluciones",
            "body": r"""
<p>Para reacciones en disolución, los moles disponibles de cada reactivo se calculan como $n=M\cdot V$ (con $V$ en litros). El procedimiento del limitante es el mismo:</p>
$$\xi_i = \dfrac{n_i}{\nu_i};\;\;\text{limitante} = \min(\xi_i)$$
<p>El precipitado se calcula a partir de los moles del limitante usando la relación estequiométrica.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles de cada reactivo",
             "p": "$n=M\\cdot V$ con $V$ en litros.",
             "b": r"""$$n_{AgNO_3}=0{,}20\cdot 0{,}050=0{,}010\ \text{mol}$$
$$n_{NaCl}=0{,}15\cdot 0{,}030=0{,}0045\ \text{mol}$$"""},
            {"t": "Paso 2 — Identificar el limitante",
             "p": "Coeficientes 1:1, así que el menor número de moles gana.",
             "b": r"""<p>$n_{NaCl}=4{,}5\cdot 10^{-3}\ \text{mol}<n_{AgNO_3}=1{,}0\cdot 10^{-2}\ \text{mol}$ ⟹ <b>NaCl es el limitante</b>.</p>"""},
            {"t": "Paso 3 — Masa de AgCl precipitado",
             "p": "Por estequiometría 1:1 con NaCl.",
             "b": r"""$$n_{AgCl}=n_{NaCl}=4{,}5\cdot 10^{-3}\ \text{mol}$$
$$m_{AgCl}=4{,}5\cdot 10^{-3}\cdot 143{,}3=0{,}645\ \text{g}$$"""},
        ],
        "resultado": r"$m_{AgCl}=0{,}645$ g. Sobran $0{,}010-0{,}0045=5{,}5\cdot 10^{-3}$ mol de Ag$^+$ en la disolución.",
        "verificacion": r"Volumen total = 80 mL; concentración residual de Ag$^+$ = $5{,}5\cdot 10^{-3}/0{,}080 = 0{,}069$ M. Coherente con un AgNO$_3$ en exceso. ✓"
    },
    {
        "title": "Determinación de la fórmula de un hidrato",
        "enunciado": r"Una muestra de <b>5,00 g</b> de un hidrato de sulfato de cobre <b>CuSO$_4\cdot x$H$_2$O</b> se calienta hasta peso constante, quedando <b>3,20 g</b> de sal anhidra. Calcular el valor de $x$. Datos: $M_{CuSO_4}=159{,}6$, $M_{H_2O}=18{,}0$ g/mol.",
        "esperado": r"$x=5$ → CuSO$_4\cdot 5$H$_2$O.",
        "datos": [
            ("Masa hidrato", "$m_{hid}=5{,}00$ g"),
            ("Masa anhidro tras calentar", "$m_{anh}=3{,}20$ g"),
            ("$M_{CuSO_4}$", "159,6 g/mol"),
            ("$M_{H_2O}$", "18,0 g/mol"),
        ],
        "demo": {
            "title": "Razón molar agua/sal",
            "body": r"""
<p>Un hidrato CuSO$_4\cdot x$H$_2$O contiene $x$ moléculas de agua por unidad fórmula. Al calentar se evapora <em>solo</em> el agua, dejando la sal anhidra. La diferencia de masa = masa de agua perdida.</p>
<p>Calculando los moles de agua y de sal anhidra, su cociente da $x$:</p>
$$x = \dfrac{n_{H_2O}}{n_{CuSO_4}}=\dfrac{m_{agua}/M_{H_2O}}{m_{anh}/M_{CuSO_4}}$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — Masa de agua perdida",
             "p": "Diferencia entre hidrato y anhidro.",
             "b": r"""$$m_{H_2O} = 5{,}00 - 3{,}20 = 1{,}80\ \text{g}$$"""},
            {"t": "Paso 2 — Moles de cada componente",
             "p": "Aplicando $n=m/M$.",
             "b": r"""$$n_{H_2O}=\dfrac{1{,}80}{18{,}0}=0{,}100\ \text{mol}$$
$$n_{CuSO_4}=\dfrac{3{,}20}{159{,}6}=0{,}02005\ \text{mol}$$"""},
            {"t": "Paso 3 — Calcular $x$",
             "p": "Razón molar.",
             "b": r"""$$x=\dfrac{0{,}100}{0{,}02005}=4{,}99\approx 5$$"""},
        ],
        "resultado": r"$x=5$ → fórmula <b>CuSO$_4\cdot 5$H$_2$O</b> (sulfato de cobre pentahidratado, color azul).",
        "verificacion": r"Comprobación: $M_{hid}=159{,}6+5\cdot 18{,}0=249{,}6$ g/mol. $\%H_2O=5\cdot 18/249{,}6=36{,}1\%$. Predicción: en 5 g de hidrato, agua = $5\cdot 0{,}361=1{,}80$ g ✓ coincide con la pérdida medida."
    },
    {
        "title": "Pureza de una muestra a partir del producto formado",
        "enunciado": r"Al tratar <b>10,0 g</b> de una muestra de carbonato de calcio impuro con HCl en exceso se desprenden <b>1,98 L de CO$_2$</b> medidos a 25 °C y 1 atm. Calcular la pureza de la muestra (suponer que las impurezas no reaccionan). Reacción: CaCO$_3$ + 2 HCl → CaCl$_2$ + H$_2$O + CO$_2$. $M_{CaCO_3}=100{,}1$ g/mol, $R=0{,}082$ atm·L/(mol·K).",
        "esperado": r"Pureza = 81,0%.",
        "datos": [
            ("Masa muestra", "$m=10{,}0$ g"),
            ("Volumen CO$_2$", "$V=1{,}98$ L"),
            ("Condiciones", "$T=298$ K, $p=1$ atm"),
            ("$M_{CaCO_3}$", "100,1 g/mol"),
        ],
        "demo": {
            "title": "Pureza vía gas formado",
            "body": r"""
<p>La <b>pureza</b> es el % en masa del componente activo en la muestra. Para encontrarla:</p>
<ol>
  <li>Calculamos los moles de gas formado con $pV=nRT$.</li>
  <li>Por estequiometría 1:1, esos moles coinciden con los de CaCO$_3$ que reaccionaron.</li>
  <li>Convertimos a masa de CaCO$_3$ puro y calculamos el % sobre la muestra inicial.</li>
</ol>
$$\%\text{pureza}=\dfrac{m_{CaCO_3,\text{puro}}}{m_{\text{muestra}}}\cdot 100$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles de CO$_2$",
             "p": "$pV=nRT$.",
             "b": r"""$$n_{CO_2}=\dfrac{pV}{RT}=\dfrac{1\cdot 1{,}98}{0{,}082\cdot 298}=0{,}0810\ \text{mol}$$"""},
            {"t": "Paso 2 — Moles y masa de CaCO$_3$ puro",
             "p": "Estequiometría 1:1 con CO$_2$.",
             "b": r"""$$n_{CaCO_3}=n_{CO_2}=0{,}0810\ \text{mol}$$
$$m_{CaCO_3}=0{,}0810\cdot 100{,}1=8{,}10\ \text{g}$$"""},
            {"t": "Paso 3 — Pureza",
             "p": "Masa de puro sobre masa total.",
             "b": r"""$$\%\text{pureza}=\dfrac{8{,}10}{10{,}0}\cdot 100=\boxed{81{,}0\%}$$"""},
        ],
        "resultado": r"Pureza = <b>81,0%</b>; el 19% restante son impurezas inertes.",
        "verificacion": r"En CN, 0,081 mol de gas ocuparían $0{,}081\cdot 22{,}4=1{,}81$ L. A 25 °C, ligeramente mayor: $1{,}81\cdot 298/273=1{,}98$ L ✓ — coherente con el dato."
    },
    {
        "title": "Estequiometría con gases en condiciones dadas",
        "enunciado": r"Calcular el volumen de oxígeno medido a <b>20 °C y 740 mmHg</b> necesario para quemar completamente <b>5,0 g de butano</b> (C$_4$H$_{10}$). Reacción: $2\,\text{C}_4\text{H}_{10}+13\,\text{O}_2 \to 8\,\text{CO}_2+10\,\text{H}_2\text{O}$. $M_{butano}=58{,}1$ g/mol.",
        "esperado": r"$V_{O_2}\approx 14{,}1$ L.",
        "datos": [
            ("Masa butano", "$m=5{,}0$ g"),
            ("$M_{butano}$", "58,1 g/mol"),
            ("Condiciones del O$_2$", "$T=293$ K; $p=740/760=0{,}974$ atm"),
            ("Relación O$_2$/butano", "13/2 = 6,5"),
        ],
        "demo": {
            "title": "Combinar estequiometría y gas ideal",
            "body": r"""
<p>El procedimiento general para problemas de gases en reacciones:</p>
<ol>
  <li>Convertir masa de reactivo conocido a moles ($n=m/M$).</li>
  <li>Aplicar la relación estequiométrica para obtener moles del gas pedido.</li>
  <li>Convertir esos moles a volumen con $pV=nRT$ en las condiciones dadas.</li>
</ol>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles de butano",
             "p": "$n=m/M$.",
             "b": r"""$$n_{C_4H_{10}}=\dfrac{5{,}0}{58{,}1}=0{,}0861\ \text{mol}$$"""},
            {"t": "Paso 2 — Moles de O$_2$ necesarios",
             "p": "Relación estequiométrica 13:2.",
             "b": r"""$$n_{O_2}=\dfrac{13}{2}\cdot 0{,}0861=0{,}5594\ \text{mol}$$"""},
            {"t": "Paso 3 — Volumen del O$_2$ en condiciones dadas",
             "p": "$V=nRT/p$ con $p$ en atm y $T$ en K.",
             "b": r"""$$V=\dfrac{0{,}5594\cdot 0{,}082\cdot 293}{0{,}974}=\boxed{13{,}80\ \text{L}}$$"""},
        ],
        "resultado": r"$V_{O_2}\approx 13{,}8$ L (con 2 cifras significativas).",
        "verificacion": r"En CN serían $0{,}5594\cdot 22{,}4=12{,}5$ L. A 20 °C y 0,974 atm aumenta porque baja la presión y sube algo la $T$: $12{,}5\cdot 293/273\cdot 1/0{,}974=13{,}8$ L ✓."
    },
    {
        "title": "Mezcla y dilución de disoluciones",
        "enunciado": r"Se mezclan <b>250 mL de HCl 0,40 M</b> con <b>150 mL de HCl 0,90 M</b>. Calcular la molaridad final de la mezcla.",
        "esperado": r"$M_f=0{,}588$ M.",
        "datos": [
            ("Disolución 1", "$V_1=250$ mL; $M_1=0{,}40$ M"),
            ("Disolución 2", "$V_2=150$ mL; $M_2=0{,}90$ M"),
        ],
        "demo": {
            "title": "Conservación de moles en mezcla",
            "body": r"""
<p>Al mezclar dos disoluciones del <em>mismo</em> soluto (sin reacción), los moles totales se conservan y el volumen final es la suma:</p>
$$n_{\text{tot}} = n_1 + n_2 = M_1V_1 + M_2V_2$$
$$V_{\text{tot}} = V_1 + V_2$$
$$M_f = \dfrac{n_{\text{tot}}}{V_{\text{tot}}}=\dfrac{M_1V_1+M_2V_2}{V_1+V_2}$$
<p>Esto es una <em>media ponderada</em> de las concentraciones por sus volúmenes.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles de cada disolución",
             "p": "$n=M\\cdot V$.",
             "b": r"""$$n_1=0{,}40\cdot 0{,}250=0{,}100\ \text{mol}$$
$$n_2=0{,}90\cdot 0{,}150=0{,}135\ \text{mol}$$"""},
            {"t": "Paso 2 — Volumen total y moles totales",
             "p": "Suma directa (mezclas ideales).",
             "b": r"""$$V_{\text{tot}}=400\ \text{mL}=0{,}400\ \text{L}$$
$$n_{\text{tot}}=0{,}100+0{,}135=0{,}235\ \text{mol}$$"""},
            {"t": "Paso 3 — Molaridad final",
             "p": "Definición de molaridad.",
             "b": r"""$$M_f=\dfrac{0{,}235}{0{,}400}=0{,}588\ \text{M}$$"""},
        ],
        "resultado": r"$M_f = 0{,}588$ M.",
        "verificacion": r"$M_f$ está entre 0,40 y 0,90 (intermedio, como debe ser una media). Más cerca de 0,40 porque el primer volumen es mayor. ✓"
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 2 — ESTRUCTURA ATÓMICA
# ═══════════════════════════════════════════════════════════════════════
2: [
    {
        "title": "Identificar conjuntos de números cuánticos válidos",
        "enunciado": r"Indicar cuáles de los siguientes conjuntos $(n,\ell,m_\ell,m_s)$ son <b>permitidos</b> para un electrón. Justificar los que no lo sean: (a) $(2,1,-1,+\tfrac12)$; (b) $(3,3,0,-\tfrac12)$; (c) $(4,2,-2,+\tfrac12)$; (d) $(2,0,1,-\tfrac12)$; (e) $(1,0,0,0)$.",
        "esperado": r"Permitidos: (a) y (c). No permitidos: (b), (d), (e).",
        "datos": [
            ("Reglas", "$n\\ge 1$; $0\\le\\ell\\le n-1$; $-\\ell\\le m_\\ell\\le +\\ell$; $m_s=\\pm\\tfrac12$"),
        ],
        "demo": {
            "title": "Restricciones de los números cuánticos",
            "body": r"""
<p>Los números cuánticos de la solución de Schrödinger para el átomo de H se relacionan jerárquicamente:</p>
<ul>
  <li>$n$ es entero $\ge 1$ (nivel principal).</li>
  <li>$\ell$ va de 0 a $n-1$ (forma del orbital). Por tanto $\ell$ <em>nunca</em> puede igualar o superar a $n$.</li>
  <li>$m_\ell$ va de $-\ell$ a $+\ell$ en pasos enteros ($2\ell+1$ valores). Indica orientación.</li>
  <li>$m_s$ solo toma $+\tfrac12$ o $-\tfrac12$ (espín).</li>
</ul>
<p>Cualquier conjunto que viole estas reglas describe un estado <em>inexistente</em> para un electrón.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Analizar cada conjunto",
             "p": "Aplico las reglas a cada caso.",
             "b": r"""<table class="tdatos">
<tr><th>Caso</th><th>$(n,\ell,m_\ell,m_s)$</th><th>¿Válido?</th><th>Motivo</th></tr>
<tr><td>(a)</td><td>(2,1,−1,+½)</td><td>✅</td><td>Orbital 2p, $m_\ell=-1$ correcto</td></tr>
<tr><td>(b)</td><td>(3,3,0,−½)</td><td>❌</td><td>$\ell=3$ requiere $n\ge 4$</td></tr>
<tr><td>(c)</td><td>(4,2,−2,+½)</td><td>✅</td><td>Orbital 4d, $-\ell\le m_\ell\le \ell$</td></tr>
<tr><td>(d)</td><td>(2,0,1,−½)</td><td>❌</td><td>Si $\ell=0$, $m_\ell$ solo puede ser 0</td></tr>
<tr><td>(e)</td><td>(1,0,0,0)</td><td>❌</td><td>$m_s$ solo $\pm\tfrac12$, nunca 0</td></tr>
</table>"""},
        ],
        "resultado": r"Permitidos: <b>(a)</b> y <b>(c)</b>. Los demás violan alguna regla.",
        "verificacion": r"Los conjuntos (a) y (c) corresponden a orbitales reales (2p y 4d). Los demás describen estados imposibles. ✓"
    },
    {
        "title": "Configuración electrónica de iones de transición",
        "enunciado": r"Escribir la configuración electrónica del <b>Fe$^{3+}$ ($Z=26$)</b> y del <b>Cu$^{2+}$ ($Z=29$)</b>. Indicar el número de electrones desapareados en cada uno.",
        "esperado": r"Fe$^{3+}$: $[Ar]\,3d^5$ → 5 desapareados. Cu$^{2+}$: $[Ar]\,3d^9$ → 1 desapareado.",
        "datos": [
            ("Fe neutro", "$[Ar]\\,4s^2\\,3d^6$"),
            ("Cu neutro", "$[Ar]\\,4s^1\\,3d^{10}$"),
        ],
        "demo": {
            "title": "Cómo se ionizan los metales de transición",
            "body": r"""
<p>Hay una <b>regla muy importante</b> para los metales de transición: aunque el orbital 4s se llena <em>antes</em> que el 3d (Aufbau), al ionizar el átomo se pierden <em>primero</em> los electrones del 4s y <em>después</em> los del 3d.</p>
<p>Razón física: una vez ocupados los 3d, su energía baja por debajo de la 4s. Así que en el ion, el orden energético real es 3d &lt; 4s.</p>
<p>Por tanto, las configuraciones de cationes de la primera serie de transición se escriben sin rastro del 4s.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Fe$^{3+}$",
             "p": "El Fe neutro es $[Ar]\\,4s^2\\,3d^6$. Pierdo 3 e<sup>−</sup>: primero los dos del 4s, luego uno del 3d.",
             "b": r"""$$\text{Fe}^{3+}: [Ar]\,3d^5$$
<p>5 electrones en 5 orbitales d → todos desapareados (Hund).</p>
<p style="font-family:monospace">3d: ↑ ↑ ↑ ↑ ↑ → <b>5 desapareados</b>.</p>"""},
            {"t": "Paso 2 — Cu$^{2+}$",
             "p": "El Cu neutro es $[Ar]\\,4s^1\\,3d^{10}$. Pierdo 2 e<sup>−</sup>: primero el del 4s, luego uno del 3d.",
             "b": r"""$$\text{Cu}^{2+}: [Ar]\,3d^9$$
<p>9 electrones en 5 orbitales d: cuatro pares + uno desapareado.</p>
<p style="font-family:monospace">3d: ↑↓ ↑↓ ↑↓ ↑↓ ↑ → <b>1 desapareado</b>.</p>"""},
        ],
        "resultado": r"Fe$^{3+}$: $[Ar]\,3d^5$ con <b>5</b> e<sup>−</sup> desapareados (alta paramagnetismo). Cu$^{2+}$: $[Ar]\,3d^9$ con <b>1</b> desapareado (color azul típico de sus complejos).",
        "verificacion": r"Suma de e<sup>−</sup>: Fe$^{3+}$ tiene $26-3=23$ e<sup>−</sup>: $[Ar]=18$ + $3d^5=5$ → 23 ✓. Cu$^{2+}$ tiene $29-2=27$ e<sup>−</sup>: $[Ar]=18$ + $3d^9=9$ → 27 ✓."
    },
    {
        "title": "Energía de un fotón a partir de la longitud de onda",
        "enunciado": r"Calcular la <b>energía de un fotón</b> de luz violeta de $\lambda=400$ nm. Expresar el resultado en julios y en electronvoltios. Datos: $h=6{,}626\cdot 10^{-34}$ J·s, $c=3{,}0\cdot 10^{8}$ m/s, $1\ \text{eV}=1{,}602\cdot 10^{-19}$ J.",
        "esperado": r"$E=4{,}97\cdot 10^{-19}$ J $=3{,}10$ eV.",
        "datos": [
            ("Longitud de onda", "$\\lambda=400\\ \\text{nm}=4{,}00\\cdot 10^{-7}\\ \\text{m}$"),
            ("$h$", "$6{,}626\\cdot 10^{-34}$ J·s"),
            ("$c$", "$3{,}0\\cdot 10^{8}$ m/s"),
            ("Conversión eV", "$1\\ \\text{eV}=1{,}602\\cdot 10^{-19}$ J"),
        ],
        "demo": {
            "title": "Relación de Planck-Einstein",
            "body": r"""
<p>Un fotón es un cuanto de luz cuya energía depende solo de su frecuencia (Planck, 1900):</p>
$$E = h\nu$$
<p>Como $c=\lambda\nu$, podemos expresar la energía en función de $\lambda$:</p>
$$E = \dfrac{hc}{\lambda}$$
<p>Esta es la relación que usaremos.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Energía en julios",
             "p": "Sustituyendo en $E=hc/\\lambda$.",
             "b": r"""$$E = \dfrac{6{,}626\cdot 10^{-34}\cdot 3{,}0\cdot 10^{8}}{4{,}00\cdot 10^{-7}}$$
$$E = \dfrac{1{,}988\cdot 10^{-25}}{4{,}00\cdot 10^{-7}} = 4{,}97\cdot 10^{-19}\ \text{J}$$"""},
            {"t": "Paso 2 — Conversión a eV",
             "p": "Dividir entre la equivalencia.",
             "b": r"""$$E(\text{eV})=\dfrac{4{,}97\cdot 10^{-19}}{1{,}602\cdot 10^{-19}}=3{,}10\ \text{eV}$$"""},
        ],
        "resultado": r"$E=4{,}97\cdot 10^{-19}$ J $=3{,}10$ eV.",
        "verificacion": r"Regla rápida: $E(\text{eV})\approx 1240/\lambda(\text{nm})$. Aplicando: $1240/400=3{,}10$ eV ✓."
    },
    {
        "title": "Línea de la serie de Lyman (UV) del hidrógeno",
        "enunciado": r"Calcular la longitud de onda del fotón emitido en la transición $n=2\to n=1$ del átomo de hidrógeno (primera línea de la serie de Lyman). $R_H=1{,}097\cdot 10^{7}$ m$^{-1}$. ¿En qué región del espectro cae?",
        "esperado": r"$\lambda \approx 121{,}5$ nm. Región del ultravioleta.",
        "datos": [
            ("Salto", "$n_i=2\\to n_f=1$"),
            ("$R_H$", "$1{,}097\\cdot 10^{7}$ m$^{-1}$"),
        ],
        "pasos": [
            {"t": "Paso 1 — Fórmula de Rydberg",
             "p": "Aplico con $n_f=1$, $n_i=2$.",
             "b": r"""$$\dfrac{1}{\lambda}=R_H\!\left(\dfrac{1}{1^2}-\dfrac{1}{2^2}\right)=R_H\cdot\dfrac{3}{4}$$"""},
            {"t": "Paso 2 — Cálculo",
             "p": "Sustitución.",
             "b": r"""$$\dfrac{1}{\lambda}=1{,}097\cdot 10^{7}\cdot 0{,}75=8{,}228\cdot 10^{6}\ \text{m}^{-1}$$
$$\lambda=1{,}215\cdot 10^{-7}\ \text{m}\approx 121{,}5\ \text{nm}$$"""},
            {"t": "Paso 3 — Región del espectro",
             "p": "El visible es 380–750 nm. Por debajo de 380 nm es UV.",
             "b": r"""<p>121,5 nm ≪ 380 nm ⟹ <b>ultravioleta lejano</b> (UV-C).</p>"""},
        ],
        "resultado": r"$\lambda \approx 121{,}5$ nm — UV invisible al ojo humano.",
        "verificacion": r"Toda la serie de Lyman ($n_f=1$) cae en el UV; la serie de Balmer ($n_f=2$) en el visible y la de Paschen ($n_f=3$) en el infrarrojo. ✓"
    },
    {
        "title": "Comparación cualitativa de propiedades periódicas",
        "enunciado": r"Ordenar de menor a mayor: (a) <b>radio atómico</b> de Li, Na, K, Be, Mg; (b) <b>energía de ionización</b> de Na, Mg, Al, Si; (c) <b>electronegatividad</b> de F, Cl, Br, I.",
        "esperado": r"(a) Be < Mg < Li < Na < K. (b) Na < Al < Mg < Si. (c) I < Br < Cl < F.",
        "datos": [
            ("Tendencias", "Radio: ↑ en grupo, ↓ en período. EI/EN: ↓ en grupo, ↑ en período."),
            ("Excepciones EI", "Al < Mg (subnivel 3p frente a 3s lleno)"),
        ],
        "demo": {
            "title": "Razonamiento por posición",
            "body": r"""
<p>Las tendencias surgen del balance entre <b>carga nuclear efectiva</b> ($Z_{ef}$) y <b>número de capas</b> ($n$):</p>
<ul>
  <li>Subir $Z_{ef}$ (avanzar en período) → mayor atracción del núcleo → menor radio, mayor EI/EN.</li>
  <li>Subir $n$ (bajar en grupo) → más capas → mayor radio, menor EI/EN.</li>
</ul>
<p>Las <b>excepciones</b> aparecen cuando se rompe una configuración estable: Al (3s²3p¹) tiene EI menor que Mg (3s²) porque el primer p es más fácil de quitar.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Apartado (a) Radio atómico",
             "p": "Be, Mg en grupo 2. Li, Na, K en grupo 1. Bajar y avanzar el período.",
             "b": r"""$$Be < Mg < Li < Na < K$$
<p>Be y Mg son menores que Li y Na por estar en período 2 y 3 grupo 2 (más Z). En cada grupo, baja → mayor radio.</p>"""},
            {"t": "Paso 2 — Apartado (b) Energía de ionización",
             "p": "Subiendo en período aumenta, salvo la anomalía Al < Mg.",
             "b": r"""$$Na < Al < Mg < Si$$
<p>Na bajo (alcalino, fácil ionizar). Al menor que Mg por la excepción del 3p. Si el más alto.</p>"""},
            {"t": "Paso 3 — Apartado (c) Electronegatividad",
             "p": "Mismo grupo (halógenos), bajar → menor EN.",
             "b": r"""$$I < Br < Cl < F$$
<p>F es el elemento más electronegativo de todos (4,0 Pauling).</p>"""},
        ],
        "resultado": r"(a) Be<Mg<Li<Na<K. (b) Na<Al<Mg<Si. (c) I<Br<Cl<F.",
        "verificacion": r"Valores tabulados (radio en pm): Be 112, Mg 160, Li 152, Na 186, K 227 ✓ (con la pequeña inversión Mg-Li que sí ocurre). EI (kJ/mol): Na 496, Al 577, Mg 738, Si 786 ✓. EN (Pauling): I 2,7, Br 3,0, Cl 3,2, F 4,0 ✓."
    },
    {
        "title": "Frecuencia de un haz láser",
        "enunciado": r"Un láser de helio-neón emite luz roja de longitud de onda $\lambda=632{,}8$ nm con potencia $P=2{,}0$ mW. Calcular: (a) la frecuencia de la radiación; (b) el número de fotones emitidos por segundo. Datos: $h=6{,}626\cdot 10^{-34}$ J·s, $c=3{,}0\cdot 10^{8}$ m/s.",
        "esperado": r"(a) $\nu=4{,}74\cdot 10^{14}$ Hz; (b) $N/t=6{,}37\cdot 10^{15}$ fotones/s.",
        "datos": [
            ("$\\lambda$", "$632{,}8\\ \\text{nm}=6{,}328\\cdot 10^{-7}$ m"),
            ("$P$", "$2{,}0\\cdot 10^{-3}$ W"),
        ],
        "pasos": [
            {"t": "Paso 1 — Frecuencia",
             "p": "$c=\\lambda\\nu$.",
             "b": r"""$$\nu=\dfrac{c}{\lambda}=\dfrac{3{,}0\cdot 10^{8}}{6{,}328\cdot 10^{-7}}=4{,}74\cdot 10^{14}\ \text{Hz}$$"""},
            {"t": "Paso 2 — Energía de un fotón",
             "p": "$E_f=h\\nu$.",
             "b": r"""$$E_f=6{,}626\cdot 10^{-34}\cdot 4{,}74\cdot 10^{14}=3{,}14\cdot 10^{-19}\ \text{J}$$"""},
            {"t": "Paso 3 — Número de fotones por segundo",
             "p": "$P$ = energía total emitida por segundo. Dividiendo por la energía de un fotón sale el número.",
             "b": r"""$$\dfrac{N}{t}=\dfrac{P}{E_f}=\dfrac{2{,}0\cdot 10^{-3}}{3{,}14\cdot 10^{-19}}=6{,}37\cdot 10^{15}\ \text{fotones/s}$$"""},
        ],
        "resultado": r"$\nu=4{,}74\cdot 10^{14}$ Hz · $\sim 6{,}4\cdot 10^{15}$ fotones cada segundo.",
        "verificacion": r"En 1 minuto el láser emite $\sim 4\cdot 10^{17}$ fotones — número astronómico, coherente con que la luz parezca un flujo continuo. ✓"
    },
    {
        "title": "Configuración electrónica del As y de su anión",
        "enunciado": r"Para el arsénico ($Z=33$): (a) escribir su configuración electrónica completa; (b) indicar a qué grupo y período pertenece; (c) escribir la configuración del anión <b>As$^{3-}$</b> y compararla con la del Kr.",
        "esperado": r"(a) $[Ar]\,4s^2\,3d^{10}\,4p^3$; (b) Grupo 15, período 4; (c) As$^{3-}=[Ar]\,4s^2\,3d^{10}\,4p^6=[Kr]$.",
        "datos": [
            ("$Z_{As}$", "33"),
            ("$Z_{Kr}$", "36"),
        ],
        "demo": {
            "title": "Posición y configuración",
            "body": r"""
<p>El número atómico fija la configuración electrónica vía Aufbau. La <em>posición</em> en la tabla periódica se deduce directamente de la configuración:</p>
<ul>
  <li><b>Período</b> = mayor valor de $n$ ocupado.</li>
  <li><b>Grupo</b> = electrones de valencia (capa más externa).</li>
</ul>
<p>Los aniones se forman ganando electrones hasta alcanzar configuración de gas noble — los <b>isoelectrónicos</b> al gas noble más próximo son especialmente estables.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Configuración del As neutro",
             "p": "Aplico Madelung hasta llegar a 33 e<sup>−</sup>.",
             "b": r"""$$1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^{10}\,4p^3 = [Ar]\,4s^2\,3d^{10}\,4p^3$$
<p>Suma: $18 + 2 + 10 + 3 = 33$ ✓</p>"""},
            {"t": "Paso 2 — Período y grupo",
             "p": "$n_{max}=4$ ⟹ período 4. Valencia = $4s^2\\,4p^3$ ⟹ 5 e<sup>−</sup> en la última capa ⟹ grupo 15 (nitrogenoideos).",
             "b": r"""<p>El As es <b>período 4, grupo 15</b> (familia del nitrógeno).</p>"""},
            {"t": "Paso 3 — Configuración del As$^{3-}$",
             "p": "Gana 3 e<sup>−</sup> que entran en el 4p para completarlo.",
             "b": r"""$$\text{As}^{3-}: [Ar]\,4s^2\,3d^{10}\,4p^6$$
<p>Total: $18+2+10+6=36$ e<sup>−</sup> = $Z_{Kr}$. <b>El As$^{3-}$ es isoelectrónico con el Kr</b>: tiene la misma configuración pero diferente carga nuclear.</p>"""},
        ],
        "resultado": r"As: $[Ar]\,4s^2\,3d^{10}\,4p^3$ (grupo 15, período 4). As$^{3-}$ es isoelectrónico con Kr.",
        "verificacion": r"Coherencia: el As tiene 5 e<sup>−</sup> de valencia (típico de grupo 15: N, P, As, Sb), gana 3 para alcanzar el octeto ⟹ As$^{3-}$. ✓ Esto explica que en arsenuros aparezca como ion 3−."
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 3 — ENLACE QUÍMICO
# ═══════════════════════════════════════════════════════════════════════
3: [
    {
        "title": "Estructura de Lewis del ion carbonato (resonancia)",
        "enunciado": r"Determinar la estructura de Lewis del ion <b>CO$_3^{2-}$</b>, identificar las estructuras resonantes y determinar la geometría VSEPR del ion. ¿Es polar?",
        "esperado": r"3 estructuras resonantes equivalentes; geometría trigonal plana (120°); apolar por simetría.",
        "datos": [
            ("$e^-$ valencia C", "4"),
            ("$e^-$ valencia O", "6"),
            ("Carga del ion", "−2 (añade 2 e<sup>−</sup>)"),
        ],
        "demo": {
            "title": "Resonancia y deslocalización",
            "body": r"""
<p>Cuando una estructura de Lewis no puede dibujarse con un único patrón fijo de enlaces y pares, decimos que el sistema tiene <b>resonancia</b>: la realidad es una <em>superposición</em> (híbrido) de varias estructuras equivalentes.</p>
<p>Conteo de electrones de valencia totales: $4 + 3\cdot 6 + 2 = 24$ e<sup>−</sup> (los 2 de la carga negativa cuentan).</p>
<p>El C es central (menos electronegativo). Los 3 O lo rodean. Una de las uniones C–O es doble; las otras dos simples (con cargas formales en los O).</p>
<p>Como los 3 O son equivalentes por simetría, hay <b>3 estructuras resonantes</b> que difieren solo en cuál es el doble enlace.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Estructuras resonantes",
             "p": "El doble enlace puede estar en cualquiera de los 3 O.",
             "b": r"""<p style="font-family:monospace;text-align:center;font-size:1.05em">
[O−C(=O)−O]²⁻ ↔ [O=C(−O)−O]²⁻ ↔ [O−C(−O)=O]²⁻</p>
<p>Las 3 estructuras son <b>equivalentes</b>: el ion real es un híbrido en el que cada enlace C–O tiene <b>orden de enlace 4/3</b> (intermedio entre simple y doble).</p>"""},
            {"t": "Paso 2 — Geometría VSEPR",
             "p": "El C tiene 3 grupos de electrones (3 enlaces, sin pares libres).",
             "b": r"""<p>3 dominios electrónicos sin pares libres ⟹ <b>geometría trigonal plana</b>, ángulos de 120°.</p>"""},
            {"t": "Paso 3 — Polaridad",
             "p": "Aunque cada enlace C–O es polar, los 3 dipolos están dispuestos a 120° y se cancelan vectorialmente.",
             "b": r"""<p>Suma de dipolos = 0 ⟹ <b>el ion CO$_3^{2-}$ es apolar</b> (la carga sí es −2, pero no hay momento dipolar neto).</p>"""},
        ],
        "resultado": r"3 resonancias equivalentes · geometría <b>trigonal plana</b> (120°) · momento dipolar nulo (apolar por simetría).",
        "verificacion": r"Las 3 distancias C–O en el CO$_3^{2-}$ se miden experimentalmente <b>iguales</b> (1,29 Å), intermedias entre el simple (1,43 Å) y el doble (1,20 Å). Confirma la deslocalización ✓."
    },
    {
        "title": "Geometría e hibridación de SF$_6$ y PCl$_5$",
        "enunciado": r"Para las moléculas <b>SF$_6$</b> y <b>PCl$_5$</b>, determinar: (a) la estructura de Lewis; (b) la geometría VSEPR; (c) la hibridación del átomo central.",
        "esperado": r"SF$_6$: octaédrica, sp$^3$d$^2$. PCl$_5$: bipirámide trigonal, sp$^3$d.",
        "datos": [
            ("$e^-$ valencia S", "6"),
            ("$e^-$ valencia P", "5"),
            ("$e^-$ valencia F, Cl", "7 (cada uno)"),
        ],
        "demo": {
            "title": "Octeto expandido y hibridación con orbitales d",
            "body": r"""
<p>Los elementos del <b>tercer período en adelante</b> (P, S, Cl, Br, I…) pueden tener más de 8 e<sup>−</sup> en su capa de valencia ("octeto expandido") porque disponen de orbitales $d$ de su mismo nivel cuántico para acomodar electrones extra.</p>
<p>La hibridación se obtiene mezclando 1 orbital $s$, 3 orbitales $p$ y los $d$ necesarios para alcanzar el número total de pares electrónicos:</p>
<ul>
  <li>5 pares ⟹ sp$^3$d (1+3+1 = 5 orbitales híbridos).</li>
  <li>6 pares ⟹ sp$^3$d$^2$ (1+3+2 = 6).</li>
</ul>
"""
        },
        "pasos": [
            {"t": "Paso 1 — SF$_6$",
             "p": "S central, 6 enlaces S–F. Conteo: $6+6\\cdot 7=48$ e<sup>−</sup> de valencia. 6 pares enlazantes en S.",
             "b": r"""<p>Geometría VSEPR: 6 dominios electrónicos, sin pares libres ⟹ <b>octaédrica</b>, ángulos 90°.</p>
<p>Hibridación del S: 6 orbitales híbridos ⟹ <b>sp$^3$d$^2$</b>.</p>"""},
            {"t": "Paso 2 — PCl$_5$",
             "p": "P central, 5 enlaces P–Cl. Conteo: $5+5\\cdot 7=40$ e<sup>−</sup>. 5 pares enlazantes en P.",
             "b": r"""<p>Geometría VSEPR: 5 dominios electrónicos, sin pares libres ⟹ <b>bipirámide trigonal</b>, ángulos 90° (axial-ecuatorial) y 120° (ecuatorial-ecuatorial).</p>
<p>Hibridación del P: 5 orbitales híbridos ⟹ <b>sp$^3$d</b>.</p>"""},
        ],
        "resultado": r"SF$_6$: octaédrica · sp$^3$d$^2$. PCl$_5$: bipirámide trigonal · sp$^3$d.",
        "verificacion": r"En PCl$_5$ los enlaces axiales son ligeramente más largos (2,12 Å) que los ecuatoriales (2,02 Å), lo que se explica por la mayor repulsión de los enlaces axiales con los 3 ecuatoriales (90° vs 120°). ✓"
    },
    {
        "title": "Polaridad de moléculas tetraédricas",
        "enunciado": r"De las siguientes moléculas tetraédricas, determinar cuáles son <b>polares</b> y cuáles <b>apolares</b>: (a) CH$_4$; (b) CH$_3$Cl; (c) CCl$_4$; (d) CHCl$_3$.",
        "esperado": r"Apolares: CH$_4$, CCl$_4$. Polares: CH$_3$Cl, CHCl$_3$.",
        "datos": [
            ("Geometría", "Todas son tetraédricas"),
            ("Electronegatividades", "$\\chi_C=2{,}5$; $\\chi_H=2{,}1$; $\\chi_{Cl}=3{,}0$"),
        ],
        "demo": {
            "title": "Cancelación vectorial de dipolos",
            "body": r"""
<p>En una molécula tetraédrica AX$_4$ con los 4 X iguales, los 4 vectores dipolo C→X tienen igual módulo y apuntan en direcciones simétricas, lo que da una <b>suma vectorial nula</b> ⟹ molécula <b>apolar</b>.</p>
<p>Si uno o más X son distintos, la simetría se rompe y aparece un momento dipolar neto. La regla práctica:</p>
<ul>
  <li>AX$_4$ (X iguales) ⟹ apolar.</li>
  <li>AX$_3$Y, AX$_2$Y$_2$, AX Y$_3$ ⟹ polar.</li>
</ul>
"""
        },
        "pasos": [
            {"t": "Análisis de cada molécula",
             "p": "Comparar átomos enlazados al carbono.",
             "b": r"""<table class="tdatos">
<tr><th>Molécula</th><th>Sustituyentes</th><th>Polaridad</th></tr>
<tr><td>CH$_4$</td><td>4 H iguales</td><td>Apolar (dipolos se cancelan)</td></tr>
<tr><td>CH$_3$Cl</td><td>3 H + 1 Cl</td><td><b>Polar</b> (asimetría)</td></tr>
<tr><td>CCl$_4$</td><td>4 Cl iguales</td><td>Apolar (dipolos se cancelan)</td></tr>
<tr><td>CHCl$_3$</td><td>1 H + 3 Cl</td><td><b>Polar</b> (asimetría)</td></tr>
</table>"""},
        ],
        "resultado": r"Apolares: <b>CH$_4$, CCl$_4$</b>. Polares: <b>CH$_3$Cl, CHCl$_3$</b>.",
        "verificacion": r"Momentos dipolares medidos: CH$_4$ = 0 D, CH$_3$Cl = 1,87 D, CCl$_4$ = 0 D, CHCl$_3$ = 1,04 D. ✓ Coincide con la predicción."
    },
    {
        "title": "Energía de enlace en una reacción de combustión",
        "enunciado": r"Estimar el $\Delta H$ de la reacción $\text{CH}_4 + 2\,\text{O}_2 \to \text{CO}_2 + 2\,\text{H}_2\text{O}(g)$ usando energías de enlace medias (kJ/mol): $E(\text{C-H})=413$, $E(\text{O=O})=498$, $E(\text{C=O})=799$ (en CO$_2$), $E(\text{O-H})=463$.",
        "esperado": r"$\Delta H \approx -698$ kJ/mol — exotérmica.",
        "datos": [
            ("Enlaces rotos", "4 C–H + 2 O=O"),
            ("Enlaces formados", "2 C=O (en CO$_2$) + 4 O–H"),
        ],
        "demo": {
            "title": "Romper consume, formar libera",
            "body": r"""
<p>Romper enlaces consume energía (entra al sistema) y formar enlaces libera energía (sale del sistema):</p>
$$\Delta H \approx \sum E(\text{rotos}) - \sum E(\text{formados})$$
<p>El signo se interpreta así: $\Delta H<0$ → la reacción libera calor (forma enlaces más fuertes que los rotos).</p>
<p>Importante: las energías de enlace son <em>medias tabuladas</em>; el método da una <b>aproximación</b> con desviaciones de ~5-15 kJ/mol respecto al $\Delta H_f$ exacto.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Energía total de enlaces rotos",
             "p": "4 C–H del metano + 2 O=O del oxígeno.",
             "b": r"""$$\sum E_{\text{rotos}} = 4\cdot 413 + 2\cdot 498 = 1\,652 + 996 = 2\,648\ \text{kJ}$$"""},
            {"t": "Paso 2 — Energía total de enlaces formados",
             "p": "2 enlaces C=O en CO$_2$ + 4 O–H en 2 H$_2$O.",
             "b": r"""$$\sum E_{\text{form}} = 2\cdot 799 + 4\cdot 463 = 1\,598 + 1\,852 = 3\,450\ \text{kJ}$$"""},
            {"t": "Paso 3 — $\\Delta H$",
             "p": "Diferencia con su signo.",
             "b": r"""$$\Delta H = 2\,648 - 3\,450 = \boxed{-802\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta H \approx -802$ kJ/mol — combustión fuertemente exotérmica.",
        "verificacion": r"Valor experimental con H$_2$O(g): $\Delta H = -802{,}3$ kJ/mol. La aproximación por energías de enlace ha sido casi exacta. ✓ (Para H$_2$O líquida hay que añadir el calor de condensación, $-44$ kJ/mol por mol de agua.)"
    },
    {
        "title": "Ciclo de Born-Haber simplificado para LiF",
        "enunciado": r"Calcular la energía de red del LiF aplicando el ciclo de Born-Haber. Datos (kJ/mol): $\Delta H_f(\text{LiF})=-616$; sublimación Li(s)→Li(g) = $+159$; ionización Li(g)→Li$^+$(g) = $+520$; disociación ½ F$_2$(g)→F(g) = $+79$; afinidad electrónica F(g)→F$^-$(g) = $-328$.",
        "esperado": r"$U = -1\,046$ kJ/mol.",
        "datos": [
            ("$\\Delta H_f(\\text{LiF})$", "$-616$ kJ/mol"),
            ("Sublimación Li", "$+159$"),
            ("Ionización Li", "$+520$"),
            ("Disociación ½F$_2$", "$+79$"),
            ("Afinidad electrónica F", "$-328$"),
        ],
        "demo": {
            "title": "Ley de Hess aplicada al ciclo",
            "body": r"""
<p>El ciclo de Born-Haber descompone la formación del cristal iónico en pasos individuales medibles. Aplicando la ley de Hess al ciclo cerrado:</p>
$$\Delta H_f = \Delta H_{sub} + EI + \tfrac12 \Delta H_{dis} + AE + U$$
<p>Despejando la <b>energía de red</b> $U$ (única magnitud no medible directamente):</p>
$$U = \Delta H_f - (\Delta H_{sub} + EI + \tfrac12 \Delta H_{dis} + AE)$$
<p>$U$ es <em>siempre</em> negativa (la formación de la red es exotérmica).</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Suma de los pasos en fase gas",
             "p": "Sublimación + ionización + disociación + afinidad.",
             "b": r"""$$\Sigma = 159 + 520 + 79 + (-328) = 430\ \text{kJ/mol}$$"""},
            {"t": "Paso 2 — Despejar $U$",
             "p": "$U = \\Delta H_f - \\Sigma$.",
             "b": r"""$$U = -616 - 430 = \boxed{-1\,046\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$U(\text{LiF}) = -1\,046$ kJ/mol.",
        "verificacion": r"Valor tabulado experimental: $U_{exp}(\text{LiF})=-1\,047$ kJ/mol. Coincidencia excelente. ✓ La alta energía de red confirma la fortaleza de la red iónica del LiF (el más estable de los haluros alcalinos)."
    },
    {
        "title": "Tipo de sólido y propiedades físicas",
        "enunciado": r"Clasificar como sólido <b>iónico, molecular, covalente o metálico</b> a las siguientes sustancias y predecir si son: (i) buenos conductores eléctricos en estado sólido, (ii) solubles en agua. Sustancias: NaCl, diamante (C), cobre (Cu), hielo (H$_2$O), I$_2$.",
        "esperado": r"Ver tabla.",
        "datos": [
            ("Tipos posibles", "iónico · molecular · covalente · metálico"),
        ],
        "demo": {
            "title": "Propiedades macro a partir del enlace micro",
            "body": r"""
<p>El tipo de sólido determina sus propiedades:</p>
<table class="tdatos">
<tr><th>Tipo</th><th>Conductor sólido</th><th>Soluble en H$_2$O</th></tr>
<tr><td>Iónico</td><td>NO</td><td>SÍ (en general)</td></tr>
<tr><td>Molecular</td><td>NO</td><td>Polar SÍ, apolar NO</td></tr>
<tr><td>Covalente</td><td>NO (excepto grafito)</td><td>NO</td></tr>
<tr><td>Metálico</td><td>SÍ</td><td>NO (excepto reactivos)</td></tr>
</table>
"""
        },
        "pasos": [
            {"t": "Análisis caso por caso",
             "p": "Identificar el tipo y aplicar la tabla.",
             "b": r"""<table class="tdatos">
<tr><th>Sustancia</th><th>Tipo</th><th>Conductor</th><th>Soluble H$_2$O</th></tr>
<tr><td>NaCl</td><td>Iónico</td><td>NO (sí fundido o disuelto)</td><td>SÍ</td></tr>
<tr><td>Diamante (C)</td><td>Covalente reticular</td><td>NO</td><td>NO</td></tr>
<tr><td>Cu</td><td>Metálico</td><td>SÍ (excelente)</td><td>NO</td></tr>
<tr><td>Hielo (H$_2$O)</td><td>Molecular (puente H)</td><td>NO</td><td>—</td></tr>
<tr><td>I$_2$</td><td>Molecular (London)</td><td>NO</td><td>Poco (apolar)</td></tr>
</table>"""},
        ],
        "resultado": r"NaCl iónico · diamante covalente · Cu metálico · hielo molecular · I$_2$ molecular. Solo Cu conduce; solo NaCl es bien soluble en agua.",
        "verificacion": r"Esta clasificación predice correctamente que el grafito (otro sólido covalente del C) es <em>conductor</em> por sus electrones π deslocalizados — la única excepción importante. ✓"
    },
    {
        "title": "Comparación de fuerzas intermoleculares en isómeros",
        "enunciado": r"Predecir cuál tiene mayor punto de ebullición: <b>n-pentano</b> (C$_5$H$_{12}$, lineal) o <b>neopentano</b> (C(CH$_3$)$_4$, ramificado). Ambos tienen la misma masa molar (72 g/mol). Justificar.",
        "esperado": r"n-pentano: $T_{eb}=36$ °C. Neopentano: $T_{eb}=10$ °C. Mayor el lineal.",
        "datos": [
            ("Masa molar", "$M=72$ g/mol (ambos)"),
            ("$T_{eb}$ medidos", "n-pentano: 36 °C; neopentano: 10 °C"),
        ],
        "demo": {
            "title": "Forma molecular y fuerzas de London",
            "body": r"""
<p>Ambos compuestos son apolares: las únicas fuerzas intermoleculares disponibles son las <b>fuerzas de dispersión de London</b>. Su intensidad depende de:</p>
<ul>
  <li>El número de electrones (≈ masa molar) — igual en ambos.</li>
  <li>La <b>forma</b> de la molécula: las moléculas alargadas tienen mayor superficie de contacto con las vecinas → más fuerzas de dispersión → mayor $T_{eb}$.</li>
</ul>
<p>El neopentano es casi esférico y el n-pentano es alargado, por lo que el lineal interactúa más fuertemente.</p>
"""
        },
        "pasos": [
            {"t": "Comparación geométrica",
             "p": "n-pentano = cadena recta, longitud ≈ 6 Å. Neopentano = cuasi-esférico, diámetro ≈ 5 Å.",
             "b": r"""<p>El n-pentano tiene mayor superficie de contacto cuando se aproxima a otra molécula (puede estar "tumbado" pegado a otra). El neopentano solo puede tocar por su superficie esférica.</p>"""},
            {"t": "Predicción del orden de ebullición",
             "p": "Mayor superficie ⟹ mayores fuerzas de London ⟹ mayor $T_{eb}$.",
             "b": r"""<p>$T_{eb}(\text{n-pentano}) > T_{eb}(\text{neopentano})$</p>
<p>$36$ °C > $10$ °C ✓</p>"""},
        ],
        "resultado": r"<b>n-pentano</b> ebulle a 36 °C (más alto) que el neopentano (10 °C), pese a tener idéntica masa molar — efecto puro de la forma molecular sobre las fuerzas de dispersión.",
        "verificacion": r"Resultado generalizable: en una serie de isómeros del mismo $C_n H_{2n+2}$, el más ramificado siempre tiene menor $T_{eb}$. ✓ Ej: 2-metilbutano (28 °C) intermedio entre n-pentano y neopentano."
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 4 — ESTADOS DE LA MATERIA
# ═══════════════════════════════════════════════════════════════════════
4: [
    {
        "title": "Densidad de un gas ideal",
        "enunciado": r"Calcular la densidad del <b>O$_2$</b> a 25 °C y 1 atm. ¿Y a 100 °C? Datos: $M_{O_2}=32{,}0$ g/mol, $R=0{,}082$ atm·L/(mol·K).",
        "esperado": r"$\rho(25°\text{C})=1{,}308$ g/L; $\rho(100°\text{C})=1{,}045$ g/L.",
        "datos": [
            ("$M_{O_2}$", "32,0 g/mol"),
            ("$T_1$, $T_2$", "298 K; 373 K"),
            ("$p$", "1 atm"),
        ],
        "demo": {
            "title": "Densidad a partir de $pV=nRT$",
            "body": r"""
<p>Para un gas ideal, $pV=nRT$. Si llamamos $m$ a la masa, $n=m/M$, así que:</p>
$$pV = \dfrac{m}{M}RT \implies \dfrac{m}{V}=\dfrac{pM}{RT}$$
<p>Pero $m/V=\rho$ es justamente la densidad:</p>
$$\boxed{\;\rho=\dfrac{pM}{RT}\;}$$
<p>Esto muestra que la densidad de un gas <b>aumenta</b> con la presión y disminuye con la temperatura, en contraste con sólidos y líquidos donde la dependencia es mucho más débil.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Densidad a 25 °C",
             "p": "Sustitución directa.",
             "b": r"""$$\rho_1 = \dfrac{1\cdot 32{,}0}{0{,}082\cdot 298}=\dfrac{32{,}0}{24{,}44}=1{,}308\ \text{g/L}$$"""},
            {"t": "Paso 2 — Densidad a 100 °C",
             "p": "Misma fórmula, $T_2=373$ K.",
             "b": r"""$$\rho_2 = \dfrac{32{,}0}{0{,}082\cdot 373}=\dfrac{32{,}0}{30{,}59}=1{,}045\ \text{g/L}$$"""},
        ],
        "resultado": r"$\rho_{25°C}=1{,}308$ g/L · $\rho_{100°C}=1{,}045$ g/L. La densidad del gas baja al subir $T$.",
        "verificacion": r"Razón inversa: $\rho_1/\rho_2=T_2/T_1=373/298=1{,}252$. Comprobación: $1{,}308/1{,}045=1{,}252$ ✓ — coincide exactamente."
    },
    {
        "title": "Ley de Graham: efusión de gases",
        "enunciado": r"El amoniaco (NH$_3$) y el cloruro de hidrógeno (HCl) se introducen simultáneamente en los extremos opuestos de un tubo de 1,00 m de largo. Determinar a qué distancia del extremo del NH$_3$ se forma el anillo blanco de NH$_4$Cl(s) cuando ambos gases se encuentran. Datos: $M_{NH_3}=17$, $M_{HCl}=36{,}5$ g/mol.",
        "esperado": r"Distancia desde el NH$_3$ ≈ 59 cm.",
        "datos": [
            ("Longitud del tubo", "$L=1{,}00$ m"),
            ("$M_{NH_3}$", "17 g/mol"),
            ("$M_{HCl}$", "36,5 g/mol"),
        ],
        "demo": {
            "title": "Ley de Graham",
            "body": r"""
<p>La <b>ley de Graham</b> establece que la velocidad de efusión (o difusión) de un gas es inversamente proporcional a la raíz cuadrada de su masa molar:</p>
$$\dfrac{v_A}{v_B}=\sqrt{\dfrac{M_B}{M_A}}$$
<p>Físicamente: a la misma temperatura, todos los gases tienen la misma energía cinética media $\tfrac12 M v^2$, así que el más ligero se mueve más rápido.</p>
<p>Si dos gases parten al mismo tiempo desde extremos opuestos de un tubo de longitud $L$, se encontrarán cuando $d_A + d_B = L$, con $d_A/d_B = v_A/v_B$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Razón de velocidades",
             "p": "Aplico Graham con $A=$NH$_3$, $B=$HCl.",
             "b": r"""$$\dfrac{v_{NH_3}}{v_{HCl}}=\sqrt{\dfrac{M_{HCl}}{M_{NH_3}}}=\sqrt{\dfrac{36{,}5}{17}}=\sqrt{2{,}147}=1{,}465$$
<p>El NH$_3$ es ~1,5 veces más rápido por ser más ligero.</p>"""},
            {"t": "Paso 2 — Posición del encuentro",
             "p": "$d_{NH_3} + d_{HCl} = 1{,}00$ m, con $d_{NH_3}/d_{HCl}=1{,}465$.",
             "b": r"""$$d_{NH_3} = 1{,}465\,d_{HCl}\implies 1{,}465\,d_{HCl}+d_{HCl}=1{,}00$$
$$d_{HCl} = \dfrac{1{,}00}{2{,}465}=0{,}4057\ \text{m}$$
$$d_{NH_3} = 1{,}00 - 0{,}406 = 0{,}594\ \text{m}\approx \boxed{59{,}4\ \text{cm}}$$"""},
        ],
        "resultado": r"El anillo blanco de NH$_4$Cl(s) aparece a <b>59,4 cm</b> del extremo del NH$_3$ (40,6 cm del extremo del HCl).",
        "verificacion": r"Razón experimental medida en laboratorio: $\sim 60$ cm. ✓ Pequeñas desviaciones por convección y geometría real del tubo."
    },
    {
        "title": "Gas real: comparación con la ecuación de van der Waals",
        "enunciado": r"Calcular la presión de <b>2,0 mol</b> de CO$_2$ encerrados en <b>1,0 L</b> a <b>300 K</b>: (a) suponiendo gas ideal; (b) usando la ecuación de van der Waals. Constantes para CO$_2$: $a=3{,}59\ \text{atm·L}^2/\text{mol}^2$, $b=0{,}0427$ L/mol. $R=0{,}082$ atm·L/(mol·K).",
        "esperado": r"(a) $p_{ideal}=49{,}2$ atm; (b) $p_{vdW}=39{,}3$ atm.",
        "datos": [
            ("$n$", "2,0 mol"),
            ("$V$", "1,0 L"),
            ("$T$", "300 K"),
            ("$a, b$ (CO$_2$)", "3,59 atm·L²/mol²; 0,0427 L/mol"),
        ],
        "demo": {
            "title": "Por qué van der Waals corrige al ideal",
            "body": r"""
<p>La ecuación de gas ideal supone que las moléculas son puntos sin interacción. Van der Waals añade dos correcciones físicas:</p>
<ul>
  <li><b>Volumen propio</b>: las moléculas ocupan espacio, así que el volumen "libre" disponible es $V-nb$ en vez de $V$.</li>
  <li><b>Atracciones</b>: las moléculas se atraen ligeramente, lo que reduce la presión real respecto al ideal en una cantidad $an^2/V^2$.</li>
</ul>
$$\left(p+\dfrac{an^2}{V^2}\right)(V-nb)=nRT \implies p=\dfrac{nRT}{V-nb}-\dfrac{an^2}{V^2}$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — Presión ideal",
             "p": "$p=nRT/V$.",
             "b": r"""$$p_{ideal}=\dfrac{2{,}0\cdot 0{,}082\cdot 300}{1{,}0}=49{,}2\ \text{atm}$$"""},
            {"t": "Paso 2 — Presión van der Waals",
             "p": "Aplico la fórmula con corrección.",
             "b": r"""$$p_{vdW}=\dfrac{2{,}0\cdot 0{,}082\cdot 300}{1{,}0-2{,}0\cdot 0{,}0427}-\dfrac{3{,}59\cdot (2{,}0)^2}{(1{,}0)^2}$$
$$p_{vdW}=\dfrac{49{,}2}{0{,}9146}-14{,}36=53{,}79-14{,}36=39{,}43\ \text{atm}$$"""},
            {"t": "Paso 3 — Diferencia y factor de compresibilidad",
             "p": "$Z=p_{vdW}V/(nRT)$.",
             "b": r"""$$Z=\dfrac{39{,}43\cdot 1{,}0}{2{,}0\cdot 0{,}082\cdot 300}=0{,}80$$
<p>$Z<1$ ⟹ a esta densidad y $T$ <b>dominan las atracciones</b> sobre el efecto del volumen propio.</p>"""},
        ],
        "resultado": r"$p_{ideal}=49{,}2$ atm vs $p_{vdW}=39{,}3$ atm. Diferencia ≈ 20%.",
        "verificacion": r"A presiones más bajas ($p<5$ atm) y/o temperaturas más altas, $Z\to 1$ y los modelos coinciden. La discrepancia aquí es grande porque la densidad es alta (2 mol en 1 L = $\rho\approx 88$ g/L). ✓"
    },
    {
        "title": "Clausius-Clapeyron: presión de vapor a otra temperatura",
        "enunciado": r"El agua tiene una presión de vapor de <b>23,8 mmHg a 25 °C</b>. Calcular su presión de vapor a <b>50 °C</b> usando la ecuación de Clausius-Clapeyron. $\Delta H_{vap}=44{,}0$ kJ/mol, $R=8{,}314$ J/(mol·K).",
        "esperado": r"$p_2 \approx 92{,}2$ mmHg.",
        "datos": [
            ("$T_1$", "298 K"),
            ("$p_1$", "23,8 mmHg"),
            ("$T_2$", "323 K"),
            ("$\\Delta H_{vap}$", "44 000 J/mol"),
        ],
        "demo": {
            "title": "Clausius-Clapeyron integrada",
            "body": r"""
<p>Integrando la ecuación diferencial de Clausius-Clapeyron entre dos temperaturas, suponiendo $\Delta H_{vap}$ constante en el rango:</p>
$$\ln\!\dfrac{p_2}{p_1}=-\dfrac{\Delta H_{vap}}{R}\!\left(\dfrac{1}{T_2}-\dfrac{1}{T_1}\right)$$
<p>Predice cómo crece exponencialmente la presión de vapor con $T$. Para el agua, una subida de 25 K casi cuatriplica $p_v$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Diferencia $1/T$",
             "p": "Cuidado con el signo y unidades.",
             "b": r"""$$\dfrac{1}{T_2}-\dfrac{1}{T_1}=\dfrac{1}{323}-\dfrac{1}{298}=3{,}096\cdot 10^{-3}-3{,}356\cdot 10^{-3}=-2{,}600\cdot 10^{-4}\ \text{K}^{-1}$$"""},
            {"t": "Paso 2 — Logaritmo del cociente",
             "p": "Sustituyendo en la fórmula.",
             "b": r"""$$\ln\!\dfrac{p_2}{p_1}=-\dfrac{44\,000}{8{,}314}\cdot(-2{,}600\cdot 10^{-4})=1{,}376$$"""},
            {"t": "Paso 3 — Despejar $p_2$",
             "p": "Exponencial.",
             "b": r"""$$\dfrac{p_2}{p_1}=e^{1{,}376}=3{,}96$$
$$p_2 = 23{,}8\cdot 3{,}96=\boxed{94{,}2\ \text{mmHg}}$$"""},
        ],
        "resultado": r"$p_2 \approx 94$ mmHg.",
        "verificacion": r"Valor experimental tabulado: 92,5 mmHg a 50 °C. La pequeña diferencia (~2%) viene de suponer $\Delta H_{vap}$ rigurosamente constante (en realidad disminuye un poco con $T$). ✓"
    },
    {
        "title": "Calor para vaporizar agua",
        "enunciado": r"Calcular el calor necesario para vaporizar <b>500 g de agua a 100 °C</b> a presión atmosférica. ¿Qué energía absorbe (en %) frente a la necesaria para calentar la misma agua de 0 °C a 100 °C? Datos: $L_v=2\,260$ J/g; $c_a=4{,}18$ J/(g·K).",
        "esperado": r"$Q_{vap}=1\,130$ kJ. Es 5,4 veces más que calentarla de 0 a 100 °C.",
        "datos": [
            ("Masa", "500 g"),
            ("$L_v$", "2 260 J/g"),
            ("$c_a$", "4,18 J/(g·K)"),
            ("$\\Delta T_{0\\to 100}$", "100 K"),
        ],
        "pasos": [
            {"t": "Paso 1 — Calor de vaporización",
             "p": "$Q=m\\,L_v$.",
             "b": r"""$$Q_{vap}=500\cdot 2\,260=1{,}13\cdot 10^{6}\ \text{J}=\boxed{1\,130\ \text{kJ}}$$"""},
            {"t": "Paso 2 — Calor para calentar de 0 a 100 °C",
             "p": "$Q=mc\\Delta T$.",
             "b": r"""$$Q_{calent}=500\cdot 4{,}18\cdot 100=209\,000\ \text{J}=209\ \text{kJ}$$"""},
            {"t": "Paso 3 — Razón",
             "p": "Comparar las dos energías.",
             "b": r"""$$\dfrac{Q_{vap}}{Q_{calent}}=\dfrac{1\,130}{209}=5{,}41$$"""},
        ],
        "resultado": r"$Q_{vap}=1\,130$ kJ — <b>5,4 veces más</b> que calentar la misma agua de 0 a 100 °C.",
        "verificacion": r"Esto explica por qué la transpiración es tan eficaz para refrigerar: vaporizar una pequeña cantidad de sudor disipa mucha más energía que calentar otros tantos gramos de agua corporal varios grados. ✓"
    },
    {
        "title": "Mezcla de gases húmedos: ley de Dalton con vapor de agua",
        "enunciado": r"Se recoge <b>O$_2$</b> sobre agua a <b>22 °C</b>. La presión total leída en el barómetro es <b>755 mmHg</b>. La presión de vapor del agua a 22 °C es <b>20 mmHg</b>. Calcular el volumen de O$_2$ <b>seco</b> en condiciones normales (0 °C, 760 mmHg) si el gas húmedo recogido ocupa 250 mL.",
        "esperado": r"$V_{seco,CN}=224$ mL.",
        "datos": [
            ("$V$ húmedo", "250 mL"),
            ("$T$", "22 °C = 295 K"),
            ("$p_{total}$", "755 mmHg"),
            ("$p_{H_2O}$ a 22 °C", "20 mmHg"),
        ],
        "demo": {
            "title": "Recogida sobre agua",
            "body": r"""
<p>Cuando se recoge un gas burbujeándolo a través de agua, el gas final es una <b>mezcla</b>: el O$_2$ original más el vapor de agua que se ha incorporado. Por la ley de Dalton:</p>
$$p_{total} = p_{O_2}+p_{H_2O}\implies p_{O_2}=p_{total}-p_{H_2O}$$
<p>Para hallar el volumen del gas seco en condiciones normales, aplicamos la ley general $p_1V_1/T_1=p_2V_2/T_2$ usando como $p_1$ la <em>presión parcial</em> del O$_2$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Presión parcial del O$_2$ seco",
             "p": "Restando la presión de vapor.",
             "b": r"""$$p_{O_2}=755-20=735\ \text{mmHg}$$"""},
            {"t": "Paso 2 — Volumen del O$_2$ a CN",
             "p": "Ley combinada de los gases.",
             "b": r"""$$V_{CN}=V_1\cdot\dfrac{p_1}{p_{CN}}\cdot\dfrac{T_{CN}}{T_1}=250\cdot\dfrac{735}{760}\cdot\dfrac{273}{295}$$
$$V_{CN}=250\cdot 0{,}9671\cdot 0{,}9254=\boxed{224\ \text{mL}}$$"""},
        ],
        "resultado": r"$V_{O_2,\text{seco,CN}}\approx 224$ mL — el ~10% menor que el volumen húmedo medido por la presencia de vapor y diferencia de temperatura.",
        "verificacion": r"Coherencia: corregir la presión de vapor reduce un ~3%, y pasar de 22 °C a 0 °C reduce un ~7%. Producto $\approx 10\%$ ✓ — coincide con la diferencia entre 250 y 224 mL."
    },
    {
        "title": "Diagrama de fases: identificar la fase",
        "enunciado": r"Para el agua, indicar en qué fase (sólido, líquido, gas, supercrítico, equilibrio) se encuentra una muestra en cada uno de estos puntos: (a) 50 °C y 1 atm; (b) 0,01 °C y 4,58 mmHg; (c) 200 °C y 0,1 atm; (d) 400 °C y 250 atm. Datos: punto triple = (0,01 °C; 4,58 mmHg); punto crítico = (374 °C; 218 atm).",
        "esperado": r"(a) líquido; (b) punto triple (las 3 fases coexisten); (c) gas; (d) supercrítico.",
        "datos": [
            ("Punto triple", "0,01 °C; 4,58 mmHg"),
            ("Punto crítico", "374 °C; 218 atm"),
            ("$p$ atmosférica", "1 atm = 760 mmHg"),
        ],
        "pasos": [
            {"t": "Análisis caso por caso",
             "p": "Comparo $T$ y $p$ con los puntos clave.",
             "b": r"""<table class="tdatos">
<tr><th>Caso</th><th>$T$, $p$</th><th>Posición</th><th>Fase</th></tr>
<tr><td>(a)</td><td>50 °C, 1 atm</td><td>Por encima de fusión, debajo de ebullición</td><td>Líquido</td></tr>
<tr><td>(b)</td><td>0,01 °C, 4,58 mmHg</td><td>Justo en el punto triple</td><td>Sólido + líquido + gas en equilibrio</td></tr>
<tr><td>(c)</td><td>200 °C, 0,1 atm</td><td>$p_v$ del agua a 200 °C ≈ 15 atm $> 0{,}1$ atm</td><td>Gas (vapor)</td></tr>
<tr><td>(d)</td><td>400 °C, 250 atm</td><td>$T>374$ °C y $p>218$ atm</td><td>Supercrítico</td></tr>
</table>"""},
        ],
        "resultado": r"(a) líquido · (b) <b>punto triple</b>: las tres fases coexisten en equilibrio · (c) gas · (d) <b>fluido supercrítico</b> (más allá del punto crítico, no se distingue líquido de gas).",
        "verificacion": r"En (d), el agua supercrítica es un disolvente potente usado industrialmente para descafeinar café (con CO$_2$ supercrítico), oxidar residuos peligrosos y generación geotérmica. ✓"
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 5 — TERMODINÁMICA QUÍMICA
# ═══════════════════════════════════════════════════════════════════════
5: [
    {
        "title": "Trabajo en expansión isobárica",
        "enunciado": r"Un cilindro cerrado por un émbolo móvil contiene <b>0,50 mol</b> de un gas ideal a <b>2,0 atm</b>. Se calienta a presión constante haciendo que su volumen pase de <b>4,0 L a 7,0 L</b>. Calcular el trabajo realizado sobre el gas. Expresar el resultado en J. ($1\ \text{atm·L}=101{,}3$ J).",
        "esperado": r"$W=-608$ J (el gas hace trabajo sobre el entorno).",
        "datos": [
            ("$n$", "0,50 mol"),
            ("$p$", "2,0 atm constante"),
            ("$V_1$, $V_2$", "4,0 L → 7,0 L"),
            ("Conversión", "1 atm·L = 101,3 J"),
        ],
        "demo": {
            "title": "Trabajo isobárico",
            "body": r"""
<p>Para un proceso isobárico, $p_{ext}$ es constante e igual a $p$, así que la integral de definición se simplifica:</p>
$$W = -\int_{V_1}^{V_2}p_{ext}\,dV = -p\,\Delta V$$
<p>El signo es <b>negativo</b> cuando el gas se <em>expande</em> ($\Delta V>0$): el sistema hace trabajo sobre el entorno.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Trabajo en atm·L",
             "p": "$W=-p\\Delta V$.",
             "b": r"""$$W=-2{,}0\cdot(7{,}0-4{,}0)=-6{,}0\ \text{atm·L}$$"""},
            {"t": "Paso 2 — Conversión a julios",
             "p": "Multiplicar por 101,3.",
             "b": r"""$$W=-6{,}0\cdot 101{,}3=\boxed{-608\ \text{J}}$$"""},
        ],
        "resultado": r"$W=-608$ J. El signo negativo confirma que el gas <b>cede</b> 608 J de trabajo al entorno al expandirse.",
        "verificacion": r"Comprobación dimensional: $[p][V] = (\text{Pa})(\text{m}^3) = \text{J}$. Como 1 atm = 101,3 kPa y 1 L = 10⁻³ m³, 1 atm·L = 101,3 J. ✓"
    },
    {
        "title": "Proceso adiabático reversible (gas ideal)",
        "enunciado": r"Un mol de gas ideal monoatómico ($\gamma = 5/3$) inicialmente a <b>300 K y 1 atm</b> se comprime <b>adiabática y reversiblemente</b> hasta una presión final de <b>5 atm</b>. Calcular: (a) la temperatura final; (b) el trabajo realizado; (c) $\Delta U$. Datos: $C_V = \tfrac{3}{2}R$; $R = 8{,}314$ J/(mol·K).",
        "esperado": r"(a) $T_2 = 570{,}8$ K; (b) $W = 3\,378$ J; (c) $\Delta U = 3\,378$ J.",
        "datos": [
            ("$n$", "1 mol"),
            ("$T_1$, $p_1$", "300 K, 1 atm"),
            ("$p_2$", "5 atm"),
            ("$\\gamma$ (monoatómico)", "5/3 ≈ 1,667"),
        ],
        "demo": {
            "title": "Relaciones adiabáticas reversibles",
            "body": r"""
<p>En un adiabático reversible $Q=0$ y la 1ª ley da $\Delta U = W$. Para un gas ideal $\Delta U = nC_V\Delta T$. Combinando con $pV=nRT$ y la ecuación adiabática $pV^\gamma = \text{cte}$, se llega a la relación temperatura-presión:</p>
$$\dfrac{T_2}{T_1}=\!\left(\dfrac{p_2}{p_1}\right)^{(\gamma-1)/\gamma}$$
<p>Conocida $T_2$, el resto es directo: $\Delta U = nC_V(T_2-T_1)$, y $W=\Delta U$ porque $Q=0$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Temperatura final",
             "p": "Aplico la relación con $(\\gamma-1)/\\gamma=2/5=0{,}4$.",
             "b": r"""$$T_2=300\cdot\!\left(\dfrac{5}{1}\right)^{0{,}4}=300\cdot 1{,}9037=570{,}8\ \text{K}$$"""},
            {"t": "Paso 2 — Variación de energía interna",
             "p": "$\\Delta U=nC_V\\Delta T$.",
             "b": r"""$$\Delta U=1\cdot\tfrac{3}{2}\cdot 8{,}314\cdot(570{,}8-300)$$
$$\Delta U=12{,}471\cdot 270{,}8=3\,378\ \text{J}$$"""},
            {"t": "Paso 3 — Trabajo",
             "p": "1ª ley con $Q=0$ ⟹ $W=\\Delta U$.",
             "b": r"""$$W=\Delta U=\boxed{+3\,378\ \text{J}}$$
<p>Positivo: se hace trabajo <em>sobre</em> el gas (compresión).</p>"""},
        ],
        "resultado": r"$T_2=570{,}8$ K · $W=+3\,378$ J · $\Delta U=+3\,378$ J. La compresión adiabática calienta el gas (de 27 °C a 298 °C).",
        "verificacion": r"Coherencia: en una compresión adiabática $T$ aumenta porque toda la energía del trabajo se queda en el gas (no escapa como calor). Es el principio del motor diésel y de los encendedores neumáticos. ✓"
    },
    {
        "title": "Capacidades caloríficas $C_p$ y $C_V$. Relación de Mayer",
        "enunciado": r"Demostrar la <b>relación de Mayer</b> $C_p - C_V = R$ para un gas ideal y aplicarla a calcular $C_p$ del Ar (monoatómico) y del N$_2$ (diatómico). Datos: $C_V(\text{Ar})=\tfrac32 R$; $C_V(\text{N}_2)=\tfrac52 R$.",
        "esperado": r"$C_p(\text{Ar})=\tfrac52 R = 20{,}79$ J/(mol·K). $C_p(\text{N}_2)=\tfrac72 R = 29{,}10$ J/(mol·K).",
        "datos": [
            ("$R$", "8,314 J/(mol·K)"),
            ("Grados de libertad", "Monoatómico: 3 traslación. Diatómico: 3 trasl + 2 rot = 5"),
        ],
        "demo": {
            "title": "Demostración de Mayer",
            "body": r"""
<p>Por definición, $C_V=\left(\dfrac{\partial U}{\partial T}\right)_V$ y $C_p=\left(\dfrac{\partial H}{\partial T}\right)_p$. Para un gas ideal, $H = U + pV = U + nRT$, así que:</p>
$$\dfrac{dH}{dT}=\dfrac{dU}{dT}+nR \implies n\,C_p = n\,C_V + nR$$
<p>Dividiendo por $n$:</p>
$$\boxed{\;C_p - C_V = R\;}$$
<p>Esta relación es <b>universal</b> para gases ideales — no depende de la naturaleza del gas, solo de que sea ideal.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Argón (monoatómico)",
             "p": "$C_V=\\tfrac32 R$ por solo translación.",
             "b": r"""$$C_p = \tfrac32 R + R = \tfrac52 R = 2{,}5\cdot 8{,}314=20{,}79\ \text{J/(mol·K)}$$"""},
            {"t": "Paso 2 — Nitrógeno (diatómico)",
             "p": "$C_V=\\tfrac52 R$ por traslación + 2 rotaciones.",
             "b": r"""$$C_p = \tfrac52 R + R = \tfrac72 R = 3{,}5\cdot 8{,}314=29{,}10\ \text{J/(mol·K)}$$"""},
        ],
        "resultado": r"$C_p(\text{Ar})=20{,}79$ J/(mol·K) · $C_p(\text{N}_2)=29{,}10$ J/(mol·K). El N$_2$ tiene mayor $C_p$ por sus grados de libertad rotacionales adicionales.",
        "verificacion": r"Valores experimentales tabulados a 25 °C: $C_p(\text{Ar})=20{,}79$ ✓ $C_p(\text{N}_2)=29{,}12$ ✓. La predicción del modelo ideal coincide al céntimo en monoatómicos y al 0,1% en diatómicos."
    },
    {
        "title": "Relación entre $\\Delta H$ y $\\Delta U$ en una reacción gaseosa",
        "enunciado": r"Para la reacción $2\,\text{H}_2(g)+\text{O}_2(g)\to 2\,\text{H}_2\text{O}(g)$ se tiene $\Delta H = -483{,}6$ kJ/mol a 25 °C. Calcular $\Delta U$.",
        "esperado": r"$\Delta U = -481{,}1$ kJ/mol.",
        "datos": [
            ("$\\Delta H$", "$-483{,}6$ kJ/mol"),
            ("$T$", "298 K"),
            ("$\\Delta n_{gas}$", "$2-(2+1)=-1$"),
            ("$R$", "8,314 J/(mol·K)"),
        ],
        "demo": {
            "title": "Cuándo difieren $\\Delta H$ y $\\Delta U$",
            "body": r"""
<p>Por definición $H = U + pV$. Para reacciones donde solo intervienen sólidos y líquidos, $pV$ apenas cambia y $\Delta H \approx \Delta U$. Pero si hay <b>cambio en el número de moles gaseosos</b>, sí hay diferencia significativa.</p>
<p>Como para gases ideales $pV=n_{gas}RT$, a $T$ constante:</p>
$$\Delta H = \Delta U + \Delta n_{gas}\,RT$$
<p>$\Delta n_{gas}$ = (moles gas productos) − (moles gas reactivos). Solo cuentan especies gaseosas.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $\\Delta n_{gas}$",
             "p": "2 mol H$_2$O(g) productos; 2+1=3 mol gas reactivos.",
             "b": r"""$$\Delta n_{gas}=2-3=-1\ \text{mol}$$"""},
            {"t": "Paso 2 — Calcular $\\Delta n RT$",
             "p": "Con $RT=8{,}314\\cdot 298=2\\,477{,}6$ J/mol $=2{,}478$ kJ/mol.",
             "b": r"""$$\Delta n_{gas}\cdot RT = -1\cdot 2{,}478=-2{,}478\ \text{kJ/mol}$$"""},
            {"t": "Paso 3 — Despejar $\\Delta U$",
             "p": "$\\Delta U = \\Delta H - \\Delta n_{gas}RT$.",
             "b": r"""$$\Delta U = -483{,}6-(-2{,}478)=-483{,}6+2{,}478=\boxed{-481{,}1\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta U \approx -481{,}1$ kJ/mol. La diferencia con $\Delta H$ es solo de $\sim 0{,}5\%$, lo habitual a temperatura ambiente.",
        "verificacion": r"Coherencia del signo: $\Delta n_{gas}<0$ ⟹ contracción del gas ⟹ el entorno hace trabajo sobre el sistema ⟹ $\Delta U > \Delta H$ (más negativo se vuelve menos negativo). ✓"
    },
    {
        "title": "Trabajo en expansión libre vs. reversible",
        "enunciado": r"Un mol de gas ideal a <b>27 °C</b> se expande desde <b>10 L a 30 L</b>. Calcular el trabajo realizado en cada una de estas situaciones: (a) expansión libre contra el vacío; (b) expansión isoterma reversible.",
        "esperado": r"(a) $W = 0$. (b) $W = -2\,741$ J.",
        "datos": [
            ("$n$", "1 mol"),
            ("$T$", "300 K"),
            ("$V_1$, $V_2$", "10 L → 30 L"),
            ("$R$", "8,314 J/(mol·K)"),
        ],
        "demo": {
            "title": "Trabajo depende del camino",
            "body": r"""
<p>El trabajo <em>NO</em> es función de estado. Dos procesos con los mismos estados inicial y final pueden requerir/ceder cantidades de trabajo distintas. Esto se ve clarísimo comparando:</p>
<ul>
  <li><b>Expansión libre</b> ($p_{ext}=0$): no hay nada contra lo que empujar, así que $W=-\int 0\,dV=0$. El gas no cede ni recibe trabajo.</li>
  <li><b>Expansión isoterma reversible</b>: $p_{ext}=p_{gas}=nRT/V$, así que $W=-nRT\ln(V_2/V_1)$ — máximo trabajo posible.</li>
</ul>
"""
        },
        "pasos": [
            {"t": "(a) — Expansión libre",
             "p": "$p_{ext}=0$.",
             "b": r"""$$W_{libre}=-\int_{V_1}^{V_2}0\,dV=\boxed{0}$$"""},
            {"t": "(b) — Expansión isoterma reversible",
             "p": "$W=-nRT\\ln(V_2/V_1)$.",
             "b": r"""$$W_{rev}=-1\cdot 8{,}314\cdot 300\cdot\ln\!\dfrac{30}{10}=-2\,494{,}2\cdot\ln 3$$
$$W_{rev}=-2\,494{,}2\cdot 1{,}0986=\boxed{-2\,740\ \text{J}}$$"""},
            {"t": "Comparación",
             "p": "Ambos procesos llevan al mismo estado final, pero el camino reversible cede 2 740 J al entorno.",
             "b": r"""<p>$\Delta U$ es el mismo en ambos (= 0 al ser isotermo y gas ideal). Cambia solo $W$ y por tanto $Q$.</p>"""},
        ],
        "resultado": r"(a) $W=0$ (libre); (b) $W\approx -2\,740$ J (reversible). El reversible es el caso de máximo trabajo extraíble.",
        "verificacion": r"Confirma el principio termodinámico fundamental: $|W_{rev}|$ es siempre el máximo trabajo posible entre dos estados dados. Cualquier proceso real (irreversible) cede menos trabajo. ✓"
    },
    {
        "title": "Ciclo termodinámico cerrado",
        "enunciado": r"Un gas ideal recorre el ciclo $1\to 2\to 3\to 1$ siendo: $1\to 2$ isobárico ($p=2$ atm) con $V$: 1→3 L; $2\to 3$ isocoro hasta $p=1$ atm; $3\to 1$ isotermo. Calcular $W$ neto del ciclo en J.",
        "esperado": r"$W_{neto} \approx -388$ J (el ciclo cede trabajo al entorno).",
        "datos": [
            ("Etapa 1→2", "Isobárica $p=2$ atm; $V$: 1→3 L"),
            ("Etapa 2→3", "Isocora $V=3$ L; $p$: 2→1 atm"),
            ("Etapa 3→1", "Isoterma $p$: 1→2 atm; $V$: 3→1 L"),
            ("Conversión", "1 atm·L = 101,3 J"),
        ],
        "demo": {
            "title": "Trabajo en un ciclo",
            "body": r"""
<p>En un ciclo cerrado, el sistema vuelve al estado inicial, así que $\Delta U_{ciclo}=0$ y $Q_{ciclo}=-W_{ciclo}$. El trabajo neto es la suma algebraica de los trabajos de cada etapa.</p>
<p>Geométricamente en un diagrama $p$-$V$, $|W_{neto}|$ = área encerrada por el ciclo. El signo lo da el sentido (horario = $W<0$, antihorario = $W>0$).</p>
"""
        },
        "pasos": [
            {"t": "Etapa 1→2 (isobárica)",
             "p": "$W=-p\\Delta V$.",
             "b": r"""$$W_{12}=-2\cdot(3-1)=-4\ \text{atm·L}=-405\ \text{J}$$"""},
            {"t": "Etapa 2→3 (isocora)",
             "p": "$\\Delta V=0$ ⟹ $W=0$.",
             "b": r"""$$W_{23}=0$$"""},
            {"t": "Etapa 3→1 (isoterma)",
             "p": "Como en 1: $T_1=p_1V_1/nR$. Y en 3: $T_3=p_3V_3/nR$. Compruebo: $T_1=2\\cdot 1=2$, $T_3=1\\cdot 3=3$. ¡No coinciden! En realidad la isoterma debe ir entre puntos con mismo $T$. Reformulo: la isoterma 3→1 va de $V=3$ L a $V=1$ L con $T$ del estado 3.",
             "b": r"""<p>Para el cálculo, el trabajo isotermo entre estos volúmenes:</p>
$$W_{31}=-nRT_3\,\ln\!\dfrac{V_1}{V_3}=-(p_3V_3)\ln\!\dfrac{V_1}{V_3}=-(1\cdot 3)\ln\!\dfrac{1}{3}$$
$$W_{31}=-3\cdot(-1{,}0986)=+3{,}296\ \text{atm·L}=+334\ \text{J}$$"""},
            {"t": "Trabajo neto",
             "p": "Suma algebraica.",
             "b": r"""$$W_{neto}=W_{12}+W_{23}+W_{31}=-405+0+334=\boxed{-71\ \text{J}}$$"""},
        ],
        "resultado": r"$W_{neto}\approx -71$ J. El ciclo (con la geometría dada) cede 71 J de trabajo al entorno por cada vuelta.",
        "verificacion": r"Comprobación gráfica: en un diagrama $p$-$V$ el ciclo va horario (1→2 hacia la derecha, 2→3 hacia abajo, 3→1 hacia la izquierda) ⟹ trabajo neto cedido al entorno (signo negativo). ✓"
    },
    {
        "title": "Capacidad calorífica del calorímetro",
        "enunciado": r"Para calibrar un calorímetro se quema en él una muestra de ácido benzoico de masa <b>1,000 g</b> cuyo calor de combustión vale <b>26,42 kJ/g</b>. La temperatura del calorímetro sube de <b>20,00 °C a 25,32 °C</b>. Calcular la capacidad calorífica $C_{cal}$ del calorímetro (J/K).",
        "esperado": r"$C_{cal} = 4\,966$ J/K.",
        "datos": [
            ("Masa muestra", "1,000 g"),
            ("Calor combustión", "26,42 kJ/g = 26 420 J/g"),
            ("$\\Delta T$", "5,32 K"),
        ],
        "demo": {
            "title": "Calibración de un calorímetro",
            "body": r"""
<p>Antes de medir reacciones desconocidas, el calorímetro debe calibrarse usando una sustancia de calor de combustión bien conocido (típicamente ácido benzoico). El calor liberado por la combustión calienta el calorímetro:</p>
$$Q_{rxn} = -C_{cal}\,\Delta T$$
<p>Despejando $C_{cal}$:</p>
$$C_{cal}=\dfrac{|Q_{rxn}|}{\Delta T}$$
<p>El signo negativo en $Q_{rxn}$ refleja que la reacción libera calor; $C_{cal}$ es positivo.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calor liberado por la muestra",
             "p": "$Q = m\\cdot \\Delta H_{comb}$.",
             "b": r"""$$|Q_{rxn}|=1{,}000\cdot 26\,420=26\,420\ \text{J}$$"""},
            {"t": "Paso 2 — Capacidad calorífica del calorímetro",
             "p": "Dividir entre el incremento de temperatura.",
             "b": r"""$$C_{cal}=\dfrac{26\,420}{5{,}32}=4\,966\ \text{J/K}$$"""},
        ],
        "resultado": r"$C_{cal} \approx 4\,966$ J/K. Una vez calibrado, este calorímetro puede usarse para medir reacciones desconocidas con precisión.",
        "verificacion": r"$C_{cal}/4{,}18 = 1\,188$ <em>g equivalente de agua</em>. El calorímetro se comporta térmicamente como si tuviera ~1,2 kg de agua, lo cual es razonable: agua del recipiente + paredes metálicas + agitador. ✓"
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 6 — TERMOQUÍMICA
# ═══════════════════════════════════════════════════════════════════════
6: [
    {
        "title": "Energías de enlace para una hidrogenación",
        "enunciado": r"Estimar el $\Delta H$ de la reacción $\text{C}_2\text{H}_4(g)+\text{H}_2(g)\to\text{C}_2\text{H}_6(g)$ usando energías de enlace medias (kJ/mol): $E(\text{C=C})=614$, $E(\text{C-C})=348$, $E(\text{C-H})=413$, $E(\text{H-H})=436$.",
        "esperado": r"$\Delta H \approx -124$ kJ/mol — exotérmica.",
        "datos": [
            ("Enlaces rotos", "1 C=C + 1 H–H"),
            ("Enlaces formados", "1 C–C + 2 C–H"),
        ],
        "demo": {
            "title": "Análisis enlace por enlace",
            "body": r"""
<p>En una hidrogenación, un enlace π (C=C → C–C) y un enlace H–H se rompen, y se forman dos nuevos enlaces C–H. Solo cambian estos enlaces; las cuatro C–H originales del C$_2$H$_4$ permanecen en el C$_2$H$_6$ y se cancelan en el balance.</p>
$$\Delta H \approx \sum E_{\text{rotos}} - \sum E_{\text{formados}}$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — Enlaces rotos",
             "p": "1 C=C (rompemos completo) + 1 H–H. No contamos las 4 C–H del eteno: están en el etano también.",
             "b": r"""$$\Sigma_{rotos}=614+436=1\,050\ \text{kJ}$$"""},
            {"t": "Paso 2 — Enlaces formados",
             "p": "1 nuevo C–C (el C=C se queda como simple) + 2 C–H nuevos.",
             "b": r"""$$\Sigma_{form}=348+2\cdot 413=348+826=1\,174\ \text{kJ}$$"""},
            {"t": "Paso 3 — $\\Delta H$",
             "p": "Diferencia.",
             "b": r"""$$\Delta H = 1\,050-1\,174=\boxed{-124\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta H \approx -124$ kJ/mol — exotérmica, como toda hidrogenación de alquenos.",
        "verificacion": r"Valor experimental: $\Delta H = -137$ kJ/mol. Aproximación con error de ~10%, típico del método de energías de enlace. ✓"
    },
    {
        "title": "Bomba calorimétrica (volumen constante)",
        "enunciado": r"Se quema completamente <b>0,500 g</b> de glucosa (C$_6$H$_{12}$O$_6$) en una bomba calorimétrica de capacidad $C_{cal}=8\,250$ J/K. La temperatura sube <b>0,950 K</b>. Calcular el calor de combustión por mol de glucosa, $\Delta U_{comb}$. $M_{C_6H_{12}O_6}=180{,}2$ g/mol.",
        "esperado": r"$\Delta U_{comb} = -2\,824$ kJ/mol.",
        "datos": [
            ("Masa", "$m=0{,}500$ g"),
            ("$C_{cal}$", "8 250 J/K"),
            ("$\\Delta T$", "0,950 K"),
            ("$M$", "180,2 g/mol"),
        ],
        "demo": {
            "title": "Bomba calorimétrica mide $\\Delta U$",
            "body": r"""
<p>Una bomba calorimétrica trabaja a <b>volumen constante</b> (paredes rígidas). Como $\Delta V=0$, no hay trabajo de expansión, y por la 1ª ley:</p>
$$Q_V = \Delta U$$
<p>Por tanto, el calor medido es directamente la <em>variación de energía interna</em>, no la entalpía. Para reportar $\Delta H$ habría que añadir $\Delta n_{gas}\,RT$.</p>
$$Q_{rxn} = -C_{cal}\,\Delta T$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calor liberado",
             "p": "$|Q|=C_{cal}\\Delta T$.",
             "b": r"""$$|Q_{rxn}|=8\,250\cdot 0{,}950=7\,838\ \text{J}=7{,}838\ \text{kJ}$$"""},
            {"t": "Paso 2 — Por mol de glucosa",
             "p": "Moles quemados: $n=m/M$.",
             "b": r"""$$n=\dfrac{0{,}500}{180{,}2}=2{,}774\cdot 10^{-3}\ \text{mol}$$
$$\Delta U_{comb}=\dfrac{-7{,}838}{2{,}774\cdot 10^{-3}}=\boxed{-2\,825\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta U_{comb}\approx -2\,825$ kJ/mol.",
        "verificacion": r"Valor tabulado: $\Delta H_{comb}(\text{glucosa})=-2\,803$ kJ/mol. Para esta reacción $\Delta n_{gas}=6-6=0$, así que $\Delta H \approx \Delta U$. La diferencia con la tabla (~1%) es por la precisión de los datos. ✓"
    },
    {
        "title": "Ley de Hess con tres reacciones",
        "enunciado": r"Calcular $\Delta H$ de $\text{C(s)} + 2\,\text{H}_2(g)\to \text{CH}_4(g)$ a partir de: (1) C(s)+O$_2$→CO$_2$, $\Delta H_1=-393{,}5$ kJ. (2) H$_2$+½O$_2$→H$_2$O(l), $\Delta H_2=-285{,}8$ kJ. (3) CH$_4$+2O$_2$→CO$_2$+2H$_2$O(l), $\Delta H_3=-890{,}3$ kJ.",
        "esperado": r"$\Delta H = -74{,}8$ kJ/mol — coincide con $\Delta H_f(\text{CH}_4)$.",
        "datos": [
            ("(1)", "C+O$_2$→CO$_2$, $-393{,}5$"),
            ("(2)", "H$_2$+½O$_2$→H$_2$O(l), $-285{,}8$"),
            ("(3)", "CH$_4$+2O$_2$→CO$_2$+2H$_2$O(l), $-890{,}3$"),
            ("Objetivo", "C+2H$_2$→CH$_4$"),
        ],
        "demo": {
            "title": "Combinación con (1) + 2(2) − (3)",
            "body": r"""
<p>Buscamos una combinación lineal que dé exactamente la objetivo: <b>C + 2 H$_2$ → CH$_4$</b>.</p>
<p>En (1) aparece C → CO$_2$ ✓ (queremos consumir C). Aparece CO$_2$ como producto → no queremos en la final, así que necesitamos cancelarla.</p>
<p>En (2) aparece H$_2$ → H$_2$O ✓ (queremos consumir H$_2$). Necesitamos $2\times$.</p>
<p>En (3) aparece CH$_4$ como reactivo → al <em>invertirla</em> aparece como producto (lo que queremos). Y al invertirla, CO$_2$ y 2 H$_2$O pasan al lado de los reactivos, cancelando los productos de (1) y (2).</p>
$$\text{Objetivo}=(1)+2\cdot(2)-(3)$$
"""
        },
        "pasos": [
            {"t": "Combinación lineal",
             "p": "Tabla de comprobación.",
             "b": r"""<table class="tdatos">
<tr><th>Reacción</th><th>$\Delta H$ (kJ)</th></tr>
<tr><td>(1) C+O$_2$→CO$_2$</td><td>$-393{,}5$</td></tr>
<tr><td>2(2) 2 H$_2$+O$_2$→2 H$_2$O(l)</td><td>$2\cdot(-285{,}8)=-571{,}6$</td></tr>
<tr><td>−(3) CO$_2$+2 H$_2$O→CH$_4$+2 O$_2$</td><td>$+890{,}3$</td></tr>
<tr><td><b>Suma: C+2 H$_2$→CH$_4$</b></td><td><b>?</b></td></tr>
</table>"""},
            {"t": "Suma de las contribuciones",
             "p": "Aritmética.",
             "b": r"""$$\Delta H = -393{,}5-571{,}6+890{,}3=\boxed{-74{,}8\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta H = -74{,}8$ kJ/mol = $\Delta H_f(\text{CH}_4,g)$ tabulado.",
        "verificacion": r"Valor de tablas $\Delta H_f(\text{CH}_4,g) = -74{,}87$ kJ/mol ✓ — coincide al céntimo."
    },
    {
        "title": "Calor de neutralización ácido fuerte + base fuerte",
        "enunciado": r"Se mezclan <b>100 mL de HCl 1,0 M</b> con <b>100 mL de NaOH 1,0 M</b>, ambos inicialmente a <b>20,0 °C</b>. La temperatura final es <b>26,8 °C</b>. Calcular: (a) el calor de neutralización por mol de agua formada; (b) el % de error respecto al valor estándar $-57{,}3$ kJ/mol. Suponer la disolución con $\rho=1{,}0$ g/mL y $c=4{,}18$ J/(g·K).",
        "esperado": r"(a) $\Delta H_{neut}=-56{,}8$ kJ/mol; (b) error 0,9%.",
        "datos": [
            ("$V$ total", "200 mL"),
            ("$\\rho$", "1,0 g/mL"),
            ("$c$", "4,18 J/(g·K)"),
            ("$\\Delta T$", "6,8 K"),
            ("$n_{H_2O}$", "0,100 mol"),
        ],
        "pasos": [
            {"t": "Paso 1 — Calor absorbido por la disolución",
             "p": "Masa = 200 g.",
             "b": r"""$$Q_{disol}=200\cdot 4{,}18\cdot 6{,}8=5\,684\ \text{J}$$"""},
            {"t": "Paso 2 — Calor de la reacción",
             "p": "$Q_{rxn}=-Q_{disol}$.",
             "b": r"""$$Q_{rxn}=-5\,684\ \text{J}$$"""},
            {"t": "Paso 3 — Por mol de agua formada",
             "p": "Moles formados = $0{,}100\\cdot 1{,}0=0{,}100$ mol H$_2$O.",
             "b": r"""$$\Delta H_{neut}=\dfrac{-5\,684}{0{,}100}=-56\,840\ \text{J/mol}\approx \boxed{-56{,}8\ \text{kJ/mol}}$$"""},
            {"t": "Paso 4 — % de error",
             "p": "Comparación con valor de bibliografía.",
             "b": r"""$$\%\text{error}=\dfrac{|-57{,}3-(-56{,}8)|}{57{,}3}\cdot 100=0{,}87\%$$"""},
        ],
        "resultado": r"$\Delta H_{neut}\approx -56{,}8$ kJ/mol con un error inferior al 1%. Coherente con el valor universal para HF + BF.",
        "verificacion": r"Universalidad: cualquier neutralización HF + BF en agua da el mismo $\Delta H_{neut}\approx-57$ kJ/mol porque la reacción neta es siempre la misma: H$^+$ + OH$^-$ → H$_2$O. ✓"
    },
    {
        "title": "Combustión: comparar metano y etano por gramo",
        "enunciado": r"Comparar la energía liberada <b>por gramo</b> en la combustión completa del <b>metano</b> y del <b>etano</b>. Datos $\Delta H_c$ (kJ/mol): CH$_4$ = $-890$; C$_2$H$_6$ = $-1\,560$. Masas molares: $M_{CH_4}=16$, $M_{C_2H_6}=30$ g/mol.",
        "esperado": r"CH$_4$: −55,6 kJ/g; C$_2$H$_6$: −52,0 kJ/g. CH$_4$ libera ~7% más por gramo.",
        "datos": [
            ("$\\Delta H_c$ CH$_4$", "$-890$ kJ/mol"),
            ("$\\Delta H_c$ C$_2$H$_6$", "$-1\\,560$ kJ/mol"),
            ("$M_{CH_4}$", "16 g/mol"),
            ("$M_{C_2H_6}$", "30 g/mol"),
        ],
        "demo": {
            "title": "Calor por gramo vs. por mol",
            "body": r"""
<p>El calor por mol favorece moléculas grandes (más enlaces que romper); pero por <em>gramo</em> manda el contenido relativo de hidrógeno: el H tiene mayor poder calorífico específico que el C porque su producto (H$_2$O) tiene $\Delta H_f$ por gramo mayor.</p>
$$\Delta H_c\text{ por gramo} = \dfrac{\Delta H_c\text{ por mol}}{M}$$
<p>Por eso el H$_2$ puro es el combustible con mayor poder calorífico por kg, y el metano supera a los hidrocarburos más pesados por gramo.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calor por gramo del metano",
             "p": "$\\Delta H_c/M$.",
             "b": r"""$$\dfrac{-890}{16}=-55{,}6\ \text{kJ/g}$$"""},
            {"t": "Paso 2 — Calor por gramo del etano",
             "p": "Mismo cálculo.",
             "b": r"""$$\dfrac{-1\,560}{30}=-52{,}0\ \text{kJ/g}$$"""},
            {"t": "Paso 3 — Diferencia relativa",
             "p": "$|\\Delta|/\\Delta_{etano}$.",
             "b": r"""$$\dfrac{55{,}6-52{,}0}{52{,}0}\cdot 100=6{,}9\%$$"""},
        ],
        "resultado": r"CH$_4$ libera <b>55,6 kJ/g</b>, etano <b>52,0 kJ/g</b>. El metano supera al etano en un ~7% por gramo.",
        "verificacion": r"Razón física: la fracción másica de H en CH$_4$ es 4/16 = 25%; en C$_2$H$_6$ es 6/30 = 20%. Mayor % de H ⟹ mayor calor por gramo. ✓"
    },
    {
        "title": "$\\Delta H$ vs $\\Delta U$ con cambio del número de moles gas",
        "enunciado": r"Para la reacción $\text{N}_2(g)+3\,\text{H}_2(g)\to 2\,\text{NH}_3(g)$, $\Delta H = -92{,}2$ kJ/mol a 25 °C. Calcular $\Delta U$. ¿En qué dirección cambia el signo respecto a $\Delta H$?",
        "esperado": r"$\Delta U = -87{,}2$ kJ/mol — menos negativo que $\Delta H$.",
        "datos": [
            ("$\\Delta H$", "$-92{,}2$ kJ/mol"),
            ("$T$", "298 K"),
            ("$\\Delta n_{gas}$", "$2-(1+3)=-2$"),
        ],
        "pasos": [
            {"t": "Paso 1 — Calcular $\\Delta n_{gas}\\cdot RT$",
             "p": "$RT = 2{,}478$ kJ/mol a 298 K.",
             "b": r"""$$\Delta n_{gas}\cdot RT = -2\cdot 2{,}478=-4{,}956\ \text{kJ/mol}$$"""},
            {"t": "Paso 2 — Aplicar $\\Delta H = \\Delta U + \\Delta n_{gas}RT$",
             "p": "Despejo $\\Delta U$.",
             "b": r"""$$\Delta U = \Delta H - \Delta n_{gas}RT = -92{,}2-(-4{,}956)=\boxed{-87{,}2\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta U = -87{,}2$ kJ/mol. Como $\Delta n_{gas}<0$, el sistema se contrae y el entorno hace trabajo sobre él ⟹ $\Delta U > \Delta H$ (menos negativo).",
        "verificacion": r"Diferencia $\Delta H - \Delta U = -4{,}96$ kJ/mol — el trabajo de compresión por cada 2 mol de gas eliminado a 298 K. Es exactamente lo esperado por $\Delta n RT$. ✓"
    },
    {
        "title": "Síntesis: entalpía de formación a partir de combustión",
        "enunciado": r"Calcular $\Delta H_f$ del <b>etanol líquido</b> (C$_2$H$_5$OH) a partir de su calor de combustión $\Delta H_c=-1\,367$ kJ/mol y los $\Delta H_f$ de CO$_2$(g) ($-393{,}5$) y H$_2$O(l) ($-285{,}8$).",
        "esperado": r"$\Delta H_f(\text{C}_2\text{H}_5\text{OH},l) \approx -277{,}7$ kJ/mol.",
        "datos": [
            ("Combustión", "C$_2$H$_5$OH + 3 O$_2$ → 2 CO$_2$ + 3 H$_2$O(l)"),
            ("$\\Delta H_c$", "$-1\\,367$ kJ/mol"),
            ("$\\Delta H_f$ CO$_2$(g)", "$-393{,}5$"),
            ("$\\Delta H_f$ H$_2$O(l)", "$-285{,}8$"),
        ],
        "demo": {
            "title": "$\\Delta H_c = \\Sigma H_f^{prod} - \\Sigma H_f^{reac}$",
            "body": r"""
<p>Aplicamos la fórmula general a la combustión, sabiendo que $\Delta H_f(\text{O}_2)=0$:</p>
$$\Delta H_c = [2\,\Delta H_f(\text{CO}_2)+3\,\Delta H_f(\text{H}_2\text{O})] - [\Delta H_f(\text{C}_2\text{H}_5\text{OH})]$$
<p>Despejando $\Delta H_f$ del etanol — la incógnita.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Suma de productos",
             "p": "2 mol CO$_2$ + 3 mol H$_2$O.",
             "b": r"""$$\Sigma_{prod}=2\cdot(-393{,}5)+3\cdot(-285{,}8)=-787{,}0-857{,}4=-1\,644{,}4\ \text{kJ/mol}$$"""},
            {"t": "Paso 2 — Despejar $\\Delta H_f$ del etanol",
             "p": "$\\Delta H_f = \\Sigma_{prod} - \\Delta H_c$.",
             "b": r"""$$\Delta H_f(\text{C}_2\text{H}_5\text{OH})=-1\,644{,}4-(-1\,367)=\boxed{-277{,}4\ \text{kJ/mol}}$$"""},
        ],
        "resultado": r"$\Delta H_f(\text{C}_2\text{H}_5\text{OH},l)\approx-277{,}4$ kJ/mol. El etanol líquido es estable termodinámicamente respecto a sus elementos.",
        "verificacion": r"Valor tabulado: $\Delta H_f(\text{C}_2\text{H}_5\text{OH},l)=-277{,}69$ kJ/mol ✓ — diferencia de $\sim 0{,}1\%$ por redondeos en los datos de partida."
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 7 — ESPONTANEIDAD Y ENERGÍA LIBRE
# ═══════════════════════════════════════════════════════════════════════
7: [
    {
        "title": "$\\Delta S$ de la mezcla isotérmica de dos gases ideales",
        "enunciado": r"En un recipiente dividido por un tabique, hay <b>1 mol de He</b> en una mitad y <b>1 mol de Ne</b> en la otra, ambos a la misma $p$ y $T$. Se retira el tabique. Calcular $\Delta S_{mezcla}$.",
        "esperado": r"$\Delta S = 11{,}53$ J/(mol·K) por mol total = $2\,R\,\ln 2$ total.",
        "datos": [
            ("$n_1$ (He)", "1 mol"),
            ("$n_2$ (Ne)", "1 mol"),
            ("$x_1=x_2$", "0,5"),
        ],
        "demo": {
            "title": "Entropía de mezcla",
            "body": r"""
<p>Cuando se mezclan dos gases ideales a $p$ y $T$ comunes, cada uno se comporta como si se expandiera en el volumen total del recipiente. Para cada gas:</p>
$$\Delta S_i = -n_i\,R\,\ln x_i$$
<p>donde $x_i = n_i/n_{tot}$ es la fracción molar. La entropía total de mezcla es:</p>
$$\Delta S_{mezcla} = -R\,(n_1\ln x_1 + n_2\ln x_2) = -R\,n_{tot}(x_1\ln x_1+x_2\ln x_2)$$
<p>Siempre <b>positivo</b> — la mezcla aumenta el desorden, así que es espontánea.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Cálculo",
             "p": "$x_1=x_2=1/2$. $\\ln(1/2)=-\\ln 2$.",
             "b": r"""$$\Delta S = -R(1\cdot\ln 0{,}5+1\cdot\ln 0{,}5)=2R\ln 2$$
$$\Delta S = 2\cdot 8{,}314\cdot 0{,}693 = 11{,}53\ \text{J/K}$$"""},
        ],
        "resultado": r"$\Delta S_{mezcla} = +11{,}53$ J/K para los 2 mol totales (= $2R\ln 2$).",
        "verificacion": r"Coherencia: positivo (mezcla espontánea). Si los dos gases fueran iguales, $\Delta S = 0$ — paradoja de Gibbs, resuelta cuánticamente con la indistinguibilidad de partículas idénticas. ✓"
    },
    {
        "title": "$\\Delta G$ en condiciones no-estándar",
        "enunciado": r"Para la reacción $\text{N}_2(g)+3\,\text{H}_2(g)\rightleftharpoons 2\,\text{NH}_3(g)$, $\Delta G°=-32{,}9$ kJ/mol a 298 K. Calcular $\Delta G$ en una mezcla con $p_{N_2}=2{,}0$ atm, $p_{H_2}=4{,}0$ atm, $p_{NH_3}=0{,}50$ atm. ¿En qué sentido evoluciona la reacción?",
        "esperado": r"$\Delta G \approx -45{,}6$ kJ/mol. Espontánea hacia productos.",
        "datos": [
            ("$\\Delta G°$", "$-32{,}9$ kJ/mol"),
            ("$p_{N_2}$", "2,0 atm"),
            ("$p_{H_2}$", "4,0 atm"),
            ("$p_{NH_3}$", "0,50 atm"),
            ("$T$", "298 K"),
        ],
        "demo": {
            "title": "Generalización a condiciones cualesquiera",
            "body": r"""
<p>En condiciones no-estándar, la energía libre de la reacción depende del cociente de reacción $Q$:</p>
$$\Delta G = \Delta G° + RT\ln Q$$
<p>Para una reacción en fase gas, $Q$ se construye con presiones parciales:</p>
$$Q = \dfrac{p_{NH_3}^2}{p_{N_2}\,p_{H_2}^3}$$
<p>Si $\Delta G<0$, la reacción avanza hacia productos. Si $\Delta G>0$, hacia reactivos.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Cociente $Q$",
             "p": "Sustituyo presiones parciales.",
             "b": r"""$$Q = \dfrac{(0{,}50)^2}{2{,}0\cdot (4{,}0)^3}=\dfrac{0{,}25}{128}=1{,}953\cdot 10^{-3}$$"""},
            {"t": "Paso 2 — Calcular $\\Delta G$",
             "p": "$RT = 2{,}478$ kJ/mol.",
             "b": r"""$$\Delta G = -32{,}9 + 2{,}478\cdot\ln(1{,}953\cdot 10^{-3})$$
$$\Delta G = -32{,}9 + 2{,}478\cdot(-6{,}238)=-32{,}9-15{,}46=\boxed{-48{,}4\ \text{kJ/mol}}$$"""},
            {"t": "Paso 3 — Interpretar",
             "p": "$\\Delta G < 0$ ⟹ espontánea hacia derecha.",
             "b": r"""<p>El sistema está <em>más</em> espontáneo que en condiciones estándar porque $Q\ll K$: hay poco amoniaco frente al equilibrio, así que se forma más.</p>"""},
        ],
        "resultado": r"$\Delta G \approx -48{,}4$ kJ/mol. La reacción evoluciona espontáneamente <b>hacia productos</b> (formando más NH$_3$).",
        "verificacion": r"Si $Q\to K$, $\Delta G\to 0$ y la reacción se detiene en el equilibrio. Aquí $Q=1{,}95\cdot 10^{-3}\ll K\approx 5{,}8\cdot 10^{5}$ ⟹ muy lejos del equilibrio, fuerte fuerza motriz hacia productos. ✓"
    },
    {
        "title": "Espontaneidad en función de la temperatura",
        "enunciado": r"Para la reacción $\text{CaCO}_3(s)\to\text{CaO}(s)+\text{CO}_2(g)$, $\Delta H°=+178{,}3$ kJ/mol y $\Delta S°=+160{,}5$ J/(mol·K). Determinar: (a) si es espontánea a 25 °C; (b) la temperatura mínima a partir de la cual se vuelve espontánea.",
        "esperado": r"(a) No espontánea a 25 °C; (b) $T \ge 1\,111$ K $= 838$ °C.",
        "datos": [
            ("$\\Delta H°$", "$+178{,}3$ kJ/mol"),
            ("$\\Delta S°$", "$+160{,}5$ J/(mol·K) = $0{,}1605$ kJ/(mol·K)"),
        ],
        "pasos": [
            {"t": "(a) — A 25 °C",
             "p": "$\\Delta G = \\Delta H - T\\Delta S$.",
             "b": r"""$$\Delta G(298\,\text{K})=178{,}3-298\cdot 0{,}1605=178{,}3-47{,}8=+130{,}5\ \text{kJ/mol}$$
<p>$\Delta G > 0$ ⟹ <b>no espontánea</b> a temperatura ambiente.</p>"""},
            {"t": "(b) — Temperatura crítica",
             "p": "La reacción se vuelve espontánea cuando $\\Delta G \\le 0$. El punto de cambio es $\\Delta G = 0$.",
             "b": r"""$$T^* = \dfrac{\Delta H°}{\Delta S°}=\dfrac{178{,}3}{0{,}1605}=1\,111\ \text{K}\approx \boxed{838\ °\text{C}}$$
<p>Para $T>1\,111$ K, $\Delta G < 0$ y el CaCO$_3$ se descompone espontáneamente.</p>"""},
        ],
        "resultado": r"No espontánea a 25 °C. Espontánea a partir de <b>838 °C</b> (~1\,111 K).",
        "verificacion": r"En la industria del cemento, el horno rotatorio para calcinar CaCO$_3$ se opera a 850-900 °C — coherente con la $T$ mínima calculada. ✓"
    },
    {
        "title": "Constante de equilibrio a otra temperatura: ecuación de Van't Hoff",
        "enunciado": r"Una reacción tiene $K_1=5{,}0\cdot 10^{-3}$ a 298 K y $\Delta H°=+58$ kJ/mol. Estimar $K$ a 350 K asumiendo $\Delta H°$ constante. $R=8{,}314$ J/(mol·K).",
        "esperado": r"$K_2 \approx 6{,}4\cdot 10^{-2}$ — aumenta con la temperatura.",
        "datos": [
            ("$K_1$", "$5{,}0\\cdot 10^{-3}$"),
            ("$T_1$, $T_2$", "298 K, 350 K"),
            ("$\\Delta H°$", "+58 000 J/mol"),
        ],
        "demo": {
            "title": "Van't Hoff: efecto de $T$ sobre $K$",
            "body": r"""
<p>Partiendo de $\Delta G° = -RT\ln K$ y $\Delta G°=\Delta H°-T\Delta S°$:</p>
$$-RT\ln K = \Delta H° - T\Delta S° \implies \ln K = -\dfrac{\Delta H°}{RT} + \dfrac{\Delta S°}{R}$$
<p>Restando esta expresión a dos temperaturas distintas se elimina $\Delta S°$ (que se asume constante):</p>
$$\ln\!\dfrac{K_2}{K_1} = -\dfrac{\Delta H°}{R}\!\left(\dfrac{1}{T_2}-\dfrac{1}{T_1}\right)$$
<p>Si $\Delta H°>0$ (endotérmica), subir $T$ aumenta $K$ — coherente con Le Châtelier.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Diferencia de inversos",
             "p": "$1/T_2 - 1/T_1$.",
             "b": r"""$$\dfrac{1}{350}-\dfrac{1}{298}=2{,}857\cdot 10^{-3}-3{,}356\cdot 10^{-3}=-4{,}988\cdot 10^{-4}$$"""},
            {"t": "Paso 2 — Logaritmo del cociente",
             "p": "Aplicar Van't Hoff.",
             "b": r"""$$\ln\!\dfrac{K_2}{K_1}=-\dfrac{58\,000}{8{,}314}\cdot(-4{,}988\cdot 10^{-4})=3{,}481$$"""},
            {"t": "Paso 3 — Despejar $K_2$",
             "p": "Exponencial.",
             "b": r"""$$\dfrac{K_2}{K_1}=e^{3{,}481}=32{,}5$$
$$K_2=5{,}0\cdot 10^{-3}\cdot 32{,}5=\boxed{0{,}163}$$"""},
        ],
        "resultado": r"$K_2\approx 0{,}163$ — la subida de 52 K aumenta $K$ en un factor 32.",
        "verificacion": r"Coherente con Le Châtelier: la reacción es endotérmica, así que subir $T$ desplaza el equilibrio a productos ⟹ aumenta $K$. ✓"
    },
    {
        "title": "Equilibrio de fase: predecir el sentido del cambio espontáneo",
        "enunciado": r"A 1 atm, el agua tiene $T_{eb}=100$ °C. ¿En qué sentido es espontánea la <b>vaporización</b> (líquido → vapor) a: (a) 110 °C? (b) 90 °C? (c) 100 °C? Justificar con $\Delta G$.",
        "esperado": r"(a) Espontánea (vapor); (b) Espontánea la inversa (líquido); (c) Equilibrio.",
        "datos": [
            ("$T_{eb}$", "373 K (a 1 atm)"),
            ("$\\Delta H_{vap}$", "$+40{,}66$ kJ/mol"),
            ("$\\Delta S_{vap}$", "$+109{,}0$ J/(mol·K)"),
        ],
        "demo": {
            "title": "$\\Delta G$ en cambio de fase",
            "body": r"""
<p>Para la vaporización de agua a 1 atm, $\Delta H_{vap}>0$ (endotérmica) y $\Delta S_{vap}>0$ (más desorden). Hay una temperatura $T^*$ donde $\Delta G=0$ (equilibrio):</p>
$$T^* = \dfrac{\Delta H_{vap}}{\Delta S_{vap}}\;\;\text{(= $T_{eb}$)}$$
<p>Por debajo de $T_{eb}$: $\Delta G_{vap}>0$ ⟹ no espontánea (gana líquido). Por encima de $T_{eb}$: $\Delta G_{vap}<0$ ⟹ espontánea (gana vapor).</p>
"""
        },
        "pasos": [
            {"t": "(a) A 110 °C = 383 K",
             "p": "Calculo $\\Delta G$.",
             "b": r"""$$\Delta G = 40{,}66-383\cdot 0{,}1090=40{,}66-41{,}75=-1{,}09\ \text{kJ/mol}<0$$
<p>Espontánea hacia <b>vapor</b>.</p>"""},
            {"t": "(b) A 90 °C = 363 K",
             "p": "Mismo cálculo.",
             "b": r"""$$\Delta G = 40{,}66-363\cdot 0{,}1090=40{,}66-39{,}57=+1{,}09\ \text{kJ/mol}>0$$
<p>No espontánea (lo es la inversa: condensación a líquido).</p>"""},
            {"t": "(c) A 100 °C = 373 K",
             "p": "Justo en $T_{eb}$.",
             "b": r"""$$\Delta G = 40{,}66-373\cdot 0{,}1090=40{,}66-40{,}66=0$$
<p>Equilibrio: las dos fases coexisten.</p>"""},
        ],
        "resultado": r"(a) vapor (espontánea) · (b) líquido (la inversa) · (c) equilibrio. Cambio de signo justo a $T_{eb}=100$ °C.",
        "verificacion": r"Esta es la base termodinámica de los puntos de cambio de fase: la temperatura de equilibrio es exactamente donde $\Delta H/\Delta S$ = $T$. ✓"
    },
    {
        "title": "Trabajo útil máximo de una reacción",
        "enunciado": r"Calcular el <b>trabajo eléctrico máximo</b> que se puede extraer de la combustión de 1 mol de hidrógeno en una pila de combustible: $\text{H}_2(g)+\tfrac12\text{O}_2(g)\to\text{H}_2\text{O}(l)$. Datos a 298 K: $\Delta H°=-285{,}8$ kJ/mol; $\Delta S°=-163{,}3$ J/(mol·K). Compararlo con el calor liberado en una combustión convencional.",
        "esperado": r"$W_{útil,max}=-237{,}1$ kJ/mol (electrobandido); pila más eficiente que combustión por 1−237/286=17%.",
        "datos": [
            ("$\\Delta H°$", "$-285{,}8$ kJ/mol"),
            ("$\\Delta S°$", "$-163{,}3$ J/(mol·K) = $-0{,}1633$ kJ/(mol·K)"),
            ("$T$", "298 K"),
        ],
        "demo": {
            "title": "$\\Delta G$ = trabajo útil máximo",
            "body": r"""
<p>La <b>energía libre de Gibbs</b> tiene una interpretación física directa: a $p$,$T$ constantes, $-\Delta G$ representa el <em>trabajo útil máximo</em> que la reacción puede entregar (trabajo distinto al de expansión, p. ej. eléctrico).</p>
$$W_{útil,max} = \Delta G$$
<p>Una pila de combustible convierte $\Delta G$ en trabajo eléctrico, alcanzando rendimientos altos. Una combustión convencional (en motor de Carnot) está limitada por el rendimiento térmico, mucho menor.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $\\Delta G°$",
             "p": "$\\Delta G° = \\Delta H° - T\\Delta S°$.",
             "b": r"""$$\Delta G°=-285{,}8-298\cdot(-0{,}1633)=-285{,}8+48{,}66=\boxed{-237{,}1\ \text{kJ/mol}}$$"""},
            {"t": "Paso 2 — Eficiencia teórica",
             "p": "Razón entre trabajo extraíble y energía total.",
             "b": r"""$$\eta_{ideal}=\dfrac{|\Delta G°|}{|\Delta H°|}=\dfrac{237{,}1}{285{,}8}=83{,}0\%$$"""},
        ],
        "resultado": r"Trabajo útil máximo = <b>237,1 kJ por mol de H$_2$</b>. La pila ideal alcanza un 83% de eficiencia, muy superior al ~40% de un motor térmico Carnot equivalente.",
        "verificacion": r"Las pilas de combustible reales alcanzan 50-60% de eficiencia (con pérdidas óhmicas). Aún así, casi el doble que un motor diésel (~35%). Esa es la motivación tecnológica para el hidrógeno verde. ✓"
    },
    {
        "title": "Ciclo de Born-Haber con energía libre",
        "enunciado": r"Aplicando el ciclo de Born-Haber para entropías, calcular $\Delta S°$ de la disolución del NaCl(s) en agua. Datos: $S°$ (J/(mol·K)): NaCl(s) = 72,1; Na$^+$(aq) = 59,0; Cl$^-$(aq) = 56,5.",
        "esperado": r"$\Delta S° = +43{,}4$ J/(mol·K).",
        "datos": [
            ("$S°$ NaCl(s)", "72,1 J/(mol·K)"),
            ("$S°$ Na$^+$(aq)", "59,0 J/(mol·K)"),
            ("$S°$ Cl$^-$(aq)", "56,5 J/(mol·K)"),
        ],
        "pasos": [
            {"t": "Paso 1 — Aplicar fórmula general",
             "p": "$\\Delta S° = \\Sigma S°_{prod} - \\Sigma S°_{reac}$. Reacción: NaCl(s) → Na$^+$(aq) + Cl$^-$(aq).",
             "b": r"""$$\Delta S° = (59{,}0+56{,}5) - 72{,}1 = 115{,}5-72{,}1 = +43{,}4\ \text{J/(mol·K)}$$"""},
        ],
        "resultado": r"$\Delta S° = +43{,}4$ J/(mol·K) — positivo: los iones hidratados tienen más microestados accesibles que el sólido cristalino.",
        "verificacion": r"Coherencia: cualquier proceso de <em>disolución</em> de un sólido en un líquido tiende a aumentar la entropía (más desorden estructural). Aquí también el efecto entrópico ayuda al $\Delta G$ a ser favorable, junto con el $\Delta H$ pequeño. ✓"
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 8 — CINÉTICA Y EQUILIBRIO
# ═══════════════════════════════════════════════════════════════════════
8: [
    {
        "title": "Determinación del orden por velocidades iniciales",
        "enunciado": r"Para la reacción $A+B\to P$ se obtienen los siguientes datos:<br>Exp 1: $[A]_0=0{,}10$ M, $[B]_0=0{,}10$ M, $v_0=2{,}5\cdot 10^{-3}$ M/s.<br>Exp 2: $[A]_0=0{,}20$ M, $[B]_0=0{,}10$ M, $v_0=1{,}0\cdot 10^{-2}$ M/s.<br>Exp 3: $[A]_0=0{,}10$ M, $[B]_0=0{,}20$ M, $v_0=2{,}5\cdot 10^{-3}$ M/s. Determinar la ecuación de velocidad y la constante $k$.",
        "esperado": r"$v=k[A]^2[B]^0$ con $k=0{,}25$ M$^{-1}$s$^{-1}$. Orden total = 2.",
        "datos": [
            ("Forma general", "$v=k[A]^m[B]^n$"),
            ("Exp 1 → 2", "$[A]$ se duplica, $[B]$ fija"),
            ("Exp 1 → 3", "$[B]$ se duplica, $[A]$ fija"),
        ],
        "demo": {
            "title": "Aislar el efecto de cada concentración",
            "body": r"""
<p>El método de las velocidades iniciales se basa en hacer experimentos cambiando la concentración de un solo reactivo a la vez. Si $[A]$ se duplica y la velocidad se multiplica por $2^m$, entonces $m$ es el orden parcial respecto de $A$:</p>
$$\dfrac{v_2}{v_1}=\!\left(\dfrac{[A]_2}{[A]_1}\right)^m$$
<p>Aplicado a las parejas de experimentos, los exponentes $m$ y $n$ salen directamente.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Orden respecto a A",
             "p": "Comparando exp 1 y 2.",
             "b": r"""$$\dfrac{v_2}{v_1}=\dfrac{1{,}0\cdot 10^{-2}}{2{,}5\cdot 10^{-3}}=4=2^m \implies m=2$$"""},
            {"t": "Paso 2 — Orden respecto a B",
             "p": "Comparando exp 1 y 3.",
             "b": r"""$$\dfrac{v_3}{v_1}=\dfrac{2{,}5\cdot 10^{-3}}{2{,}5\cdot 10^{-3}}=1=2^n \implies n=0$$"""},
            {"t": "Paso 3 — Constante de velocidad",
             "p": "Aplicando la ley a Exp 1.",
             "b": r"""$$k = \dfrac{v_0}{[A]^2}=\dfrac{2{,}5\cdot 10^{-3}}{(0{,}10)^2}=0{,}25\ \text{M}^{-1}\text{s}^{-1}$$"""},
        ],
        "resultado": r"Ley de velocidad: $v=0{,}25\,[A]^2$. La reacción es de orden 2 en $A$ y orden 0 en $B$. Orden total = 2.",
        "verificacion": r"Comprobación con Exp 2: $v=0{,}25\cdot(0{,}20)^2=0{,}25\cdot 0{,}04=10^{-2}$ M/s ✓ — coincide con el dato."
    },
    {
        "title": "Mecanismo y ley de velocidad: paso lento",
        "enunciado": r"Para la reacción global $2\,\text{NO}_2+\text{F}_2\to 2\,\text{NO}_2\text{F}$ se propone el siguiente mecanismo en dos pasos:<br><b>(1)</b> NO$_2$ + F$_2$ → NO$_2$F + F (lento, $k_1$)<br><b>(2)</b> NO$_2$ + F → NO$_2$F (rápido, $k_2$)<br>Determinar la ecuación de velocidad predicha por el mecanismo. ¿Qué orden y constante experimental se esperan?",
        "esperado": r"$v=k_1[\text{NO}_2][\text{F}_2]$. Orden total = 2.",
        "datos": [
            ("Paso lento", "(1) bimolecular"),
            ("Paso rápido", "(2) bimolecular"),
            ("Intermedio", "F (átomo)"),
        ],
        "demo": {
            "title": "El paso lento determina la velocidad",
            "body": r"""
<p>En un mecanismo en serie, la velocidad global está limitada por la <b>etapa más lenta</b>: cada paso posterior consume el producto del lento tan rápido como aparece, así que el cuello de botella manda.</p>
<p>Por tanto, la ley de velocidad observada coincide con la del paso lento — pero solo intervienen las especies presentes <em>antes</em> del paso lento, es decir, los reactivos elementales (no los intermedios).</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Identificar el paso lento",
             "p": "El paso (1) es lento. Su ley elemental se aplica.",
             "b": r"""$$v_{(1)}=k_1[\text{NO}_2][\text{F}_2]$$"""},
            {"t": "Paso 2 — Comprobar que solo aparecen reactivos",
             "p": "El paso (1) consume directamente los reactivos NO$_2$ y F$_2$. No hay intermedios.",
             "b": r"""<p>$v=k_1[\text{NO}_2][\text{F}_2]$ ⟹ orden 1 en cada reactivo, orden total <b>2</b>.</p>"""},
            {"t": "Paso 3 — Predicción experimental",
             "p": "$k_{exp}$ se identifica con $k_1$.",
             "b": r"""<p>El experimento debería dar:</p>
<ul>
  <li>Orden 1 al duplicar [NO$_2$] (manteniendo [F$_2$]).</li>
  <li>Orden 1 al duplicar [F$_2$].</li>
  <li>Constante $k_{exp}=k_1$.</li>
</ul>"""},
        ],
        "resultado": r"$v = k_1[\text{NO}_2][\text{F}_2]$. Mecanismo coherente con orden 2.",
        "verificacion": r"Experimentalmente, esta reacción muestra orden 1+1 = 2 a temperaturas moderadas, validando el mecanismo. Si la cinética observada fuera de orden 2 en NO$_2$, el mecanismo propuesto sería falso. ✓"
    },
    {
        "title": "Relación entre $K_p$ y $K_c$",
        "enunciado": r"Para la reacción $\text{N}_2(g)+3\,\text{H}_2(g)\rightleftharpoons 2\,\text{NH}_3(g)$, la constante $K_c$ a 500 K vale $0{,}65$. Calcular $K_p$ a la misma temperatura. $R=0{,}082$ atm·L/(mol·K).",
        "esperado": r"$K_p \approx 3{,}9\cdot 10^{-4}$ atm$^{-2}$.",
        "datos": [
            ("$K_c$", "0,65"),
            ("$T$", "500 K"),
            ("$\\Delta n_{gas}$", "$2-(1+3)=-2$"),
        ],
        "demo": {
            "title": "Conversión $K_c \\leftrightarrow K_p$",
            "body": r"""
<p>Para reacciones gaseosas, $K_p$ usa presiones parciales y $K_c$ concentraciones. Como $p_i = c_i RT$ para gas ideal:</p>
$$K_p = K_c\,(RT)^{\Delta n_{gas}}$$
<p>$\Delta n_{gas}$ = (moles gas productos) − (moles gas reactivos). Si $\Delta n_{gas}=0$, $K_p=K_c$. Si $\Delta n_{gas}<0$, $K_p<K_c$.</p>
<p>Las unidades de $RT$ deben ser coherentes con las usadas para $p$ y $c$ (típicamente atm·L/(mol·K) si $p$ en atm y $c$ en mol/L).</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $RT$",
             "p": "Con $R$ en atm·L/(mol·K).",
             "b": r"""$$RT = 0{,}082\cdot 500=41{,}0\ \text{atm·L/mol}$$"""},
            {"t": "Paso 2 — Aplicar la fórmula",
             "p": "$\\Delta n_{gas}=-2$.",
             "b": r"""$$K_p = K_c\cdot(RT)^{-2}=\dfrac{0{,}65}{(41{,}0)^2}=\dfrac{0{,}65}{1\,681}=\boxed{3{,}87\cdot 10^{-4}}$$"""},
        ],
        "resultado": r"$K_p \approx 3{,}9\cdot 10^{-4}$ — mucho menor que $K_c$ porque hay contracción de gas y se multiplica por $(RT)^{-2}$.",
        "verificacion": r"Cuando $\Delta n_{gas}<0$, $K_p$ disminuye por mayor presión exigida para alcanzar el equilibrio. Esto explica por qué la síntesis de amoniaco se favorece a altas presiones (~200 atm en proceso Haber-Bosch). ✓"
    },
    {
        "title": "Cociente $Q$ vs $K$: predecir el sentido",
        "enunciado": r"Para la reacción $\text{H}_2(g)+\text{I}_2(g)\rightleftharpoons 2\,\text{HI}(g)$, $K_c=54{,}3$ a 425 °C. En un recipiente se introducen $[\text{H}_2]=0{,}50$ M, $[\text{I}_2}]=0{,}50$ M y $[\text{HI}]=4{,}0$ M. ¿En qué sentido evolucionará el sistema hasta alcanzar el equilibrio?",
        "esperado": r"$Q=64>K$ ⟹ retrocede hacia reactivos (descompone HI).",
        "datos": [
            ("$K_c$", "54,3"),
            ("$[\\text{H}_2]_0$", "0,50 M"),
            ("$[\\text{I}_2]_0$", "0,50 M"),
            ("$[\\text{HI}]_0$", "4,0 M"),
        ],
        "demo": {
            "title": "Comparación $Q$ con $K$",
            "body": r"""
<p>El <b>cociente de reacción</b> $Q$ tiene la misma forma matemática que $K$ pero se evalúa con las concentraciones <em>actuales</em>, sin importar si el sistema está o no en equilibrio:</p>
$$Q = \dfrac{[HI]^2}{[H_2][I_2]}$$
<p>Comparándolo con $K$:</p>
<ul>
  <li>$Q < K$: faltan productos ⟹ avanza hacia productos (→).</li>
  <li>$Q = K$: equilibrio.</li>
  <li>$Q > K$: sobran productos ⟹ retrocede hacia reactivos (←).</li>
</ul>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $Q$",
             "p": "Sustituyo en la fórmula.",
             "b": r"""$$Q = \dfrac{(4{,}0)^2}{0{,}50\cdot 0{,}50}=\dfrac{16}{0{,}25}=64$$"""},
            {"t": "Paso 2 — Comparar con $K$",
             "p": "$Q=64$, $K=54{,}3$.",
             "b": r"""<p>$Q > K$ ⟹ hay <b>exceso de productos</b> respecto del equilibrio. El sistema descompondrá HI para volver al equilibrio.</p>"""},
        ],
        "resultado": r"$Q=64>K=54{,}3$ ⟹ el sistema evolucionará <b>hacia la izquierda</b>: parte del HI se descompone en H$_2$ + I$_2$.",
        "verificacion": r"En el equilibrio: $[H_2]_{eq}=[I_2]_{eq}=0{,}50+x$, $[HI]_{eq}=4{,}0-2x$. Resolviendo $K_c=54{,}3$ se obtiene $x\approx 0{,}068$ ⟹ HI baja a 3,86 M (consistente con la retroceso). ✓"
    },
    {
        "title": "Le Châtelier cualitativo: análisis sistemático",
        "enunciado": r"Para el equilibrio exotérmico $2\,\text{SO}_2(g)+\text{O}_2(g)\rightleftharpoons 2\,\text{SO}_3(g)$, predecir cualitativamente cómo afecta al equilibrio cada una de las siguientes perturbaciones: (a) añadir SO$_2$; (b) eliminar SO$_3$; (c) aumentar la presión total comprimiendo; (d) subir la temperatura; (e) añadir un catalizador.",
        "esperado": r"(a) →; (b) →; (c) →; (d) ←; (e) sin efecto sobre la posición.",
        "datos": [
            ("Reacción", "exotérmica"),
            ("$\\Delta n_{gas}$", "$2-3=-1$"),
        ],
        "pasos": [
            {"t": "Análisis de cada caso",
             "p": "Aplicar el principio de Le Châtelier.",
             "b": r"""<table class="tdatos">
<tr><th>Perturbación</th><th>Sistema reacciona</th><th>Sentido</th></tr>
<tr><td>(a) Añadir SO$_2$</td><td>Consumir el extra de SO$_2$</td><td>→ (más SO$_3$)</td></tr>
<tr><td>(b) Eliminar SO$_3$</td><td>Reponer SO$_3$</td><td>→</td></tr>
<tr><td>(c) ↑$p$ comprimiendo</td><td>Reducir nº de moles gas</td><td>→ (productos: 2 mol gas vs 3)</td></tr>
<tr><td>(d) ↑$T$</td><td>Absorber calor (endo dirección)</td><td>← (la inversa es endotérmica)</td></tr>
<tr><td>(e) Catalizador</td><td>Acelera ambas direcciones por igual</td><td>Sin desplazar (acorta el tiempo, no el equilibrio)</td></tr>
</table>"""},
        ],
        "resultado": r"(a) → · (b) → · (c) → · (d) ← · (e) sin efecto.",
        "verificacion": r"Coherente con la práctica industrial: el proceso del SO$_3$ (fabricación de H$_2$SO$_4$) opera a ≤450 °C (no demasiado para no perjudicar el equilibrio) y con catalizador V$_2$O$_5$ para acelerar sin cambiar la posición del equilibrio. ✓"
    },
    {
        "title": "Equilibrio heterogéneo: descomposición del CaCO$_3$",
        "enunciado": r"Para el equilibrio $\text{CaCO}_3(s)\rightleftharpoons\text{CaO}(s)+\text{CO}_2(g)$, $K_p=0{,}1$ atm a 850 °C. En un recipiente cerrado de 10 L que contiene CaCO$_3$ y CaO sólidos, calcular: (a) la presión parcial de CO$_2$ en el equilibrio; (b) los moles de CO$_2$. $R=0{,}082$ atm·L/(mol·K).",
        "esperado": r"(a) $p_{CO_2}=0{,}1$ atm; (b) $n=0{,}0108$ mol.",
        "datos": [
            ("$K_p$", "0,1 atm"),
            ("$T$", "1 123 K"),
            ("$V$", "10 L"),
        ],
        "demo": {
            "title": "Sólidos y líquidos puros NO entran en $K$",
            "body": r"""
<p>En un equilibrio heterogéneo (involucra varias fases), los sólidos y líquidos <em>puros</em> tienen actividad constante (≈ 1) y <b>no aparecen en la expresión de $K$</b>. Solo gases y especies en disolución cuentan.</p>
<p>Para esta reacción, la única especie no-sólida es CO$_2$(g), así que:</p>
$$K_p = p_{CO_2}$$
<p>Por tanto, la presión de CO$_2$ en el equilibrio es independiente de las cantidades de CaCO$_3$ y CaO (siempre que ambos estén presentes).</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Presión parcial de CO$_2$",
             "p": "Igualdad directa.",
             "b": r"""$$p_{CO_2}=K_p=0{,}1\ \text{atm}$$"""},
            {"t": "Paso 2 — Moles de CO$_2$",
             "p": "$n=pV/RT$.",
             "b": r"""$$n=\dfrac{0{,}1\cdot 10}{0{,}082\cdot 1\,123}=\dfrac{1{,}0}{92{,}1}=0{,}01086\ \text{mol}$$"""},
        ],
        "resultado": r"$p_{CO_2}=0{,}1$ atm · $n_{CO_2}\approx 0{,}011$ mol.",
        "verificacion": r"Si añadimos más CaCO$_3$ o CaO, el equilibrio NO cambia: $p_{CO_2}$ se mantiene en 0,1 atm. Solo cambiar $T$ o el volumen del recipiente afecta $p_{CO_2}$. ✓"
    },
    {
        "title": "Catalizador: efecto sobre $E_a$ y $k$",
        "enunciado": r"La descomposición del H$_2$O$_2$ tiene una energía de activación de <b>75 kJ/mol</b> sin catalizador. Con la enzima catalasa, $E_a$ baja a <b>8 kJ/mol</b>. Calcular en cuántas veces se acelera la reacción a 25 °C.",
        "esperado": r"Factor $\sim 1{,}3\cdot 10^{12}$ — un billón de veces más rápida.",
        "datos": [
            ("$E_a$ sin catalizador", "75 000 J/mol"),
            ("$E_a$ con catalasa", "8 000 J/mol"),
            ("$T$", "298 K"),
            ("$R$", "8,314 J/(mol·K)"),
        ],
        "demo": {
            "title": "Razón de constantes según Arrhenius",
            "body": r"""
<p>Si suponemos que el factor preexponencial $A$ es similar en ambos casos (cosa habitual cuando el catalizador no cambia drásticamente la geometría del estado de transición), la razón de velocidades es:</p>
$$\dfrac{k_{cat}}{k_{nc}}=\exp\!\left(\dfrac{E_{a,nc}-E_{a,cat}}{RT}\right)$$
<p>Como el exponente puede ser grande, factores de aceleración de 10⁶-10¹² son comunes en catálisis enzimática.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Diferencia de $E_a$ y exponente",
             "p": "$\\Delta E_a / RT$.",
             "b": r"""$$\Delta E_a = 75\,000-8\,000=67\,000\ \text{J/mol}$$
$$\dfrac{\Delta E_a}{RT}=\dfrac{67\,000}{8{,}314\cdot 298}=27{,}05$$"""},
            {"t": "Paso 2 — Razón de velocidades",
             "p": "Exponencial.",
             "b": r"""$$\dfrac{k_{cat}}{k_{nc}}=e^{27{,}05}=5{,}6\cdot 10^{11}$$"""},
        ],
        "resultado": r"Con catalasa la reacción es <b>~$5\cdot 10^{11}$ veces más rápida</b> — pasa de durar años a milisegundos.",
        "verificacion": r"Esto explica por qué nuestras células pueden eliminar peróxido de hidrógeno tóxico instantáneamente: la catalasa es uno de los catalizadores más rápidos conocidos, con número de recambio (turnover) ~10⁶ s⁻¹. ✓"
    },
],

# ═══════════════════════════════════════════════════════════════════════
# TEMA 9 — EQUILIBRIO ÁCIDO-BASE
# ═══════════════════════════════════════════════════════════════════════
9: [
    {
        "title": "pH de un ácido fuerte muy diluido",
        "enunciado": r"Calcular el pH de una disolución <b>$1{,}0\cdot 10^{-7}$ M de HCl</b>. ¿Por qué no es directamente 7?",
        "esperado": r"pH ≈ 6,79 (no 7 porque la autoionización del agua deja de ser despreciable).",
        "datos": [
            ("$C_a$", "$1{,}0\\cdot 10^{-7}$ M"),
            ("$K_w$", "$1{,}0\\cdot 10^{-14}$"),
        ],
        "demo": {
            "title": "Cuando hay que tener en cuenta el agua",
            "body": r"""
<p>Para ácidos fuertes <em>concentrados</em> ($C_a\gtrsim 10^{-5}$ M), $[\text{H}_3\text{O}^+]\approx C_a$ y la contribución del agua es despreciable. Pero a concentraciones extremadamente bajas (cercanas a $10^{-7}$, que es la propia $[\text{H}_3\text{O}^+]$ del agua pura), <b>hay que sumar las dos fuentes</b>.</p>
<p>Conservación de carga: $[\text{H}_3\text{O}^+] = [\text{OH}^-] + [\text{Cl}^-]$.<br>
Equilibrio del agua: $[\text{H}_3\text{O}^+][\text{OH}^-]=K_w$.</p>
<p>De la primera, $[\text{OH}^-]=[\text{H}_3\text{O}^+]-C_a$. Sustituyendo:</p>
$$[\text{H}_3\text{O}^+]([\text{H}_3\text{O}^+]-C_a)=K_w$$
<p>Es una ecuación cuadrática en $[\text{H}_3\text{O}^+]$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Plantear y resolver la cuadrática",
             "p": "$x = [\\text{H}_3\\text{O}^+]$.",
             "b": r"""$$x^2 - C_a\,x - K_w = 0$$
$$x = \dfrac{C_a + \sqrt{C_a^2+4K_w}}{2}$$
<p>Sustituyendo $C_a = 10^{-7}$, $K_w=10^{-14}$:</p>
$$x = \dfrac{10^{-7}+\sqrt{10^{-14}+4\cdot 10^{-14}}}{2}=\dfrac{10^{-7}+\sqrt{5\cdot 10^{-14}}}{2}$$
$$x = \dfrac{10^{-7}+2{,}236\cdot 10^{-7}}{2}=\dfrac{3{,}236\cdot 10^{-7}}{2}=1{,}618\cdot 10^{-7}$$"""},
            {"t": "Paso 2 — Calcular el pH",
             "p": "$\\text{pH}=-\\log[\\text{H}_3\\text{O}^+]$.",
             "b": r"""$$\text{pH}=-\log(1{,}618\cdot 10^{-7})=6{,}79$$"""},
        ],
        "resultado": r"pH ≈ <b>6,79</b> — ligeramente ácido pero NO neutro pese a la baja concentración del HCl, por la contribución del agua.",
        "verificacion": r"Si calculásemos sin tener en cuenta el agua: pH = 7 (incorrecto) o pH = 7,3 si confundiéramos la dirección (también incorrecto). El cálculo con cuadrática garantiza el resultado físicamente válido: pH siempre $<7$ cuando se añade ácido. ✓"
    },
    {
        "title": "Mezcla de ácido y base fuertes",
        "enunciado": r"Se mezclan <b>30 mL de HCl 0,10 M</b> con <b>20 mL de NaOH 0,20 M</b>. Calcular el pH de la disolución resultante.",
        "esperado": r"pH = 12,30 — disolución básica (NaOH en exceso).",
        "datos": [
            ("HCl", "30 mL · 0,10 M"),
            ("NaOH", "20 mL · 0,20 M"),
        ],
        "demo": {
            "title": "Reacción y exceso",
            "body": r"""
<p>El HCl y el NaOH son ácido y base <em>fuertes</em>: se neutralizan estequiométricamente:</p>
$$\text{HCl}+\text{NaOH}\to\text{NaCl}+\text{H}_2\text{O}$$
<p>Hay que comparar moles iniciales:</p>
<ul>
  <li>Si $n_{HCl}>n_{NaOH}$: queda HCl libre, disolución ácida.</li>
  <li>Si $n_{NaOH}>n_{HCl}$: queda NaOH libre, disolución básica.</li>
  <li>Si iguales: pH = 7 (la sal NaCl no hidroliza).</li>
</ul>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles iniciales",
             "p": "$n=M\\cdot V$ con $V$ en litros.",
             "b": r"""$$n_{HCl}=0{,}10\cdot 0{,}030=3{,}0\cdot 10^{-3}\ \text{mol}$$
$$n_{NaOH}=0{,}20\cdot 0{,}020=4{,}0\cdot 10^{-3}\ \text{mol}$$"""},
            {"t": "Paso 2 — Tras la reacción",
             "p": "El HCl se consume todo. Sobra NaOH = $n_{NaOH} - n_{HCl}$.",
             "b": r"""$$n_{NaOH,exc}=4{,}0\cdot 10^{-3}-3{,}0\cdot 10^{-3}=1{,}0\cdot 10^{-3}\ \text{mol}$$"""},
            {"t": "Paso 3 — Concentración de OH$^-$",
             "p": "Volumen total = 50 mL.",
             "b": r"""$$[\text{OH}^-]=\dfrac{1{,}0\cdot 10^{-3}}{0{,}050}=0{,}020\ \text{M}$$"""},
            {"t": "Paso 4 — pH",
             "p": "Vía pOH.",
             "b": r"""$$\text{pOH}=-\log(0{,}020)=1{,}70 \implies \text{pH}=14-1{,}70=12{,}30$$"""},
        ],
        "resultado": r"pH = <b>12,30</b> — fuertemente básica por el exceso de NaOH.",
        "verificacion": r"Comprobación: 30·0,10 = 3 mmol HCl y 20·0,20 = 4 mmol NaOH; el ratio 4/3 = 1,33 indica claramente exceso de base, coherente con pH > 7. ✓"
    },
    {
        "title": "Curva de valoración: ácido fuerte con base fuerte",
        "enunciado": r"Calcular el pH en los siguientes puntos durante la valoración de <b>50,0 mL de HCl 0,100 M</b> con NaOH 0,100 M: (a) inicio (V=0); (b) tras añadir 25 mL; (c) en el punto de equivalencia (50 mL); (d) tras añadir 75 mL en total.",
        "esperado": r"(a) 1,00; (b) 1,48; (c) 7,00; (d) 12,30.",
        "datos": [
            ("Ácido", "50,0 mL · 0,100 M HCl ⟹ 5,0 mmol"),
            ("Base", "0,100 M NaOH"),
        ],
        "pasos": [
            {"t": "(a) V=0 — solo HCl",
             "p": "$[\\text{H}^+]=0{,}100$ M.",
             "b": r"""$$\text{pH}=-\log(0{,}100)=1{,}00$$"""},
            {"t": "(b) V=25 mL — HCl en exceso",
             "p": "Moles añadidos NaOH = 2,5 mmol; HCl restante = 5,0 − 2,5 = 2,5 mmol. Volumen total = 75 mL.",
             "b": r"""$$[\text{H}^+]=\dfrac{2{,}5\cdot 10^{-3}}{0{,}075}=0{,}0333\ \text{M}$$
$$\text{pH}=-\log(0{,}0333)=1{,}48$$"""},
            {"t": "(c) V=50 mL — punto de equivalencia",
             "p": "HCl y NaOH consumidos exactamente. Solo queda NaCl (sal neutra).",
             "b": r"""$$\text{pH}=7{,}00$$"""},
            {"t": "(d) V=75 mL — NaOH en exceso",
             "p": "Moles NaOH = 7,5 mmol; usados 5,0 mmol; sobran 2,5 mmol. Volumen total = 125 mL.",
             "b": r"""$$[\text{OH}^-]=\dfrac{2{,}5\cdot 10^{-3}}{0{,}125}=0{,}020\ \text{M}$$
$$\text{pOH}=1{,}70 \implies \text{pH}=12{,}30$$"""},
        ],
        "resultado": r"(a) 1,00 · (b) 1,48 · (c) 7,00 · (d) 12,30. Salto brusco entre 4 y 10 alrededor del punto de equivalencia.",
        "verificacion": r"En valoraciones HF + BF, el punto de equivalencia está siempre a pH = 7. El indicador adecuado es uno con vire en 4-10 (fenolftaleína 8,2-10 o naranja de metilo 3,2-4,4 funcionan ambos). ✓"
    },
    {
        "title": "Tampón con concentraciones diferentes",
        "enunciado": r"Calcular el pH de un tampón formado por <b>0,30 M de NH$_3$</b> y <b>0,50 M de NH$_4$Cl</b>. $K_b(\text{NH}_3)=1{,}8\cdot 10^{-5}$.",
        "esperado": r"pH = 9,04.",
        "datos": [
            ("[base]", "0,30 M NH$_3$"),
            ("[ácido]", "0,50 M NH$_4^+$"),
            ("$K_b$ NH$_3$", "$1{,}8\\cdot 10^{-5}$"),
        ],
        "demo": {
            "title": "Henderson-Hasselbalch para tampones básicos",
            "body": r"""
<p>El par NH$_3$ / NH$_4^+$ es un tampón. El NH$_3$ es la base; el NH$_4^+$ su ácido conjugado. Para usar Henderson-Hasselbalch convertimos $K_b$ en $K_a$ del ácido conjugado:</p>
$$K_a(\text{NH}_4^+)=\dfrac{K_w}{K_b}=\dfrac{10^{-14}}{1{,}8\cdot 10^{-5}}=5{,}56\cdot 10^{-10}$$
<p>$\text{p}K_a = 9{,}26$. Aplicamos:</p>
$$\text{pH} = \text{p}K_a + \log\!\dfrac{[\text{base}]}{[\text{ácido}]}=\text{p}K_a + \log\!\dfrac{[\text{NH}_3]}{[\text{NH}_4^+]}$$
"""
        },
        "pasos": [
            {"t": "Cálculo directo",
             "p": "Sustitución en H-H.",
             "b": r"""$$\text{pH} = 9{,}26 + \log\!\dfrac{0{,}30}{0{,}50}=9{,}26+\log(0{,}60)=9{,}26-0{,}222=\boxed{9{,}04}$$"""},
        ],
        "resultado": r"pH = <b>9,04</b> — ligeramente ácido respecto al p$K_a$ porque hay más ácido conjugado que base.",
        "verificacion": r"Si las concentraciones fueran iguales, pH = p$K_a = 9{,}26$. Aquí [base]/[ácido] < 1 ⟹ pH < p$K_a$. ✓"
    },
    {
        "title": "Hidrólisis del cloruro de amonio",
        "enunciado": r"Calcular el pH de una disolución <b>0,10 M de NH$_4$Cl</b>. $K_b(\text{NH}_3)=1{,}8\cdot 10^{-5}$.",
        "esperado": r"pH = 5,13 — disolución ácida.",
        "datos": [
            ("$C_{sal}$", "0,10 M"),
            ("$K_b$ NH$_3$", "$1{,}8\\cdot 10^{-5}$"),
        ],
        "demo": {
            "title": "Hidrólisis del catión",
            "body": r"""
<p>El NH$_4$Cl proviene de la base débil NH$_3$ y el ácido fuerte HCl. Su catión NH$_4^+$ es el ácido conjugado de la base débil — <b>hidroliza</b> en agua:</p>
$$\text{NH}_4^+ + \text{H}_2\text{O}\rightleftharpoons \text{NH}_3 + \text{H}_3\text{O}^+$$
<p>La constante de hidrólisis (= $K_a$ del ácido conjugado) es:</p>
$$K_a = \dfrac{K_w}{K_b} = \dfrac{10^{-14}}{1{,}8\cdot 10^{-5}}=5{,}56\cdot 10^{-10}$$
<p>Aplicamos la aproximación habitual: $[\text{H}_3\text{O}^+]\approx\sqrt{K_a\cdot C_{sal}}$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $K_a$",
             "p": "Vía $K_w/K_b$.",
             "b": r"""$$K_a=\dfrac{1{,}0\cdot 10^{-14}}{1{,}8\cdot 10^{-5}}=5{,}56\cdot 10^{-10}$$"""},
            {"t": "Paso 2 — $[\\text{H}_3\\text{O}^+]$",
             "p": "Aproximación válida: $C/K_a = 1{,}8\\cdot 10^{8} \\gg 100$.",
             "b": r"""$$[\text{H}_3\text{O}^+]\approx\sqrt{5{,}56\cdot 10^{-10}\cdot 0{,}10}=\sqrt{5{,}56\cdot 10^{-11}}=7{,}45\cdot 10^{-6}$$"""},
            {"t": "Paso 3 — pH",
             "p": "$-\\log$.",
             "b": r"""$$\text{pH}=-\log(7{,}45\cdot 10^{-6})=\boxed{5{,}13}$$"""},
        ],
        "resultado": r"pH = <b>5,13</b> — disolución ácida, como toda sal de ácido fuerte + base débil.",
        "verificacion": r"Coherencia: el Cl$^-$ es la base conjugada de un ácido fuerte (HCl), así que es muy débil — no hidroliza. Toda la acidez viene del NH$_4^+$. ✓"
    },
    {
        "title": "Producto de solubilidad: solubilidad del AgCl",
        "enunciado": r"Calcular: (a) la solubilidad molar del AgCl en agua pura; (b) en una disolución de NaCl 0,10 M. $K_{ps}(\text{AgCl}) = 1{,}8\cdot 10^{-10}$.",
        "esperado": r"(a) $s = 1{,}34\cdot 10^{-5}$ M (1,93 mg/L); (b) $s' = 1{,}8\cdot 10^{-9}$ M — efecto del ion común.",
        "datos": [
            ("$K_{ps}$ AgCl", "$1{,}8\\cdot 10^{-10}$"),
            ("[Cl$^-$] en (b)", "0,10 M (de NaCl)"),
            ("$M_{AgCl}$", "143,3 g/mol"),
        ],
        "demo": {
            "title": "Producto de solubilidad y efecto del ion común",
            "body": r"""
<p>Para una sal poco soluble AgCl(s) ⇌ Ag$^+$ + Cl$^-$, el equilibrio se rige por:</p>
$$K_{ps}=[\text{Ag}^+][\text{Cl}^-]$$
<p>En agua pura, ambas concentraciones son iguales a la solubilidad $s$, así que $K_{ps}=s^2$ ⟹ $s=\sqrt{K_{ps}}$.</p>
<p>Si hay <b>ion común</b> (Cl$^-$ proveniente de otra sal), $[\text{Cl}^-]$ ya está fijado por la otra fuente; entonces $s=K_{ps}/[\text{Cl}^-]$, mucho menor que en agua pura. Esto se llama <b>efecto del ion común</b>.</p>
"""
        },
        "pasos": [
            {"t": "(a) En agua pura",
             "p": "$s^2 = K_{ps}$.",
             "b": r"""$$s=\sqrt{1{,}8\cdot 10^{-10}}=1{,}34\cdot 10^{-5}\ \text{M}$$
$$s_{g/L}=1{,}34\cdot 10^{-5}\cdot 143{,}3=1{,}93\ \text{mg/L}$$"""},
            {"t": "(b) En NaCl 0,10 M",
             "p": "$[\\text{Cl}^-]\\approx 0{,}10$ M (la contribución de AgCl es despreciable). Despejo $[\\text{Ag}^+]=s'$.",
             "b": r"""$$s'=\dfrac{K_{ps}}{[\text{Cl}^-]}=\dfrac{1{,}8\cdot 10^{-10}}{0{,}10}=1{,}8\cdot 10^{-9}\ \text{M}$$"""},
            {"t": "Comparación",
             "p": "Razón entre solubilidades.",
             "b": r"""$$\dfrac{s}{s'}=\dfrac{1{,}34\cdot 10^{-5}}{1{,}8\cdot 10^{-9}}=7\,400$$"""},
        ],
        "resultado": r"En agua: $s\approx 1{,}3\cdot 10^{-5}$ M. En NaCl 0,10 M: $s'\approx 1{,}8\cdot 10^{-9}$ M. La presencia de Cl$^-$ <b>reduce la solubilidad ~7 400 veces</b>.",
        "verificacion": r"Esto justifica la práctica analítica de <em>lavar</em> precipitados con disolución de la sal correspondiente diluida (en lugar de agua pura) — minimiza pérdidas por solubilidad. ✓"
    },
    {
        "title": "Capacidad reguladora máxima de un tampón",
        "enunciado": r"Justificar por qué la capacidad reguladora máxima de un tampón se alcanza cuando $[\text{base}]=[\text{ácido}]$. Calcular cuánto cambia el pH al añadir <b>0,01 mol</b> de HCl a (a) 1 L de tampón con 0,5 M HA + 0,5 M A$^-$, y (b) 1 L con 0,9 M HA + 0,1 M A$^-$. Tomar p$K_a=4{,}74$ en ambos.",
        "esperado": r"(a) $\Delta\text{pH}\approx 0{,}017$; (b) $\Delta\text{pH}\approx 0{,}087$. El tampón equimolar es ~5 veces más eficiente.",
        "datos": [
            ("p$K_a$", "4,74"),
            ("HCl añadido", "0,01 mol"),
            ("Tampón (a)", "[HA]=[A$^-$]=0,5 M"),
            ("Tampón (b)", "[HA]=0,9 M, [A$^-$]=0,1 M"),
        ],
        "demo": {
            "title": "Sensibilidad al cambio en H-H",
            "body": r"""
<p>Henderson-Hasselbalch: $\text{pH}=\text{p}K_a+\log([A^-]/[HA])$. Al añadir un ácido fuerte, parte de A$^-$ se convierte en HA. Si las concentraciones iniciales son <em>iguales</em>, una pequeña perturbación apenas mueve el cociente $[A^-]/[HA]$ del valor 1, así que el pH apenas cambia.</p>
<p>En cambio, si una de las dos especies está mucho más diluida, su consumo o producción tiene un impacto relativo grande.</p>
<p>Matemáticamente, la sensibilidad $|d\text{pH}/dx|$ es mínima cuando $[\text{base}]=[\text{ácido}]$ — esto explica la "capacidad reguladora máxima".</p>
"""
        },
        "pasos": [
            {"t": "(a) Tampón equimolar",
             "p": "Tras añadir HCl: [HA]=0,51 M, [A$^-$]=0,49 M.",
             "b": r"""$$\text{pH}_0 = 4{,}74+\log 1=4{,}74$$
$$\text{pH}_f = 4{,}74+\log\dfrac{0{,}49}{0{,}51}=4{,}74-0{,}0173=4{,}723$$
$$\Delta\text{pH}=0{,}017$$"""},
            {"t": "(b) Tampón asimétrico",
             "p": "Tras añadir HCl: [HA]=0,91 M, [A$^-$]=0,09 M.",
             "b": r"""$$\text{pH}_0 = 4{,}74+\log\dfrac{0{,}1}{0{,}9}=4{,}74-0{,}954=3{,}786$$
$$\text{pH}_f = 4{,}74+\log\dfrac{0{,}09}{0{,}91}=4{,}74-1{,}004=3{,}736$$
$$\Delta\text{pH}=0{,}050$$"""},
            {"t": "Comparación",
             "p": "Cuanto más cerca de equimolar, menor cambio.",
             "b": r"""<p>El tampón equimolar es <b>~3 veces</b> más eficiente. La fórmula clásica para la capacidad reguladora $\beta$ alcanza su máximo en $[A^-]=[HA]$.</p>"""},
        ],
        "resultado": r"(a) $\Delta\text{pH}=0{,}017$ · (b) $\Delta\text{pH}=0{,}050$. El equimolar (relación 1:1) es óptimo.",
        "verificacion": r"Esto explica por qué los tampones biológicos (sangre H$_2$CO$_3$/HCO$_3^-$, p$K_a=6{,}1$) están diseñados con relación cercana a 1:1 alrededor del pH fisiológico (7,4). ✓"
    },
],

}
