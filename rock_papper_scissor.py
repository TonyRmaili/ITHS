from dataclasses import dataclass
import random as rn
import time

@dataclass
class Game:
    player_score: int=0
    computer_score: int=0
    rock: int=0
    papper:int=0
    scissor: int=0
    items = ['Rock','Papper','Scissor']

    def player_scores(self):
        print('player wins! Combat continues.')
        self.player_score+= 1
        
    def computer_scores(self):
        print('computer win! Combat continues.')
        self.computer_score+=1
             
    def combat_ends(self):
        if self.player_score == self.computer_score:
            print('Combat ends in draw!')
        elif self.player_score > self.computer_score:
            print('Combat ends with your victory,You win!')
        else:
            print('Combat ends with your defeat, Computer wins!')
        
    def player_choice(self):
        print('Choose...')
        time.sleep(1)
        player_choice = int(input('Rock(0) Papper(1) or Scissor(2), Quit(3)?'))
        time.sleep(1)             
        if player_choice < 0 or player_choice > 3:
             print('invalid number')        
             raise ValueError                  
        return player_choice
           
    def computer_roll(self):
        roll = rn.randint(0, 2)
        return roll
    
    def roll_compare(self,player,computer):       
        if player == computer:
           print('draw! Combat continues.')          
        elif player == 0:
           if computer== 2:
               self.player_scores()
           else:
               self.computer_scores()            
        elif player == 1:
            if computer == 0:
                self.player_scores()
            else:
                self.computer_scores()              
        elif player== 2:
            if computer== 1:
                self.player_scores()
            else:
                self.computer_scores()
    
    def run(self):
        running= True
        while running:  
            try:                  
                p= self.player_choice()
                c= self.computer_roll()
                if p == 3:
                    self.combat_ends()
                    break
                print(f'{self.items[p]}(player) vs {self.items[c]}(computer)')
                self.roll_compare(p,c)           
                print(f'Player score:{self.player_score}  Computer score{self.computer_score}')
            except ValueError:
                print('Try again')


                
if __name__ == '__main__':    
    game= Game()
    game.run()



