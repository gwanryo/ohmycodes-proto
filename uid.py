import secrets

# Remove i, I, l, L, o, O, 1, 0
DEFAULT_CHARSET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '2', '3', '4', '5', '6', '7', '8', '9']

def generate(item=DEFAULT_CHARSET, len=10):
    srand = secrets.SystemRandom()
    result = srand.sample(item, len)
    return ''.join(result)

if __name__ == "__main__":
    for i in range(10):
        print(generate(len=10))