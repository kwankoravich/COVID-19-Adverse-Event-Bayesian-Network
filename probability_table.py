# This function helps to calculate probability distribution, which goes into BBN (note, can handle up to 2 parents)
def probs(data, child, parent1=None, parent2=None, parent3=None, parent4=None, parent5=None):
    # Initialize empty list
    prob=[]
    if parent1==None:
        # Calculate probabilities
        prob=data[child].value_counts(normalize=True, sort=False).sort_index().tolist()
    elif parent1!=None:
            # Check if child node has 1 parent or 2 parents
            if parent2==None:
                # Work out the bands present in the parent variable
                bands=data[parent1].value_counts(sort=False).sort_index().index.tolist()
                # Caclucate probabilities
                for val in bands:
                    temp=data[data[parent1]==val][child].value_counts(normalize=True).sort_index().tolist()
                    prob=prob+temp
            elif parent2!=None:
                if parent3==None:    
                  # Work out the bands present in the parent variable
                  bands1=data[parent1].value_counts(sort=False).sort_index().index.tolist()
                  bands2=data[parent2].value_counts(sort=False).sort_index().index.tolist()
                  # Caclucate probabilities
                  for val1 in bands1:
                      for val2 in bands2:
                          #print(val1)
                          #print(val2)
                          temp=data[(data[parent1]==val1) & (data[parent2]==val2)][child].value_counts(normalize=True).sort_index().tolist()
                          prob=prob+temp
                elif parent3!=None:
                    if parent4==None:
                      bands1=data[parent1].value_counts(sort=False).sort_index().index.tolist()
                      bands2=data[parent2].value_counts(sort=False).sort_index().index.tolist()
                      bands3=data[parent3].value_counts(sort=False).sort_index().index.tolist()
                      # Caclucate probabilities
                      for val1 in bands1:
                          for val2 in bands2:
                              for val3 in bands3:
                                  temp=data[(data[parent1]==val1) & (data[parent2]==val2) & (data[parent3]==val3)][child].value_counts(normalize=True).sort_index().tolist()
                                  prob=prob+temp
                    elif parent4!=None:
                        if parent5==None:
                            bands1=data[parent1].value_counts(sort=False).sort_index().index.tolist()
                            bands2=data[parent2].value_counts(sort=False).sort_index().index.tolist()
                            bands3=data[parent3].value_counts(sort=False).sort_index().index.tolist()
                            bands4=data[parent4].value_counts(sort=False).sort_index().index.tolist()
                            # Caclucate probabilities
                            for val1 in bands1:
                                for val2 in bands2:
                                    for val3 in bands3:
                                        for val4 in bands4:
                                            temp=data[(data[parent1]==val1) & (data[parent2]==val2) & (data[parent3]==val3) & (data[parent4]==val4)][child].value_counts(normalize=True).sort_index().tolist()
                                            prob=prob+temp
                        else:
                            bands1=data[parent1].value_counts(sort=False).sort_index().index.tolist()
                            bands2=data[parent2].value_counts(sort=False).sort_index().index.tolist()
                            bands3=data[parent3].value_counts(sort=False).sort_index().index.tolist()
                            bands4=data[parent4].value_counts(sort=False).sort_index().index.tolist()
                            bands5=data[parent5].value_counts(sort=False).sort_index().index.tolist()
                      # Caclucate probabilities
                            for val1 in bands1:
                                for val2 in bands2:
                                    for val3 in band3:
                                        for val4 in bands4:
                                            for val5 in bands5:
                                                temp=data[(data[parent1]==val1) & (data[parent2]==val2) & (data[parent3]==val3) & (data[parent4]==val4) & (data[parent5]==val5)][child].value_counts(normalize=True).sort_index().tolist()
                                                prob=prob+temp

    else: print("Error in Probability Frequency Calculations")
    
    if (child != None) & (parent1 == None) & (parent2 == None):
      i = len(prob)
      while i != len(data[child].unique()):
        prob.extend([0])
        i+=1
    
    if (parent1 != None) & (parent2 == None):
      i = len(prob)
      while i != len(data[child].unique()) * len(data[parent1].unique()): 
        prob.extend([0]) 
        i+=1

    if (parent1 != None) & (parent2 != None):
      i = len(prob)
      while i != len(data[child].unique()) * len(data[parent1].unique()) * len(data[parent2].unique()):
        prob.extend([0])
        i+=1
    return prob  
