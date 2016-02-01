from projet import *

joueur1 = Player("Joueur1",FonceurStrategy())
joueur2 = Player("Joueur2",GardienStrategy())
joueur3 = Player("Joueur3",DefenseurStrategy())
joueur4 = Player("Joueur4",PasseurStrategy())

team1 = SoccerTeam("team1",[joueur1])
team2 = SoccerTeam("team2",[joueur1,joueur2])
team4 = SoccerTeam("team4",[joueur1,joueur1,joueur2,joueur2])
