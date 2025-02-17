job_categories <- c("Sales","Sales","Sales","Sales", "Marketing", "Engineering", "Sales", "Engineering", "Marketing", "Sales", "Finance", "Marketing", "Engineering","Aeronautical","Aeronautical","Aeronautical","Aeronautical")
category_counts <- table(job_categories)
barplot(category_counts,
        main = "Frequency of Job Categories", 
        xlab = "Job Category",             
        ylab = "Frequency",                
        col = rainbow(length(category_counts)),
        border = "black",                   
        las = 1,                            
        cex.names = 0.8                   
)


