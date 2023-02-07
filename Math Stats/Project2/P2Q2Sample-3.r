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

##qqplots help us determine whether we can assume normality, if the distribution is normal, 
# it should lie along the line
ggplot(ToothGrowth, aes(sample = len )) + stat_qq() +stat_qq_line() 
ggplot(ToothGrowth, aes(sample = len, color = supp )) + stat_qq() +stat_qq_line()
ggplot(Groups, aes(sample = Groups$mean )) + stat_qq() +stat_qq_line()
ggplot(Groups, aes(sample = Groups$mean, color = supp )) + stat_qq() +stat_qq_line()

#confidence interval for the mean, we have to pull out the line where it says confidence interval
VC = ToothGrowth %>% filter(supp == "VC")
OJ = ToothGrowth %>% filter(supp == "OJ")
t.test(ToothGrowth$len, conf.level = .98)
t.test(VC$len,conf.level=.98)
t.test(OJ$len, conf.level = .98)

#one-sided confidence intervals
t.test(ToothGrowth$len, mu = 0, alternative = "less", conf.level = .98)
t.test(ToothGrowth$len, mu = 0, alternative = "greater", conf.level = .98)

# T-test: It looks like the mean of the whole data is about 18.8. I want to test whether the mean of the OJ treatment is 
#greater than 18.8. So H_0 = 18.8 and H_1 is greater
t.test(OJ$len, mu=18.8, alternative = "greater", conf.level = 0.95)
#we fail to rejevt H_0 at a confidence level of .95, but we would reject H_0 at a confidence level of .9

# two -sample t-test
t.test(ToothGrowth$len ~ supp, data=ToothGrowth,  conf.level = .95)
# Fail to reject H_0 at a .95 percent confidence interval, but if 
# we look at the p-value, we would reject H_0 at a .9 confidence interval

# Ratio of variances sigma^2_x/sigma^2_y using Fisher's F Distribution. H_0 is that this ration is 1
#(i.e. the variances are equal)
var.test(len ~ supp, data = ToothGrowth)
var.test(len ~ supp, data = ToothGrowth, alternative = "less")
# We don't have enough evidence to reject the null hypothesis that the variances are equal

#Confidence interval for the variance. R doesn't have this built in, so we have to use the fact that we know
# the sample variance is approximately Chi-squared with degrees of freedom (n-1) and use the built-in 
#chi-squared probability to find a 95% confidence interval
v = var(ToothGrowth$len);  n = length(ToothGrowth$len)
(n-1)*v/qchisq(c(.975,.025), n-1)




