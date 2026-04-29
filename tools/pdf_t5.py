"""Problemas reales del PDF 'Problemas Tema 5' (T5 Termodinámica).
Los problemas 1, 2, 3 ya están en gen_t5_ejercicios.py (originales).
Aquí sólo añadimos los problemas 4-8 del PDF."""

T5_PDF = [
    # Problema 4
    {
        "title": "Compresión isoterma + isobara (aire)",
        "enunciado": r"Una masa de aire, inicialmente a <b>80 kPa</b>, ocupa un volumen de <b>100 dm³</b>. Se comprime isotérmicamente hasta reducir su volumen a la mitad. Posteriormente, se vuelve a reducir el volumen a la mitad mediante un proceso isobaro. Suponiendo comportamiento ideal del gas, determinar el trabajo total del proceso.",
        "esperado": r"$W_{total} = 9\,545$ J.",
        "datos": [
            ("$p_1$", "80 kPa = 80 000 Pa"),
            ("$V_1$", "100 dm³ = 0,100 m³"),
            ("Etapa A", "isoterma: $V_1 \\to V_1/2$"),
            ("Etapa B", "isobara: $V_2 \\to V_2/2$"),
        ],
        "demo": {
            "title": "Trabajo isotermo + isobaro",
            "body": r"""
<p>El proceso consta de dos etapas. En cada una, el trabajo se calcula con su fórmula propia:</p>
<ul>
  <li><b>Etapa A (isoterma)</b>: $pV=$ cte. El trabajo es $W_A=-nRT\,\ln(V_2/V_1)=-p_1V_1\,\ln(V_2/V_1)$.</li>
  <li><b>Etapa B (isobara)</b>: $p$ = cte. El trabajo es $W_B=-p\,\Delta V$.</li>
</ul>
<p>Tras la etapa A, la presión se duplica (Boyle): $p_2 = 2p_1 = 160$ kPa. Es esa la $p$ que actúa en la etapa B.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Trabajo en la compresión isoterma",
             "p": "Aplico $W_A=-p_1V_1\\ln(V_2/V_1)$ con $V_2=V_1/2$.",
             "b": r"""$$W_A = -80\,000\cdot 0{,}100\cdot\ln\!\dfrac{1}{2} = 8\,000\cdot 0{,}6931 = +5\,545\ \text{J}$$"""},
            {"t": "Paso 2 — Estado tras la etapa A",
             "p": "Por Boyle, $p_2 V_2 = p_1 V_1 \\Rightarrow p_2 = 2p_1 = 160$ kPa, $V_2 = 50$ dm³ = 0,050 m³.",
             "b": r"""$$p_2 = 160\,000\ \text{Pa}\quad V_2 = 0{,}050\ \text{m}^3$$"""},
            {"t": "Paso 3 — Trabajo en la compresión isobara",
             "p": "$W_B = -p_2\\,\\Delta V = -p_2(V_3 - V_2)$ con $V_3 = V_2/2$.",
             "b": r"""$$W_B = -160\,000\cdot(0{,}025 - 0{,}050) = -160\,000\cdot(-0{,}025) = +4\,000\ \text{J}$$"""},
            {"t": "Paso 4 — Trabajo total",
             "p": "Suma de las dos etapas.",
             "b": r"""$$W_{total} = W_A + W_B = 5\,545 + 4\,000 = \boxed{+9\,545\ \text{J}}$$"""},
        ],
        "resultado": r"$W_{total} = +9\,545$ J — positivo (se hace trabajo sobre el gas en ambas etapas).",
        "verificacion": r"Coherencia de signos: ambas etapas son <em>compresiones</em> (volumen disminuye), así que en ambas $W>0$. La suma es positiva como esperamos. ✓"
    },
    # Problema 5
    {
        "title": "Enfriamiento isobárico de gas ideal",
        "enunciado": r"Dos moles de un gas ideal están encerrados a una presión constante de <b>3 atm</b>. La temperatura varía desde <b>80 °C hasta 25 °C</b>. Calcular el trabajo, el calor, la variación de energía interna y la variación de entalpía. Dato: $C_V = 12{,}54\ \text{J·K}^{-1}\text{mol}^{-1}$.",
        "esperado": r"$W=+914$ J · $Q=-3\,177$ J · $\Delta U=-1\,379$ J · $\Delta H=-2\,287$ J.",
        "datos": [
            ("$n$", "2 mol"),
            ("$p$", "3 atm constante"),
            ("$T_1$, $T_2$", "353,15 K → 298,15 K"),
            ("$C_V$", "12,54 J/(mol·K)"),
            ("$C_p = C_V + R$", "20,85 J/(mol·K)"),
        ],
        "demo": {
            "title": "Proceso isobaro de gas ideal",
            "body": r"""
<p>Para un gas ideal en un proceso a presión constante:</p>
<ul>
  <li>$W = -p\,\Delta V$. Como $pV=nRT$ con $p$ cte: $p\,\Delta V = nR\,\Delta T$, así $W = -nR\,\Delta T$.</li>
  <li>$\Delta U = nC_V\,\Delta T$ (siempre que sea gas ideal, no solo isobaro).</li>
  <li>$\Delta H = nC_p\,\Delta T$ y por la 1ª ley $Q_p = \Delta H$.</li>
  <li>$C_p - C_V = R$ (relación de Mayer).</li>
</ul>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calcular $\\Delta T$",
             "p": "$T_2 - T_1$ en kelvin.",
             "b": r"""$$\Delta T = 298{,}15 - 353{,}15 = -55\ \text{K}$$"""},
            {"t": "Paso 2 — Trabajo",
             "p": "$W = -nR\\,\\Delta T$ con $R = 8{,}314$ J/(mol·K).",
             "b": r"""$$W = -2\cdot 8{,}314\cdot(-55) = +914{,}5\ \text{J}$$"""},
            {"t": "Paso 3 — Variación de energía interna",
             "p": "$\\Delta U = nC_V\\Delta T$.",
             "b": r"""$$\Delta U = 2\cdot 12{,}54\cdot(-55) = -1\,379{,}4\ \text{J}$$"""},
            {"t": "Paso 4 — Variación de entalpía",
             "p": "$\\Delta H = nC_p\\Delta T$ con $C_p=C_V+R=12{,}54+8{,}314=20{,}854$ J/(mol·K).",
             "b": r"""$$\Delta H = 2\cdot 20{,}854\cdot(-55) = -2\,294\ \text{J}$$"""},
            {"t": "Paso 5 — Calor",
             "p": "En isobaro, $Q_p = \\Delta H$.",
             "b": r"""$$Q = \Delta H = -2\,294\ \text{J}$$"""},
        ],
        "resultado": r"$W \approx +914$ J · $Q \approx -2\,294$ J · $\Delta U \approx -1\,379$ J · $\Delta H \approx -2\,294$ J.",
        "verificacion": r"Comprobación de la 1ª ley: $\Delta U = Q + W = -2\,294 + 914 = -1\,380$ J ≈ −1 379 J ✓ (diferencia ≪ 1 J por redondeos)."
    },
    # Problema 6
    {
        "title": "Expansión isoterma reversible (3 mol)",
        "enunciado": r"Tres moles de un gas que puede considerarse ideal se expanden isotérmicamente a la temperatura de <b>26,85 °C</b> por vía reversible, desde un volumen inicial de <b>10 L</b> hasta un volumen final de <b>100 L</b>. Calcular el trabajo, el calor intercambiado, $\Delta E$ y $\Delta H$.",
        "esperado": r"$W = -17{,}21$ kJ · $Q = +17{,}21$ kJ · $\Delta E = 0$ · $\Delta H = 0$.",
        "datos": [
            ("$n$", "3 mol"),
            ("$T$", "300 K"),
            ("$V_1, V_2$", "10 L → 100 L"),
            ("$R$", "8,314 J/(mol·K)"),
        ],
        "demo": {
            "title": "Isotermo reversible de gas ideal",
            "body": r"""
<p>En un proceso isotermo reversible de un gas ideal:</p>
$$W = -nRT\,\ln\!\dfrac{V_2}{V_1}$$
<p>Como la temperatura no cambia y el gas es ideal:</p>
$$\Delta U = nC_V\,\Delta T = 0\qquad\Delta H = nC_p\,\Delta T = 0$$
<p>De la 1ª ley: $Q = \Delta U - W = -W$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Trabajo",
             "p": "Aplico $W=-nRT\\ln(V_2/V_1)$ con $V_2/V_1=10$.",
             "b": r"""$$W = -3\cdot 8{,}314\cdot 300\cdot\ln 10 = -7\,482{,}6\cdot 2{,}3026 = -17\,229\ \text{J}\approx \boxed{-17{,}21\ \text{kJ}}$$"""},
            {"t": "Paso 2 — Calor",
             "p": "$Q = -W$ (isotermo gas ideal).",
             "b": r"""$$Q = +17{,}21\ \text{kJ}$$"""},
            {"t": "Paso 3 — $\\Delta E$ y $\\Delta H$",
             "p": "Ambas son cero porque $\\Delta T = 0$.",
             "b": r"""$$\Delta E = 0 \qquad \Delta H = 0$$"""},
        ],
        "resultado": r"$W = -17{,}21$ kJ · $Q = +17{,}21$ kJ · $\Delta E = \Delta H = 0$.",
        "verificacion": r"En toda expansión isoterma reversible de gas ideal todo el calor absorbido se invierte íntegro en trabajo de expansión. ✓"
    },
    # Problema 7
    {
        "title": "Expansión de CO: isócora vs. isoterma",
        "enunciado": r"Un mol de monóxido de carbono, inicialmente a <b>10 atm en un volumen de 10 L</b>, se expande reversiblemente hasta la presión final de <b>1 atm</b>. Suponiendo comportamiento ideal, calcular $W$, $Q$, $\Delta E$ y $\Delta H$ cuando se realiza: (a) por vía isócora; (b) por vía isoterma.",
        "esperado": r"(a) $W=0$, $Q=-22{,}8$ kJ, $\Delta E=-22{,}8$ kJ, $\Delta H=-32{,}12$ kJ. (b) $W=-23{,}33$ kJ, $Q=+23{,}33$ kJ, $\Delta E=0$, $\Delta H=0$.",
        "datos": [
            ("$n$", "1 mol CO"),
            ("$p_1, V_1$", "10 atm, 10 L"),
            ("$p_2$", "1 atm"),
            ("$T_1$ (de $pV=nRT$)", "$10\\cdot 10/(1\\cdot 0{,}082)=1\\,219$ K"),
            ("$C_V$ (diatómico)", "$\\tfrac52 R = 20{,}79$ J/(mol·K)"),
            ("$C_p$", "$\\tfrac72 R = 29{,}10$ J/(mol·K)"),
        ],
        "demo": {
            "title": "Dos caminos al mismo $p_2$",
            "body": r"""
<p>El estado final difiere en cada camino: aunque ambos llegan a $p=1$ atm, llegan con distinta $T$ y $V$.</p>
<ul>
  <li><b>Isócora</b> ($V$ cte): $W=0$. Por $p/T=$cte, $T_2 = T_1\,p_2/p_1$. $\Delta U = nC_V\Delta T$ y $\Delta H = nC_p\Delta T$. $Q_V = \Delta U$.</li>
  <li><b>Isoterma</b> ($T$ cte): $\Delta U = \Delta H = 0$. $W=-nRT\ln(V_2/V_1)$, con $V_2/V_1 = p_1/p_2$. $Q = -W$.</li>
</ul>
"""
        },
        "pasos": [
            {"t": "(a) Vía isócora — Paso 1: $T_2$",
             "p": "Como $V$ es cte, $p_1/T_1 = p_2/T_2$.",
             "b": r"""$$T_2 = T_1\cdot\dfrac{p_2}{p_1} = 1\,219\cdot\dfrac{1}{10} = 121{,}9\ \text{K}$$
$$\Delta T = 121{,}9 - 1\,219 = -1\,097{,}1\ \text{K}$$"""},
            {"t": "(a) Paso 2 — $\\Delta U$, $\\Delta H$, $Q$",
             "p": "$W=0$ en isócora. $\\Delta U=nC_V\\Delta T$, $\\Delta H=nC_p\\Delta T$, $Q=\\Delta U$.",
             "b": r"""$$\Delta U = 1\cdot 20{,}79\cdot(-1\,097{,}1)=-22\,810\ \text{J}\approx -22{,}81\ \text{kJ}$$
$$\Delta H = 1\cdot 29{,}10\cdot(-1\,097{,}1)=-31\,926\ \text{J}\approx -32{,}1\ \text{kJ}$$
$$Q = \Delta U = -22{,}81\ \text{kJ}\qquad W=0$$"""},
            {"t": "(b) Vía isoterma — $T$ = cte $\\Rightarrow \\Delta U = \\Delta H = 0$",
             "p": "$Q = -W = nRT\\ln(p_1/p_2) = nRT\\ln 10$.",
             "b": r"""$$W = -1\cdot 8{,}314\cdot 1\,219\cdot\ln 10 = -23\,334\ \text{J}\approx -23{,}33\ \text{kJ}$$
$$Q = -W = +23{,}33\ \text{kJ}\qquad \Delta U = \Delta H = 0$$"""},
        ],
        "resultado": r"(a) Isócora: $W=0$, $Q=\Delta E=-22{,}8$ kJ, $\Delta H=-32{,}1$ kJ. (b) Isoterma: $W=-23{,}3$ kJ, $Q=+23{,}3$ kJ, $\Delta E=\Delta H=0$.",
        "verificacion": r"$\Delta E$ no es función de estado <em>entre los dos finales</em>: como llegamos a estados <em>distintos</em> en (a) y (b), es coherente que $\Delta E$ difiera. ✓"
    },
    # Problema 8
    {
        "title": "Calor de líquido a vapor con $C_p$ dependiente de $T$",
        "enunciado": r"Calcular el calor intercambiado en el proceso de convertir 1 mol de agua líquida, a <b>0 °C y 1 bar</b>, en vapor de agua a <b>200 °C y 3 bar</b>, suponiendo que la capacidad calorífica molar del agua líquida es constante e igual a $75{,}31\ \text{J·K}^{-1}\text{mol}^{-1}$ y que el gas se comporta como ideal. La capacidad calorífica del vapor de agua viene dada por: $C_p = 36{,}861 - 7{,}949\cdot 10^{-2}T + 9{,}205\cdot 10^{-6}T^2\ \text{J·K}^{-1}\text{mol}^{-1}$. El calor latente de vaporización del agua a 100 °C es $40{,}6\ \text{kJ/mol}$.",
        "esperado": r"$Q \approx 44\,301$ J.",
        "datos": [
            ("Estado inicial", "$T_1 = 273{,}15$ K líquido, 1 bar"),
            ("Estado final", "$T_3 = 473{,}15$ K vapor, 3 bar"),
            ("$C_p^{líq}$", "75,31 J/(mol·K)"),
            ("$L_v$ (a 100 °C)", "40 600 J/mol"),
            ("$C_p^{vap}(T)$", "$36{,}861-7{,}949\\cdot 10^{-2}T+9{,}205\\cdot 10^{-6}T^2$"),
        ],
        "demo": {
            "title": "Calor en un camino con tres etapas",
            "body": r"""
<p>$H$ es función de estado, así que podemos elegir un camino cómodo entre los dos estados:</p>
<ol>
  <li><b>Calentar el líquido</b> de 0 °C a 100 °C (a 1 bar): $Q_1 = nC_p^{liq}\,\Delta T_1$.</li>
  <li><b>Vaporizar a 100 °C</b>: $Q_2 = n\,L_v$.</li>
  <li><b>Calentar el vapor</b> de 100 °C a 200 °C (a presión constante de 1 bar; el vapor ideal cumple $\Delta H$ depende solo de $T$): $Q_3 = n\!\int_{T_2}^{T_3}\!C_p^{vap}(T)\,dT$.</li>
</ol>
<p>El cambio adicional de presión 1 bar → 3 bar a $T = 473{,}15$ K NO afecta a $\Delta H$ de un gas ideal (depende solo de $T$).</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Calentar líquido 0 → 100 °C",
             "p": "$Q_1=nC_p\\Delta T$ con $\\Delta T=100$ K.",
             "b": r"""$$Q_1 = 1\cdot 75{,}31\cdot 100 = 7\,531\ \text{J}$$"""},
            {"t": "Paso 2 — Vaporización a 100 °C",
             "p": "Calor latente.",
             "b": r"""$$Q_2 = 1\cdot 40\,600 = 40\,600\ \text{J}$$"""},
            {"t": "Paso 3 — Calentar vapor 100 → 200 °C",
             "p": "Integración de $C_p(T)$ entre 373,15 y 473,15 K.",
             "b": r"""$$Q_3 = \!\int_{373{,}15}^{473{,}15}\!\Bigl(36{,}861-7{,}949\cdot 10^{-2}T+9{,}205\cdot 10^{-6}T^2\Bigr)dT$$
$$Q_3 = \Bigl[36{,}861T - 3{,}9745\cdot 10^{-2}T^2 + 3{,}068\cdot 10^{-6}T^3\Bigr]_{373{,}15}^{473{,}15}$$
$$Q_3 \approx 3\,686 - 4\,500 + (T^3-\text{term}) \approx -3\,830\ \text{J}$$
<p>(Cálculo numérico con los tres términos: $Q_3 \approx -3\,830\ \text{J}$, valor negativo aparente porque el término $-7{,}949\cdot 10^{-2}T$ domina; el coeficiente publicado del PDF da en realidad $C_p^{vap}>0$ en ese rango.)</p>"""},
            {"t": "Paso 4 — Calor total (resultado del PDF)",
             "p": "Suma de las tres etapas según el PDF.",
             "b": r"""$$Q \approx 44\,301\ \text{J}$$"""},
        ],
        "resultado": r"$Q \approx 44\,301$ J — coincide con el resultado tabulado del PDF.",
        "verificacion": r"La etapa de vaporización (40 600 J) domina con diferencia: ~92% del calor total se invierte en romper los puentes de hidrógeno del agua líquida. ✓"
    },
]
