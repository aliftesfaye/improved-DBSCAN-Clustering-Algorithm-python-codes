ClusterList = [[[1,2],[3,5],[6,1]],[[3,3],[7,6],[5,4]]]
ClusterList1 = [[[1,2],[3,5],[6,1]],[[3,3],[7,6],[5,4]]]
ClusterList2 = [[[1,2],[3,5],[6,1]],[[3,3],[7,6],[5,4]]]
ClusterListn = [[[1,2],[3,5],[6,1]],[[3,3],[7,6],[5,4]]]

def EuclideanDistance(pt1, pt2):
        sum = 0
        distance = 0
        for i in range(len(pt1)):
            sum += (pt1[i] - pt2[i])**2
        distance = sum**(1/2)
        return distance
def silhouetteCoefficientInternalCluster():
    DistList = []
    AverageList = []
    MeanDist = 0
    for cluster in ClusterList:
        for item in range(0,len(cluster)):
            for item2 in range(0,len(cluster)):                    
                DistList.append(EuclideanDistance(cluster[item], cluster[item2]))
            AverageList.append(average(DistList))
            DistList.clear()
    return AverageList
            
            
def silhouetteCoefficientExternalCluster():
    DistList1 = []
    AverageList1 = []
    newAverageList1 = []
    MeanDist = 0
    for cluster1 in ClusterList1:
        for item1 in range(0,len(cluster1)):
            for cluster2 in ClusterList2:

                if ClusterList1.index(cluster1) == ClusterList1.index(cluster2):
                    continue
                else:

                    for item2 in range(0,len(cluster2)):
                        DistList1.append(EuclideanDistance(cluster1[item1], cluster2[item2]))
                    
                    AverageList1.append(average1(DistList1))
                    DistList1.clear()

            if len(AverageList1) == 0:
                newAverageList1.append(0)
            else:
                newAverageList1.append(min(AverageList1))
            AverageList1.clear()

    return newAverageList1
            
    
def silhouetteCoefficient():
    ClusterListn1 = silhouetteCoefficientInternalCluster()
    ClusterListn2 = silhouetteCoefficientExternalCluster()
    finalRes = []
    for i in range(0,len(ClusterListn1)):
        result = (ClusterListn2[i] - ClusterListn1[i]) / max(ClusterListn1[i],ClusterListn2[i])
        finalRes.append(result)
    averageFinal = average(finalRes)
    return(averageFinal)
            
def average(lst):
    return sum(lst) / (len(lst) - 1)
def average1(lst1):
    return (sum(lst1) / len(lst1))

silhouetteCoefficient()
