# Wie LLMs (Large Language Models) funktionieren

Ein **LLM** (Large Language Model) ist ein Machine-Learning-Modell, das so groß ist, dass es ein **allgemeines Sprachverständnis** und eine **allgemeine Sprachgenerierung** erreicht.

## Tokenisierung

Zuerst wird der **Input** des Users tokenisiert. Das bedeutet, dass die Eingabe in **einzelne Token** umgewandelt wird, die dann vom Modell verarbeitet werden können.

### Beispiel:

**Input:**  
_"Monarch butterflies lay eggs on"_

Die Tokenisierung könnte wie folgt aussehen:

| Token        | [Mon] | [arch] | [butterflies] | [lay] | [eggs] | [on] | [ ] |
|--------------|------|--------|---------------|-------|--------|------|-----|
| **Token IDs** | 7088 | 1417   | 110255        | 15634 | 27226  | 402  | 220 |

Jedes Token wird durch eine **Token-ID** repräsentiert, die im Modell als Eingabe dient.

---

### Erklärung:

- **Token**: Die kleinsten Einheiten, in die der Text zerlegt wird (meist Wörter, Subwörter oder Zeichen).
- **Token IDs**: Numerische Repräsentationen der Tokens, die das Modell versteht und verarbeitet.

Die Tokenisierung ist ein wesentlicher Schritt, um Text für ein LLM verständlich zu machen. Sobald der Text in Tokens zerlegt ist, kann das Modell mit den **Token-IDs** arbeiten, um die Bedeutung zu verstehen und darauf zu reagieren.
