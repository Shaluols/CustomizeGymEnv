# Build custom gym environment 
In this repository, we will guide you to build a basic gym framework for your own environment and install it as a package in the local system. 
We tested it on Ubuntu 20.04 with python 3.8.
## Install gym
You can install it with pip (if your default phthon is phthon2, use pip3)
```
pip install gym # or pip3
```
You can also download the source and build gym from source:
```commandline
git clone https://github.com/openai/gym
cd gym
pip3 install -e . # if there is a permission problem, try to add --user before -e
```
If you prefer to install all of the gym environments, you can do:
```commandline
pip3 install -e .[all]
```
You can test if the installation succeed by:
```commandline
python3
import gym
env = gym.make('CartPole-v0')
```
## Create the framework
Create folders and empty files following the structure:

```commandline
├── myGymEnvs
│   ├── README.md
│   ├── setup.py
│   ├── customEnvs
│   │   ├── envs
│   │   │   ├── __init__.py
│   │   │   ├── testEnv.py
│   │   ├── __init__.py
```

### myGymEnvs/setup.py
Specify the required packages needed to execute the package.
```commandline
from setuptools import setup

setup(name='myGymEnvs', # name of your package
  version='1.0',
  install_requires=['gym']  # And any other dependencies Env needs
  )
```
### myGymEnvs/customEnvs/__init__.py
Register your environment in gym library
```commandline
from gym.envs.registration import register

register(
     id='testenv-v0', # use this id to index/invoke the environment in training and testing
     entry_point='customEnvs.envs:myEnv', # customEnvs.envs is the folder directory to the file that contains the myEnv class
     max_episode_steps=200,
     reward_threshold=195.0,
 )
```

### myGymEnvs/customEnvs/envs/testEnv.py
You can define the basic RL functions in this file, for example: reset, step, reward.  
```commandline
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

class myEnv(gym.Env):
    def __init__(self):
        return None

    def seed(self, seed=None):
        return None

    def step(self, action):
        return None
    def reset(self):
        return None
```
### myGymEnvs/customEnvs/envs/__init__.py
To enable your environment to be imported correctly, you need to add the following command into the __init__.py file.
```commandline
from customEnvs.envs.testEnv import myEnv
```

## Install your environment
In order to install the created folder structure as a package in your local system, 
you can navigate to the folder myGymEnvs, run:
```commandline
pip3 install -e .
```

## Test
```commandline
import gym 
import customEnvs
env = gym.make('testenv-v0')
```
If you encounter an error about: "module 'customEnvs.envs' has no attribute 'myEnv'", please check the __init__.py file under the envs folder to see if it is empty. Make sure you import the environment myEnv in the initialization file. 
