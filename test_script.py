import dock.dock as d

# Url is dynamically input in the terminal
getUrl = input("Enter the URL: ")
d.driver.get(getUrl)

# Run Function
def run():
    # Your script goes here
    print("Test ran successfully!")




# New instance of a driver
test = d.Driver(d.driver)



### Use Cases Examples ###

# Rerunnning a test for multiple times
# test.rerun(3, lambda: run())


# Gets the title of the webpage
# test.getTitle()


# Check for the availability of the element in the webpage
# test.checkElement("CLASS_NAME","form-control")


# Check for if the button is clickable or not
# This check operation uses the url field change while submit, so make sure to fill up the desired input field before submission.
# test.checkClick("button")

