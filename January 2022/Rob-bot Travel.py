import winsound
filename = "Chinese.wav"
flyingTo = input("Where are you flying to ").strip(' ').lower()
flyingFrom = input("Where are you flying from ").strip(' ').lower()
locations = [
    "london",
    "newyork",
    "capetown",
    "shanghai",
    "cairo",
    "sydney",
    "toronto",
    "reykjavik",
    "helsinki",
    "hongkong",
    "berlin",
    "lasvegas"]
if flyingFrom in locations and flyingTo in locations:
    print("We support the place you are flying from and to! 😊")
elif flyingTo not in locations:
    print("你不会离开这个国家。☹️")
    winsound.PlaySound(filename, winsound.SND_FILENAME)
elif flyingFrom not in locations:
    print("你不会离开这个国家。☹️")
    winsound.play(filename, winsound.SND_FILENAME)
A