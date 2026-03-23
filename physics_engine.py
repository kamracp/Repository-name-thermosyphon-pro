import numpy as np

def heat_pipe_performance(Tg, Ta, pipe_dia, pipe_length):

    # geometry
    Le = pipe_length * 0.45
    area = np.pi * pipe_dia * Le

    # heat transfer coefficients
    h_e = 2000
    h_c = 4000

    # overall U
    U = 1 / (1/h_e + 1/h_c)

    deltaT = Tg - Ta

    if deltaT <= 0:
        return 0, 0

    # heat per pipe
    Q_pipe = U * area * deltaT  # W

    # heat flux
    q_flux = Q_pipe / area

    # boiling limit
    q_max = 8000

    if q_flux > q_max:
        Q_pipe = q_max * area
        q_flux = q_max

    return Q_pipe/1000, q_flux  # kW, W/m²