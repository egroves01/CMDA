# Ethan Groves
# Ethan Groves
# InClass 8
# Oct. 24, 2014

# Part 1 - Set working directory and load data
setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Data")
load('fData.RData')

# Part 2 - Create and summarize model
attach(final)
model <- lm(ssc ~ som1 + som2 + som3 + som4 + som5 + som6 + som7 + som8 + som9 + som10 + som11 + som12 + som13 + som14)
summary(model)
detach(final)

# Results
'''Call:
lm(formula = ssc ~ som1 + som2 + som3 + som4 + som5 + som6 + 
    som7 + som8 + som9 + som10 + som11 + som12 + som13 + som14)

Residuals:
Min      1Q  Median      3Q     Max 
-4.1541 -0.9040 -0.2357  0.8258  5.0844 

Coefficients:
Estimate Std. Error t value Pr(>|t|)    
(Intercept)  0.62257    0.14184   4.389 1.56e-05 ***
som1         0.20700    0.06207   3.335 0.000958 ***
som2         0.32486    0.06410   5.068 6.94e-07 ***
som3         0.24497    0.03364   7.281 2.78e-12 ***
som4         0.15397    0.04599   3.348 0.000914 ***
som5         0.16308    0.07082   2.303 0.021963 *  
som6         0.07097    0.08311   0.854 0.393833    
som7         0.09678    0.08071   1.199 0.231418    
som8        -0.01069    0.17654  -0.061 0.951757    
som9         0.11097    0.08753   1.268 0.205825    
som10        0.25536    0.07304   3.496 0.000541 ***
som11        0.18985    0.08565   2.217 0.027378 *  
som12        0.20548    0.05935   3.462 0.000612 ***
som13        0.40608    0.04602   8.825  < 2e-16 ***
som14        0.19875    0.05434   3.657 0.000300 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.531 on 308 degrees of freedom
Multiple R-squared:  0.792,  Adjusted R-squared:  0.7826 
F-statistic: 83.79 on 14 and 308 DF,  p-value: < 2.2e-16
'''

# Q&A
'''
Are the 14 somatic markers (physical characteristics) successful in predicting the disorder score?
 - Yes, because the coefficient of determination is above 70% (79%), which is considered good.

What are the somatic features most indicative of the disorder?
 - The most important features in determining wine quality are: Som1, Som2, Som3, Som4, Som10, Som12, Som13, Som14 
   (where p-value < 0.05; or we have one or more stars in R results).
'''