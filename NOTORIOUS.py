#SHORTLISTED NAME STUDENT SHOULD NOT BE NOTORIOUS AND SHOULD HAVE SCORE MORE THAN 5
notorious=["DARSHAN","ANUJ","ROHIT"]
names=["ANU","DARSHAN","ROHIT","JACK","PRIYA","BALA","RAI","RAM", "RAJ" , "BEN"]
score=[2,5,6,8,3,5,6,9,8,2]
for i in range(len(names)):
    if score[i]>5:
        if names[i] not in notorious:
            print(names[i])