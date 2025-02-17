x <- c(1, 2, 3, 4, 5)  
y <- c(2, 4, 5, 4, 6) 

df <- data.frame(x = x, y = y) 

model <- lm(y ~ x, data = df)

summary(model)

new_data <- data.frame(x = c(6, 7))
predictions <- predict(model, newdata = new_data)
print(predictions)


plot(df$x, df$y, main = "Linear Regression", xlab = "X", ylab = "Y")
abline(model, col = "red")

data(mtcars) 
model_mtcars <- lm(mpg ~ wt, data = mtcars) 
summary(model_mtcars)
plot(mtcars$wt, mtcars$mpg, main = "MPG vs. Weight", xlab = "Weight", ylab = "MPG")
abline(model_mtcars, col = "blue")