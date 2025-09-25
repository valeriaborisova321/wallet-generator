import random
import string

def random_btc_address():
    prefix = random.choice(["1", "3", "bc1"])
    body = ''.join(random.choices(string.ascii_letters + string.digits, k=33))
    return prefix + body

def random_eth_address():
    return "0x" + ''.join(random.choices("abcdef" + string.digits, k=40))

if __name__ == "__main__":
    print("Random BTC Address:", random_btc_address())
    print("Random ETH Address:", random_eth_address())
