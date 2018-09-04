import numpy as np
import matplotlib.pyplot as plt

# los datos
x = np.array(float(input('Dame los coeficientes: ')))
y = np.array(float(input('Dame los coeficientes: ')))

# Calcular ajustes para diferentes grados
sols = {}
for grado in range(1,6):
  z = np.polyfit(x, y, grado, full=True)
  sols[grado] = z

# trazar datos
plt.plot(x, y, 'o')

# trazar las curvas de ajuste
xp = np.linspace(0, 5.2, 100)
for grado, sol in sols.items():
  coefs, error, *_ = sol
  p = np.poly1d(coefs)
  plt.plot(xp, p(xp), "-", label="Gr: %s. Error %.3f" % (grado, error) )
plt.legend()
