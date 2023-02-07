#This is Question 2


#sequence of 10 coin tosses
#Each trial is called cointoss
#The two possible outcomes are H for heads and T for tails 
cointoss <- sample(c("H", "T"),10, replace=TRUE)
cointoss
sum(cointoss=="H") #sum every time there is an H 
#we get 8 when we execute the above command, it should be one since we expected it to be the first 
sum(cointoss=="H") == 1
#We find out that it is false in this case, and now we can sum the 10th coin toss when it is heads
sum(cointoss[10]=="H")
#now we can replicate this 10000 times and add up the chances that you get the first head on the 10th flip
event<- replicate(10000, {
  cointoss<-sample(c("H","T"), 10, replace = TRUE)
  (sum(cointoss=="H") ==1) & sum(cointoss[10]=="H")
})
mean(event)

# This is question 3



dice <- sample(x=1:6, size = 2, replace=TRUE) #Roll two dice 
sum(dice) 
sum(dice) == 3 
#Now run the simulation, first check for when the sum is 3 (Event A)
#Then check when the sum is either 3 or 5 (Event B)
#Then we can calculate P(A|B)
eventA<-replicate (10000, {
  dice <- sample(x=1:6, size = 2, replace=TRUE)
  (sum(dice)) == 3
})
probabilityA <- mean(eventA)
probabilityA #here is estimating that the probability of the sum of the dice is 3, so the probability of event A
#now let's estimate the probability that the sum is 3 or 5 (I do not know how to write "or") 
eventB<- replicate (10000, {
  dice <- sample(x=1:6, size = 2, replace=TRUE)
  (sum(dice))==3 | (sum(dice)) == 5
})
probabilityB <- mean(eventB)
probabilityB #probability of the sum being equal to 3 or 5 
#now we want to find P(A|B)
#Do we need to first find A intersect B? **not too sure**
eventAB<- replicate (10000, {
  dice <- sample(x=1:6, size = 2, replace=TRUE)
  (sum(dice))==3 &  ((sum(dice))==3 | (sum(dice)) == 5 )
}) #This is how I think you can find the intersection of A and B **not too sure**
probabilityAB <- mean(eventAB) #A intersect B 
probabilityAB
#now we can find P(A|B) by dividing the intersection and the P(B)
probabilityAB/probabilityB #P(A|B)
#We get a value of  0.3274282


#This is question 4

# An urn contains two red balls and four white balls. Sample successively five times
# at random and with replacement so that the trials are independent. Compute the probability of each 
# of the two sequences WWRWR and RWWWR.

balls <- c("R","R","W","W","W","W")
balls_prob <- sample (balls, size = 5, replace = TRUE) #picking up random 5 balls 
balls_prob
# sum(balls_prob == "R")
# sum(balls_prob=="R") == 1
# sum(balls_prob[3] == "R")
# sum(balls_prob[5] == "R")

# Calculating the probability of getting RWWWR
eventWWRWR<- replicate (100000, {
  balls_prob <- sample(balls, size = 5, replace=TRUE)
  (sum((balls_prob=="R") ==1) == 2) & sum(balls_prob[3]=="R" & sum(balls_prob[5] == "R"))
})
mean(eventWWRWR)

# Calculating the probability of getting RWWWR
eventRWWWR<- replicate (10000, {
  balls_prob <- sample(balls, size = 5, replace=TRUE)
  (sum((balls_prob=="R") ==1)==2) & sum(balls_prob[1]=="R" & sum(balls_prob[5] == "R"))
})
mean(eventRWWWR)


