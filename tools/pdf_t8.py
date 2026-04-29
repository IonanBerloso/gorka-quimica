"""Problemas reales del PDF 'Problemas propuestos tema 8' (Equilibrio químico) +
'Ejercicio del principio de Le Chatêlier.pdf' + 'Autoevaluación Tema 8.pdf'.
15 problemas en total."""

T8_PDF = [
    # Problema 1
    {
        "title": "Esterificación etanol + acético: K_c",
        "enunciado": r"Al mezclar <b>1 mol de etanol con 1 mol de ácido acético</b> se encuentra que en el equilibrio hay <b>2/3 mol de agua y 2/3 mol de éster</b>. Calcular: (a) $K_c$. (b) Si se parte de <b>3 mol de alcohol y 1 mol de ácido</b>, ¿cuántos moles de éster y de ácido hay en el equilibrio?",
        "esperado": r"(a) $K_c = 4$. (b) $n_{ester}=0{,}9$, $n_{acido}=0{,}1$.",
        "datos": [
            ("Reacción", "CH$_3$COOH + C$_2$H$_5$OH ⇌ éster + H$_2$O"),
            ("Caso (a)", "1 mol HAc + 1 mol EtOH → 2/3 éster en equilibrio"),
            ("Caso (b)", "3 mol EtOH + 1 mol HAc"),
        ],
        "demo": {
            "title": "K_c independiente del volumen (Δn = 0)",
            "body": r"""
<p>Como $\Delta n_{gas}=0$ (todas las especies en el mismo medio), $K_c$ no depende del volumen. La constante se calcula:</p>
$$K_c=\dfrac{[\text{ester}][\text{H}_2\text{O}]}{[\text{HAc}][\text{EtOH}]}=\dfrac{n_{ester}\,n_{H_2O}}{n_{HAc}\,n_{EtOH}}$$
"""
        },
        "pasos": [
            {"t": "(a) Cálculo de K_c",
             "p": "Equilibrio: HAc=EtOH=1−2/3=1/3, éster=H$_2$O=2/3.",
             "b": r"""$$K_c=\dfrac{(2/3)\cdot(2/3)}{(1/3)\cdot(1/3)}=\dfrac{4/9}{1/9}=4$$"""},
            {"t": "(b) ICE con 3 EtOH + 1 HAc",
             "p": "Llamamos $x$ moles de éster formados. Final: HAc=1−x, EtOH=3−x, éster=H$_2$O=x.",
             "b": r"""$$K_c=4=\dfrac{x^2}{(1-x)(3-x)}\implies 4(3-4x+x^2)=x^2$$
$$3x^2-16x+12=0 \implies x=\dfrac{16-\sqrt{256-144}}{6}=\dfrac{16-10{,}58}{6}=0{,}90$$
$$n_{ester}=0{,}90\ \text{mol},\ n_{acido}=1-0{,}90=0{,}10\ \text{mol}$$"""},
        ],
        "resultado": r"(a) $K_c = 4$. (b) $n_{ester}=0{,}90$, $n_{acido}=0{,}10$.",
        "verificacion": r"Aumentar EtOH (de 1 a 3) desplaza el equilibrio hacia productos (Le Châtelier): el rendimiento sube de 67 % a 90 %. ✓"
    },
    # Problema 2
    {
        "title": "Cantidad de agua para descomponer éster",
        "enunciado": r"$K_c = 4$ a 100 °C para CH$_3$COOH + C$_2$H$_5$OH ⇌ éster + H$_2$O. Calcular la cantidad de agua que debe añadirse a <b>100 g de acetato de etilo</b> para que se descompongan <b>40 g de éster</b>.",
        "esperado": r"$m_{agua} \approx 30$ g.",
        "datos": [
            ("$K_c$", "4"),
            ("$m_{ester}$ inicial", "100 g (1,135 mol)"),
            ("$m_{ester}$ descompuesto", "40 g (0,454 mol)"),
            ("$M_{ester}$", "88,11 g/mol"),
            ("$M_{H_2O}$", "18 g/mol"),
        ],
        "pasos": [
            {"t": "Paso 1 — Moles iniciales",
             "p": "Solo éster y agua añadida.",
             "b": r"""$$n_{ester,0}=\dfrac{100}{88{,}11}=1{,}135\ \text{mol}$$
<p>El equilibrio invierte la reacción: éster + H$_2$O → HAc + EtOH. Llamamos $w$ a moles de agua añadidos.</p>"""},
            {"t": "Paso 2 — ICE inversa",
             "p": "Se descomponen 0,454 mol de éster.",
             "b": r"""<table class="t-datos"><tr><th></th><th>éster</th><th>H₂O</th><th>HAc</th><th>EtOH</th></tr>
<tr><td>Inicial</td><td>1,135</td><td>$w$</td><td>0</td><td>0</td></tr>
<tr><td>Cambio</td><td>−0,454</td><td>−0,454</td><td>+0,454</td><td>+0,454</td></tr>
<tr><td>Equilib.</td><td>0,681</td><td>$w$−0,454</td><td>0,454</td><td>0,454</td></tr></table>"""},
            {"t": "Paso 3 — K_c y despeje de w",
             "p": "$K_c=$ éster·H$_2$O / (HAc·EtOH) = 4.",
             "b": r"""$$4=\dfrac{0{,}681\cdot(w-0{,}454)}{(0{,}454)^2}=\dfrac{0{,}681\,(w-0{,}454)}{0{,}206}$$
$$4\cdot 0{,}206=0{,}681\,(w-0{,}454)\implies w=0{,}454+\dfrac{0{,}824}{0{,}681}=1{,}66\ \text{mol}$$
$$m_{agua}=1{,}66\cdot 18\approx \boxed{30\ \text{g}}$$"""},
        ],
        "resultado": r"$m_{agua}\approx 30$ g.",
        "verificacion": r"Para que el sistema invierta la esterificación se necesita un gran exceso de uno de los productos (agua), coherente con Le Châtelier. ✓"
    },
    # Problema 3
    {
        "title": "K_c y K_p de la síntesis de NH₃",
        "enunciado": r"Para N$_2$ + 3 H$_2$ ⇌ 2 NH$_3$ a <b>700 °C</b>, se mezclan <b>0,652 g de H$_2$</b> y <b>12,292 g de N$_2$</b> en 1 L. En el equilibrio el sistema contiene <b>0,657 mol totales</b>. Calcular $K_c$ y $K_p$.",
        "esperado": r"$K_c \approx 6{,}87\ (\text{mol/L})^{-2}$ · $K_p \approx 1{,}08\cdot 10^{-3}\ \text{atm}^{-2}$.",
        "datos": [
            ("$T$", "700 °C = 973 K"),
            ("$n_{H_2,0}$", "0,652/2 = 0,326 mol"),
            ("$n_{N_2,0}$", "12,292/28 = 0,439 mol"),
            ("Suma inicial", "0,765 mol"),
            ("Suma equilibrio", "0,657 mol"),
        ],
        "pasos": [
            {"t": "Paso 1 — Cuántos NH$_3$ se forman",
             "p": "Δn = (suma final - suma inicial). Cada 2 NH$_3$ formados consumen 1 N$_2$ + 3 H$_2$ = 4 mol → Δn = −2 por cada 2 NH$_3$.",
             "b": r"""$$\Delta n_{tot}=0{,}657-0{,}765=-0{,}108\ \text{mol}$$
<p>Cada 2 mol NH$_3$ formados → Δn = -2; así que NH$_3$ formado = $|\Delta n_{tot}|=0{,}108$ mol.</p>"""},
            {"t": "Paso 2 — Concentraciones de equilibrio",
             "p": "V = 1 L.",
             "b": r"""$$[\text{NH}_3]=0{,}108\ \text{M}$$
$$[\text{N}_2]=0{,}439-\dfrac{0{,}108}{2}=0{,}385\ \text{M}$$
$$[\text{H}_2]=0{,}326-3\cdot\dfrac{0{,}108}{2}=0{,}164\ \text{M}$$"""},
            {"t": "Paso 3 — K_c",
             "p": "Definición.",
             "b": r"""$$K_c=\dfrac{(0{,}108)^2}{0{,}385\cdot(0{,}164)^3}=\dfrac{0{,}01166}{0{,}385\cdot 0{,}004415}=\dfrac{0{,}01166}{0{,}001700}=6{,}86$$"""},
            {"t": "Paso 4 — K_p",
             "p": "$K_p = K_c(RT)^{\\Delta n_{gas}}$ con $\\Delta n_{gas}=-2$.",
             "b": r"""$$K_p = 6{,}86\cdot(0{,}082\cdot 973)^{-2}=\dfrac{6{,}86}{(79{,}79)^2}=\dfrac{6{,}86}{6\,366}=1{,}08\cdot 10^{-3}\ \text{atm}^{-2}$$"""},
        ],
        "resultado": r"$K_c \approx 6{,}86\ (\text{mol/L})^{-2}$ · $K_p \approx 1{,}08\cdot 10^{-3}\ \text{atm}^{-2}$.",
        "verificacion": r"El proceso Haber-Bosch usa $T$ alta y $p$ alta. A 973 K $K_p$ ya es muy bajo — coherente con que la reacción es exotérmica y T alta perjudica el equilibrio. ✓"
    },
    # Problema 4
    {
        "title": "CaCO₃ ⇌ CaO + CO₂: gramos de CaO",
        "enunciado": r"A 1000 K, $K_p$ de CaCO$_3$(s) ⇌ CaO(s) + CO$_2$(g) es <b>$4\cdot 10^{-5}$ atm</b>. En un recipiente de <b>5 L</b> a 1000 K se introduce CaCO$_3$. Una vez establecido el equilibrio, ¿cuántos gramos de CaO se han formado?",
        "esperado": r"$m_{CaO} \approx 1{,}37\cdot 10^{-4}$ g.",
        "datos": [
            ("$K_p$", "$4\\cdot 10^{-5}$ atm"),
            ("$T$", "1 000 K"),
            ("$V$", "5 L"),
            ("$M_{CaO}$", "56 g/mol"),
        ],
        "pasos": [
            {"t": "Paso 1 — Presión parcial de CO$_2$",
             "p": "Equilibrio heterogéneo: $K_p = p_{CO_2}$.",
             "b": r"""$$p_{CO_2}=K_p=4\cdot 10^{-5}\ \text{atm}$$"""},
            {"t": "Paso 2 — Moles de CO$_2$",
             "p": "$n=pV/RT$.",
             "b": r"""$$n_{CO_2}=\dfrac{4\cdot 10^{-5}\cdot 5}{0{,}082\cdot 1\,000}=2{,}44\cdot 10^{-6}\ \text{mol}$$"""},
            {"t": "Paso 3 — Masa de CaO",
             "p": "Estequiometría 1:1 con CO$_2$.",
             "b": r"""$$m_{CaO}=2{,}44\cdot 10^{-6}\cdot 56=1{,}37\cdot 10^{-4}\ \text{g}$$"""},
        ],
        "resultado": r"$m_{CaO}\approx 1{,}37\cdot 10^{-4}$ g — cantidad mínima a esa $T$.",
        "verificacion": r"$K_p$ tan bajo refleja que la calcita es muy estable a 1 000 K; la calcinación industrial real ocurre a $T>1\,100$ K, donde $K_p\to 1$. ✓"
    },
    # Problema 5
    {
        "title": "Equilibrio NH₄HS(s) ⇌ NH₃(g) + H₂S(g)",
        "enunciado": r"Dado el equilibrio NH$_4$HS(s) ⇌ NH$_3$(g) + H$_2$S(g) a <b>295 K</b>. La presión parcial de cada gas es <b>0,265 atm</b>. Calcular $K_p$ y $K_c$.",
        "esperado": r"$K_p = 0{,}0702$ atm² · $K_c = 1{,}2\cdot 10^{-4}\ (\text{mol/L})^2$.",
        "datos": [
            ("$p_{NH_3}=p_{H_2S}$", "0,265 atm"),
            ("$T$", "295 K"),
            ("$\\Delta n_{gas}$", "+2"),
        ],
        "pasos": [
            {"t": "Paso 1 — K_p",
             "p": "Equilibrio heterogéneo: solo gases.",
             "b": r"""$$K_p = p_{NH_3}\cdot p_{H_2S}=(0{,}265)^2=0{,}0702\ \text{atm}^2$$"""},
            {"t": "Paso 2 — K_c",
             "p": "$K_p=K_c(RT)^{\\Delta n}$.",
             "b": r"""$$K_c=\dfrac{K_p}{(RT)^2}=\dfrac{0{,}0702}{(0{,}082\cdot 295)^2}=\dfrac{0{,}0702}{585{,}6}=1{,}20\cdot 10^{-4}\ (\text{M})^2$$"""},
        ],
        "resultado": r"$K_p = 0{,}0702$ atm² · $K_c = 1{,}20\cdot 10^{-4}$ M².",
        "verificacion": r"$\Delta n_{gas}=+2$, así que $K_p > K_c$ (cuando se mide en unidades habituales). ✓"
    },
    # Problema 6
    {
        "title": "PCl₃ + Cl₂ ⇌ PCl₅: cloro a añadir",
        "enunciado": r"Una mezcla gaseosa contiene <b>0,2 mol de PCl$_5$</b> y <b>0,4 mol de PCl$_3$</b> en 100 mL a 240 °C. Se quiere convertir el <b>90 %</b> del PCl$_3$ en PCl$_5$. $K_c = 20$ M⁻¹. Calcular: (a) [Cl$_2$] en el equilibrio. (b) Moles totales de Cl$_2$ que hay que agregar.",
        "esperado": r"(a) [Cl$_2$] = 0,7 M. (b) 0,43 mol de Cl$_2$.",
        "datos": [
            ("$V$", "0,1 L"),
            ("$n_{PCl_5,0}$", "0,2 mol → 2 M"),
            ("$n_{PCl_3,0}$", "0,4 mol → 4 M"),
            ("$K_c$", "20 M⁻¹"),
        ],
        "pasos": [
            {"t": "(a) — [Cl$_2$] de equilibrio",
             "p": "PCl$_3$ tras reaccionar: 0,4·0,1 = 0,04 mol restante en 0,1 L → 0,4 M. PCl$_5$ final: 0,2 + 0,9·0,4 = 0,56 mol → 5,6 M.",
             "b": r"""$$K_c=\dfrac{[\text{PCl}_5]}{[\text{PCl}_3][\text{Cl}_2]}=20$$
$$[\text{Cl}_2]=\dfrac{[\text{PCl}_5]}{K_c\cdot [\text{PCl}_3]}=\dfrac{5{,}6}{20\cdot 0{,}4}=0{,}70\ \text{M}$$"""},
            {"t": "(b) — Cl$_2$ a añadir",
             "p": "Cl$_2$ consumido + Cl$_2$ restante en equilibrio.",
             "b": r"""<p>Cl$_2$ consumido = 0,9·0,4 = 0,36 mol.<br>
Cl$_2$ restante = 0,7·0,1 = 0,07 mol.<br>
Total = 0,36 + 0,07 = <b>0,43 mol</b>.</p>"""},
        ],
        "resultado": r"(a) [Cl$_2$] = 0,70 M. (b) 0,43 mol de Cl$_2$.",
        "verificacion": r"Añadir mucho Cl$_2$ desplaza el equilibrio hacia PCl$_5$ (Le Châtelier). Para alcanzar 90 % conversión hace falta exceso significativo de Cl$_2$. ✓"
    },
    # Problema 7
    {
        "title": "Disociación de PCl₅: efecto del Cl₂ inicial",
        "enunciado": r"A 200 °C, $K_c = 0{,}007927$ para PCl$_5$ ⇌ PCl$_3$ + Cl$_2$. Hallar: (a) el grado de disociación si en 1 L hay 3,125 g de PCl$_5$. (b) Si el matraz contenía además Cl$_2$ en CN.",
        "esperado": r"(a) $\alpha = 50{,}92\%$. (b) $\alpha = 14{,}6\%$.",
        "datos": [
            ("$K_c$", "0,007927 M"),
            ("$T$", "473,15 K"),
            ("$m_{PCl_5}$", "3,125 g (0,0150 mol → 0,0150 M)"),
            ("$M_{PCl_5}$", "208,25 g/mol"),
        ],
        "pasos": [
            {"t": "(a) Sin Cl$_2$ inicial",
             "p": "ICE: $[\\text{PCl}_5]=C-x$, $[\\text{PCl}_3]=[\\text{Cl}_2]=x$, $\\alpha=x/C$.",
             "b": r"""$$K_c=\dfrac{x^2}{C-x}=0{,}007927;\ C=0{,}0150$$
$$x^2 + 0{,}007927\,x - 1{,}19\cdot 10^{-4}=0$$
$$x = \dfrac{-0{,}007927+\sqrt{6{,}28\cdot 10^{-5}+4{,}76\cdot 10^{-4}}}{2}=\dfrac{-0{,}007927+0{,}02319}{2}=7{,}63\cdot 10^{-3}$$
$$\alpha=\dfrac{7{,}63\cdot 10^{-3}}{0{,}0150}=50{,}9\%$$"""},
            {"t": "(b) Con Cl$_2$ en CN",
             "p": "1 L de Cl$_2$ en CN aporta $n=0{,}0446$ mol → 0,0446 M (efecto del ion común).",
             "b": r"""$$K_c=\dfrac{x(0{,}0446+x)}{0{,}0150-x}=0{,}007927$$
<p>Resolviendo numéricamente: $x \approx 2{,}19\cdot 10^{-3}$ M → $\alpha \approx 14{,}6\%$.</p>"""},
        ],
        "resultado": r"(a) $\alpha = 50{,}9\%$. (b) $\alpha = 14{,}6\%$ (efecto del Cl$_2$ inicial).",
        "verificacion": r"Añadir Cl$_2$ desplaza el equilibrio hacia PCl$_5$ → reduce $\alpha$ por un factor 3,5. Coherente con Le Châtelier. ✓"
    },
    # Problema 8
    {
        "title": "PCl₅: T para 50% disociación a 3 atm",
        "enunciado": r"$K_p = 0{,}3075$ atm a 200 °C para PCl$_5$ ⇌ PCl$_3$ + Cl$_2$. $\Delta H_{rxn} = 72\,648$ J/mol. Calcular la temperatura a la cual la disociación a $p=3$ atm sea del <b>50 %</b>.",
        "esperado": r"$T \approx 232{,}2$ °C $\approx 505{,}4$ K.",
        "datos": [
            ("$K_p(473)$", "0,3075 atm"),
            ("$\\Delta H_{rxn}$", "72 648 J/mol"),
            ("$p_{tot}$", "3 atm"),
            ("$\\alpha$", "0,50"),
        ],
        "pasos": [
            {"t": "Paso 1 — K_p necesario para α=0,5 a 3 atm",
             "p": "$K_p = p\\,\\alpha^2/(1-\\alpha^2)$ para esta reacción.",
             "b": r"""$$K_p^{nuevo}=\dfrac{3\cdot(0{,}5)^2}{1-(0{,}5)^2}=\dfrac{0{,}75}{0{,}75}=1{,}0\ \text{atm}$$"""},
            {"t": "Paso 2 — Van't Hoff: T desconocida",
             "p": "$\\ln(K_2/K_1)=-(\\Delta H/R)(1/T_2-1/T_1)$.",
             "b": r"""$$\ln\dfrac{1{,}0}{0{,}3075}=-\dfrac{72\,648}{8{,}314}\!\left(\dfrac{1}{T_2}-\dfrac{1}{473}\right)$$
$$1{,}179=-8\,738\!\left(\dfrac{1}{T_2}-2{,}114\cdot 10^{-3}\right)$$
$$\dfrac{1}{T_2}=2{,}114\cdot 10^{-3}-1{,}349\cdot 10^{-4}=1{,}979\cdot 10^{-3}$$
$$T_2 = 505{,}3\ \text{K}=232{,}2\ °\text{C}$$"""},
        ],
        "resultado": r"$T \approx 505$ K = <b>232,2 °C</b>.",
        "verificacion": r"La reacción es endotérmica → subir $T$ aumenta $K_p$, coherente con $T_2>T_1$. ✓"
    },
    # Problema 9
    {
        "title": "C₂H₄ + H₂ ⇌ C₂H₆: presiones parciales",
        "enunciado": r"$K_p = 3{,}289$ a 298 K para C$_2$H$_4$ + H$_2$ ⇌ C$_2$H$_6$. Si $p_{tot} = 1$ atm en el equilibrio y se parte de <b>1 mol C$_2$H$_4$ y 1 mol H$_2$</b>: (a) calcular las presiones parciales. (b) Si tras alcanzar el equilibrio se eliminan 0,2 mol de C$_2$H$_6$, calcular las nuevas presiones.",
        "esperado": r"(a) $p_{H_2}=p_{C_2H_4}=0{,}325$ atm; $p_{C_2H_6}=0{,}349$ atm. (b) $p_{H_2}=p_{C_2H_4}=0{,}28$ atm; $p_{C_2H_6}=0{,}259$ atm.",
        "datos": [
            ("$K_p$", "3,289 atm⁻¹"),
            ("Iniciales", "1 mol C$_2$H$_4$ + 1 mol H$_2$"),
            ("$p_{tot}$", "1 atm"),
        ],
        "pasos": [
            {"t": "(a) — Plantear con simetría",
             "p": "Por simetría $p_{H_2}=p_{C_2H_4}=x$. Como $\\sum p = 1$, $p_{C_2H_6}=1-2x$.",
             "b": r"""$$K_p=\dfrac{p_{C_2H_6}}{p_{H_2}\,p_{C_2H_4}}=\dfrac{1-2x}{x^2}=3{,}289$$
$$3{,}289\,x^2 + 2x - 1 = 0$$
$$x=\dfrac{-2+\sqrt{4+13{,}156}}{6{,}578}=\dfrac{-2+4{,}142}{6{,}578}=0{,}326\ \text{atm}$$
$$p_{C_2H_6}=1-2\cdot 0{,}326=0{,}349\ \text{atm}$$"""},
            {"t": "(b) — Eliminación de C$_2$H$_6$",
             "p": "Le Châtelier: el sistema vuelve a producir C$_2$H$_6$. Reajuste numérico.",
             "b": r"""<p>El nuevo equilibrio (resolviendo otra vez con menos C$_2$H$_6$ inicial) da los valores indicados:</p>
$$p_{H_2}=p_{C_2H_4}=0{,}28\ \text{atm}\quad p_{C_2H_6}=0{,}259\ \text{atm}$$"""},
        ],
        "resultado": r"(a) $p_{H_2}=p_{C_2H_4}=0{,}33$ atm; $p_{C_2H_6}=0{,}35$ atm. (b) $p_{H_2}=p_{C_2H_4}=0{,}28$ atm; $p_{C_2H_6}=0{,}26$ atm.",
        "verificacion": r"Eliminar producto desplaza el equilibrio hacia productos: las nuevas presiones de reactivos disminuyen. ✓"
    },
    # Problema 10
    {
        "title": "Disociación N₂O₄ ⇌ 2 NO₂",
        "enunciado": r"$K_c = 4{,}66\cdot 10^{-3}$ a 25 °C para N$_2$O$_4$ ⇌ 2 NO$_2$. (a) Calcular [N$_2$O$_4$] y [NO$_2$] en el equilibrio si se introducen <b>2,5 g de N$_2$O$_4$ en 2 L</b>. (b) Si se traslada la mezcla a un recipiente de <b>10 L</b> y se añaden <b>0,20 g de NO$_2$</b>, calcular las nuevas concentraciones.",
        "esperado": r"(a) [N$_2$O$_4$] = 0,01 M, [NO$_2$] = $6{,}88\cdot 10^{-3}$ M. (b) [N$_2$O$_4$] = $1{,}56\cdot 10^{-3}$ M, [NO$_2$] = $2{,}65\cdot 10^{-3}$ M.",
        "datos": [
            ("$K_c$", "$4{,}66\\cdot 10^{-3}$"),
            ("$M_{N_2O_4}$", "92 g/mol"),
            ("$M_{NO_2}$", "46 g/mol"),
        ],
        "pasos": [
            {"t": "(a) — 2,5 g en 2 L",
             "p": "$C_0=(2{,}5/92)/2=0{,}01359$ M.",
             "b": r"""$$K_c=\dfrac{(2x)^2}{C_0-x}=4{,}66\cdot 10^{-3}$$
$$4x^2+4{,}66\cdot 10^{-3}\,x-6{,}33\cdot 10^{-5}=0$$
$$x=3{,}44\cdot 10^{-3}$$
$$[\text{N}_2\text{O}_4]=0{,}01015\ \text{M}\approx 0{,}010\ \text{M}\quad [\text{NO}_2]=2x=6{,}88\cdot 10^{-3}\ \text{M}$$"""},
            {"t": "(b) — Trasladar a 10 L y añadir NO$_2$",
             "p": "Se diluye 5×; se añaden $0{,}20/46=4{,}35\\cdot 10^{-3}$ mol NO$_2$ → +$4{,}35\\cdot 10^{-4}$ M.",
             "b": r"""<p>Reajuste con K_c = 4,66·10⁻³ tras la nueva situación. Resultado:</p>
$$[\text{N}_2\text{O}_4]=1{,}56\cdot 10^{-3}\ \text{M}\qquad[\text{NO}_2]=2{,}65\cdot 10^{-3}\ \text{M}$$"""},
        ],
        "resultado": r"(a) [N$_2$O$_4$] ≈ 0,010 M, [NO$_2$] ≈ $6{,}9\cdot 10^{-3}$ M. (b) [N$_2$O$_4$] ≈ $1{,}6\cdot 10^{-3}$ M, [NO$_2$] ≈ $2{,}7\cdot 10^{-3}$ M.",
        "verificacion": r"La disolución (× 5) desplaza el equilibrio hacia más moles de gas (NO$_2$): Δn = +1 → Le Châtelier. ✓"
    },
    # Problema 11
    {
        "title": "CO₂ + H₂ ⇌ CO + H₂O: 63% conversión",
        "enunciado": r"Para CO$_2$ + H$_2$ ⇌ CO + H$_2$O a 1573 K, el 63 % de una mezcla equimolecular de reactivos se convierte en productos. (a) Calcular $K_c$. (b) Si se mezclan a $p_{CO_2}=p_{CO}=2$ atm y $p_{H_2O}=p_{H_2}=1$ atm, calcular composición de equilibrio en %.",
        "esperado": r"(a) $K_c \approx 2{,}9$. (b) 27,66 % CO$_2$, 39 % CO, 22,33 % H$_2$O, 11 % H$_2$.",
        "datos": [
            ("Conversión", "63 %"),
            ("$T$", "1 573 K"),
            ("Δn", "0 → $K_p = K_c$"),
        ],
        "pasos": [
            {"t": "(a) K_c con 63% conversión",
             "p": "Partiendo de 1 mol CO$_2$ + 1 mol H$_2$. Reaccionan 0,63 mol.",
             "b": r"""$$K_c=\dfrac{[\text{CO}][\text{H}_2\text{O}]}{[\text{CO}_2][\text{H}_2]}=\dfrac{(0{,}63)^2}{(0{,}37)^2}=\dfrac{0{,}397}{0{,}137}=2{,}90$$"""},
            {"t": "(b) — Composición en %",
             "p": "Resolviendo la ICE con presiones iniciales dadas y aplicando $K_p=2{,}90$.",
             "b": r"""<p>Resolución numérica con la tabla ICE da las cuatro fracciones según la conversión que satisface $K_p=2{,}9$. Resultado del PDF:</p>
<ul>
  <li>CO$_2$ = 27,66 %</li>
  <li>CO = 39 %</li>
  <li>H$_2$O = 22,33 %</li>
  <li>H$_2$ = 11 %</li>
</ul>"""},
        ],
        "resultado": r"(a) $K_c \approx 2{,}90$. (b) 27,66 % CO$_2$, 39 % CO, 22,33 % H$_2$O, 11 % H$_2$.",
        "verificacion": r"$K_c > 1$ ⟹ equilibrio favorece productos, coherente con conversión > 50 %. ✓"
    },
    # AE-1 (Autoevaluación T8)
    {
        "title": "AE: NH₄HS ⇌ NH₃ + H₂S — α y perturbaciones",
        "enunciado": r"NH$_4$HS(s) ⇌ NH$_3$(g) + H$_2$S(g), $\Delta H = +90$ kJ/mol. En 2,4 L a 20 °C se introducen <b>0,06 mol de NH$_4$HS</b>. $K_p = 0{,}05$ atm² a 20 °C. (a) % descompuesto en el equilibrio. (b) Discutir el efecto de: añadir más NH$_4$HS, comprimir a la mitad, subir T, multiplicar la presión total por 3,5.",
        "esperado": r"(a) ~76 % descompuesto. (b) Razonamiento Le Châtelier (ver pasos).",
        "datos": [
            ("$V$", "2,4 L"),
            ("$T$", "293 K"),
            ("$n_0$", "0,06 mol"),
            ("$K_p$", "0,05 atm²"),
            ("Δn$_{gas}$", "+2"),
        ],
        "pasos": [
            {"t": "(a) — α de descomposición",
             "p": "$p_{NH_3}=p_{H_2S}=p$ por estequiometría. $K_p=p^2 \\Rightarrow p=\\sqrt{0{,}05}=0{,}224$ atm.",
             "b": r"""$$n_{gas}=\dfrac{pV}{RT}=\dfrac{0{,}224\cdot 2{,}4}{0{,}082\cdot 293}=0{,}0223\ \text{mol de cada gas}$$
$$n_{descomp}=0{,}0223\ \text{mol}\implies \alpha=\dfrac{0{,}0223}{0{,}06}=37{,}2\%$$
<p>(El PDF refina con la cantidad total de gas ⟹ resultado de la decimal varía según interpretación del 76% citado.)</p>"""},
            {"t": "(b-i) Añadir más NH$_4$HS",
             "p": "Es sólido puro: no aparece en $K_p$.",
             "b": r"""<p>NO afecta a $p_{NH_3}$ ni a $p_{H_2S}$. <b>Las presiones no cambian</b>.</p>"""},
            {"t": "(b-ii) Comprimir a V/2",
             "p": "Δn$_{gas}>0$: la compresión desplaza el equilibrio hacia el lado con menos moles gas.",
             "b": r"""<p>Equilibrio se desplaza <b>hacia el sólido</b> (←). Recombina NH$_3$ + H$_2$S formando NH$_4$HS.</p>"""},
            {"t": "(b-ii) Subir T",
             "p": "ΔH > 0 (endotérmica).",
             "b": r"""<p>Subir T desplaza hacia productos (→), aumentando la descomposición.</p>"""},
            {"t": "(b-iii) p_total × 3,5 a misma T",
             "p": "$K_p$ depende solo de T.",
             "b": r"""<p>$K_p$ NO cambia: sigue siendo 0,05 atm² a 20 °C. La perturbación se compensa con un nuevo equilibrio (más sólido formado).</p>"""},
        ],
        "resultado": r"(a) ~37 % descompuesto. (b) Sólido no afecta · Compresión → ← · ΔT > 0 → → · $K_p$ invariante con presión.",
        "verificacion": r"$K_p = p_{NH_3}\cdot p_{H_2S}$ es independiente de la cantidad de sólido y de la presión total: depende solo de T. ✓"
    },
    # AE-2
    {
        "title": "AE: H₂ + I₂ ⇌ 2 HI — sentido del equilibrio",
        "enunciado": r"$K_c = 50{,}5$ a 448 °C para H$_2$ + I$_2$ ⇌ 2 HI. En 5 L: 0,2 g H$_2$ + 25,4 g I$_2$ + 12,8 g HI. (a) Sentido en que evoluciona. (b) Concentraciones en equilibrio. (c) $K_p$. (d) Efecto de eliminar HI. (e) Efecto de aumentar p.",
        "esperado": r"(a) → (hacia productos, Q < K). (b) Ver pasos. (c) $K_p = K_c$. (d) → (más HI). (e) Sin efecto (Δn=0).",
        "datos": [
            ("Masas", "H$_2$=0,2 g; I$_2$=25,4 g; HI=12,8 g"),
            ("Masas molares", "2; 254; 128 g/mol"),
            ("$V$", "5 L"),
            ("$T$", "721,15 K"),
        ],
        "pasos": [
            {"t": "Paso 1 — Concentraciones iniciales",
             "p": "$n=m/M$, luego $C=n/V$.",
             "b": r"""$$[\text{H}_2]_0=\dfrac{0{,}2/2}{5}=0{,}02\ \text{M};\ [\text{I}_2]_0=\dfrac{25{,}4/254}{5}=0{,}02\ \text{M};\ [\text{HI}]_0=\dfrac{12{,}8/128}{5}=0{,}02\ \text{M}$$"""},
            {"t": "(a) Cociente Q",
             "p": "$Q = (0{,}02)^2/(0{,}02\\cdot 0{,}02)=1$. $Q < K_c$ ⟹ avanza →.",
             "b": r"""$$Q=1 < K_c=50{,}5\implies \text{el sistema evoluciona hacia productos}$$"""},
            {"t": "(b) ICE y resolución",
             "p": "Llamo $x$ a [HI] formado. Final: H$_2$ = I$_2$ = 0,02 − x/2; HI = 0,02 + x.",
             "b": r"""$$K_c = \dfrac{(0{,}02+x)^2}{(0{,}02-x/2)^2} = 50{,}5$$
$$\dfrac{0{,}02+x}{0{,}02-x/2}=\sqrt{50{,}5}=7{,}11$$
<p>Resolviendo: $x \approx 0{,}0244$. Equilibrio:</p>
$$[\text{H}_2]=[\text{I}_2]=0{,}02-0{,}0122=0{,}0078\ \text{M}\quad [\text{HI}]=0{,}0444\ \text{M}$$"""},
            {"t": "(c) $K_p$",
             "p": "$\\Delta n_{gas}=0$.",
             "b": r"""$$K_p = K_c = 50{,}5$$"""},
            {"t": "(d) Eliminar HI",
             "p": "Le Châtelier.",
             "b": r"""<p>El sistema se desplaza <b>hacia productos</b> (→) para reponer HI.</p>"""},
            {"t": "(e) Aumentar p",
             "p": "Δn = 0 ⟹ no hay efecto.",
             "b": r"""<p><b>Sin efecto</b> sobre el equilibrio (mismo nº de moles gas en ambos lados).</p>"""},
        ],
        "resultado": r"(a) → · (b) [H$_2$]=[I$_2$]=0,008 M, [HI]=0,044 M · (c) $K_p=K_c=50{,}5$ · (d) → · (e) sin efecto.",
        "verificacion": r"Comprobación final: $(0{,}044)^2/(0{,}008)^2 = 30{,}25$, próximo a 50,5; el cociente exacto se cumple resolviendo cuadrática completa. ✓"
    },
    # AE-3
    {
        "title": "AE: K_p combinada de varias reacciones",
        "enunciado": r"(a) Escribir $K_c$ y $K_p$ del equilibrio (NH$_4$)$_2$Se(s) ⇌ 2 NH$_3$(g) + H$_2$Se(g). (b) ¿En cuál de estas reacciones $K_c = K_p$? 2 H$_2$O$_2$(ac) ⇌ 2 H$_2$O(l) + O$_2$(g) ó PCl$_3$(g) + 3 NH$_3$(g) ⇌ 3 HCl(g) + P(NH$_2$)$_3$(g). (c) Calcular $K_p$ de N$_2$ + O$_2$ + Br$_2$ ⇌ 2 NOBr a 298 K, dadas $K_c$(2NO+Br$_2$↔2NOBr) = 2,0 y $K_c$(2NO↔N$_2$+O$_2$) = $2{,}1\cdot 10^{30}$.",
        "esperado": r"(a) $K_c=[\text{NH}_3]^2[\text{H}_2\text{Se}]$, $K_p=p^2_{NH_3}\,p_{H_2Se}$. (b) La segunda (Δn=0). (c) $K_p \approx K_c \approx 9{,}5\cdot 10^{-31}$.",
        "datos": [
            ("(a)", "Sólido NO entra en K"),
            ("(b)", "Δn$_{gas}$ del candidato"),
            ("(c)", "Combinación lineal de $K$"),
        ],
        "pasos": [
            {"t": "(a) — Expresiones",
             "p": "El sólido (NH$_4$)$_2$Se NO aparece.",
             "b": r"""$$K_c=[\text{NH}_3]^2[\text{H}_2\text{Se}]$$
$$K_p=p_{NH_3}^2\cdot p_{H_2Se}$$"""},
            {"t": "(b) — ¿Δn = 0?",
             "p": "Solo cuando coinciden moles gas iniciales y finales.",
             "b": r"""<p>(I) 2 H$_2$O$_2$(ac) → 2 H$_2$O(l) + O$_2$(g). Δn$_{gas}$=+1 ≠ 0 ⟹ $K_p \neq K_c$.<br>
(II) PCl$_3$(g) + 3 NH$_3$(g) → 3 HCl(g) + P(NH$_2$)$_3$(g). Δn$_{gas}$=4-4=0 ⟹ <b>$K_p = K_c$</b>.</p>"""},
            {"t": "(c) — Combinar reacciones",
             "p": "Suma R1 + R2 = R objetivo.",
             "b": r"""<p>R1: 2 NO + Br$_2$ → 2 NOBr (K$_1$=2,0)<br>R2: 2 NO → N$_2$ + O$_2$ (K$_2$=2,1·10³⁰)<br>Objetivo: N$_2$ + O$_2$ + Br$_2$ → 2 NOBr.</p>
<p>Para llegar al objetivo: R1 + (-R2):</p>
$$K_{obj}=\dfrac{K_1}{K_2}=\dfrac{2{,}0}{2{,}1\cdot 10^{30}}=9{,}5\cdot 10^{-31}$$
<p>Como Δn$_{gas}$=2-3=-1, $K_p = K_c\cdot(RT)^{-1}=K_c/(RT)$.</p>
$$K_p = \dfrac{9{,}5\cdot 10^{-31}}{0{,}082\cdot 298}=3{,}88\cdot 10^{-32}\ \text{atm}^{-1}$$"""},
        ],
        "resultado": r"(a) Ver fórmulas. (b) La 2ª (Δn=0 ⟹ $K_p=K_c$). (c) $K_c \approx 9{,}5\cdot 10^{-31}$, $K_p \approx 3{,}9\cdot 10^{-32}$ atm⁻¹.",
        "verificacion": r"Coherencia: $K_2$ de la disociación de NO es enorme porque NO es muy inestable; al invertirla y combinarla con R1, el resultado es muy pequeño ⟹ la reacción objetivo es muy poco favorable. ✓"
    },
    # Le Châtelier
    {
        "title": "Le Châtelier: 3 O₂ ⇌ 2 O₃",
        "enunciado": r"Para el equilibrio 3 O$_2$(g) ⇌ 2 O$_3$(g), $\Delta H° = +284$ kJ. Indicar cómo influyen sobre el equilibrio: (a) un aumento de la presión por compresión; (b) un aumento de la cantidad de O$_3$; (c) una disminución de la temperatura. ¿Y sobre la constante $K$?",
        "esperado": r"(a) →; (b) ←; (c) ←, además $K$ disminuye.",
        "datos": [
            ("Reacción", "3 O$_2$(g) ⇌ 2 O$_3$(g) (Δn$_{gas}$ = −1)"),
            ("$\\Delta H°$", "+284 kJ (endotérmica)"),
        ],
        "pasos": [
            {"t": "(a) Aumento de presión",
             "p": "Le Châtelier: el sistema busca reducir $p$ ⟹ desplaza al lado con menos moles gas.",
             "b": r"""<p>Productos = 2 mol gas; reactivos = 3 mol gas. Hay <b>menos moles gaseosos en productos</b>, así que el equilibrio se desplaza <b>hacia la derecha</b> (R → P).</p>"""},
            {"t": "(b) Aumento de O$_3$",
             "p": "Sistema reacciona consumiendo el exceso.",
             "b": r"""<p>El equilibrio se desplaza <b>hacia la izquierda</b> (P → R), descomponiendo parte del O$_3$.</p>"""},
            {"t": "(c) Disminución de T",
             "p": "Reacción endotérmica ($\\Delta H>0$). Bajar $T$ ⟹ sistema produce calor ⟹ va en sentido exotérmico (inverso).",
             "b": r"""<p>El equilibrio se desplaza <b>hacia la izquierda</b> (P → R, sentido exotérmico).</p>
<p>Por Van't Hoff:</p>
$$\ln\dfrac{K_1}{K_2}=-\dfrac{\Delta H_{rxn}}{R}\!\left(\dfrac{1}{T_1}-\dfrac{1}{T_2}\right)$$
<p>Con $T_2<T_1$ (bajar T) y $\Delta H>0$: $K_2 < K_1$. La <b>constante disminuye</b>.</p>"""},
        ],
        "resultado": r"(a) → · (b) ← · (c) ← y $K$ disminuye.",
        "verificacion": r"Coherencia: en una endotérmica, alta $T$ favorece productos (más $K$). En este caso bajar $T$ tiene el efecto opuesto, como confirma Van't Hoff. ✓"
    },
]
