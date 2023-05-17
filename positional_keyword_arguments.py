# Functions with more than 1 input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# positional arguments are passed in the order that were specified
greet_with("Roger", 'Australia')


# keyword arguments specify the parameter they belong to
# even if we switch the order of arguments
greet_with(location="Nowhere", name="Maurice")
