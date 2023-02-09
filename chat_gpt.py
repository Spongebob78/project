import math

def collision_speed(mass1, vel1, mass2, vel2):
    return (2 * mass2 * vel2 + vel1 * (mass1 - mass2)) / (mass1 + mass2), (2 * mass1 * vel1 + vel2 * (mass2 - mass1)) / (mass1 + mass2)

def wall_collision_speed(mass, vel, elasticity):
    return -elasticity * vel

def simulate_collision(pos1, vel1, pos2, vel2, mass1, mass2, elasticity, box_size):
    x1, y1 = pos1
    x2, y2 = pos2
    vx1, vy1 = vel1
    vx2, vy2 = vel2

    # Check if balls are colliding
    delta_x = x2 - x1
    delta_y = y2 - y1
    delta_vx = vx2 - vx1
    delta_vy = vy2 - vy1
    delta_v_squared = delta_vx**2 + delta_vy**2
    delta_v_distance = math.sqrt(delta_x**2 + delta_y**2)
    
    if delta_v_squared > 0 and delta_v_distance < (mass1 + mass2):
        # Calculate new velocities after collision
        vx1, vx2 = collision_speed(mass1, vx1, mass2, vx2)
        vy1, vy2 = collision_speed(mass1, vy1, mass2, vy2)
        
    # Check if ball is colliding with wall
    if x1 + mass1 >= box_size:
        vx1 = wall_collision_speed(mass1, vx1, elasticity)
    if x1 - mass1 <= 0:
        vx1 = -wall_collision_speed(mass1, vx1, elasticity)
    if y1 + mass1 >= box_size:
        vy1 = wall_collision_speed(mass1, vy1, elasticity)
    if y1 - mass1 <= 0:
        vy1 = -wall_collision_speed(mass1, vy1, elasticity)
        
    if x2 + mass2 >= box_size:
        vx2 = wall_collision_speed(mass2, vx2, elasticity)
    if x2 - mass2 <= 0:
        vx2 = -wall_collision_speed(mass2, vx2, elasticity)
    if y2 + mass2 >= box_size:
        vy2 = wall_collision_speed(mass2, vy2, elasticity)
    if y2 - mass2 <= 0:
        vy2 = -wall_collision_speed(mass2, vy2, elasticity)
        
    return (x1 + vx1, y1 + vy1), (vx1, vy1), (x2 + vx2, y2 + vy2), (vx2, vy2)