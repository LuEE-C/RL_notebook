import gym
import itertools

def space_size(space):
    if isinstance(space, gym.spaces.Discrete):
        return range(space.n)
    elif isinstance(space, gym.spaces.Tuple):
        return itertools.product(*[space_size(s) for s in space.spaces])
    else:
        raise NotImplementedError