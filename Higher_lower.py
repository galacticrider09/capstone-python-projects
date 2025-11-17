import asciiarts
from H_L_DICT import instagram_data

def info(r1):
    name = instagram_data[r1]["name"]
    followers = instagram_data[r1]["follower_count"]
    desc = instagram_data[r1]["description"]
    country = instagram_data[r1]["country"]
    return f"{name},{followers},{desc},{country}"
print(asciiarts.vs_logo)
print(info(2))