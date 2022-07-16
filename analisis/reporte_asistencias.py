import pandas as pd
import matplotlib.pyplot as ptl

est = pd.read_csv("../datos/estudiante.csv", sep=",")
asis = pd.read_csv("../datos/asistencia.csv", sep=",")

asistencias_totales = pd.merge(est, asis, how = "outer", left_index = True, right_index = True )
print(asistencias_totales)

asistencias_totales = pd.merge(est, asis, left_on='cedula', right_on='1100203040')
asistencias_totales.to_csv('reporte_1100203040.csv', sep=",")

ptl.plot(asistencias_totales['primer_apellido'], asistencias_totales['java'])
ptl.show()