from cmath import exp
import pytest
from mach_eight_challange import find_pairs

def test_challange_example(capsys):
    find_pairs(139)
    captured = capsys.readouterr()
    players = [
                ['Brevin Knight', 'Nate Robinson'],
                ['Nate Robinson', 'Mike Wilks']
              ]
    expected = "\n".join(["- {player1:<25s}{player2}".format(player1=couple[0], player2=couple[1]) for couple in players])
    expected = expected + "\n"
    assert captured.out == expected
    

def test_many_couples_found(capsys):
    find_pairs(141)    
    captured = capsys.readouterr()
    
    players = [
                ['Chucky Atkins', 'Brevin Knight'],
                ['Chucky Atkins', 'Mike Wilks'],
                ['D.J. Augustin', 'Nate Robinson'],
                ['Jose Barea', 'Nate Robinson'],
                ['Aaron Brooks', 'Nate Robinson'],
                ['Dee Brown', 'Nate Robinson'],
                ['Will Bynum', 'Nate Robinson'],
                ['Speedy Claxton', 'Brevin Knight'],
                ['Speedy Claxton', 'Mike Wilks'],
                ['T.J. Ford', 'Nate Robinson'],
                ['Allen Iverson', 'Nate Robinson'],
                ['Kyle Lowry', 'Nate Robinson'],
                ['Tyronn Lue', 'Nate Robinson'],
                ['Jameer Nelson', 'Nate Robinson'],
                ['Chris Paul', 'Nate Robinson'],
                ['Nate Robinson', 'Sean Singletary'],                
                ['Nate Robinson', 'Sebastian Telfair'],
              ]
    expected = "\n".join(["- {player1:<25s}{player2}".format(player1=couple[0], player2=couple[1]) for couple in players])
    expected = expected + "\n"        
    assert captured.out == expected

def test_not_couple_found(capsys):
    find_pairs(189222)
    captured = capsys.readouterr()
    assert captured.out == 'No matches found\n'