from callLimit import callLimit


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"Error: {e}")
