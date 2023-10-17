import csv
listr=['1','2','3']
head= ['temp','pos']
with open('space.csv','w') as right:
    
    w=  csv.writer(right)
  
    w.writerow(['pos','temp'])

    w.writerows(listr)





      