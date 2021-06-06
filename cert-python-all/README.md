

This repo is created to track progress in the Path to the Python certification. It is private!



## Tuples


### Creation

```
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

### Access: 

```
thistuple = ("apple", "banana", "cherry")
print(thistuple[
```
```
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
```

```
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
```

### Changin Tuples:

```
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```

### Loop in a tuple:
```
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
``` 
  
### check if an element exist
```
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
```  
  
### Length
```
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```
### Add Items (Once a tuple is created you cannot add items to -no modifiable-)

```
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
```

### One element Tuple:
```
thistuple = ("apple",)
print(type(thistuple))

NOT a tuple:
thistuple = ("apple")
print(type(thistuple))
```

### remove the tuple completely
```
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
```

### join tuples
```
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

### tuple constructor
```
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple
```
### Tuple methods
1. count()
2. index()


## Lists

### Create a List:
```
thislist = ["apple", "banana", "cherry"]
print(thislist)
```
### Access Ittems:
```
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
### Negative Indexing
```
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
### Range of indexes
```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5] (the last item is not included)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```
### Range of negatives
```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```
### Change item value
```
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
### Loops in a list
```
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
```
### check if an item exist
```
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```
### List Length
```
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

### Add items using append() 
```
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```
### Add items using append() 
```
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

### remove items using remove()
```
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

### remote specified index, (or the last item if index is not specified
```
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```

### del removes the specified index
```
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```
### del also deletes an entire list
```
thislist = ["apple", "banana", "cherry"]
del thislist
```
### clear() empty the list
```
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```
### Copy the list
```
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```
### Join 2 lists
```
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

### another way to join lists is using append()
```
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```

### another way to join lists using extend()
```
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```
### the list() constructor
```
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```


Method() | DEscription
------------ | ------------
append()	| Adds an element at the end of the list
clear()	| Removes all the elements from the list
copy()	| Returns a copy of the list
count()	| Returns the number of elements with the specified value
extend()	| Add the elements of a list (or any iterable), to the end of the current list
index()	| Returns the index of the first element with the specified value
insert()	| Adds an element at the specified position
pop()	| Removes the element at the specified position
remove()	| Removes the item with the specified value
reverse()	| Reverses the order of the list
sort()	| Sorts the list


---

**Edit a file, create a new file, and clone from Bitbucket in under 2 minutes**

When you're done, you can delete the content in this README and update the file with details for others getting started with your repository.

*We recommend that you open this README in another tab as you perform the tasks below. You can [watch our video](https://youtu.be/0ocf7u76WSo) for a full demo of all the steps in this tutorial. Open the video in a new tab to avoid leaving Bitbucket.*

---

## Edit a file

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

---

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).
