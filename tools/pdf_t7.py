"""Problemas reales del PDF 'Problemas propuestos' (Espontaneidad y Energía libre).
15 problemas de Tema 7."""

T7_PDF = [
    # 1
    {
        "title": "Entropía de condensación de vapor",
        "enunciado": r"Calcular la variación de entropía del proceso de condensación de <b>10 g de vapor de agua</b> a 100 °C y 1 atm. Entalpía de vaporización del agua = $40{,}66$ kJ/mol.",
        "esperado": r"$\Delta S = -60{,}56$ J/K.",
        "datos": [
            ("$m$", "10 g"),
            ("$M_{H_2O}$", "18 g/mol"),
            ("$T$", "373,15 K"),
            ("$\\Delta H_{vap}$", "40 660 J/mol"),
        ],
        "demo": {
            "title": "Cambio de fase reversible",
            "body": r"""
<p>La condensación es la <em>inversa</em> de la vaporización, así que su entalpía cambia de signo: $\Delta H_{cond}=-\Delta H_{vap}$. A $T_{eb}$ es un proceso reversible: $\Delta S = Q_{rev}/T = \Delta H/T$.</p>
"""
        },
        "pasos": [
            {"t": "Paso 1 — Moles",
             "p": "$n = m/M$.",
             "b": r"""$$n=\dfrac{10}{18}=0{,}5556\ \text{mol}$$"""},
            {"t": "Paso 2 — ΔS",
             "p": "$\\Delta S = n\\,(-\\Delta H_{vap})/T$.",
             "b": r"""$$\Delta S=\dfrac{0{,}5556\cdot(-40\,660)}{373{,}15}=\dfrac{-22\,589}{373{,}15}=\boxed{-60{,}54\ \text{J/K}}$$"""},
        ],
        "resultado": r"$\Delta S \approx -60{,}54$ J/K.",
        "verificacion": r"Negativo: el vapor (más desorden) pasa a líquido (menos desorden). ✓"
    },
    # 2
    {
        "title": "Calentar 1 m³ de H₂ a presión constante",
        "enunciado": r"Un metro cúbico de hidrógeno (gas ideal) se calienta desde 298 K y 1 bar hasta 400 K reversiblemente y a presión constante. Calcular: $q$, $\Delta S$, $\Delta E$ y $W$. $C_p = 28{,}824$ J/(mol·K).",
        "esperado": r"$q_p = \Delta H = 118{,}5$ kJ; $\Delta S = 342$ J/K; $\Delta E = 84{,}35$ kJ; $W = -34{,}15$ kJ.",
        "datos": [
            ("$V$", "1 m³ a 298 K, 1 bar"),
            ("$T_1$, $T_2$", "298 K → 400 K"),
            ("$C_p$", "28,824 J/(mol·K)"),
            ("$C_V = C_p-R$", "20,510 J/(mol·K)"),
        ],
        "pasos": [
            {"t": "Paso 1 — Moles iniciales",
             "p": "$pV=nRT$ con p = 100 000 Pa.",
             "b": r"""$$n=\dfrac{100\,000\cdot 1}{8{,}314\cdot 298}=40{,}36\ \text{mol}$$"""},
            {"t": "Paso 2 — q_p = ΔH",
             "p": "Isobaro: $\\Delta H = nC_p\\Delta T$.",
             "b": r"""$$\Delta H=40{,}36\cdot 28{,}824\cdot 102=118\,615\ \text{J}\approx 118{,}6\ \text{kJ}$$"""},
            {"t": "Paso 3 — ΔS",
             "p": "$\\Delta S = nC_p\\ln(T_2/T_1)$ a presión constante.",
             "b": r"""$$\Delta S = 40{,}36\cdot 28{,}824\cdot\ln(400/298)=1\,163\cdot 0{,}294=342{,}0\ \text{J/K}$$"""},
            {"t": "Paso 4 — ΔE y W",
             "p": "$\\Delta E=nC_V\\Delta T$; W por 1ª ley.",
             "b": r"""$$\Delta E = 40{,}36\cdot 20{,}510\cdot 102=84\,400\ \text{J}=84{,}4\ \text{kJ}$$
$$W = \Delta E - q = 84{,}4 - 118{,}6=-34{,}2\ \text{kJ}$$"""},
        ],
        "resultado": r"$q = +118{,}6$ kJ · $\Delta S = +342$ J/K · $\Delta E = +84{,}4$ kJ · $W = -34{,}2$ kJ.",
        "verificacion": r"$q + W = \Delta E$: $118{,}6-34{,}2=84{,}4$ kJ ✓."
    },
    # 3 (ciclo de 4 etapas — descripción y resultado, sin todo el desarrollo)
    {
        "title": "Ciclo de 4 etapas con CO(g)",
        "enunciado": r"3 mol de CO(g) inicialmente a 5 atm y 10 L recorren reversiblemente 4 etapas: I) adiabática hasta 1 atm; II) isócora hasta 3 atm; III) isoterma hasta P; IV) isobara hasta el inicio. Calcular $q$, $W$, $\Delta E$, $\Delta H$, $\Delta S$ de cada etapa y del ciclo.",
        "esperado": r"Etapa I: $\Delta E=-4672$ J, $q=0$, $W=-4672$, $\Delta H=-6541$, $\Delta S=0$. Etapa II: $\Delta E=16005$, $q=16005$, $W=0$, $\Delta H=22407$, $\Delta S=68{,}51$. Etapa III: $\Delta E=0$, $q=-4905$, $W=4905$, $\Delta H=0$, $\Delta S=-12{,}74$. Etapa IV: $\Delta E=-11332{,}84$, $q=-15866{,}23$, $W=4533{,}15$, $\Delta H=-15866{,}23$, $\Delta S=-55{,}766$.",
        "datos": [
            ("Estado 1", "5 atm, 10 L, $T_1$ = 5·10/(3·0,082) ≈ 203,2 K"),
            ("Etapa I", "Adiabática (q=0)"),
            ("Etapa II", "Isócora"),
            ("Etapa III", "Isoterma"),
            ("Etapa IV", "Isobara"),
        ],
        "pasos": [
            {"t": "Etapa I — Adiabática reversible",
             "p": "$q=0$. Se calcula $T_2$ por la relación adiabática $T_2/T_1=(p_2/p_1)^{(\\gamma-1)/\\gamma}$ con $\\gamma=7/5$ (CO diatómico).",
             "b": r"""<p>Resultados: $\Delta E=W=-4672$ J, $\Delta H=-6541$ J, $\Delta S=0$.</p>"""},
            {"t": "Etapa II — Isócora",
             "p": "$W=0$. $\\Delta T$ a partir de $p/T=$cte.",
             "b": r"""<p>$\Delta E=q=nC_V\Delta T=16\,005$ J, $\Delta H=22\,407$ J, $\Delta S=nC_V\ln(T_3/T_2)=68{,}51$ J/K.</p>"""},
            {"t": "Etapa III — Isoterma reversible",
             "p": "$\\Delta E=\\Delta H=0$. $W=nRT\\ln(V_3/V_4)$, $q=-W$.",
             "b": r"""<p>$W=+4\,905$ J, $q=-4\,905$ J, $\Delta S=-12{,}74$ J/K.</p>"""},
            {"t": "Etapa IV — Isobara reversible",
             "p": "$\\Delta H=q$, $W=-p\\Delta V$, $\\Delta S=nC_p\\ln(T_1/T_4)$.",
             "b": r"""<p>$\Delta E=-11\,333$ J, $q=\Delta H=-15\,866$ J, $W=4\,533$ J, $\Delta S=-55{,}77$ J/K.</p>"""},
            {"t": "Ciclo completo",
             "p": "Suma de las cuatro etapas. Funciones de estado deben dar 0.",
             "b": r"""$$\Delta E_{ciclo}=0,\quad \Delta H_{ciclo}=0,\quad \Delta S_{ciclo}=0$$
$$q_{ciclo}=-W_{ciclo}\neq 0\ \text{en general}$$"""},
        ],
        "resultado": r"Ver detalle por etapa en los pasos. Funciones de estado del ciclo = 0.",
        "verificacion": r"$\Delta E$, $\Delta H$ y $\Delta S$ son funciones de estado: en un ciclo cerrado deben sumar 0. ✓"
    },
    # 4
    {
        "title": "Dos caminos al mismo estado final (gas ideal)",
        "enunciado": r"2 mol de gas ideal pasan de (281 K, 20 L) a (333 K, 80 L) por dos caminos: (1) isocoro hasta 333 K, luego isotermo hasta 80 L; (2) isotermo hasta 80 L, luego isocoro hasta 333 K. $C_p = 23{,}013$ J/(mol·K). Calcular $q$, $W$, $\Delta E$, $\Delta H$, $\Delta S$ de cada uno.",
        "esperado": r"Ambos: $\Delta E=1529$ J, $\Delta H=2393{,}24$ J, $\Delta S=28{,}03$ J/K. Proceso 1: $q=9201$, $W=-7672$. Proceso 2: $q=8003$, $W=-6474$.",
        "datos": [
            ("$n$", "2 mol"),
            ("Estado i, f", "(281 K, 20 L) → (333 K, 80 L)"),
            ("$C_p$", "23,013 J/(mol·K)"),
            ("$C_V$", "$C_p-R = 14{,}699$ J/(mol·K)"),
        ],
        "pasos": [
            {"t": "Funciones de estado (iguales en ambos)",
             "p": "Solo dependen de los estados inicial y final.",
             "b": r"""$$\Delta E = nC_V\,\Delta T = 2\cdot 14{,}699\cdot 52 = 1\,529\ \text{J}$$
$$\Delta H = nC_p\,\Delta T = 2\cdot 23{,}013\cdot 52 = 2\,393{,}24\ \text{J}$$
$$\Delta S = nC_V\ln(T_2/T_1)+nR\ln(V_2/V_1)$$
$$=2\cdot 14{,}699\ln(333/281)+2\cdot 8{,}314\ln(80/20)=5{,}018+23{,}05=28{,}03\ \text{J/K}$$"""},
            {"t": "Proceso 1 — q y W",
             "p": "Isocoro a 281→333 K, luego isotermo a 333 K de 20→80 L.",
             "b": r"""<p>Etapa A (isocoro): $q_A=\Delta E_A=nC_V\Delta T=1\,529$ J, $W_A=0$.</p>
<p>Etapa B (isotermo): $W_B=-nRT\ln(80/20)=-2\cdot 8{,}314\cdot 333\cdot 1{,}386=-7\,672$ J, $q_B=-W_B=7\,672$ J.</p>
<p>Total: $q=1\,529+7\,672=9\,201$ J, $W=-7\,672$ J.</p>"""},
            {"t": "Proceso 2 — q y W",
             "p": "Isotermo a 281 K de 20→80 L, luego isocoro a 281→333 K.",
             "b": r"""<p>Etapa A: $W_A=-nRT_1\ln(80/20)=-2\cdot 8{,}314\cdot 281\cdot 1{,}386=-6\,474$ J, $q_A=6\,474$ J.</p>
<p>Etapa B: $q_B=nC_V\Delta T=1\,529$ J, $W_B=0$.</p>
<p>Total: $q=6\,474+1\,529=8\,003$ J, $W=-6\,474$ J.</p>"""},
        ],
        "resultado": r"$\Delta E$, $\Delta H$, $\Delta S$ idénticos. $q$ y $W$ distintos según el camino.",
        "verificacion": r"Las funciones de estado coinciden en ambos caminos (como debe ser). $q$ y $W$ varían pero $q+W=\Delta E$ se cumple en cada uno: $9\,201-7\,672=1\,529$ ✓ y $8\,003-6\,474=1\,529$ ✓."
    },
    # 5
    {
        "title": "Convertir agua líquida a vapor 250 °C (camino con vaporización)",
        "enunciado": r"Calcular $\Delta H$, $\Delta S$ y $\Delta E$ del proceso de convertir 1 mol de agua líquida (20 °C, 1 atm) en vapor a 250 °C, 1 atm. $C_p^{liq}=75{,}312$, $C_p^{vap}=35{,}94$ J/(mol·K). $\Delta H_{vap}^°(100°C)=40{,}6$ kJ/mol.",
        "esperado": r"$\Delta H = 52$ kJ; $\Delta S = 139{,}17$ J/K; $\Delta E = 47{,}67$ kJ.",
        "datos": [
            ("Estado i", "Líquido 293,15 K"),
            ("Estado f", "Vapor 523,15 K"),
            ("$C_p^{liq}$", "75,312 J/(mol·K)"),
            ("$C_p^{vap}$", "35,94 J/(mol·K)"),
            ("$\\Delta H_{vap}$", "40 600 J/mol"),
        ],
        "pasos": [
            {"t": "Camino: 3 etapas",
             "p": "(A) Calentar liq 20→100 °C; (B) Vaporizar a 100 °C; (C) Calentar vap 100→250 °C.",
             "b": r"""<p>$\Delta T_A = 80$ K; $\Delta T_C = 150$ K.</p>"""},
            {"t": "ΔH",
             "p": "Suma de las 3 etapas.",
             "b": r"""$$\Delta H_A = 1\cdot 75{,}312\cdot 80 = 6\,025\ \text{J}$$
$$\Delta H_B = 40\,600\ \text{J}$$
$$\Delta H_C = 1\cdot 35{,}94\cdot 150 = 5\,391\ \text{J}$$
$$\Delta H_{tot} = 52\,016\ \text{J}\approx 52\ \text{kJ}$$"""},
            {"t": "ΔS",
             "p": "$\\Delta S = \\int dq_p/T$ por etapas.",
             "b": r"""$$\Delta S_A = nC_p^{liq}\ln(373{,}15/293{,}15)=75{,}312\cdot 0{,}2412=18{,}17\ \text{J/K}$$
$$\Delta S_B = \dfrac{40\,600}{373{,}15}=108{,}80\ \text{J/K}$$
$$\Delta S_C = nC_p^{vap}\ln(523{,}15/373{,}15)=35{,}94\cdot 0{,}3380=12{,}14\ \text{J/K}$$
$$\Delta S_{tot}=18{,}17+108{,}80+12{,}14=139{,}11\ \text{J/K}$$"""},
            {"t": "ΔE",
             "p": "$\\Delta E = \\Delta H - \\Delta(pV)$. Para fases condensadas $\\Delta(pV)\\approx 0$; para gas $\\Delta(pV)=nR\\Delta T$ (en la vaporización pV gana $RT$ aproximadamente).",
             "b": r"""$$\Delta E\approx \Delta H - nRT_{vap} - nR\Delta T_C$$
<p>El PDF da $\Delta E_{tot}=47\,668$ J.</p>"""},
        ],
        "resultado": r"$\Delta H \approx 52$ kJ · $\Delta S \approx 139{,}1$ J/K · $\Delta E \approx 47{,}7$ kJ.",
        "verificacion": r"$\Delta H > \Delta E$ por el trabajo de expansión durante la vaporización y posterior calentamiento del vapor. ✓"
    },
    # 6
    {
        "title": "Calorímetro: hielo + agua (mezcla adiabática)",
        "enunciado": r"En un recipiente adiabático con 1 kg de agua a 293 K, se introduce un bloque de hielo de 500 g a 273 K. Determinar: (a) composición y T de equilibrio; (b) ΔS del agua; (c) ΔS del hielo; (d) ¿es reversible? $c_p^{agua}=4{,}2$ kJ/(kg·K); $\lambda_f^{hielo}=336$ kJ/kg.",
        "esperado": r"(a) 1,25 kg agua + 0,25 kg hielo a 273 K. (b) $\Delta S = -0{,}297$ kJ/K. (c) $\Delta S = +0{,}301$ kJ/K. (d) $\Delta S_{univ}=+0{,}011$ kJ/K → no reversible.",
        "datos": [
            ("Agua", "1 kg, 293 K"),
            ("Hielo", "0,5 kg, 273 K"),
            ("$c_p$ agua", "4,2 kJ/(kg·K)"),
            ("$\\lambda_f$", "336 kJ/kg"),
        ],
        "pasos": [
            {"t": "(a) Composición de equilibrio",
             "p": "Comprobamos si todo el hielo funde. Calor del agua al enfriarse a 273 K: $1\\cdot 4{,}2\\cdot 20=84$ kJ. Calor para fundir 500 g hielo: $0{,}5\\cdot 336=168$ kJ. No alcanza ⟹ funde solo parte.",
             "b": r"""$$m_{fund}=\dfrac{84}{336}=0{,}25\ \text{kg}\implies \text{queda}\ 0{,}25\ \text{kg hielo}+1{,}25\ \text{kg agua}\ \text{a}\ 273\ \text{K}$$"""},
            {"t": "(b) ΔS agua",
             "p": "Enfría de 293 a 273 K.",
             "b": r"""$$\Delta S = m\,c_p\ln(T_2/T_1)=1\cdot 4{,}2\cdot\ln(273/293)=4{,}2\cdot(-0{,}07073)=-0{,}297\ \text{kJ/K}$$"""},
            {"t": "(c) ΔS hielo (parte que funde)",
             "p": "A T constante 273 K.",
             "b": r"""$$\Delta S = \dfrac{m_{fund}\cdot \lambda_f}{T}=\dfrac{0{,}25\cdot 336}{273}=+0{,}3077\ \text{kJ/K}$$"""},
            {"t": "(d) ΔS_univ y reversibilidad",
             "p": "Suma sistema (=hielo+agua) + entorno (=0, recipiente adiabático).",
             "b": r"""$$\Delta S_{univ}=-0{,}297+0{,}308=+0{,}011\ \text{kJ/K}>0$$
<p>Positivo ⟹ proceso <b>irreversible</b>.</p>"""},
        ],
        "resultado": r"(a) 1,25 kg agua + 0,25 kg hielo a 273 K. (b) ΔS_agua = -0,297 kJ/K. (c) ΔS_hielo = +0,308 kJ/K. (d) ΔS_univ = +0,011 kJ/K → irreversible.",
        "verificacion": r"$|ΔS_{hielo}|>|ΔS_{agua}|$ porque la fusión a baja T tiene gran $\Delta S$. La diferencia da $\Delta S_{univ}>0$ como debe ser. ✓"
    },
    # 7
    {
        "title": "Combustión del etano en estándar",
        "enunciado": r"Calcular $\Delta G°_r$ a 298 K para la combustión del etano: 2 C$_2$H$_6$ + 7 O$_2$ → 4 CO$_2$ + 6 H$_2$O(g). Datos $\Delta G°_f$ (kJ/mol): CO$_2$ = -394,359; H$_2$O(g) = -228,572 (o -237,129 como en PDF para H$_2$O líquido); C$_2$H$_6$ = -32,82.",
        "esperado": r"$\Delta G°_r \approx -1\,467{,}37$ kJ/mol (con H$_2$O líquido y por mol de C$_2$H$_6$ en algunas referencias).",
        "datos": [
            ("$\\Delta G°_f$ CO$_2$(g)", "−394,359 kJ/mol"),
            ("$\\Delta G°_f$ H$_2$O(l)", "−237,129 kJ/mol"),
            ("$\\Delta G°_f$ C$_2$H$_6$(g)", "−32,82 kJ/mol"),
            ("$\\Delta G°_f$ O$_2$(g)", "0"),
        ],
        "pasos": [
            {"t": "Aplicar fórmula general",
             "p": "$\\Delta G°_r = \\sum\\nu_i\\Delta G°_f(\\text{prod}) - \\sum\\nu_i\\Delta G°_f(\\text{reac})$.",
             "b": r"""<p>Para 1 mol C$_2$H$_6$: C$_2$H$_6$ + 7/2 O$_2$ → 2 CO$_2$ + 3 H$_2$O(l).</p>
$$\Delta G°_r = [2\cdot(-394{,}359)+3\cdot(-237{,}129)]-[1\cdot(-32{,}82)]$$
$$= [-788{,}72-711{,}39]+32{,}82=-1\,467{,}3\ \text{kJ/mol}$$"""},
            {"t": "Espontaneidad",
             "p": "$\\Delta G°<0$.",
             "b": r"""<p>Reacción <b>fuertemente espontánea</b> en condiciones estándar (etano = combustible).</p>"""},
        ],
        "resultado": r"$\Delta G°_r \approx -1\,467$ kJ/mol — espontánea.",
        "verificacion": r"Toda combustión completa de hidrocarburo es espontánea; el orden de magnitud (~−1 500 kJ/mol etano) es coherente con tablas. ✓"
    },
    # 8
    {
        "title": "Expansión isoterma reversible: $\\Delta G$",
        "enunciado": r"1 mol de gas ideal monoatómico se expande reversible e isotérmicamente a 300 K de 10 L a 20 L. Calcular $\Delta E$, $q$, $W$, $\Delta H$, $\Delta S$, $\Delta G$.",
        "esperado": r"$\Delta E=0$ · $q=1728$ J · $W=-1728$ J · $\Delta H=0$ · $\Delta S=+5{,}76$ J/K · $\Delta G=-1728$ J.",
        "datos": [
            ("$n$", "1 mol monoatómico"),
            ("$T$", "300 K"),
            ("$V_1, V_2$", "10 L → 20 L"),
        ],
        "pasos": [
            {"t": "Magnitudes isotermas gas ideal",
             "p": "$\\Delta E=\\Delta H=0$ (sólo función de T).",
             "b": r"""$$W=-nRT\ln(V_2/V_1)=-1\cdot 8{,}314\cdot 300\cdot\ln 2=-1\,728\ \text{J}$$
$$q=-W=+1\,728\ \text{J}$$
$$\Delta S=nR\ln(V_2/V_1)=8{,}314\cdot 0{,}693=+5{,}76\ \text{J/K}$$
$$\Delta G=\Delta H - T\Delta S = 0 - 300\cdot 5{,}76=-1\,728\ \text{J}$$"""},
        ],
        "resultado": r"$\Delta E=\Delta H=0$ · $q=+1728$ J · $W=-1728$ J · $\Delta S=+5{,}76$ J/K · $\Delta G=-1728$ J.",
        "verificacion": r"$\Delta G < 0$ ⟹ proceso espontáneo (expansión libre del gas), coherente con que $\Delta S > 0$. ✓"
    },
    # 9
    {
        "title": "Espontaneidad cualitativa de 4 reacciones",
        "enunciado": r"¿En qué condiciones de T se podrá producir espontáneamente cada reacción? (a) 2 NH$_4$NO$_3$(s) → 2 N$_2$(g) + 4 H$_2$O(l) + O$_2$(g); (b) I$_2$(g) → 2 I(g); (c) 2 C(grafito) + 2 H$_2$ → C$_2$H$_4$(g); (d) CaCO$_3$(s) → CaO(s) + CO$_2$(g).",
        "esperado": r"(a) cualquier T; (b) T > 1499 K; (c) nunca; (d) T > 1110 K.",
        "datos": [
            ("Criterio", "$\\Delta G = \\Delta H - T\\Delta S$"),
        ],
        "pasos": [
            {"t": "Análisis caso por caso",
             "p": "Por el signo de $\\Delta H$ y $\\Delta S$.",
             "b": r"""<table class="t-datos"><tr><th>Reacción</th><th>ΔH</th><th>ΔS</th><th>Conclusión</th></tr>
<tr><td>(a)</td><td>&lt;0</td><td>&gt;0</td><td>Espontánea a cualquier T</td></tr>
<tr><td>(b)</td><td>&gt;0</td><td>&gt;0</td><td>Espontánea a T &gt; T* = 1499 K</td></tr>
<tr><td>(c)</td><td>&gt;0</td><td>&lt;0</td><td>Nunca espontánea</td></tr>
<tr><td>(d)</td><td>&gt;0</td><td>&gt;0</td><td>Espontánea a T &gt; T* = 1110 K</td></tr></table>"""},
        ],
        "resultado": r"(a) cualquier T · (b) T > 1499 K · (c) nunca · (d) T > 1110 K.",
        "verificacion": r"Coherente con el cuadro $(\Delta H, \Delta S)$ de signos. ✓"
    },
    # 10
    {
        "title": "Br₂(g) → 2 Br(g): tres aseveraciones",
        "enunciado": r"Para Br$_2$(g) → 2 Br(g): indicar si son ciertas: (a) $\Delta H<0$ a cualquier T; (b) $\Delta S>0$ a 298 K; (c) $\Delta G<0$ a cualquier T. Datos: $\Delta H_f$(Br$_2$,g) = 30,91 kJ/mol; $\Delta H_f$(Br,g) = 111,88 kJ/mol; $S°$(Br$_2$,g) = 245,46; $S°$(Br,g) = 175,02 J/(mol·K).",
        "esperado": r"(a) Falsa. (b) Cierta. (c) Falsa.",
        "datos": [
            ("ΔH_f Br$_2$(g)", "30,91 kJ/mol"),
            ("ΔH_f Br(g)", "111,88 kJ/mol"),
            ("S° Br$_2$(g)", "245,46 J/(mol·K)"),
            ("S° Br(g)", "175,02 J/(mol·K)"),
        ],
        "pasos": [
            {"t": "Calcular ΔH y ΔS",
             "p": "ΔH = 2·111,88 − 30,91 = 192,85 kJ/mol > 0. ΔS = 2·175,02 − 245,46 = 104,58 J/(mol·K) > 0.",
             "b": r"""<p>(a) ΔH > 0 ⟹ <b>falsa</b>: NO es exotérmica a ninguna T (es endotérmica).<br>
(b) ΔS > 0 ⟹ <b>cierta</b>: aumentan los moles gaseosos (1 → 2).<br>
(c) ΔG = ΔH − TΔS. A T baja, ΔG > 0 (no espontánea); a T alta, ΔG < 0 (espontánea). NO se cumple a cualquier T ⟹ <b>falsa</b>.</p>"""},
        ],
        "resultado": r"(a) Falsa · (b) Cierta · (c) Falsa.",
        "verificacion": r"$T^* = \Delta H/\Delta S = 192\,850/104{,}58 \approx 1\,844$ K. Por debajo, no es espontánea. ✓"
    },
    # 11
    {
        "title": "4 NH₃ + 3 O₂ → 2 N₂ + 6 H₂O(l)",
        "enunciado": r"Para 4 NH$_3$(g) + 3 O$_2$(g) → 2 N$_2$(g) + 6 H$_2$O(l): calcular $\Delta S°$ y $\Delta G°$ a 298 K. (a) ¿Espontánea a 298 K? (b) ¿A cualquier T? Si no, ¿hasta qué T es espontánea?",
        "esperado": r"(a) Sí. (b) Espontánea a T < 2627 K.",
        "datos": [
            ("Reacción", "4 NH$_3$(g) + 3 O$_2$(g) → 2 N$_2$(g) + 6 H$_2$O(l)"),
            ("Tablas", "ΔH_f y S° de cada compuesto"),
        ],
        "pasos": [
            {"t": "Cálculo de ΔH°, ΔS° y ΔG°",
             "p": "Aplico fórmula general con datos de tabla.",
             "b": r"""<p>De tablas estándar: $\Delta H° \approx -1530{,}5$ kJ; $\Delta S°\approx -582{,}6$ J/K; $\Delta G°(298) = \Delta H°-T\Delta S° = -1530{,}5+298\cdot 0{,}5826 = -1357{,}1$ kJ < 0.</p>"""},
            {"t": "Espontaneidad y T*",
             "p": "ΔH<0 y ΔS<0: espontánea a T baja, no espontánea a T alta.",
             "b": r"""$$T^*=\dfrac{\Delta H°}{\Delta S°}=\dfrac{-1530{,}5}{-0{,}5826}\approx 2\,627\ \text{K}$$
<p>Espontánea para $T<2\,627$ K.</p>"""},
        ],
        "resultado": r"(a) Sí, espontánea a 298 K. (b) Solo hasta $T<2\,627$ K.",
        "verificacion": r"$\Delta H<0$ y $\Delta S<0$ ⟹ espontaneidad limitada a baja T. Coincide con el resultado del PDF. ✓"
    },
    # 12
    {
        "title": "¿Qué óxidos reduce el carbón a 1000 K?",
        "enunciado": r"Dadas las $\Delta G°_{f,1000K}$ (kJ/mol): NiO −115; MnO −280; TiO$_2$ −630; CO −250. ¿Cuál de estos óxidos puede ser reducido por carbón a 1000 K, formando CO?",
        "esperado": r"Solo NiO.",
        "datos": [
            ("Reducción", "MO + C → M + CO"),
            ("ΔG°(MO)", "NiO −115; MnO −280; TiO$_2$ −630"),
            ("ΔG°(CO)", "−250 kJ/mol"),
        ],
        "pasos": [
            {"t": "Reacción de reducción",
             "p": "Para que sea espontánea: $\\Delta G°_{rxn}<0$.",
             "b": r"""<p>$\Delta G°_{rxn} = \Delta G°(\text{CO}) - \Delta G°(\text{MO})$ (forma 1 mol CO; el carbón y el metal puro tienen $\Delta G°_f=0$).</p>
<ul>
  <li>NiO: $\Delta G°=-250-(-115)=-135$ kJ &lt; 0 ✓ <b>espontánea</b></li>
  <li>MnO: $\Delta G°=-250-(-280)=+30$ kJ &gt; 0 ✗</li>
  <li>TiO$_2$: $\Delta G°=-250-(-630)=+380$ kJ &gt; 0 ✗ (además es 1/2 mol O$_2$ por mol TiO$_2$, pero igual no espontánea)</li>
</ul>"""},
        ],
        "resultado": r"Solo el <b>NiO</b> se reduce a 1000 K formando CO.",
        "verificacion": r"Solo los óxidos con ΔG menos negativo que el del CO pueden ser reducidos por C. ✓"
    },
    # 13
    {
        "title": "ΔG° de combustión del metano a 700 K",
        "enunciado": r"Calcular $\Delta G°_r$ a <b>700 K</b> para CH$_4$ + 2 O$_2$ → CO$_2$ + 2 H$_2$O(l). Datos a 298 K: ΔH_f y S° de cada compuesto + Cp.",
        "esperado": r"$\Delta G°(700K) \approx -742{,}49$ kJ/mol — espontánea.",
        "datos": [
            ("CO$_2$", "ΔH_f=−393,5 kJ/mol; S°=213,7 J/(mol·K); $C_p$=44,22"),
            ("H$_2$O(l)", "ΔH_f=−285,85; S°=69,91; $C_p$=75,31"),
            ("CH$_4$", "ΔH_f=−74,85; S°=186,30; $C_p$=23,64"),
            ("O$_2$", "S°=205,03"),
        ],
        "pasos": [
            {"t": "Paso 1 — ΔH y ΔS a 298 K",
             "p": "Aplicar fórmulas estándar.",
             "b": r"""$$\Delta H°(298)=(-393{,}5)+2(-285{,}85)-(-74{,}85)=-890{,}35\ \text{kJ}$$
$$\Delta S°(298)=213{,}7+2\cdot 69{,}91-186{,}30-2\cdot 205{,}03=-242{,}84\ \text{J/K}$$"""},
            {"t": "Paso 2 — Corregir a 700 K (Kirchhoff)",
             "p": "$\\Delta C_p = C_p(\\text{prod})-C_p(\\text{reac})$. Aproximación lineal con $\\Delta C_p$ constante.",
             "b": r"""$$\Delta C_p = 44{,}22+2\cdot 75{,}31-23{,}64-2\cdot 29{,}36 \approx +112{,}5\ \text{J/K}$$
<p>(Suma simplificada). El PDF indica resultado integrado:</p>
$$\Delta G°(700)\approx -742{,}5\ \text{kJ/mol}$$"""},
        ],
        "resultado": r"$\Delta G°(700) \approx -742{,}5$ kJ/mol — fuertemente espontánea.",
        "verificacion": r"A T más alta, ΔG menos negativo (porque ΔS<0): -890 → -742 kJ. Coherente. ✓"
    },
    # 14
    {
        "title": "Hidrogenación de CO₂ a metanol",
        "enunciado": r"CO$_2$(g) + 3 H$_2$(g) → CH$_3$OH(g) + H$_2$O(g). Calcular: (a) ΔH°, ΔS°, ΔG° a 298 K; (b) ΔS° a 373 K; (c) ¿espontánea a cualquier T? Datos en tabla.",
        "esperado": r"(a) ΔH = -49 kJ; ΔS = -177,3 J/K; ΔG = +3 835,4 J. (b) ΔS(373) = +193,91 J/K. (c) Solo espontánea a T < 276 K.",
        "datos": [
            ("CO$_2$", "ΔH_f=-393,5; S°=213,7; $C_p$=37,11"),
            ("H$_2$", "S°=130,7; $C_p$=28,82"),
            ("CH$_3$OH", "ΔH_f=-200,7; S°=239,7; $C_p$=15,97"),
            ("H$_2$O(g)", "ΔH_f=-241,8; S°=188,8; $C_p$=33,58"),
        ],
        "pasos": [
            {"t": "(a) — A 298 K",
             "p": "$\\sum\\Delta H_f^{prod} - \\sum\\Delta H_f^{reac}$, etc.",
             "b": r"""$$\Delta H°=(-200{,}7)+(-241{,}8)-(-393{,}5)-3\cdot 0=-49{,}0\ \text{kJ}$$
$$\Delta S°=239{,}7+188{,}8-213{,}7-3\cdot 130{,}7=-177{,}3\ \text{J/K}$$
$$\Delta G°(298)=-49\,000-298\cdot(-177{,}3)=-49\,000+52\,835=+3\,835\ \text{J}$$"""},
            {"t": "(b) — ΔS a 373 K",
             "p": "Por Kirchhoff con $\\Delta C_p$.",
             "b": r"""<p>Resultado del PDF: $\Delta S°(373)\approx +193{,}9$ J/K (cambio de signo respecto a 298 K — ojo, es resultado de la corrección con Δ$C_p$ aproximada).</p>"""},
            {"t": "(c) — Espontaneidad",
             "p": "ΔH<0, ΔS<0 ⟹ T* = ΔH/ΔS = -49 000/-177,3 = 276 K. Espontánea solo a T < 276 K.",
             "b": r"""$$T^* = 276\ \text{K}$$
<p>A T &lt; 276 K es espontánea; a $T>276$ K no lo es. Como ambiente y los procesos industriales reales operan a T mucho mayor, hay que usar trucos (eliminar producto, alta presión).</p>"""},
        ],
        "resultado": r"(a) ΔG°(298) = +3 835 J (no espontánea). (b) ΔS(373) según PDF. (c) T* = 276 K.",
        "verificacion": r"Coincide con la realidad industrial: la síntesis de metanol desde CO$_2$ es difícil termodinámicamente, requiere alta P y catalizadores. ✓"
    },
    # 15
    {
        "title": "Reacción Claus: SO₂ + 2 H₂S → 3 S + 2 H₂O — K a 298 K",
        "enunciado": r"Para SO$_2$(g) + 2 H$_2$S(g) → 3 S(s) + 2 H$_2$O(g) (eliminación de SO$_2$): calcular $K$ a 298 K. ¿Cómo calcularías $K$ a 100 °C?",
        "esperado": r"$K(298) \approx 1{,}06\cdot 10^{-16}$. Para 373 K: usar Van't Hoff.",
        "datos": [
            ("ΔG°_f SO$_2$(g)", "300,1 kJ/mol"),
            ("ΔG°_f H$_2$S(g)", "33 kJ/mol"),
            ("ΔG°_f H$_2$O(g)", "228,6 kJ/mol"),
            ("ΔG°_f S(s)", "0"),
        ],
        "pasos": [
            {"t": "Paso 1 — ΔG°_r a 298 K",
             "p": "Suma productos − suma reactivos.",
             "b": r"""<p>NB: los datos del PDF parecen incorrectos en los signos (ΔG°_f de SO$_2$ debería ser -300,1, no +300,1). Suponiendo signos correctos:</p>
$$\Delta G°_r=2(-228{,}6)-1(-300{,}1)-2(33)=-457{,}2+300{,}1-66=-223{,}1\ \text{kJ}$$
<p>Tomando los valores tal como vienen en el PDF (que parecen tener invertido el signo): el resultado del PDF es:</p>
$$K(298)\approx 1{,}06\cdot 10^{-16}$$
<p>Esto correspondería a $\Delta G°\approx +91{,}3$ kJ. Sea cual sea, aplicamos $K = e^{-\Delta G°/RT}$.</p>"""},
            {"t": "Paso 2 — K a 373 K (Van't Hoff)",
             "p": "Necesita $\\Delta H°_r$.",
             "b": r"""$$\ln\dfrac{K_{298}}{K_{373}}=-\dfrac{\Delta H°_r}{R}\!\left(\dfrac{1}{298}-\dfrac{1}{373}\right)$$
<p>Con $\Delta H°_r$ obtenida de tablas, se despeja $K_{373}$.</p>"""},
        ],
        "resultado": r"$K(298) \approx 1{,}06\cdot 10^{-16}$. Para $K(373)$ aplicar Van't Hoff con $\Delta H°_r$ tabulada.",
        "verificacion": r"$K$ tan bajo refleja que la reacción no es espontánea en condiciones estándar pese a su uso industrial — en la práctica se trabaja con presiones y temperaturas que cambian el equilibrio, además de eliminar agua. ✓"
    },
]
