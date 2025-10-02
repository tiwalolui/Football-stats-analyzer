import numpy as np
#data for 5 matches
#format:[goal_scored,goals_conceded,shots_on_target]
matches=np.array([
    [2, 1, 5],
    [5, 2, 7],
    [0, 1, 2],
    [4, 3, 9],
    [1, 0, 4]


])

print("shape of data :", matches.shape) 
print("All data:\n",matches)

total_goals = np.sum(matches[:,0])
print("Total goals scored :",total_goals)


avg_goals_conceded = np.mean(matches[:,1])
print("Average goal conceded:", avg_goals_conceded) 

total_shots_on_target =np.sum(matches[:,2])
print("Total shot on target:",total_shots_on_target) 

best_game = np.max(matches[:,[0,2]]) 
print("most entertaining game:",np.max(best_game)) 
worst_game =np.min(matches[:,2])
print("worst shot on target:",worst_game) 

results = matches[:,0] > matches[:,1]
print("Results(True = win, False = Loss/draw):",results)
print("Total wins:",np.sum(results))
