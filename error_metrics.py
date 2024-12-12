def calculate_mse(m, b, data_points):
    m_delta = 0
    b_delta = 0
    error = 0
    for p in data_points:
        m_delta += 2 * (p.pos[1] - m*p.pos[0]-b) * (-p.pos[0])
        b_delta += 2 * (p.pos[1] - m*p.pos[0]-b) * (-1)
        error += (p.pos[1] - m*p.pos[0]-b) * (p.pos[1] - m*p.pos[0]-b)
    m_delta /= len(data_points)
    b_delta /= len(data_points)
    error /= len(data_points) 
    return [m_delta, b_delta, error]
