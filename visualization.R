library(dplyr)
library(ggplot2)
library(lubridate)

# Load scraped data
nytimes <- read.csv("nytimes.csv")

# Parse date and time
nytimes$date <- parse_date_time(nytimes$date_time,orders="ymd_hms")
nytimes$year <- year(nytimes$date)
nytimes$month <- month(nytimes$date)

# Remove duplicated data, summarise by months
nytimes_clean  <- nytimes %>%
    distinct(id) %>%
    group_by(year,month) %>%
    summarise(n=n())

# Parse date and time in cleaned dataset
nytimes_clean$year_month <- paste(nytimes_clean$year, nytimes_clean$month,"01",sep="-")
nytimes_clean$year_month <- ymd(nytimes_clean$year_month)

# Media coverage since 1850
png(file="figure/all_time.png",
    width = 900, height = 300)
ggplot(nytimes_clean,aes(year_month,n))+geom_line()+theme_bw()+
    scale_x_datetime()+labs(x="Year")+labs(y="Frequency")
dev.off()

# Media coverage since 2000
nytimes_since_2000 <- nytimes_clean %>%
    filter(year(year_month)>=2000)
png(file="figure/since_2000.png",
    width = 900, height = 300)
ggplot(nytimes_since_2000,aes(year_month,n))+geom_line()+theme_bw()+
    scale_x_datetime()+labs(x="Year")+labs(y="Frequency")
dev.off()


