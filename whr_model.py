from physics_engine import heat_pipe_performance

def run_whr_model(gas_flow, air_flow, Tg_in, Ta_in, rows, cols, pipe_dia, pipe_length):

    Cp_gas = 0.24
    Cp_air = 0.241

    Tg = Tg_in
    Ta = Ta_in

    Q_total = 0
    data = []

    for r in range(rows):

        deltaT = Tg - Ta

        if deltaT < 5:
            break

        Q_pipe, q_flux = heat_pipe_performance(Tg, Ta, pipe_dia, pipe_length)

        Q_row = cols * Q_pipe

        Tg_new = Tg - (Q_row / (gas_flow * Cp_gas))
        Ta_new = Ta + (Q_row / (air_flow * Cp_air))

        data.append([r+1, Tg, Ta, deltaT, Q_pipe, q_flux])

        Tg = Tg_new
        Ta = Ta_new

        Q_total += Q_row

    return Q_total, Tg, Ta, data