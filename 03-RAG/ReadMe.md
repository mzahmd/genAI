# RAG (Retrieval Augmented Generation)

RAG ist eine Methode, die es einer KI ermöglicht, temporär neues Wissen zu integrieren, um ihre Antworten zu verbessern. Ein bekanntes Beispiel für die Anwendung von RAG ist GitHub Copilot, bei dem Nutzer ihre Dateien teilen können, um die KI mit relevanten Informationen zu versorgen. 

## RAG mit Mehrfach-Interaktionen (Multiturn)

RAG ermöglicht es auch, in einer Mehrfach-Interaktions-Situation zu arbeiten, bei der die KI nicht nur auf den aktuellen Input reagiert, sondern auch auf vorherige Informationen zurückgreift. Diese Funktion verbessert die Fähigkeit der KI, in einem längeren Gespräch oder über mehrere Anfragen hinweg kohärente und kontextuell passende Antworten zu liefern

### RAG Document Ingestion (Dokumentaufnahme)

Um Dokumente zu verarbeiten und für ein RAG-System nutzbar zu machen, folgt man einem sogenannten „Ingestion Flow“. Dieser könnte folgendermaßen aussehen:

1. **PDF**: Ein PDF-Dokument wird als Ausgangspunkt verwendet.
2. **pymupdf**: Mit dieser Bibliothek wird der Text aus dem PDF extrahiert.
3. **Langchain**: Der extrahierte Text wird in kleinere Abschnitte (Chunks) unterteilt, um ihn effizient verarbeiten zu können.
4. **Azure OpenAI**: Diese Textabschnitte werden in Vektoren umgewandelt, um sie für die KI zugänglich und analysierbar zu machen.
5. **JSON**: Die Vektoren werden dann im JSON-Format gespeichert, um sie für spätere Abfragen oder die Nutzung im RAG-Prozess verfügbar zu halten.

## RAG on AzureAI Search
Zur effizienten Suche und Abfrage relevanter Textinformationen wird Azure AI Search verwendet.
Diese Lösung ist leistungsfähiger und skalierbarer als klassische Bibliotheken wie lunr (Python) und bietet:

<ul>
  <li>Semantische Suche auf Basis von Vektoren
  <li>Skalierbare Indexierung großer Textmengen
  <li>Integration mit Azure OpenAI für kontextuelle Generierung
</ul>

