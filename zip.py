# create a tupple with 4 arrays with the paths of each forklift

forklifts_paths = ([1,2,3,4,5,6,7,8,9,10], [11,12,12,14,5,6], [21,22,23,24,5], [1,32,33,34])


# Iterate over the arrays simultaneously
zipped = list(zip(*forklifts_paths))
penalizacao = 0
print(zipped)
for array in zipped:
    print(len(set(array)))
    print(len(array))
    if len(set(array)) < len(array):

        penalizacao += 1


print("Penalização: ", penalizacao)
#for index, paths in enumerate(zip(*forklifts_paths)):
    #print(len(forklifts_paths))
    #if all(cell == paths[0] for cell in paths):
     #   self.penalizacao += 1
    #    print("At least two forklifts at step : ", index, " collide.")