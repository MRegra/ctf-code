import base64
import urllib.parse

def solve(expected):
    expected = bytes(expected, 'ascii')
    decoded_string = base64.b64decode(expected)
    print("picoCTF{" + urllib.parse.unquote(decoded_string) + "}")

expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
solve(expected)

# flag: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}