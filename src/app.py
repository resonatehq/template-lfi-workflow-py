from resonate.stores import LocalStore
from resonate import Resonate


# Initialize Resonate with a local store (in memory)
resonate = Resonate(store=LocalStore())


# Register the top-level function with Resonate
@resonate.register
def foo(ctx, greeting):
    print("running foo")
    greeting = yield ctx.lfc(bar, greeting)
    # to make this call asynchronous
    # promise = yield ctx.lfi(bar, greeting)
    # greeting = yield promise
    greeting = yield ctx.lfc(baz, greeting)
    return greeting


def bar(_, v):
    print("running bar")
    return f"{v} world"


def baz(_, v):
    print("running baz")
    return f"{v}!"


# Define a main function
def main():
    try:
        handle = foo.run("hello-world-greeting", greeting="hello")
        print(handle.result())
    except Exception as e:
        print(e)


# Run the main function when the script is invoked
if __name__ == "__main__":
    main()
