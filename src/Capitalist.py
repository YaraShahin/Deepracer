def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    #Boolean,  flag to indicate if the agent is on the track
    all_wheels_on_track = params['all_wheels_on_track']
    #float, distance in meters from the track center
    distance_from_center = params['distance_from_center'] 
    #Boolean, Flag to indicate if the agent is left side to track center
    is_left_of_center = params['is_left_of_center']
    #Boolean, Boolean flag to indicate whether the agent has gone off track.
    is_offtrack = params['is_offtrack']
    #Boolean, flag to indicate if the agent is driving CW (T) or CCW (F).
    is_reversed = params['is_reversed']
    #float, agent's yaw in degrees
    heading = params['heading']
    #float, percentage of track completed
    progress = params['progress']
    #float, agent's speed in meters per second (m/s)
    speed = params['speed']
    #float, agent's steering angle in degrees
    steering_angle = params['steering_angle']
    #int, number steps completed
    steps = params['steps']
    #float, track length in meters.
    track_length = params['track_length']
    #float, width of the track
    track_width = params['track_width']
    
    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if (not all_wheels_on_track):
        reward = 1e-3
    else:
        reward = 2
        if (not is_left_of_center):
            reward += 0.5
        if (abs(steering_angle)>20):
            reward -= 0.1

    # Always return a float value
    return float(reward)
