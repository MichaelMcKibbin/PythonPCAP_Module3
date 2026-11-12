class Hominidae(object):
    def __init__(self, name="Hominidae"):
        self.name = name

    def speak(self):
        print("I am a member of the Hominidae family.")
        return "I am a member of the Hominidae family."

    def communication(self):
        print("I use auditory calls and visual cues.")
        return "I use auditory calls and visual cues"

    def walk(self):
        print("I am a knuckle-walker, used for walking on all fours. I also hang and swing from tree to tree.")
        return "I am a knuckle-walker, used for walking on all fours. I also hang and swing from tree to tree."


class Human(Hominidae):
    def __init__(self, name="Human"):
        super().__init__(name)

    def speak(self):
        print("I am a human.")
        return "I am a Human."

    def communication(self):
        print("I use language and gestures.")
        return "I use language and gestures"

    def walk(self):
        print("I am bipedal, walking on two legs.")
        return "I am bipedal, walking on two legs."


class Gorilla(Hominidae):
    def __init__(self, name="Gorilla"):
        super().__init__(name)

    def speak(self):
        print("I am a Gorilla.")
        return "I am a Gorilla."

    def communication(self):
        print("I use vocalizations and body language.")
        return "I use vocalizations and body language"

    def walk(self):
        print("I am a knuckle-walker, walking on all fours.\nI also use my arms for climbing and swinging.")
        return "I am a knuckle-walker, walking on all fours.\nI also use my arms for climbing and swinging."


hominid1 = Hominidae()
human1 = Human()
gorilla1 = Gorilla()

hominid1.speak()
hominid1.communication()
hominid1.walk()

human1.speak()
human1.communication()
human1.walk()

gorilla1.speak()
gorilla1.communication()
gorilla1.walk()
