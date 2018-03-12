import os
import sys
import json
import random
from enum import Enum
from flags import Flags

class Me(object):
    state       = 0
    emotion     = 0
    topic       = None
    brain       = None
    def __init__(self, snowflake):
        self.brain = Brain(snowflake)
        
class Brain(object):
    id = 0
    network = None
    def __init__(self, id):
        self.id = id
        if os.path.isfile("./brains/{}.brain".format(self.id)):
            self.Load()
            return
        self.Create()
    
    def Create(self):
        self.network = Network()
    
    def Load(self):
        with open("./brains/{}.brain".format(self.id), "r") as f:
            self.network = json.load(f)
    
    def Save(self):
        with open("./brains/{}.brain".format(self.id), "w") as f:
            f.write(json.dumps(self.network))

class Network(object):
    def __init__(self):
        pass
    
    def Get(self, data): # Get data from network
        pass
    
    def Add(self, data): # Add a new node to the network
        pass
    
    def Del(self, data): # Delete a node and its connections from the network
        pass

    def Fit(self, data, value): # Set a fitness value onto a node
        pass

class Node(object):
    UUID    = -1
    type    = None
    name    = None
    value   = None
    def __init__(self, name, value):
        self.UUID   = GenerateUUID()
        self.name   = name
        self.value  = value
    
    @staticmethod
    def GenerateUUID():
        r = random.randint(0, sys.maxsize)
        return r

class EmotionHandler(object):
    emotion     = 0 # wheel(0, 1) Emotion index (can be betwin 2 different states)
    strength    = 0 # range(0, 1) 0 = nautral, 1 = max
    def __init__(self):
        pass

class State(Flags):
    #IDLE        = 0
    AWAKE       = 1 << 0
    READING     = 1 << 1
    WRITING     = 1 << 2
    LEARNING    = 1 << 3
