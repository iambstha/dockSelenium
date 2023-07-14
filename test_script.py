import dock.dock as d

# Url is dynamically input in the terminal
getUrl = input("Enter the URL: ")
d.driver.get(getUrl)

# Run Function
def run():
    # Your script goes here
    title = d.driver.title
    print(title)


i = d.Driver(d.driver)
i.rerun(3, lambda: run())