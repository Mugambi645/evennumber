class FindEvenNumber():
    def __init__(self, play1,play2,count):
        self.play1 = play1
        self.play2 = play2
        self.count = count
    def playGame(self, user1, user2):
        for _ in range(3):
        
            self.user1 = input("Enter your name: (Player 1)")
            self.user2 = input("Enter your name: (Player 2)")
            self.play1 = int(input("{} Enter a number: (Player 1)".format(self.user1)))
            self.play2 = int(input("{} Enter a number: (Player 2)".format(self.user2)))
            
            if (self.play1 % 2 == 0):
                print("{}, you got it!{} is even!".format(self.user1,self.play1))
            else:
                print("{}, {} is not even".format(self.user1, self.play1))
            if (self.play2 % 2 == 0):
                print("{}, you it!{} is even!".format(self.user2,self.play2))
            else:
                print("{}, {} is not even".format(self.user2,self.play2))
nums = FindEvenNumber("john","kev","ian")
nums.playGame("joy", "ken")


