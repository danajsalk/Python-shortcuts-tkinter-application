## Summary
<br>
Once you have created a set of Python shortcuts you use on a daily basis, you can use the built in Tkinter Python library to build your own GUI to click buttons, initilizaing your codes. 

You can see each shortcut script in this repository: https://github.com/danajsalk/Python-shorcuts

This GUI has some fun features like color options and attributes that keep it on the topmost level at all times. This is very useful when you are clicking back and forth from a SQL windows or Excel sheet. You can easily add or edit functions to create your own version of Python Shortcuts.

You can pick other colors here: http://color-picker.appsmaster.co/#00FF7B

TKinter functions: https://docs.python.org/3/library/tkinter.html



![shortcutGUI](https://user-images.githubusercontent.com/46821074/69642892-b2527380-101f-11ea-98b5-026723b24f33.png)



## Source Data
<br>
When the scripts are run, they directly access values copied to your clipboard.

## Run Directions:
<br>

1. Double click on python file to open TKinter window

2. Copy values to clipboard

3. Click on shortcut button to execute code

4. Paste new string

## Examples
Below are some examaples of the inputs and outputs for the shortcuts. 

| Shortcut          | Input                                        | Output                           |
|-------------------|----------------------------------------------|----------------------------------|
| Comma Shortcut    | apples <br> apples <br> oranges <br> bananas | apples, oranges, bananas         |
| Tick Shortcut     | apples <br> apples <br> oranges <br> bananas | 'apples', 'oranges', 'bananas'   |
| Tick a Comma      | apples, oranges, bananas                     | 'apples', 'oranges', 'bananas'   |
| Remove Duplicates | apples <br> apples <br> oranges <br> bananas | apples <br> oranges <br> bananas |


## Adding a New Button
<br>

1. Define a new function for the button to activate

```
def newCommand():
    setClip("""Testing your new button!""")
```

2. Add button to queryFrame

queryFrame = the section the button will appear in

```
newButton = Button(queryFrame, text="Your New Button Text", command=newCommand)
newButton.pack(fill=X)
```
