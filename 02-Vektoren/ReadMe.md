# Vektoren

Vektoreinbettungen stellen Eingaben so dar, dass Computer sie einfacher verarbeiten können: als Listen von Zahlen.

- Das Ziel einer Einbettung ist es, die Bedeutung der Eingabe zu erfassen.
- Sobald die Bedeutung in numerischer Form erfasst ist, können Computer auf der Grundlage dieser Bedeutungen suchen.

### Beispiel

A big Dog =>  `[0.017198, -0.007493, -0.057982, …]`

## Vektor-Einbettungsmodelle

Ein Vektor-Einbettungsmodell wird speziell darauf trainiert, Eingaben in einen Vektor umzuwandeln. Hierbei kommen riesige Trainingsdatensätze und ähnliche Architekturen wie bei großen Sprachmodellen (LLMs) zum Einsatz.

### Beispiel:

**Eingabe:** "A big dog"  
**Vektor (nach Modell):**  
`[0.052703, -0.028099, 4.963873, …]`

**Eingabe:** "A small cat"  
**Vektor (nach Modell):**  
`[0.009188, -0.035375, -0.00924, …]`
