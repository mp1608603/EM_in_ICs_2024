import matplotlib.pyplot as plt
import numpy as np

# MTTF-Werte und deren Standardabweichungen
parameter_names = [r'$w$', r'$h$', r'$\beta$', r'$A$', r'$E_a$', 'Alle \nParameter']

mttf_values = [657, 655,  658, 657, 661, 658]  # Mittelwerte der MTTF
sigma_values = [21.2, 21.3, 28.4, 31, 44.4, 60.7]  # Standardabweichungen der MTTF

# Erstellen des Fehlerbalkendiagramms
fig, ax = plt.subplots(figsize=(7, 5))

# Fehlerbalken zeichnen
ax.errorbar(parameter_names, mttf_values, yerr=sigma_values, fmt='o', color='black', 
            capsize=5, markersize=8, label='Mittelwerte mit Fehlerbalken', 
            fillstyle='none', markeredgecolor='black', markeredgewidth=2.5, elinewidth=1)

# Y-Achsenbeschriftung anpassen
ax.set_ylabel(r'$\bar{\mu} \pm \sigma$', fontsize=18) 
ax.set_xticklabels(parameter_names, fontsize=18)

# Y-Achse anpassen, um nicht bei 0 zu beginnen
lower_limit = 590  # Untere Grenze anpassen
upper_limit = 730  # Obere Grenze anpassen
ax.set_ylim(lower_limit, upper_limit)

ax.grid(axis='y')

# Zeige das Diagramm
plt.tight_layout()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
