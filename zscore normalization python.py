import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

class Zscore_Normalization:
    newsum = 0
    sum1 = 0 
    sum2 = 0
    resutlList = []
    resultList2 = []
    def __init__(self, x):
        self.x = x
    def zscore_nor_DBA(self):
        for i in self.x:
            self.newsum = self.newsum + i        
        mean_val = self.newsum/len(self.x)
        for i in self.x:
            val = (i - mean_val)**2
            self.sum2 = self.sum2 + val
        std = np.sqrt(self.sum2/len(self.x))
        for i in self.x:
            z_score = (i - mean_val)/std
            self.resutlList.append(z_score)
        return self.resutlList
    def zscore_nor_City(self):
            for i in self.x:
                self.newsum = self.newsum + i        
            mean_val = self.newsum/len(self.x)
            for i in self.x:
                val = (i - mean_val)**2
                self.sum2 = self.sum2 + val
            std = np.sqrt(self.sum2/len(self.x))
            for i in self.x:
                z_score = (i - mean_val)/std
                self.resultList2.append(z_score)
            return self.resultList2
    

def main():
    
    excel_file_loc = "dataset_sample.xlsx"

    df = pd.read_excel(excel_file_loc,engine='openpyxl')
    df.dropna(subset=['DBAName_Number'], inplace=True)
    df.dropna(subset=['City_Number'], inplace=True)
    DBA_Name = df['DBAName_Number'].tolist()
    City_Number = df['City_Number'].tolist()
    
    zscore_instance2 = Zscore_Normalization(City_Number)
    zscore_instance = Zscore_Normalization(DBA_Name)
    DBA = zscore_instance.zscore_nor_DBA()
    City = zscore_instance2.zscore_nor_City()
    plt.scatter(DBA,City)
    plt.xlabel('DBA')
    plt.ylabel('City')
    plt.show()
    

if __name__ == '__main__':
    main()








