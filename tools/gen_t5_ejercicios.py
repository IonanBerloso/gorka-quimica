"""
Regenera ejercicios/tema5.html añadiendo los 7 extras al final de los 3 originales,
sin tocar teoria/tema5.html (ya manual).
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from gen_content import render_ejercicios, EJ
from ejercicios_extra import EJERCICIOS_EXTRA

# 3 ejercicios originales de T5 (mismos que ya están en tema5.html actual).
T5_BASE = {
    "titulo": "Termodinámica química",
    "subtitulo": "Trabajo · Calor · 1ª Ley · Procesos en gases ideales · Entalpía con cambio de fase",
    "ej": [
        {
            "title": "Trabajo de compresión y variación de energía interna",
            "enunciado": r"El trabajo realizado cuando se comprime un gas en un cilindro es de <b>450 J</b>. Durante este proceso hay transferencia de calor de <b>125 J</b> del gas hacia el entorno. Calcular el cambio de energía interna en este proceso.",
            "esperado": r"$\Delta U = 325\ \text{J}$.",
            "datos": [
                ("Trabajo realizado <em>sobre</em> el gas", "$+450\\ \\text{J}$"),
                ("Calor cedido al entorno", "$-125\\ \\text{J}$"),
            ],
            "demo": {
                "title": r"De dónde sale $\Delta U = Q + W$",
                "body": r"""
<p>La <b>1ª ley de la termodinámica</b> es el principio de conservación de la energía aplicado a un sistema. La variación de energía interna es la suma de la energía intercambiada como calor y como trabajo:</p>
$$\Delta U = Q + W$$
<p>Físicamente: si entra calor ($Q>0$) o se hace trabajo sobre el gas ($W>0$), su energía interna aumenta. Si sale calor o el gas hace trabajo expandiéndose, $U$ disminuye.</p>
"""
            },
            "pasos": [
                {"t": "Paso 1 — Asignar signos según el convenio",
                 "p": "El enunciado dice 'se comprime el gas' → el entorno hace trabajo sobre el sistema → $W>0$. 'El gas cede calor al entorno' → sale calor del sistema → $Q<0$.",
                 "b": r"""$$W = +450\ \text{J}\qquad Q = -125\ \text{J}$$"""},
                {"t": "Paso 2 — Aplicar la 1ª ley",
                 "p": "Sustitución directa.",
                 "b": r"""$$\Delta U = Q + W = -125 + 450 = \boxed{+325\ \text{J}}$$"""},
            ],
            "resultado": r"$\Delta U = +325\ \text{J}$ (la energía interna del gas aumenta).",
            "verificacion": r"Coherencia física: el trabajo de compresión (450 J) entrega energía al gas. Una parte se pierde como calor al entorno (125 J). El resto se almacena en el gas como aumento de su energía interna: $450 - 125 = 325\ \text{J}$. ✓"
        },
        {
            "title": "Compresión isoterma reversible de un gas ideal",
            "enunciado": r"Dos moles de helio gas, inicialmente a <b>1 atm y 300 K</b>, se comprimen <b>reversible e isotérmicamente</b> hasta una presión de <b>4 atm</b>. Calcular el trabajo y calor intercambiados y la variación de energía interna del proceso, suponiendo que se comporta como gas ideal.",
            "esperado": r"$W=6\,912{,}06\ \text{J}$, $Q=-6\,912{,}06\ \text{J}$, $\Delta U=0$.",
            "datos": [
                ("Moles", "$n=2\\ \\text{mol}$"),
                ("Presión inicial", "$p_1=1\\ \\text{atm}$"),
                ("Presión final", "$p_2=4\\ \\text{atm}$"),
                ("Temperatura (constante)", "$T=300\\ \\text{K}$"),
                ("Constante $R$", "$8{,}314\\ \\text{J/(mol·K)}$"),
            ],
            "demo": {
                "title": "Trabajo en proceso isotermo reversible",
                "body": r"""
<p>El trabajo de compresión-expansión sobre un gas se define como:</p>
$$W = -\int_{V_1}^{V_2} p_{ext}\,dV$$
<p>En un proceso <b>reversible</b>, la presión externa coincide con la del gas: $p_{ext}=p_{gas}$. Como además es <b>isotermo</b> y se trata de gas ideal, $pV = nRT$ con $T$ constante, entonces $p = nRT/V$.</p>
<p class="step"><b>🟧 Paso 1</b> — Sustituir en la integral:</p>
$$W = -\int_{V_1}^{V_2}\!\dfrac{nRT}{V}\,dV = -nRT\!\int_{V_1}^{V_2}\!\dfrac{dV}{V} = -nRT\,\ln\!\dfrac{V_2}{V_1}$$
<p class="step"><b>🟧 Paso 2</b> — Como $T$ = cte, por Boyle $p_1V_1 = p_2V_2 \Rightarrow V_2/V_1 = p_1/p_2$. Sustituyendo:</p>
$$\boxed{\;W = -nRT\,\ln\!\dfrac{p_1}{p_2} = nRT\,\ln\!\dfrac{p_2}{p_1}\;}$$
<p class="step"><b>🟧 Paso 3</b> — Como $\Delta T=0$ en gas ideal, $\Delta U = nC_V\Delta T = 0$. Por la 1ª ley, $Q = -W$.</p>
"""
            },
            "pasos": [
                {"t": "Paso 1 — Cálculo del trabajo",
                 "p": "Aplico la fórmula demostrada con los datos: $p_2/p_1 = 4/1 = 4$.",
                 "b": r"""$$W = nRT\,\ln\!\dfrac{p_2}{p_1} = 2\cdot 8{,}314\cdot 300\cdot\ln 4$$
$$W = 4\,988{,}4\cdot 1{,}3863 = \boxed{+6\,912{,}06\ \text{J}}$$
<p>El signo es positivo: se hace trabajo <em>sobre</em> el gas (compresión).</p>"""},
                {"t": "Paso 2 — Variación de energía interna",
                 "p": "Para un gas ideal, $U$ depende solo de $T$. Como $\\Delta T = 0$.",
                 "b": r"""$$\Delta U = nC_V\,\Delta T = 0 \implies \boxed{\Delta U = 0}$$"""},
                {"t": "Paso 3 — Calor intercambiado (1ª ley)",
                 "p": "Despejando de $\\Delta U = Q + W$.",
                 "b": r"""$$Q = \Delta U - W = 0 - 6\,912{,}06 = \boxed{-6\,912{,}06\ \text{J}}$$
<p>El signo negativo indica que el gas <b>cede</b> calor al entorno. Tiene sentido: al comprimir un gas isotérmicamente, el trabajo entregado se evacua íntegro como calor para que la temperatura no suba.</p>"""},
            ],
            "resultado": r"$W = +6\,912{,}06\ \text{J}$ · $Q = -6\,912{,}06\ \text{J}$ · $\Delta U = 0$.",
            "verificacion": r"Comprobación de la 1ª ley: $\Delta U = Q + W = -6\,912 + 6\,912 = 0$ ✓. Coherencia física del isotermo de gas ideal: $\Delta U = 0 \Rightarrow Q = -W$ exactamente. Todo el trabajo entregado se transfiere al entorno como calor para mantener $T$ constante."
        },
        {
            "title": "Calor para calentar agua líquida (entalpía isobárica)",
            "enunciado": r"Se eleva la temperatura de <b>100 g</b> de agua líquida de <b>20 °C a 100 °C</b> a presión atmosférica. Calcular la variación de entalpía del proceso, sabiendo que la capacidad calorífica del agua líquida es $C_p = 75{,}31\ \text{J·K}^{-1}\text{mol}^{-1}$.",
            "esperado": r"$\Delta H = 33{,}44\ \text{kJ}$.",
            "datos": [
                ("Masa de agua", "$m=100\\ \\text{g}$"),
                ("Masa molar del agua", "$M=18\\ \\text{g/mol}$"),
                ("$T_1$, $T_2$", "$20\\ °\\text{C} \\to 100\\ °\\text{C}$"),
                ("Capacidad calorífica molar", "$C_p = 75{,}31\\ \\text{J/(mol·K)}$"),
                ("Presión", "$p = $ cte (atmosférica)"),
            ],
            "demo": {
                "title": r"Por qué $\Delta H = nC_p\Delta T$ a presión constante",
                "body": r"""
<p>La entalpía se define como $H = U + pV$. Diferenciando: $dH = dU + p\,dV + V\,dp$.</p>
<p>A <b>presión constante</b>, $V\,dp = 0$. Combinando con la 1ª ley ($dU = \delta Q + \delta W$ y $\delta W = -p\,dV$):</p>
$$dH = \delta Q + (-p\,dV) + p\,dV = \delta Q_p$$
<p>Por tanto, $\Delta H = Q_p$. Y como $\delta Q_p = nC_p\,dT$ (definición de $C_p$):</p>
$$\boxed{\;\Delta H = n\!\int_{T_1}^{T_2}\!C_p\,dT = nC_p\,\Delta T\;\;\text{(si }C_p=\text{cte)}\;}$$
"""
            },
            "pasos": [
                {"t": "Paso 1 — Calcular el número de moles",
                 "p": "$n=m/M$.",
                 "b": r"""$$n = \dfrac{m}{M} = \dfrac{100\ \text{g}}{18\ \text{g/mol}} = 5{,}556\ \text{mol}$$"""},
                {"t": "Paso 2 — Calcular $\\Delta T$",
                 "p": "$\\Delta T$ en kelvin coincide con $\\Delta T$ en grados Celsius (la diferencia es 273,15 que se cancela).",
                 "b": r"""$$\Delta T = 100 - 20 = 80\ \text{K}$$"""},
                {"t": "Paso 3 — Aplicar $\\Delta H = nC_p\\,\\Delta T$",
                 "p": "Sustitución directa.",
                 "b": r"""$$\Delta H = 5{,}556\cdot 75{,}31\cdot 80 = 33\,475\ \text{J}$$
$$\boxed{\;\Delta H \approx 33{,}44\ \text{kJ}\;}$$"""},
            ],
            "resultado": r"$\Delta H = 33{,}44\ \text{kJ}$ (proceso endotérmico — el agua absorbe calor).",
            "verificacion": r"Comprobación rápida con la capacidad calorífica específica del agua: $c = 4{,}18\ \text{J/(g·K)}$. $Q = m\,c\,\Delta T = 100\cdot 4{,}18\cdot 80 = 33\,440\ \text{J} = 33{,}44\ \text{kJ}$ ✓ — coincide. Los dos enfoques (molar y específico) son equivalentes mientras se respeten las unidades."
        },
    ],
}

if __name__ == "__main__":
    out = render_ejercicios(5, T5_BASE)
    path = EJ / "tema5.html"
    path.write_text(out, encoding="utf-8")
    total = len(T5_BASE["ej"]) + len(EJERCICIOS_EXTRA.get(5, []))
    print(f"  · ejercicios/tema5.html ({total} ejercicios)")
