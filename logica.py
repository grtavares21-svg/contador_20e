
VALOR= 20
OBJETIVO =450

def calcular_metricas(guardados):
    faltam = OBJETIVO - guardados
    total_guardado = guardados * VALOR
    total_falta = faltam * VALOR
    percent = guardados/ OBJETIVO if OBJETIVO > 0 else 0 

    return {
        'faltam':faltam,
        'total_guardado':total_guardado,
        'total_falta':total_falta,
        'percent':percent,
        'objetivo_total':VALOR *OBJETIVO

    }