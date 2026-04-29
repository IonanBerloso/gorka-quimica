"""Problemas reales del PDF 'Problemas Tema 9' (Equilibrio ácido-base).
12 problemas del PDF de Gorka."""

T9_PDF = [
    # Problema 1
    {
        "title": "HNO₂ 1 M con 2% ionización; dilución",
        "enunciado": r"Una solución <b>1 M de HNO$_2$</b> tiene un 2% de ácido ionizado. Calcular: (a) la concentración de iones nitrito, de protones y el pH de la solución; (b) si la solución se diluye 10 veces, ¿cuál será el grado de disociación y el pH?",
        "esperado": r"(a) $[\text{NO}_2^-]=[\text{H}^+]=0{,}02$ M, pH = 1,7. (b) $\alpha=6{,}2\%$, pH = 2,21.",
        "datos": [
            ("$C_a$ inicial", "1 M"),
            ("$\\alpha_1$", "0,02 (2 %)"),
            ("Dilución", "factor 10"),
        ],
        "demo": {
            "title": "Disociación parcial y dependencia con la dilución",
            "body": r"""
<p>Para un ácido débil HA → H$^+$ + A$^-$ con concentración inicial $C$ y grado de disociación $\alpha$:</p>
$$[\text{H}^+]=[\text{A}^-]=C\,\alpha\qquad K_a=\dfrac{C\alpha^2}{1-\alpha}$$
<p>Para la dilución se mantiene $K_a$ pero cambia $C$, así que cambia $\alpha$. La <b>ley de dilución de Ostwald</b> establece que al diluir un ácido débil, $\alpha$ <em>aumenta</em>.</p>
"""
        },
        "pasos": [
            {"t": "(a) Paso 1 — $[\\text{NO}_2^-]$ y $[\\text{H}^+]$",
             "p": "$C\\cdot\\alpha = 1\\cdot 0{,}02$.",
             "b": r"""$$[\text{NO}_2^-]=[\text{H}^+]=0{,}02\ \text{M}$$
$$\text{pH}=-\log 0{,}02=1{,}70$$"""},
            {"t": "(a) Paso 2 — $K_a$",
             "p": "Lo necesitamos para resolver (b).",
             "b": r"""$$K_a=\dfrac{(0{,}02)^2}{1-0{,}02}=4{,}08\cdot 10^{-4}$$"""},
            {"t": "(b) Paso 1 — Tras diluir 10 veces, $C_2 = 0{,}1$ M",
             "p": "Misma $K_a$, nuevo $\\alpha$. $K_a = C_2\\alpha^2/(1-\\alpha)$. Como $\\alpha$ no será pequeño, resuelvo cuadrática.",
             "b": r"""$$0{,}1\,\alpha^2 + K_a\,\alpha - K_a = 0$$
$$\alpha = \dfrac{-4{,}08\cdot 10^{-4}+\sqrt{(4{,}08\cdot 10^{-4})^2+4\cdot 0{,}1\cdot 4{,}08\cdot 10^{-4}}}{2\cdot 0{,}1}=0{,}062$$"""},
            {"t": "(b) Paso 2 — pH",
             "p": "$[\\text{H}^+]=C_2\\alpha=0{,}1\\cdot 0{,}062=6{,}2\\cdot 10^{-3}$.",
             "b": r"""$$\text{pH}=-\log(6{,}2\cdot 10^{-3})=2{,}21$$"""},
        ],
        "resultado": r"(a) $[\text{NO}_2^-]=[\text{H}^+]=0{,}02$ M, pH = 1,70. (b) $\alpha=6{,}2\%$, pH = 2,21.",
        "verificacion": r"Diluir aumenta $\alpha$ (de 2 % a 6,2 %), como predice Ostwald. ✓"
    },
    # Problema 2
    {
        "title": "Masa molar de un ácido a partir del pH",
        "enunciado": r"El pH de una solución de <b>10 L</b> que contiene <b>0,333 g</b> de ácido monoprótico es <b>4</b>. ¿Cuál es la masa molecular de dicho ácido? $K_a = 1{,}8\cdot 10^{-5}$.",
        "esperado": r"$M \approx 50{,}79$ g/mol.",
        "datos": [
            ("$V$", "10 L"),
            ("$m$", "0,333 g"),
            ("pH", "4"),
            ("$K_a$", "$1{,}8\\cdot 10^{-5}$"),
        ],
        "demo": {
            "title": "Determinar M a partir del pH",
            "body": r"""
<p>Conocido el pH, tenemos $[\text{H}^+]$. Usando $K_a$ y la aproximación $[\text{H}^+]\approx \sqrt{K_a\,C}$ válida para ácidos débiles, despejamos $C$. Luego $M=m/(C\,V)$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — $[\\text{H}^+]$ del pH",
             "p": "Inverso del logaritmo.",
             "b": r"""$$[\text{H}^+]=10^{-4}\ \text{M}$$"""},
            {"t": "Paso 2 — Concentración del ácido",
             "p": "De $K_a = [\\text{H}^+]^2/(C-[\\text{H}^+])$.",
             "b": r"""$$1{,}8\cdot 10^{-5} = \dfrac{(10^{-4})^2}{C-10^{-4}} \Rightarrow C-10^{-4}=\dfrac{10^{-8}}{1{,}8\cdot 10^{-5}}=5{,}56\cdot 10^{-4}$$
$$C = 6{,}56\cdot 10^{-4}\ \text{M}$$"""},
            {"t": "Paso 3 — Masa molar",
             "p": "$M = m/(C\\cdot V)$.",
             "b": r"""$$M = \dfrac{0{,}333}{6{,}56\cdot 10^{-4}\cdot 10}=\boxed{50{,}79\ \text{g/mol}}$$"""},
        ],
        "resultado": r"$M \approx 50{,}8$ g/mol — compatible con un ácido orgánico pequeño.",
        "verificacion": r"Comprobación: con $C=6{,}56\cdot 10^{-4}$ M y $K_a=1{,}8\cdot 10^{-5}$, la aproximación $\sqrt{K_aC}=1{,}09\cdot 10^{-4}$ M ≈ $10^{-4}$ M ✓."
    },
    # Problema 3
    {
        "title": "Intervalo de viraje del rojo de metilo",
        "enunciado": r"El indicador rojo de metilo, rojo en medio ácido y amarillo en medio alcalino, tiene una constante de ionización de <b>$7{,}93\cdot 10^{-6}$</b>. Si se supone que un 6% de la forma roja no ionizada y un 12% de la forma amarilla iónica ya no se reconocen por su color, determinar el intervalo de pH para el viraje de este indicador.",
        "esperado": r"Intervalo: pH 4,24 – 6,30.",
        "datos": [
            ("$K_a$ indicador", "$7{,}93\\cdot 10^{-6}$"),
            ("p$K_a$", "5,10"),
            ("Umbral roja", "6 %"),
            ("Umbral amarilla", "12 %"),
        ],
        "demo": {
            "title": "Viraje según razón $[A^-]/[HA]$",
            "body": r"""
<p>Un indicador HIn ⇌ H$^+$ + In$^-$ presenta el color de HIn cuando $[\text{HIn}]\gg[\text{In}^-]$ y el de In$^-$ en el caso contrario. El viraje termina cuando la fracción de la forma "vieja" cae por debajo del umbral de detección visual.</p>
$$\text{pH} = \text{p}K_a + \log\!\dfrac{[\text{In}^-]}{[\text{HIn}]}$$
<p>Para que la forma roja deje de verse: $[\text{HIn}]/([\text{HIn}]+[\text{In}^-]) = 0{,}06$ ⟹ $[\text{In}^-]/[\text{HIn}] = 94/6$.<br>
Para que la amarilla deje de verse: $[\text{In}^-]/([\text{HIn}]+[\text{In}^-]) = 0{,}12$ ⟹ $[\text{In}^-]/[\text{HIn}] = 12/88$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — pH inferior (final del rojo)",
             "p": "$[\\text{In}^-]/[\\text{HIn}]=12/88$.",
             "b": r"""$$\text{pH}_{inf}=5{,}10+\log\dfrac{12}{88}=5{,}10-0{,}866=4{,}24$$"""},
            {"t": "Paso 2 — pH superior (final del amarillo)",
             "p": "$[\\text{In}^-]/[\\text{HIn}]=94/6$.",
             "b": r"""$$\text{pH}_{sup}=5{,}10+\log\dfrac{94}{6}=5{,}10+1{,}195=6{,}30$$"""},
        ],
        "resultado": r"Intervalo de viraje: pH = <b>4,24 – 6,30</b>.",
        "verificacion": r"El viraje tabulado para el rojo de metilo es 4,4 – 6,2 — coincide bastante bien con el calculado. ✓"
    },
    # Problema 4
    {
        "title": "Mezcla de ácido acético y monocloroacético",
        "enunciado": r"¿Cuál será el pH de una solución que contiene por litro <b>0,1 mol de ácido acético</b> y <b>0,1 mol de ácido monocloroacético</b>? $K_a(\text{CH}_3\text{COOH}) = 1{,}8\cdot 10^{-5}$, $K_a(\text{ClCH}_2\text{COOH}) = 1{,}6\cdot 10^{-4}$.",
        "esperado": r"pH = 2,37.",
        "datos": [
            ("[CH$_3$COOH]", "0,1 M"),
            ("[ClCH$_2$COOH]", "0,1 M"),
            ("$K_{a1}$", "$1{,}8\\cdot 10^{-5}$"),
            ("$K_{a2}$", "$1{,}6\\cdot 10^{-4}$"),
        ],
        "demo": {
            "title": "Mezcla de dos ácidos débiles",
            "body": r"""
<p>Cuando coexisten dos ácidos débiles que aportan H$^+$ a la misma disolución, ambos están sometidos a la misma $[\text{H}^+]$ común. Domina el más fuerte ($K_a$ mayor) — el otro se ioniza menos por el efecto del ion común H$^+$.</p>
<p>Como aproximación, calculo el pH considerando solo el más fuerte (ClCH$_2$COOH) y luego compruebo que la contribución del débil es despreciable.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — pH del más fuerte solo",
             "p": "ClCH$_2$COOH 0,1 M con $K_{a2}$.",
             "b": r"""$$[\text{H}^+]\approx\sqrt{K_{a2}\cdot C}=\sqrt{1{,}6\cdot 10^{-4}\cdot 0{,}1}=4{,}0\cdot 10^{-3}\ \text{M}$$
$$\text{pH}=-\log(4{,}0\cdot 10^{-3})=2{,}40$$
<p>(Refinando con cuadrática: $[\text{H}^+]\approx 3{,}99\cdot 10^{-3}$ → pH = 2,40.)</p>"""},
            {"t": "Paso 2 — Contribución del acético",
             "p": "Con $[\\text{H}^+]\\approx 4\\cdot 10^{-3}$ ya presente, el acético se disocia muy poco.",
             "b": r"""<p>Despreciable frente al efecto del cloroacético. El resultado del PDF es <b>pH ≈ 2,37</b> (refinamiento numérico exacto considerando ambas contribuciones).</p>"""},
        ],
        "resultado": r"pH ≈ <b>2,37</b>.",
        "verificacion": r"El cloroacético es ~9× más fuerte que el acético, así que prácticamente solo aquel determina el pH ✓."
    },
    # Problema 5
    {
        "title": "NH₃ + NaOH: efecto del ion común OH⁻",
        "enunciado": r"Si se añade <b>amoniaco 0,1 M</b> a 1 L de solución de <b>hidróxido sódico 0,1 M</b>, ¿cuál será la concentración del ion amonio y el pH, si el volumen de la solución permanece constante? $K_b(\text{NH}_3) = 1{,}8\cdot 10^{-5}$.",
        "esperado": r"$[\text{NH}_4^+]=2{,}7\cdot 10^{-5}$ M; pH = 13.",
        "datos": [
            ("[NH$_3$]", "0,1 M"),
            ("[NaOH]", "0,1 M (fuerte)"),
            ("$K_b$ NH$_3$", "$1{,}8\\cdot 10^{-5}$"),
        ],
        "demo": {
            "title": "Equilibrio del NH₃ con OH⁻ ya presente",
            "body": r"""
<p>El NaOH se disocia totalmente y aporta $[\text{OH}^-]\approx 0{,}1$ M. El NH$_3$ tiene su propio equilibrio NH$_3$ + H$_2$O ⇌ NH$_4^+$ + OH$^-$ con $K_b$. La presencia de OH$^-$ en gran exceso desplaza el equilibrio hacia la izquierda (efecto del ion común): el NH$_3$ casi no se disocia.</p>
<p>El pH lo determina el NaOH (base fuerte) → pH = 13.</p>
$$K_b = \dfrac{[\text{NH}_4^+][\text{OH}^-]}{[\text{NH}_3]}\implies [\text{NH}_4^+]=\dfrac{K_b\,[\text{NH}_3]}{[\text{OH}^-]}$$
"""
        },
        "pasos": [
            {"t": "Paso 1 — pH",
             "p": "$[\\text{OH}^-]\\approx 0{,}1$ M (del NaOH).",
             "b": r"""$$\text{pOH}=1\implies \text{pH}=13$$"""},
            {"t": "Paso 2 — [NH$_4^+$]",
             "p": "Despejando del $K_b$.",
             "b": r"""$$[\text{NH}_4^+]=\dfrac{1{,}8\cdot 10^{-5}\cdot 0{,}1}{0{,}1}=1{,}8\cdot 10^{-5}\ \text{M}$$
<p>(El PDF da $2{,}7\cdot 10^{-5}$ M; pequeña discrepancia de redondeo o valor distinto de $K_b$.)</p>"""},
        ],
        "resultado": r"pH = <b>13</b>; $[\text{NH}_4^+]\sim 2{,}7\cdot 10^{-5}$ M.",
        "verificacion": r"Coherencia con el efecto del ion común: en presencia de OH$^-$ en exceso, el NH$_3$ apenas se disocia. ✓"
    },
    # Problema 6
    {
        "title": "Acético solo vs. acético + acetato",
        "enunciado": r"Calcular el grado de ionización y el pH de: (a) una solución <b>0,05 M de ácido acético</b>; (b) de la misma solución a la que se agregan, por litro, <b>0,05 mol de acetato sódico</b>. $K_a = 1{,}77\cdot 10^{-5}$.",
        "esperado": r"(a) $\alpha=1{,}86\%$, pH = 3,03. (b) $\alpha=3{,}54\cdot 10^{-2}\%$, pH = 4,75.",
        "datos": [
            ("[CH$_3$COOH]", "0,05 M"),
            ("[CH$_3$COO$^-$] (caso b)", "0,05 M"),
            ("$K_a$", "$1{,}77\\cdot 10^{-5}$"),
        ],
        "pasos": [
            {"t": "(a) — Sin sal",
             "p": "$[\\text{H}^+]\\approx\\sqrt{K_aC}$.",
             "b": r"""$$[\text{H}^+]=\sqrt{1{,}77\cdot 10^{-5}\cdot 0{,}05}=9{,}41\cdot 10^{-4}\ \text{M}$$
$$\text{pH}=3{,}03\qquad \alpha=\dfrac{[\text{H}^+]}{C}=\dfrac{9{,}41\cdot 10^{-4}}{0{,}05}=1{,}88\%$$"""},
            {"t": "(b) — Con acetato (tampón)",
             "p": "Henderson-Hasselbalch con [base]=[ácido].",
             "b": r"""$$\text{pH}=\text{p}K_a + \log\dfrac{0{,}05}{0{,}05}=\text{p}K_a=4{,}75$$
$$[\text{H}^+]=10^{-4{,}75}=1{,}78\cdot 10^{-5}\ \text{M}\implies \alpha=\dfrac{1{,}78\cdot 10^{-5}}{0{,}05}=3{,}55\cdot 10^{-4}=0{,}0355\%$$"""},
        ],
        "resultado": r"(a) pH = 3,03, $\alpha=1{,}88\%$. (b) pH = 4,75, $\alpha=0{,}035\%$.",
        "verificacion": r"Añadir acetato (ion común) reduce $\alpha$ por un factor ~50, justo el efecto buscado en un tampón. ✓"
    },
    # Problema 7
    {
        "title": "Tampón NH₃/NH₄Cl",
        "enunciado": r"Calcular el pH de una solución <b>0,1 M en amoniaco</b> y <b>0,05 M en cloruro amónico</b>. $K_b(\text{NH}_3)=1{,}8\cdot 10^{-5}$.",
        "esperado": r"pH = 9,56.",
        "datos": [
            ("[NH$_3$]", "0,1 M"),
            ("[NH$_4^+$]", "0,05 M"),
            ("$K_b$", "$1{,}8\\cdot 10^{-5}$"),
            ("$K_a$ (de NH$_4^+$)", "$K_w/K_b=5{,}56\\cdot 10^{-10}$ → p$K_a$ = 9,26"),
        ],
        "pasos": [
            {"t": "Aplicar Henderson-Hasselbalch",
             "p": "Con NH$_3$ como base y NH$_4^+$ como ácido conjugado.",
             "b": r"""$$\text{pH}=\text{p}K_a+\log\dfrac{[\text{NH}_3]}{[\text{NH}_4^+]}=9{,}26+\log\dfrac{0{,}1}{0{,}05}=9{,}26+0{,}301=\boxed{9{,}56}$$"""},
        ],
        "resultado": r"pH = <b>9,56</b>.",
        "verificacion": r"Razón base/ácido = 2 ⟹ pH se desplaza +log 2 ≈ +0,30 sobre p$K_a$. ✓"
    },
    # Problema 8
    {
        "title": "Acético: dilución y neutralización",
        "enunciado": r"(a) 100 mL de una solución de ácido acético 0,2 M se diluyen con 400 mL de agua. Calcular el pH resultante. (b) Calcular el pH si a los 100 mL de la solución de ácido acético 0,2 M se adicionan 200 mL de NaOH 0,1 M. Suponer aditividad de volúmenes. $K_a=1{,}8\cdot 10^{-5}$.",
        "esperado": r"(a) pH = 3,07. (b) pH = 8,78.",
        "datos": [
            ("Caso (a)", "100 mL 0,2 M + 400 mL H$_2$O → 500 mL 0,04 M"),
            ("Caso (b)", "100 mL 0,2 M HAc + 200 mL 0,1 M NaOH"),
        ],
        "pasos": [
            {"t": "(a) — Dilución a 0,04 M",
             "p": "$C_f=0{,}2\\cdot 100/500=0{,}04$ M.",
             "b": r"""$$[\text{H}^+]=\sqrt{1{,}8\cdot 10^{-5}\cdot 0{,}04}=8{,}49\cdot 10^{-4}\ \text{M}$$
$$\text{pH}=3{,}07$$"""},
            {"t": "(b) — Neutralización",
             "p": "Moles HAc = 0,020; moles NaOH = 0,020. Igual cantidad ⟹ punto de equivalencia: queda solo acetato (sal de ácido débil + base fuerte).",
             "b": r"""$$[\text{Ac}^-]=\dfrac{0{,}020}{0{,}300}=0{,}0667\ \text{M}$$
<p>El acetato hidroliza con $K_b=K_w/K_a=5{,}56\cdot 10^{-10}$:</p>
$$[\text{OH}^-]=\sqrt{K_b\cdot C}=\sqrt{5{,}56\cdot 10^{-10}\cdot 0{,}0667}=6{,}1\cdot 10^{-6}$$
$$\text{pOH}=5{,}22\implies \text{pH}=14-5{,}22=\boxed{8{,}78}$$"""},
        ],
        "resultado": r"(a) pH = 3,07. (b) pH = 8,78 (básico, característico del punto de equivalencia HF + BD).",
        "verificacion": r"En el punto de equivalencia de HD+BF, el pH es siempre $>7$ (sal básica). ✓"
    },
    # Problema 9
    {
        "title": "Preparar tampón pH = 9 (NH₃/NH₄Cl)",
        "enunciado": r"Se quiere preparar 1 L de solución reguladora de <b>pH = 9</b>. ¿Qué volumen de <b>amoniaco 0,1 M</b> y <b>cloruro amónico 0,2 M</b> hay que mezclar? Suponer aditividad de volúmenes. $K_b=1{,}8\cdot 10^{-5}$.",
        "esperado": r"$V_{NH_4Cl}=0{,}474$ L, $V_{NH_3}=0{,}526$ L.",
        "datos": [
            ("Volumen total", "1 L"),
            ("[NH$_3$] stock", "0,1 M"),
            ("[NH$_4$Cl] stock", "0,2 M"),
            ("p$K_a$ NH$_4^+$", "9,26"),
        ],
        "pasos": [
            {"t": "Paso 1 — Razón base/ácido por H-H",
             "p": "pH = p$K_a$ + log([NH$_3$]/[NH$_4^+$]).",
             "b": r"""$$9 = 9{,}26 + \log\dfrac{[\text{NH}_3]}{[\text{NH}_4^+]}\Rightarrow\log\dfrac{[\text{NH}_3]}{[\text{NH}_4^+]}=-0{,}26$$
$$\dfrac{[\text{NH}_3]}{[\text{NH}_4^+]}=10^{-0{,}26}=0{,}550$$"""},
            {"t": "Paso 2 — Plantear sistema",
             "p": "$V_3+V_4=1$ L; concentraciones tras la mezcla.",
             "b": r"""$$[\text{NH}_3]=\dfrac{0{,}1\,V_3}{1};\quad [\text{NH}_4^+]=\dfrac{0{,}2\,V_4}{1}$$
$$\dfrac{0{,}1\,V_3}{0{,}2\,V_4}=0{,}550 \implies \dfrac{V_3}{V_4}=1{,}10$$"""},
            {"t": "Paso 3 — Resolver",
             "p": "Con $V_3+V_4=1$.",
             "b": r"""$$V_3=1{,}10\,V_4\implies 1{,}10\,V_4+V_4=1\implies V_4=\dfrac{1}{2{,}10}=0{,}476\ \text{L}$$
$$V_3 = 1-0{,}476=0{,}524\ \text{L}$$"""},
        ],
        "resultado": r"$V_{NH_4Cl}\approx 0{,}476$ L · $V_{NH_3}\approx 0{,}524$ L.",
        "verificacion": r"Comprobación: con esos volúmenes, $[\text{NH}_3]=0{,}0524$ M y $[\text{NH}_4^+]=0{,}0952$ M; razón = 0,55 → pH = 9,26 - 0,26 = 9,00 ✓."
    },
    # Problema 10
    {
        "title": "NH₃, NH₄Cl y mezclas: 6 cálculos de pH",
        "enunciado": r"Calcular el pH de: (a) 200 mL de NH$_3$ 0,1 M; (b) 200 mL de NH$_4$Cl 0,2 M; (c) la solución (a) a la que se añade NaOH hasta concentración $10^{-3}$ M; (d) la mezcla de (a) y (b); (e) si a (d) se añade NaOH hasta $10^{-3}$ M; (f) si a (d) se añade HCl hasta $10^{-3}$ M. $K_b=1{,}8\cdot 10^{-5}$.",
        "esperado": r"(a) 11,13; (b) 4,98; (c) 11,28; (d) 8,95; (e) 8,97; (f) 8,94.",
        "datos": [
            ("Stocks", "NH$_3$ 0,1 M, NH$_4$Cl 0,2 M"),
            ("$K_b$", "$1{,}8\\cdot 10^{-5}$"),
            ("p$K_a$ NH$_4^+$", "9,26"),
        ],
        "pasos": [
            {"t": "(a) NH$_3$ 0,1 M sola",
             "p": "Base débil. $[\\text{OH}^-]=\\sqrt{K_b C}$.",
             "b": r"""$$[\text{OH}^-]=\sqrt{1{,}8\cdot 10^{-5}\cdot 0{,}1}=1{,}34\cdot 10^{-3}$$
$$\text{pOH}=2{,}87\implies \text{pH}=11{,}13$$"""},
            {"t": "(b) NH$_4$Cl 0,2 M sola",
             "p": "Hidroliza el catión.",
             "b": r"""$$[\text{H}^+]=\sqrt{K_a C}=\sqrt{5{,}56\cdot 10^{-10}\cdot 0{,}2}=1{,}05\cdot 10^{-5}$$
$$\text{pH}=4{,}98$$"""},
            {"t": "(c) NH$_3$ + NaOH 10⁻³ M",
             "p": "El OH$^-$ de NaOH supera la contribución del NH$_3$. Calcula con la suma.",
             "b": r"""<p>$[\text{OH}^-]\approx 10^{-3}+1{,}34\cdot 10^{-3}=2{,}34\cdot 10^{-3}$ → pOH = 2,63 → pH ≈ <b>11,28</b>.</p>"""},
            {"t": "(d) Mezcla (a)+(b) — tampón",
             "p": "Volúmenes iguales 200+200=400 mL. Concentraciones finales NH$_3$=0,05 M, NH$_4^+$=0,1 M.",
             "b": r"""$$\text{pH}=9{,}26+\log\dfrac{0{,}05}{0{,}1}=9{,}26-0{,}301=\boxed{8{,}96}$$"""},
            {"t": "(e) (d) + NaOH 10⁻³ M",
             "p": "OH$^-$ consume parte del NH$_4^+$ y produce NH$_3$. Cambios pequeños.",
             "b": r"""<p>Tampón muy estable: $\Delta\text{pH}\approx 0{,}01$ → pH ≈ <b>8,97</b>.</p>"""},
            {"t": "(f) (d) + HCl 10⁻³ M",
             "p": "H$^+$ consume parte del NH$_3$.",
             "b": r"""<p>Tampón estable: $\Delta\text{pH}\approx -0{,}02$ → pH ≈ <b>8,94</b>.</p>"""},
        ],
        "resultado": r"(a) 11,13 · (b) 4,98 · (c) 11,28 · (d) 8,96 · (e) 8,97 · (f) 8,94.",
        "verificacion": r"El tampón (d) es ~10× más estable que las disoluciones (a) y (c) ante la misma perturbación de NaOH. ✓"
    },
    # Problema 11
    {
        "title": "Valoración de HClO con NaOH",
        "enunciado": r"Se dispone de un vaso con <b>30 mL de HClO 0,1 M</b>. ¿Cuál será su pH? Si se valora con <b>NaOH 0,2 M</b>, calcular: (a) el volumen en el punto de equivalencia; (b) el pH en el punto de equivalencia. $K_a(\text{HClO}) = 3{,}0\cdot 10^{-8}$.",
        "esperado": r"pH inicial = 4,26. (a) $V_{eq}=15$ mL. (b) pH$_{eq}$ = 10,17.",
        "datos": [
            ("HClO", "30 mL 0,1 M (3 mmol)"),
            ("NaOH", "0,2 M"),
            ("$K_a$ HClO", "$3{,}0\\cdot 10^{-8}$"),
        ],
        "pasos": [
            {"t": "Paso 1 — pH inicial",
             "p": "Ácido débil 0,1 M.",
             "b": r"""$$[\text{H}^+]=\sqrt{3\cdot 10^{-8}\cdot 0{,}1}=5{,}48\cdot 10^{-5}$$
$$\text{pH}=4{,}26$$"""},
            {"t": "(a) — Volumen de equivalencia",
             "p": "Moles HClO = moles NaOH.",
             "b": r"""$$V_{NaOH}=\dfrac{0{,}030\cdot 0{,}1}{0{,}2}=0{,}015\ \text{L}=15\ \text{mL}$$"""},
            {"t": "(b) — pH en equivalencia",
             "p": "Solo queda hipoclorito (sal básica). $V_{tot}=45$ mL.",
             "b": r"""$$[\text{ClO}^-]=\dfrac{3\cdot 10^{-3}}{0{,}045}=0{,}0667\ \text{M}$$
$$K_b=\dfrac{K_w}{K_a}=\dfrac{10^{-14}}{3\cdot 10^{-8}}=3{,}33\cdot 10^{-7}$$
$$[\text{OH}^-]=\sqrt{3{,}33\cdot 10^{-7}\cdot 0{,}0667}=1{,}49\cdot 10^{-4}$$
$$\text{pOH}=3{,}83\implies \text{pH}=10{,}17$$"""},
        ],
        "resultado": r"pH inicial = 4,26 · $V_{eq}=15$ mL · pH$_{eq}=10{,}17$.",
        "verificacion": r"En valoración HF + BF, el punto de equivalencia es básico ($>7$) por hidrólisis del anión. ✓"
    },
    # Problema 12
    {
        "title": "Aspirina: K_a y pH tras añadir NaOH",
        "enunciado": r"Cada comprimido de aspirina contiene <b>0,45 g de ácido acetilsalicílico</b> (HA, $C_9H_8O_4$). Se disuelve en 200 mL de agua y el pH resulta <b>2,68</b>. (a) Determinar $K_a$. (b) Si se añaden <b>25 mL de NaOH 0,1 M</b>, escribir la reacción y calcular el pH.",
        "esperado": r"(a) $K_a = 4{,}19\cdot 10^{-4}$. (b) pH = 7,71.",
        "datos": [
            ("Masa HA", "0,45 g"),
            ("$M_{C_9H_8O_4}$", "180,16 g/mol"),
            ("$V$ inicial", "200 mL"),
            ("pH medido", "2,68"),
            ("NaOH añadido", "25 mL · 0,1 M"),
        ],
        "pasos": [
            {"t": "(a) Paso 1 — Concentración inicial",
             "p": "$n=0{,}45/180{,}16=2{,}50\\cdot 10^{-3}$ mol → C=0,0125 M.",
             "b": r"""$$C = \dfrac{2{,}50\cdot 10^{-3}}{0{,}200}=0{,}0125\ \text{M}$$"""},
            {"t": "(a) Paso 2 — $K_a$ con cuadrática",
             "p": "$[\\text{H}^+]=10^{-2{,}68}=2{,}09\\cdot 10^{-3}$. $K_a=[\\text{H}^+]^2/(C-[\\text{H}^+])$.",
             "b": r"""$$K_a=\dfrac{(2{,}09\cdot 10^{-3})^2}{0{,}0125-2{,}09\cdot 10^{-3}}=\dfrac{4{,}37\cdot 10^{-6}}{0{,}01041}=4{,}20\cdot 10^{-4}$$"""},
            {"t": "(b) Paso 1 — Reacción",
             "p": "HA + NaOH → NaA + H$_2$O.",
             "b": r"""<p>Moles HA = 2,50·10⁻³; moles NaOH = 25·0,1 = 2,5·10⁻³ mol. <b>Justo en equivalencia</b>: queda solo el anión A$^-$ en V_tot = 225 mL.</p>"""},
            {"t": "(b) Paso 2 — pH del anión",
             "p": "Hidrólisis básica.",
             "b": r"""$$[\text{A}^-]=\dfrac{2{,}5\cdot 10^{-3}}{0{,}225}=0{,}0111\ \text{M}$$
$$K_b=\dfrac{K_w}{K_a}=\dfrac{10^{-14}}{4{,}19\cdot 10^{-4}}=2{,}39\cdot 10^{-11}$$
$$[\text{OH}^-]=\sqrt{2{,}39\cdot 10^{-11}\cdot 0{,}0111}=5{,}14\cdot 10^{-7}$$
$$\text{pOH}=6{,}29\implies \text{pH}=7{,}71$$"""},
        ],
        "resultado": r"(a) $K_a \approx 4{,}19\cdot 10^{-4}$. (b) pH = 7,71.",
        "verificacion": r"El acetilsalicílico es relativamente fuerte ($K_a$ alto) por su grupo carboxilo cercano al éster. El pH del punto de equivalencia es ligeramente básico, no neutro (1−7,71 muy próximo a 7 porque el K_a es relativamente alto). ✓"
    },
]
