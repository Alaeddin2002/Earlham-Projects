library(dplyr)
library(ggplot2)

head(ToothGrowth) #shows the beginning of the data set to get an idea of what it looks like

Groups = as_tibble(ToothGrowth) %>%  #gets in the data format I want
    group_by(supp,dose) %>% #Groups it by type of treatment (supp) and dose amount (dose)
    summarize(mean = mean(len)) ##takes the mean of the growth for each of these groups
Groups #prints resulting table

Groups %>% filter(dose>.5) #Gives me all the cases where the dose was greater than .5
VC = Groups %>% filter(supp == "VC") #Gives me only the treatment method for VC
VC

library(ggplot2)
dose = Groups$dose
mean = Groups$mean
ggplot(Groups, aes(x = dose, y = mean, size = 8, color = supp)) + 
  geom_point() +
  geom_line()

ggplot(Groups, aes(x = supp, y = mean)) + 
  geom_boxplot()

ggplot(Groups, aes(group = dose, y = mean)) + 
  geom_boxplot() #looks like the dose had more of an effect on the growth than the treatment...


