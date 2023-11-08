#Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. 
class Player:
  """A class to represent a cricket player."""

  def play(self):
    """Prints a message indicating that the player is playing cricket."""

    print("The player is playing cricket.")


class Batsman(Player):
  """A class to represent a batsman."""

  def play(self):
    """Prints a message indicating that the batsman is batting."""

    print("The batsman is batting.")


class Bowler(Player):
  """A class to represent a bowler."""

  def play(self):
    """Prints a message indicating that the bowler is bowling."""

    print("The bowler is bowling.")


def main():
  # Create a batsman object.
  batsman = Batsman()

  # Create a bowler object.
  bowler = Bowler()

  # Call the play() method for the batsman object.
  batsman.play()

  # Call the play() method for the bowler object.
  bowler.play()


if __name__ == "__main__":
  main()


#The batsman is batting.
#The bowler is bowling.
