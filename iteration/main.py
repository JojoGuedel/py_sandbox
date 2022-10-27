t_kal = 25.4
m_w = 0.1195
c_w = 4182
m_kal_w = 0.0176

t_end = 36.1
m_cu = 0.0104

t_cu = 1000

# t_kal = 25.7
# m_w = 0.0864
# c_w = 4182
# m_kal_w = 0.0176

# t_end = 48.1
# m_cu = 0.0262

# t_cu = 1000

def c_cu(t):
    return (99/580) * t + 383-(99/299)

def f1(x):
    return (c_w * (m_kal_w + m_w) * (t_end - t_kal)) / (((c_cu(x) + c_cu(t_end)/2)) * m_cu) + t_end

for i in range(40):
    t_cu = f1(t_cu)
    print(t_cu)