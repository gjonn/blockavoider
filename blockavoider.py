# Program Name: blockavoider.py
# Developer: Gjon Gojcevic
# Date: 12/06/2013
# Desscription: Block avoider game


from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Game(object):
    
    def __init__(self):
        #set bg
        self.set_background("resources\\bg.jpg")
        self.level = 0
        self.lives = 10
        self.maxlevels = "5"

        #add logo
        self.logo = Logo(game = self, x = games.screen.width/2, y = 20)
        games.screen.add(self.logo)

        #add platform
        self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
        games.screen.add(self.player1)
        self.introGoal = Goal(game = self, x = games.screen.width, y = games.screen.height/2)
        games.screen.add(self.introGoal)

        #add score
        self.scorevalue = 0
        self.score = games.Text(value = "Score: " + str(self.scorevalue),
                                size = 30,
                                color = color.red,
                                left = 10,
                                bottom = 75,
                                is_collideable = False)
        games.screen.add(self.score)

        #add lives
        self.life = games.Text(value = "Lives: " + str(self.lives),
                                   size = 30,
                                   color = color.red,
                                   left = 10,
                                   bottom = 94,
                                   is_collideable = False)
        games.screen.add(self.life)
        

        #add level meter
        self.progress = games.Text(value = "Level: " + str(self.level) + "/" + self.maxlevels,
                                   size = 30,
                                   color = color.red,
                                   left = 10,
                                   bottom = 117,
                                   is_collideable = False)
        games.screen.add(self.progress)

    def update_levelmeter(self):

        # updates the level meter
        self.progress.value = "Level: " + str(self.level) + "/" + self.maxlevels

    def update_score(self):

        # updates the score
        self.score.value = "Score: " + str(self.scorevalue)
        
    def set_background(self, bg):

        # set background settings
        background_image = games.load_image(bg, transparent = False)
        games.screen.background = background_image

    def next_level(self):
        # changes to the next level
        self.player1.destroy()
        if self.level != 0:
            self.scorevalue += 500
            self.update_score()
        self.level += 1
        self.update_levelmeter()
        enemyi = games.load_image("resources\\enemyi.bmp")
        enemyx = games.load_image("resources\\xenemy.png")
        enemyb = games.load_image("resources\\ball.png")

        # level data
        if self.level == 1:
            self.header.value = "Watch out for the red blocks!"
            self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
            games.screen.add(self.player1)
            self.new_enemy = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy)
            self.new_enemy1 = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2 + 15, y = games.screen.height/2, dy = -2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy1)


        if self.level == 2:
            self.clear()
            self.header.value = "There are many different dangerous block behaviors."
            self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
            games.screen.add(self.player1)
            self.new_enemy = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2 - 100, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy)
            self.new_enemy1 = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2 - 100 + 15, y = games.screen.height/2, dy = -2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy1)
            self.new_enemy2 = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy2)
            self.new_enemy3 = Enemy(game = self, enemyType = "y", image = enemyi,
                                   x = games.screen.width/2 + 15, y = games.screen.height/2, dy = -2, dx = 0, aspeed = 0)
            games.screen.add(self.new_enemy3)
            self.senemy = Enemy(game = self, enemyType = "s", image = enemyi,
                           x = games.screen.width/2 + 200, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 1)
            games.screen.add(self.senemy)

        if self.level == 3:
            self.clear()
            self.header.value = "Have fun!"
            self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
            games.screen.add(self.player1)
            self.senemy = Enemy(game = self, enemyType = "s", image = enemyi,
                                x = games.screen.width/2 + 200, y = games.screen.height/2, dy = -2, dx = 0, aspeed = 1)
            games.screen.add(self.senemy)
            self.senemy1 = Enemy(game = self, enemyType = "s", image = enemyi,
                                x = games.screen.width/2 - 220, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 1)
            games.screen.add(self.senemy1)
            self.senemy2 = Enemy(game = self, enemyType = "s", image = enemyi,
                                x = games.screen.width/2, y = games.screen.height/2, dy = -1, dx = 0, aspeed = 1)
            games.screen.add(self.senemy2)
            self.senemy3 = Enemy(game = self, enemyType = "s", image = enemyi,
                                 x = games.screen.width/2 - 100, y = games.screen.height/2, dy = -2, dx = 0, aspeed = 1)
            games.screen.add(self.senemy3)
            self.senemy4 = Enemy(game = self, enemyType = "s", image = enemyi,
                                 x = games.screen.width/2 + 110, y = games.screen.height/2, dy = 2, dx = 0, aspeed = 1)
            games.screen.add(self.senemy4)
        if self.level == 4:
            self.clear()
            self.header.value = "Little harder now!"
            self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
            games.screen.add(self.player1)
            self.xenemy = Enemy(game = self, enemyType = "x", image = enemyx,
                                x = games.screen.width/2, y = games.screen.height/2 + 41, dy = 0, dx = -2, aspeed = 0)
            games.screen.add(self.xenemy)
            self.xenemy1 = Enemy(game = self, enemyType = "x", image = enemyx,
                                x = games.screen.width/2, y = games.screen.height/2 - 50, dy = 0, dx = 4, aspeed = 0)
            games.screen.add(self.xenemy1)
        if self.level == 5:
            self.clear()
            self.header.value = ""
            self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
            games.screen.add(self.player1)
            self.benemy = Enemy(game = self, enemyType = "bounce", image = enemyb,
                                 x = games.screen.width/2, y = games.screen.height/2 - 50, dy = 1, dx = 1, aspeed = 1)
            games.screen.add(self.benemy)
            self.benemy1 = Enemy(game = self, enemyType = "bounce", image = enemyb,
                                x = games.screen.width/2, y = games.screen.height/2, dy = -1, dx = -1, aspeed = 1)
            games.screen.add(self.benemy1)
            self.benemy2 = Enemy(game = self, enemyType = "bounce", image = enemyb,
                                 x = games.screen.width/2 - 50, y = games.screen.height/2 - 30, dy = -2, dx = -1, aspeed = 1)
            games.screen.add(self.benemy2)
            self.benemy3 = Enemy(game = self, enemyType = "bounce", image = enemyb,
                                 x = games.screen.width/2 - 50, y = games.screen.height/2 - 30, dy = -2, dx = -2, aspeed = 1)
            games.screen.add(self.benemy3)
            self.benemy4 = Enemy(game = self, enemyType = "bounce", image = enemyb,
                                 x = games.screen.width/2 -70, y = games.screen.height/2 - 30, dy = 3, dx = -2, aspeed = 1)
            games.screen.add(self.benemy4)
        if self.level == 6:
            self.clear()


        if self.level > int(self.maxlevels):
            self.win()

    def die(self):
        # lose a life, update lives, return player to beginning
        self.lives -= 1
        self.life.value = "Lives: " + str(self.lives)
        self.player1 = Player(game = self, x = 15, y = games.screen.height/2)
        games.screen.add(self.player1)

        if self.lives < 0:
            self.header.value = "You suck!"
            self.game_over()
            

    def intro_text(self):
        # sets header text
        self.header = games.Text(value = "Welcome to Block Avoider! To win, reach the green goal.",
                                size = 25,
                                color = color.red,
                                x = games.screen.width/2,
                                y = 130,
                                is_collideable = False)
        games.screen.add(self.header)
        
    def play(self):

        #music
        games.music.load("resources//bgmusic.mp3")
        games.music.play(-1)

        #play
        games.screen.mainloop()

    def game_over(self):
        # game over
        self.life.value = ""
        self.life.value = "Lives: 0"
        self.player1.destroy()
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)

    def win(self):
        # game over
        self.header.value = "Good Job!"
        self.player1.destroy()
        end_message = games.Message(value = "You Win",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)
        

    def clear(self):
        # clears the sprites off game for new levels
        if self.level == 2:
            self.new_enemy.destroy()
            self.new_enemy1.destroy()
        if self.level == 3:
            self.new_enemy.destroy()
            self.new_enemy1.destroy()
            self.new_enemy2.destroy()
            self.new_enemy3.destroy()
            self.senemy.destroy()
        if self.level == 4:
            self.senemy.destroy()
            self.senemy1.destroy()
            self.senemy2.destroy()
            self.senemy3.destroy()
            self.senemy4.destroy()
        if self.level == 5:
            self.xenemy.destroy()
            self.xenemy1.destroy()
        if self.level == 6:
            self.benemy.destroy()
            self.benemy1.destroy()
            self.benemy2.destroy()
            self.benemy3.destroy()
            self.benemy4.destroy()
        
class Player(games.Sprite):
    #player class
    image = games.load_image("resources\\player.png")
    def __init__(self, game, x, y):
        super(Player, self).__init__(image = Player.image, x = x, y = y)

        self.game = game
        self.sound = games.load_sound("resources\\death.wav")

    def update(self):

        # aligns the score, lives, and progress so it doesnt move 
        if self.game.score.left != 10:
            self.game.score.left = 10
        if self.game.life.left != 10:
            self.game.life.left = 10
        if self.game.progress.left != 10:
            self.game.progress.left = 10
            
        # keyboard controls
        if games.keyboard.is_pressed(games.K_UP):
            self.y -= 2
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y += 2
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 2

        #boundary
        if self.bottom > 331:
            self.bottom = 331
        if self.top < 140:
            self.top = 140
        if self.left < 3:
            self.left = 3
        if self.right > games.screen.width - 2:
            self.right = games.screen.width - 2

        self.check_collide()
            
    def check_collide(self):
        
        for sprite in self.overlapping_sprites:
            sprite.handle_collide()

    def handle_collide(self):
        # play sound, die, subtract 200 points, update the score
        self.sound.play()
        self.destroy()
        self.game.scorevalue -= 200
        self.game.update_score()
        self.game.die()
        
class Enemy(games.Sprite):
    # enemy block class
    def __init__(self, game, enemyType, image, x, y, dy, dx, aspeed):
        
        super(Enemy, self).__init__(image = image, x = x, y = y, dy = dy)

        self.game = game
        self.type = enemyType
        self.aspeed = aspeed
        self.dx = dx

    def update(self):
        # y axis moving enemy
        if self.type == "y":
            if self.top < 140 or self.bottom > 331:
                self.dy = -self.dy
        # spinning enemy
        if self.type == "s":
            self.angle += self.aspeed
            if self.top < 140 or self.bottom > 331:
                self.dy = -self.dy
        # x axis moving enemy
        if self.type == "x":
            if self.left < 200 or self.right > games.screen.width - 15:
                self.dx = -self.dx
        # a ball enemy
        if self.type == "bounce":
            if self.left < 150 or self.right > games.screen.width - 15:
                self.dx = -self.dx
            if self.top < 140 or self.bottom > 331:
                self.dy = -self.dy
                
            
                
        self.check_collide()

    def check_collide(self):
        for sprite in self.overlapping_sprites:
            sprite.handle_collide()

    def handle_collide(self):
        None
        
class Goal(games.Sprite):
    # goal class
    image = games.load_image("resources\\goal.png")
    def __init__(self, game, x, y):
        super(Goal, self).__init__(image = Goal.image, x = x, y = y)

        self.game = game
        self.sound = games.load_sound("resources\\goal.wav")

    def handle_collide(self):
        # go to next level
        self.game.next_level()
        self.sound.play()

class Logo(games.Sprite):
    image = games.load_image("resources\\logo.png")
    def __init__(self, game, x, y):
        super(Logo, self).__init__(image = Logo.image, x = x, y = y)

def main():
    # start game
    bav = Game()
    bav.intro_text()
    bav.play()

main()
