import dock

# Url is dynamically input in the terminal
getUrl = input("Enter the URL: ")
dock.driver.get(getUrl)

# Run Function
def run():
    # Your script goes here
    title = dock.driver.title
    print(title)


d = dock.Driver(dock.driver)
d.rerun(3, lambda: run())