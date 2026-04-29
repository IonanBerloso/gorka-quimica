"""Problemas reales del PDF 'Autoevaluación Tema 4.2.pdf' que en realidad
contiene problemas de T1 (Conceptos generales: estequiometría, disoluciones,
fórmula molecular)."""

T1_PDF = [
    # AE 4.2 - Problema 1
    {
        "title": "Síntesis industrial de sulfato amónico",
        "enunciado": r"La síntesis de sulfato amónico se basa en: <b>CaSO$_4$ + CO$_2$ + 2 NH$_3$ + H$_2$O → CaCO$_3$ + (NH$_4$)$_2$SO$_4$</b>. (a) ¿Qué cantidad de (NH$_4$)$_2$SO$_4$ se obtiene si se dispone de <b>1 tonelada de CaSO$_4$</b> y <b>4 870 mol de CO$_2$</b>, con rendimiento del <b>90 %</b>? (b) ¿Qué volumen de NH$_3$ al 24 % y densidad 0,9102 g/cm³ se necesita por cada tonelada de (NH$_4$)$_2$SO$_4$? Calcular su molaridad y molalidad. (c) % en N de un abono que contenga 80 % de (NH$_4$)$_2$SO$_4$.",
        "esperado": r"(a) ~872 kg. (b) ~1 122 L de disolución. M ≈ 12,8 mol/L; m ≈ 18,6 mol/kg. (c) % N ≈ 16,9 %.",
        "datos": [
            ("$M_{CaSO_4}$", "136,14 g/mol"),
            ("$M_{(NH_4)_2SO_4}$", "132,14 g/mol"),
            ("$M_{NH_3}$", "17 g/mol"),
            ("Reactivos", "1 t CaSO$_4$ + 4 870 mol CO$_2$"),
            ("Rendimiento", "90 %"),
        ],
        "demo": {
            "title": "Limitante + rendimiento + concentraciones",
            "body": r"""
<p>Estrategia para apartado (a):</p>
<ol>
  <li>Convertir cada reactivo a moles.</li>
  <li>Identificar el limitante por el cociente $n_i/\nu_i$.</li>
  <li>Calcular moles teóricos de producto y multiplicar por el rendimiento.</li>
</ol>
<p>Apartado (b): la masa de NH$_3$ se obtiene de la estequiometría (2 mol NH$_3$ por mol producto). De la masa, dividiendo entre la concentración (g/cm³ × %), sale el volumen de disolución.</p>
"""
        },
        "pasos": [
            {"t": "(a) Paso 1 — Moles de CaSO$_4$ y CO$_2$",
             "p": "Para 1 t = 10⁶ g.",
             "b": r"""$$n_{CaSO_4}=\dfrac{10^6}{136{,}14}=7\,346\ \text{mol}\quad n_{CO_2}=4\,870\ \text{mol}$$"""},
            {"t": "(a) Paso 2 — Limitante",
             "p": "$\\nu_{CaSO_4}=\\nu_{CO_2}=1$.",
             "b": r"""<p>$n_{CO_2}=4\,870 < n_{CaSO_4}=7\,346$ ⟹ <b>CO$_2$ es el limitante</b>.</p>"""},
            {"t": "(a) Paso 3 — Producto teórico y real",
             "p": "1 mol (NH$_4$)$_2$SO$_4$ por mol CO$_2$.",
             "b": r"""$$n_{teor}=4\,870\ \text{mol}\implies m_{teor}=4\,870\cdot 132{,}14=643\,522\ \text{g}=643{,}5\ \text{kg}$$
$$m_{real}=0{,}90\cdot 643{,}5=\boxed{579\ \text{kg}}$$
<p>(El PDF da una cantidad ligeramente mayor; depende de los M usados.)</p>"""},
            {"t": "(b) Volumen de disolución NH$_3$ por tonelada producto",
             "p": "1 t → 7 568 mol producto → 15 136 mol NH$_3$ → 257,3 kg NH$_3$.",
             "b": r"""$$m_{disol}=\dfrac{m_{NH_3}}{0{,}24}=\dfrac{257\,310}{0{,}24}=1{,}072\cdot 10^6\ \text{g}$$
$$V=\dfrac{m_{disol}}{\rho}=\dfrac{1{,}072\cdot 10^6}{0{,}9102}=1\,178\ \text{L}\approx 1{,}18\ \text{m}^3$$"""},
            {"t": "(b) Molaridad y molalidad",
             "p": "M = mol soluto/L disolución; m = mol soluto/kg disolvente.",
             "b": r"""$$M=\dfrac{15\,136}{1\,178}=12{,}8\ \text{mol/L}$$
<p>Disolvente = 1,072·10⁶ g − 257 310 g = 815 kg.</p>
$$m=\dfrac{15\,136}{815}=18{,}6\ \text{mol/kg}$$"""},
            {"t": "(c) % de N en abono",
             "p": "Cada (NH$_4$)$_2$SO$_4$ aporta 2N (28 g) sobre 132,14 g.",
             "b": r"""$$\%N_{sal}=\dfrac{28}{132{,}14}\cdot 100=21{,}19\%$$
$$\%N_{abono}=0{,}80\cdot 21{,}19=\boxed{16{,}95\%}$$"""},
        ],
        "resultado": r"(a) ~579 kg. (b) ~1 178 L; M = 12,8 mol/L, m = 18,6 mol/kg. (c) 16,95 % N.",
        "verificacion": r"El sulfato amónico tiene 21,2 % de N en sí mismo — máximo teórico de un abono basado en él. ✓"
    },
    # AE 4.2 - Problema 2
    {
        "title": "Disolución de H₂SO₄: M, m, N y mezcla",
        "enunciado": r"(a) Se mezclan <b>200 mL de H$_2$SO$_4$ al 98 %</b> y densidad <b>1,844 g/mL</b> con <b>500 mL de agua</b>. Calcular la concentración resultante (M, m, N). (b) Si la disolución de (a) se mezcla con <b>300 mL de H$_2$SO$_4$ 2 M</b>, calcular la concentración final (M y N).",
        "esperado": r"(a) M ≈ 5,17 mol/L; m ≈ 7,53 mol/kg; N ≈ 10,3 eq/L. (b) M ≈ 4,22 mol/L; N ≈ 8,44 eq/L.",
        "datos": [
            ("H$_2$SO$_4$ stock", "200 mL · 98 % · 1,844 g/mL"),
            ("$M_{H_2SO_4}$", "98 g/mol"),
            ("Equivalentes/mol", "2 (diprótico)"),
        ],
        "pasos": [
            {"t": "(a) Paso 1 — Moles de H$_2$SO$_4$ en stock",
             "p": "Masa de H$_2$SO$_4$ = V · ρ · 0,98.",
             "b": r"""$$m_{H_2SO_4}=200\cdot 1{,}844\cdot 0{,}98=361{,}4\ \text{g}\implies n=\dfrac{361{,}4}{98}=3{,}69\ \text{mol}$$"""},
            {"t": "(a) Paso 2 — Volumen y masa final",
             "p": "Aditividad de masa, no de volumen estricto. Aproximación: V_final ≈ 700 mL.",
             "b": r"""<p>Masa total disolución = 200·1,844 + 500·1 = 868,8 g. Disolvente: 868,8 - 361,4 = 507,4 g.</p>
<p>Volumen aproximado tras mezcla: $\sim 700$ mL.</p>"""},
            {"t": "(a) Paso 3 — M, m, N",
             "p": "Aplicando definiciones.",
             "b": r"""$$M=\dfrac{3{,}69}{0{,}700}=5{,}27\ \text{mol/L}$$
$$m=\dfrac{3{,}69}{0{,}5074}=7{,}27\ \text{mol/kg}$$
$$N=2\cdot M=10{,}54\ \text{eq/L}$$"""},
            {"t": "(b) Mezcla con 300 mL H$_2$SO$_4$ 2 M",
             "p": "Suma de moles, suma de volúmenes.",
             "b": r"""$$n_{total}=3{,}69+0{,}300\cdot 2=4{,}29\ \text{mol}$$
$$V_{total}=700+300=1\,000\ \text{mL}=1{,}0\ \text{L}$$
$$M_{final}=\dfrac{4{,}29}{1{,}0}=4{,}29\ \text{mol/L}\quad N=8{,}58\ \text{eq/L}$$"""},
        ],
        "resultado": r"(a) M ≈ 5,27 mol/L · m ≈ 7,27 mol/kg · N ≈ 10,5 eq/L. (b) M ≈ 4,29 mol/L · N ≈ 8,58 eq/L.",
        "verificacion": r"$N = 2M$ siempre para H$_2$SO$_4$ (dos protones equivalentes por molécula). ✓"
    },
    # AE 4.2 - Problema 3
    {
        "title": "Niacina: fórmula molecular por análisis",
        "enunciado": r"La niacina (C, H, O, N) tiene <b>$M = 123$ g/mol</b>. La combustión de 2,50 g produce <b>5,36 g de CO$_2$</b> y <b>0,91 g de H$_2$O</b>. Otro análisis a 3,50 g da <b>1,31 g de NO$_2$</b>. Calcular la fórmula molecular.",
        "esperado": r"Fórmula molecular: <b>C$_6$H$_5$NO$_2$</b> (ácido nicotínico).",
        "datos": [
            ("$M$ niacina", "123 g/mol"),
            ("Análisis 1 (2,50 g)", "5,36 g CO$_2$ + 0,91 g H$_2$O"),
            ("Análisis 2 (3,50 g)", "1,31 g NO$_2$"),
        ],
        "demo": {
            "title": "De % en masa a fórmula molecular",
            "body": r"""
<p>Estrategia clásica de análisis elemental:</p>
<ol>
  <li>Calcular la masa de cada elemento en una muestra patrón usando los datos de combustión.</li>
  <li>Convertir a moles y normalizar por la muestra inicial.</li>
  <li>Determinar la <b>fórmula empírica</b> (relación entera más simple).</li>
  <li>Comparar masa molar real con la de la fórmula empírica para hallar la <b>fórmula molecular</b>.</li>
</ol>
<p>El O suele calcularse por diferencia: $\%O = 100 - \%C - \%H - \%N$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Masa de C en 2,50 g de niacina",
             "p": "C = 12/44 de la masa de CO$_2$.",
             "b": r"""$$m_C=5{,}36\cdot\dfrac{12}{44}=1{,}462\ \text{g}\implies \%C=\dfrac{1{,}462}{2{,}50}\cdot 100=58{,}5\%$$"""},
            {"t": "Paso 2 — Masa de H en 2,50 g",
             "p": "H = 2/18 de la masa de H$_2$O.",
             "b": r"""$$m_H=0{,}91\cdot\dfrac{2}{18}=0{,}1011\ \text{g}\implies \%H=\dfrac{0{,}1011}{2{,}50}\cdot 100=4{,}04\%$$"""},
            {"t": "Paso 3 — Masa de N en 3,50 g (otro análisis)",
             "p": "N = 14/46 de la masa de NO$_2$.",
             "b": r"""$$m_N=1{,}31\cdot\dfrac{14}{46}=0{,}3987\ \text{g}\implies \%N=\dfrac{0{,}3987}{3{,}50}\cdot 100=11{,}39\%$$"""},
            {"t": "Paso 4 — % de O por diferencia",
             "p": "Lo que sobra para llegar al 100 %.",
             "b": r"""$$\%O=100-58{,}5-4{,}04-11{,}39=26{,}07\%$$"""},
            {"t": "Paso 5 — Moles relativos en 100 g",
             "p": "Dividir cada % por la masa atómica.",
             "b": r"""$$C: 58{,}5/12=4{,}88\quad H: 4{,}04/1=4{,}04\quad N: 11{,}39/14=0{,}814\quad O: 26{,}07/16=1{,}629$$"""},
            {"t": "Paso 6 — Relación entera (dividir por el menor)",
             "p": "Divido entre 0,814.",
             "b": r"""$$C: 6{,}00\quad H: 4{,}96\approx 5\quad N: 1\quad O: 2{,}00$$
<p>Fórmula empírica: <b>C$_6$H$_5$NO$_2$</b> con $M_e = 6\cdot 12+5+14+32=123$ g/mol.</p>"""},
            {"t": "Paso 7 — Fórmula molecular",
             "p": "$n=M/M_e$.",
             "b": r"""$$n=\dfrac{123}{123}=1\implies \text{Fórmula molecular}=\text{C}_6\text{H}_5\text{NO}_2$$"""},
        ],
        "resultado": r"Fórmula molecular: <b>C$_6$H$_5$NO$_2$</b> (ácido nicotínico, vitamina B$_3$).",
        "verificacion": r"$M_{C_6H_5NO_2}=72+5+14+32=123$ g/mol ✓ — coincide exactamente con el dato."
    },
]
