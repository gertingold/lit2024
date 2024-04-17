# Einleitung

Dies ist ein MyST-Beispiel für den LinuxInfoTag 2024, in dem es allgemein um
<wiki:Linux> geht.

Beim LinuxInfoTag 2017 habe ich ein [Bild](#exponential_raccoon) gezeigt. Man kann
auf das Bild auch mit seiner Nummer verweisen: [Abb. %s](#exponential_raccoon), aber
in der Bildüberschrift steht trotzdem "Figure 1".

Im Hauptteil steht eine berühmte [Gleichung](#einstein), die die Gleichungsnummer
{numref}`einstein` besitzt.

Hier wurde die erste Beobachtung von Gravitationswellen publiziert:
@doi:10.1103/PhysRevD.93.122003

Intersphinx-Link zu einer Seite der Jupyter Book Dokumentation: [](myst:jupyterbook#publish/gh-pages)

Dieses Diagramm ist mit mermaid erstellt und stammt aus der MyST-Dokumentation:

```{mermaid}
flowchart LR
  A[Jupyter Notebook] --> C
  B[MyST Markdown] --> C
  C(mystmd) --> D{AST}
  D <--> E[LaTeX]
  E --> F[PDF]
  D --> G[Word]
  D --> H[React]
  D --> I[HTML]
  D <--> J[JATS]
```
