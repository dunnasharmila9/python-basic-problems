## Find the longest word in a list using lambda functions
words=["Apple","Banana","pineapple","strawberry"]
source=max(words,key=lambda n:len(n))
print(source)
