class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new):
        self.name = new
        print('My name is' ,self.name)

    def change_age(self, new_age):
        self.age = new_age
        print("I am" , self.age ,"years old")
    
    def add_track(self, tracks):
        self.tracks.append(tracks)
        print("I am enrolled in ",self.tracks)

    def get_score(self):
        print("My score is ",self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
