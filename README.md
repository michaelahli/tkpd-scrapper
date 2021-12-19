# TKPD-Scrapper

## Description
is a fist coding assignment to apply as a backend developer in Bricks.

## Question
```
Brick is on a mission to democratise financial services in Southeast Asia - by empowering innovators to build amazing products and solve big problems - starting with financial data APIs that allow fintech developers to create easy and accessible experiences for their users, therefore we need an Information Security Engineer to join the adventure.

As Backend Engineer, we would like you to create a programming Utility in your favorite programming language (preferably JAVA) that extracts top 100 products of category Mobile phones/Handphone from Tokopedia and stores it in a csv file. It should include the following information:
1. Name of Product
2. Description
3. Image Link
4. Price
5. Rating (out of 5 stars)
6. Name of store or merchant
```

## Background
This project is written in Python because its quicker to write project on python rather than Java, not in Go because Go is not suitable for this case. 

There is no containerizations because time not enough in order to do that. So you should setup by your own.

## Dependencies
1. Python version 3
2. Pip version 3
3. Chromedriver (https://chromedriver.storage.googleapis.com/index.html)
4. Unix Environment

## How to run locally
1. ```make dependency```
2. rename ```.env.example``` to ```.env```
3. change DRIVER_LOC into your chromedriver location
4. ```make run```

## Author
Michael Ahli