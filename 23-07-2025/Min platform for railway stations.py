def min_platform(arrival,departure):
    platform=[]
    for i in range(len(arrival)):
        if len(platform)==0:
            platform.append(departure[i])
        else:
            for j in range(len(platform)):
                if arrival[i]<platform[j]:
                    platform.append(departure[i])
                else:
                    platform[j]=departure[i]
    return len(platform)



arrival= [100, 140, 150, 151, 210, 300]
departure= [110, 160, 180, 210, 230, 350]
print(min_platform(arrival,departure))