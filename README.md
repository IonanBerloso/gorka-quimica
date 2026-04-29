# Química · Gorka · 2025-26

Apuntes, ejercicios y exámenes resueltos de **Química** (1º Grado).

> Proyecto inspirado en [upv-ehu-project](https://github.com/IonanBerloso/upv-ehu-project) pero independiente,
> con paleta azul/violeta para diferenciar las dos asignaturas.

## 🌐 Web

Hosted en GitHub Pages — instalable como app (PWA).

## 📚 Temario

1. Conceptos generales
2. Estructura atómica
3. Enlace químico (iónico, covalente, intermoleculares)
4. Estados de la materia (sólido, líquido, gaseoso, cambios de estado)
5. Termodinámica química
6. Termoquímica
7. Espontaneidad y energía libre
8. Cinética y equilibrio químico
9. Equilibrio ácido-base

## 🛠️ Estructura

```
gorka-quimica/
├── index.html               ← Command center (landing)
├── formulario.html          ← Chuleta de fórmulas y constantes
├── manifest.json + sw.js    ← PWA instalable
├── shared/quimica.css       ← Estilo común (paleta azul/violeta)
├── teoria/                  ← Apuntes resumidos por tema
│   ├── tema1.html ... tema9.html
├── ejercicios/              ← Problemas resueltos paso a paso
│   ├── index.html (hub)
│   └── tema5.html (ejemplo completo con 3 problemas)
├── examenes/                ← Controles y autoevaluaciones (próximamente)
├── icons/                   ← PNG/SVG para PWA
└── tools/                   ← Scripts de generación
```

## ✍️ Convenciones

- **Constantes**: $R = 8{,}314\ \text{J/(mol·K)} = 0{,}082\ \text{atm·L/(mol·K)}$, $g = 9{,}8\ \text{m/s}^2$.
- **Notación**: coma decimal, KaTeX para fórmulas.
- **Cada ejercicio resuelto** incluye: enunciado, datos, demostración (de dónde sale cada fórmula), resolución paso a paso con "¿Por qué?" en cada paso, y verificación final.

## 📦 Instalación local

```bash
# Servidor estático sencillo
cd gorka-quimica
python -m http.server 8000
# Abrir http://localhost:8000
```

Como PWA: abrir en Chrome/Edge → menú → "Instalar Química".

## 🤝 Créditos

Hecho con ☕ por **Ionan** para **Gorka**.
