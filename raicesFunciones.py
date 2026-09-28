"""
Módulo raicesFunciones.py
Contiene el método de bisección para encontrar raíces de funciones.
"""


def biseccion(f, xi, xf, eamax):
    """
    Método de bisección para resolver f(x) = 0.
    
    Parámetros:
    -----------
    f     : function
        Función en la forma y = f(x)
    xi    : float
        Extremo izquierdo del intervalo
    xf    : float
        Extremo derecho del intervalo
    eamax : float
        Error aproximado máximo permitido (en porcentaje)
    
    Retorna:
    --------
    xr    : float
        Aproximación de la raíz encontrada
    
    Levanta:
    --------
    ValueError : Si la función no cambia de signo en [xi, xf]
    """
    
    # Verificar si los extremos son raíces
    if f(xi) == 0:
        return xi
    if f(xf) == 0:
        return xf
    
    # Verificar que la función cambie de signo
    if f(xi) * f(xf) > 0:
        raise ValueError("Error: La función debe cambiar de signo en el intervalo [xi, xf]")
    
    # Inicializar
    xr = (xi + xf) / 2.0
    ea = float("inf")
    iteraciones = 0
    
    # Iteración del método
    while ea > eamax:
        yi = f(xi)
        yr = f(xr)
        
        # Determinar en cuál subintervalo está la raíz
        if yi * yr < 0:
            xf = xr  # La raíz está en [xi, xr]
        elif yi * yr > 0:
            xi = xr  # La raíz está en [xr, xf]
        else:
            return xr  # xr es la raíz exacta
        
        # Calcular nuevo xr
        xant = xr
        xr = (xi + xf) / 2.0
        
        # Calcular error aproximado
        ea = abs((xr - xant) / xr) * 100
        iteraciones += 1
        
        # Protección contra ciclos infinitos
        if iteraciones > 10000:
            raise RuntimeError("El método no converge después de 10000 iteraciones")
    
    return xr
