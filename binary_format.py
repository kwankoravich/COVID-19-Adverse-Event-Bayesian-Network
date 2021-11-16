### This function would find the symptoms in each patient. 
If the patiens have the symptoms, we will assign in which column as 1. 
Otherwise it's assigned as 0 ###


def binary_form(df):
   df_symptom = df['symptoms']
    for i in df_symptom:
      arr = []
      for j in range(len(df_symptom)):
        if df_symptom[j] == i:
          arr.append(1)
        else:
          arr.append(0)
      df[i] = arr
    df
