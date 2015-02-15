library(dplyr)
library(ggplot2)
library(lubridate)

nytimes <- read.csv("nytimes.csv")
nytimes$date <- parse_date_time(nytimes$date_time,orders="ymd_hms")
nytimes$year <- year(nytimes$date)
nytimes$month <- month(nytimes$date)

nytimes_clean  <- nytimes %>%
    distinct(id) %>%
    group_by(year,month) %>%
    summarise(n=n())

nytimes_clean$year_month <- paste(nytimes_clean$year, nytimes_clean$month,"01",sep="-")
nytimes_clean$year_month <- ymd(nytimes_clean$year_month)

png(file="figure/budget.png",
    width = 800, height = 600)
ggplot(nytimes_clean,aes(year_month,n))+geom_line()+theme_bw()
dev.off()