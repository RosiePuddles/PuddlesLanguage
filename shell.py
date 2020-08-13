import puddles

while True:
    text = input('>> ')
    result, error = puddles.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)
