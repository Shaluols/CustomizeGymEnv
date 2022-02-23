from gym.envs.registration import register

register(
     id='testenv-v0',
     entry_point='customEnvs.envs:myEnv',
     max_episode_steps=200,
     reward_threshold=195.0,
 )
