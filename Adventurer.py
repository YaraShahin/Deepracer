def reward_function(params):
    #############################################################################
    '''
    Example of using steps and progress
    '''

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 850

    # Initialize the reward with typical value
    reward = 1.0

    # Give additional reward if the car pass every 100 steps faster than expected
    if ((steps <= ((progress*TOTAL_NUM_STEPS)/100)) and all_wheels_on_track):
        reward = 50

    return float(reward)
