import random

### Design Parameters ###
N = 2   # Number of Module Links
L = 'd'   # Type of Module Links
C = [1, 2, 3, 4, 5, 6]  # Labels of Connection Faces
A = [0, 90, 180, 270] # Rotation Angles

### GA Global Variables ###
POP_SIZE = 10
GENERATIONS = 1000

### Dtto Robot composed of 2 modules ###
d2 = [(1, 0, 0, 0), (4, 0, 0, 0)]

### Step 1 -- Generate Initial Population ###
#print('(',random.choice(C), ',' , random.choice(A), ',' , random.choice(A), ',' , random.choice(A), ')')
e = N-1   # Number of Edges

def individual():
    'Create a member of the population'
    return random.sample(list(zip(random.sample(C, len(C)), random.sample(A, len(A)), random.sample(A, len(A)), random.sample(A, len(A)))), N)

#print (individual())

def population():
    'Create a population of individuals'
    return [ individual() for x in range(POP_SIZE) ]

#print (population())

### Step 2 -- Evaluation ##
def fitness(individual, target):
    return -1

### Step 3 -- Selection ##
def grade(pop, target):
    'Calculate Avg'
    return -1

### Step 4 -- Crossover ###
def crossover(mom, dad):
    return mom[:1] + dad[1:]

print (crossover([(2, 0, 90, 90), (3, 90, 270, 270)], [(4, 0, 90, 270), (6, 90, 0, 180)]))

### Step 5 -- Mutation ###
def mutate(child):
    return -1